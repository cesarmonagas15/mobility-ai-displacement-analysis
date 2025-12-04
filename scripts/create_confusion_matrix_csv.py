#!/usr/bin/env python3
"""
Helper script to create confusion_matrix.csv from machine learning predictions.

This script helps you create the confusion matrix CSV file needed for the dashboard.
You can either:
1. Run this script if you have y_test and y_pred variables available
2. Or manually create a CSV with columns: true_label, predicted_label
"""

import pandas as pd
import numpy as np
import os
import sys

def create_confusion_matrix_csv(y_test, y_pred, output_path=None):
    """
    Create confusion matrix CSV from true and predicted labels.
    
    Parameters:
    -----------
    y_test : array-like
        True labels
    y_pred : array-like
        Predicted labels
    output_path : str, optional
        Path to save CSV. Defaults to data/processed/confusion_matrix.csv
    """
    if output_path is None:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_path = os.path.join(script_dir, '..', 'data', 'processed', 'confusion_matrix.csv')
    
    # Create DataFrame
    df = pd.DataFrame({
        'true_label': y_test,
        'predicted_label': y_pred
    })
    
    # Save to CSV
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"✓ Confusion matrix CSV created at: {output_path}")
    print(f"  Shape: {df.shape}")
    print(f"  True labels: {df['true_label'].value_counts().to_dict()}")
    print(f"  Predicted labels: {df['predicted_label'].value_counts().to_dict()}")
    
    return df

if __name__ == "__main__":
    print("="*60)
    print("Confusion Matrix CSV Generator")
    print("="*60)
    print("\nThis script helps create the confusion_matrix.csv file.")
    print("You need to provide y_test and y_pred from your ML model.\n")
    print("Example usage in Python:")
    print("  from scripts.create_confusion_matrix_csv import create_confusion_matrix_csv")
    print("  create_confusion_matrix_csv(y_test, y_pred)\n")
    print("Or run this from your notebook after training:")
    print("  %run scripts/create_confusion_matrix_csv.py")
    print("  create_confusion_matrix_csv(y_test, y_pred)\n")
    print("="*60)

