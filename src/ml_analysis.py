"""
Machine Learning Analysis Module
================================
Comprehensive ML analysis with Logistic Regression, Regularized Regression (Lasso/Ridge),
and Random Forest models for predicting AI displacement risk.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, Lasso, Ridge
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    confusion_matrix, classification_report, roc_auc_score, 
    roc_curve, accuracy_score, precision_score, recall_score, f1_score
)
import warnings
warnings.filterwarnings('ignore')


def create_regions(df):
    """Create regional dummy variables"""
    # Define regions based on state
    region_mapping = {
        'Northeast': ['Maine', 'New Hampshire', 'Vermont', 'Massachusetts', 'Rhode Island', 
                      'Connecticut', 'New York', 'New Jersey', 'Pennsylvania'],
        'South': ['Delaware', 'Maryland', 'Virginia', 'West Virginia', 'Kentucky', 'Tennessee',
                  'North Carolina', 'South Carolina', 'Georgia', 'Florida', 'Alabama',
                  'Mississippi', 'Arkansas', 'Louisiana', 'Oklahoma', 'Texas'],
        'Midwest': ['Ohio', 'Indiana', 'Illinois', 'Michigan', 'Wisconsin', 'Minnesota',
                    'Iowa', 'Missouri', 'North Dakota', 'South Dakota', 'Nebraska', 'Kansas'],
        'West': ['Montana', 'Idaho', 'Wyoming', 'Colorado', 'New Mexico', 'Arizona', 'Utah',
                 'Nevada', 'Washington', 'Oregon', 'California', 'Alaska', 'Hawaii'],
        'Other': ['Puerto Rico']
    }
    
    # Create reverse mapping
    state_to_region = {}
    for region, states in region_mapping.items():
        for state in states:
            state_to_region[state] = region
    
    df['region'] = df['state_name'].map(state_to_region).fillna('Other')
    
    # Create dummy variables
    region_dummies = pd.get_dummies(df['region'], prefix='region')
    return df, region_dummies


def engineer_features(df):
    """Create feature engineering: regions, quadratic terms, interactions"""
    
    # Start with base features - ONLY use mobility_score, NOT ai_exposure
    # (ai_exposure is what we're trying to predict, so it would cause data leakage)
    features_df = df[['mobility_score']].copy()
    
    # Create regions
    df_with_regions, region_dummies = create_regions(df)
    features_df = pd.concat([features_df, region_dummies], axis=1)
    
    # Quadratic terms (only for mobility since we don't have ai_exposure)
    features_df['mobility_score_sq'] = features_df['mobility_score'] ** 2
    
    # Absolute values (capture magnitude)
    features_df['mobility_abs'] = np.abs(features_df['mobility_score'])
    
    # Add state-level features (aggregated mobility by state)
    state_mobility = df_with_regions.groupby('state_name')['mobility_score'].agg(['mean', 'std']).reset_index()
    state_mobility.columns = ['state_name', 'state_mobility_mean', 'state_mobility_std']
    df_with_regions = df_with_regions.merge(state_mobility, on='state_name', how='left')
    features_df['state_mobility_mean'] = df_with_regions['state_mobility_mean'].values
    features_df['state_mobility_std'] = df_with_regions['state_mobility_std'].fillna(0).values
    
    return features_df, df_with_regions


def create_binary_target(df):
    """Create binary target: Double Disadvantage (1) vs Not (0)"""
    # Double Disadvantage = Low mobility AND High AI risk
    # This tests our core hypothesis: can we predict double disadvantage from mobility patterns?
    mobility_median = df['mobility_score'].median()
    ai_median = df['ai_exposure'].median()
    
    # 1 = Double Disadvantage (low mobility + high AI risk)
    # 0 = All other categories (Safe, Tech Disruption, Stagnant Protected)
    y = ((df['mobility_score'] < mobility_median) & (df['ai_exposure'] > ai_median)).astype(int)
    return y


def train_models(X_train, X_test, y_train, y_test, scaler=None):
    """Train all three model types"""
    
    results = {}
    
    # 1. Logistic Regression (baseline, no regularization)
    print("Training Logistic Regression...")
    lr = LogisticRegression(penalty=None, max_iter=1000, random_state=42, solver='lbfgs')
    lr.fit(X_train, y_train)
    lr_pred = lr.predict(X_test)
    lr_pred_proba = lr.predict_proba(X_test)[:, 1]
    
    results['Logistic Regression'] = {
        'model': lr,
        'predictions': lr_pred,
        'probabilities': lr_pred_proba,
        'true_labels': y_test,
        'accuracy': accuracy_score(y_test, lr_pred),
        'precision': precision_score(y_test, lr_pred, zero_division=0),
        'recall': recall_score(y_test, lr_pred, zero_division=0),
        'f1': f1_score(y_test, lr_pred, zero_division=0),
        'roc_auc': roc_auc_score(y_test, lr_pred_proba),
        'confusion_matrix': confusion_matrix(y_test, lr_pred),
        'coefficients': lr.coef_[0] if hasattr(lr, 'coef_') else None
    }
    
    # 2. Regularized Logistic Regression (L1 and L2) - Different regularization strengths
    print("Training Regularized Logistic Regression (L1/L2)...")
    
    # Lasso (L1 regularization) - Strong regularization for feature selection
    lasso_lr = LogisticRegression(penalty='l1', C=0.01, solver='liblinear', max_iter=1000, random_state=42)
    lasso_lr.fit(X_train, y_train)
    lasso_pred = lasso_lr.predict(X_test)
    lasso_pred_proba = lasso_lr.predict_proba(X_test)[:, 1]
    
    results['Lasso Regression'] = {
        'model': lasso_lr,
        'predictions': lasso_pred,
        'probabilities': lasso_pred_proba,
        'true_labels': y_test,
        'accuracy': accuracy_score(y_test, lasso_pred),
        'precision': precision_score(y_test, lasso_pred, zero_division=0),
        'recall': recall_score(y_test, lasso_pred, zero_division=0),
        'f1': f1_score(y_test, lasso_pred, zero_division=0),
        'roc_auc': roc_auc_score(y_test, lasso_pred_proba),
        'confusion_matrix': confusion_matrix(y_test, lasso_pred),
        'coefficients': lasso_lr.coef_[0] if hasattr(lasso_lr, 'coef_') else None
    }
    
    # Ridge (L2 regularization) - Moderate regularization
    ridge_lr = LogisticRegression(penalty='l2', C=0.1, max_iter=1000, random_state=42)
    ridge_lr.fit(X_train, y_train)
    ridge_pred = ridge_lr.predict(X_test)
    ridge_pred_proba = ridge_lr.predict_proba(X_test)[:, 1]
    
    results['Ridge Regression'] = {
        'model': ridge_lr,
        'predictions': ridge_pred,
        'probabilities': ridge_pred_proba,
        'true_labels': y_test,
        'accuracy': accuracy_score(y_test, ridge_pred),
        'precision': precision_score(y_test, ridge_pred, zero_division=0),
        'recall': recall_score(y_test, ridge_pred, zero_division=0),
        'f1': f1_score(y_test, ridge_pred, zero_division=0),
        'roc_auc': roc_auc_score(y_test, ridge_pred_proba),
        'confusion_matrix': confusion_matrix(y_test, ridge_pred),
        'coefficients': ridge_lr.coef_[0] if hasattr(ridge_lr, 'coef_') else None
    }
    
    # 3. Random Forest - Different hyperparameters to capture non-linearities
    print("Training Random Forest...")
    rf = RandomForestClassifier(
        n_estimators=200, 
        max_depth=15, 
        min_samples_split=10,
        min_samples_leaf=5,
        max_features='sqrt',
        random_state=42, 
        n_jobs=-1,
        class_weight='balanced'  # Handle class imbalance
    )
    rf.fit(X_train, y_train)
    rf_pred = rf.predict(X_test)
    rf_pred_proba = rf.predict_proba(X_test)[:, 1]
    
    results['Random Forest'] = {
        'model': rf,
        'predictions': rf_pred,
        'probabilities': rf_pred_proba,
        'true_labels': y_test,
        'accuracy': accuracy_score(y_test, rf_pred),
        'precision': precision_score(y_test, rf_pred, zero_division=0),
        'recall': recall_score(y_test, rf_pred, zero_division=0),
        'f1': f1_score(y_test, rf_pred, zero_division=0),
        'roc_auc': roc_auc_score(y_test, rf_pred_proba),
        'confusion_matrix': confusion_matrix(y_test, rf_pred),
        'feature_importances': rf.feature_importances_
    }
    
    return results


def run_ml_analysis(df):
    """Run complete ML analysis pipeline"""
    
    print("="*60)
    print("MACHINE LEARNING ANALYSIS")
    print("="*60)
    
    # Feature Engineering
    print("\n[STEP 1] Feature Engineering...")
    X, df_with_regions = engineer_features(df)
    feature_names = X.columns.tolist()
    print(f"  Created {len(feature_names)} features")
    print(f"  Features: {', '.join(feature_names[:5])}...")
    
    # Create target
    print("\n[STEP 2] Creating binary target (Double Disadvantage)...")
    y = create_binary_target(df)
    target_dist = pd.Series(y).value_counts().to_dict()
    print(f"  Target distribution: {target_dist}")
    print(f"  Double Disadvantage (1): {target_dist.get(1, 0)} counties ({target_dist.get(1, 0)/len(y)*100:.1f}%)")
    print(f"  Other Categories (0): {target_dist.get(0, 0)} counties ({target_dist.get(0, 0)/len(y)*100:.1f}%)")
    print(f"  Note: Predicting double disadvantage using ONLY mobility and regional features")
    print(f"  Hypothesis: Low mobility patterns predict double disadvantage counties")
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print(f"\n[STEP 3-5] Training models...")
    print(f"  Training set: {X_train.shape[0]} samples")
    print(f"  Test set: {X_test.shape[0]} samples")
    
    # Train all models
    results = train_models(X_train_scaled, X_test_scaled, y_train, y_test, scaler)
    
    # Print summary
    print("\n" + "="*60)
    print("MODEL PERFORMANCE SUMMARY")
    print("="*60)
    for model_name, metrics in results.items():
        print(f"\n{model_name}:")
        print(f"  Accuracy:  {metrics['accuracy']:.3f}")
        print(f"  Precision: {metrics['precision']:.3f}")
        print(f"  Recall:    {metrics['recall']:.3f}")
        print(f"  F1-Score:  {metrics['f1']:.3f}")
        print(f"  ROC-AUC:   {metrics['roc_auc']:.3f}")
    
    return results, feature_names, X_test_scaled, y_test, scaler


if __name__ == "__main__":
    # Load data
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, '..', '..', 'data', 'processed', 'merged_clean.csv')
    df = pd.read_csv(data_path)
    
    # Run analysis
    results, feature_names, X_test, y_test, scaler = run_ml_analysis(df)
    
    # Save results for dashboard
    output_path = os.path.join(script_dir, '..', '..', 'data', 'processed', 'ml_results.pkl')
    import pickle
    with open(output_path, 'wb') as f:
        pickle.dump({
            'results': results,
            'feature_names': feature_names,
            'X_test': X_test,
            'y_test': y_test
        }, f)
    print(f"\n✓ Results saved to {output_path}")

