"""
Visualization utilities for the Sales Prediction project
"""

import matplotlib.pyplot as plt
import seaborn as sns

def plot_sales_distribution(df):
    """Plot the distribution of sales"""
    plt.figure(figsize=(8, 5))
    df['Sales'].hist(bins=20, edgecolor='black', alpha=0.7)
    plt.xlabel('Sales')
    plt.ylabel('Frequency')
    plt.title('Distribution of Sales')
    plt.grid(True, alpha=0.3)
    plt.show()

def plot_scatter_relationships(df):
    """Create scatter plots for each advertising medium vs sales"""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    mediums = ['TV', 'Radio', 'Newspaper']
    for i, medium in enumerate(mediums):
        axes[i].scatter(df[medium], df['Sales'], alpha=0.6)
        axes[i].set_xlabel(f'{medium} Spend')
        axes[i].set_ylabel('Sales')
        axes[i].set_title(f'{medium} vs Sales')
        axes[i].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

def plot_correlation_heatmap(df):
    """Create correlation heatmap"""
    plt.figure(figsize=(8, 6))
    corr = df[['TV', 'Radio', 'Newspaper', 'Sales']].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, 
                square=True, fmt='.3f')
    plt.title('Correlation Matrix')
    plt.show()

def plot_actual_vs_predicted(y_actual, y_predicted):
    """Plot actual vs predicted values"""
    plt.figure(figsize=(8, 6))
    plt.scatter(y_actual, y_predicted, alpha=0.6)
    plt.plot([y_actual.min(), y_actual.max()], 
             [y_actual.min(), y_actual.max()], 
             'r--', lw=2)
    plt.xlabel('Actual Sales')
    plt.ylabel('Predicted Sales')
    plt.title('Actual vs Predicted Sales')
    plt.grid(True, alpha=0.3)
    plt.show()

def plot_residuals(y_actual, y_predicted):
    """Plot residuals (errors)"""
    residuals = y_actual - y_predicted
    
    plt.figure(figsize=(8, 6))
    plt.scatter(y_predicted, residuals, alpha=0.6)
    plt.axhline(y=0, color='r', linestyle='--', linewidth=2)
    plt.xlabel('Predicted Sales')
    plt.ylabel('Residuals')
    plt.title('Residual Plot')
    plt.grid(True, alpha=0.3)
    plt.show()
    
    # Histogram of residuals
    plt.figure(figsize=(8, 6))
    plt.hist(residuals, bins=15, edgecolor='black', alpha=0.7)
    plt.xlabel('Prediction Error')
    plt.ylabel('Frequency')
    plt.title('Distribution of Prediction Errors')
    plt.grid(True, alpha=0.3)
    plt.show()