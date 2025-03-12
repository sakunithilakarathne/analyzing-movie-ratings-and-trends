import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


def splitting_dataset(dataset):

    target_column = "Domestic Gross"

    X = dataset.drop(columns = [target_column])
    y = dataset[target_column]

    # Split the dataset into training and test sets
    # Using 80% of the data for training and 20% for testing
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Print the shapes of the resulting datasets
    print("Training data shape:", X_train.shape)
    print("Test data shape:", X_test.shape)
    print("Training labels shape:", y_train.shape)
    print("Test labels shape:", y_test.shape)

    # Save the datasets to files
    X_train.to_csv("data/processed/X_train.csv", index=False)
    X_test.to_csv("data/processed/X_test.csv", index=False)
    y_train.to_csv("data/processed/y_train.csv", index=False)
    y_test.to_csv("data/processed/y_test.csv", index=False)

    print("Datasets saved successfully!")
    return X_test,X_train,y_test,y_train