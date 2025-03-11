import pandas as pd
from sklearn.ensemble import RandomForestRegressor

def mean_median_mode_imputation(dataset):
    """
    Impute missing values that are less than 5% in the dataset.
    """
    dataset['Movie Runtime'] = dataset['Movie Runtime'].fillna(dataset['Movie Runtime'].mode()[0])
    dataset['Writers'] = dataset['Writers'].fillna('Unknown')
    dataset['Language'] = dataset['Language'].fillna(dataset['Language'].mode()[0])
    dataset['IMDB Vote Count'] = dataset['IMDB Vote Count'].fillna(int(dataset['IMDB Vote Count'].median()))
    dataset['IMDB Rating'] = dataset['IMDB Rating'].fillna(dataset['IMDB Rating'].mean())
    dataset["RT Rating"] = dataset["RT Rating"].fillna(int(dataset["RT Rating"].mean()))

    print("\n Imputation complete for columns with less than 5% missing values! \n")
    return dataset

def statistical_imputation(dataset, target_col, feature_columns):
    """
    Imputes missing values in `target_col` using a predictive model trained on `feature_cols`.
    """
    # Split data into rows with and without missing values
    df_missing = dataset[dataset[target_col].isna()]
    df_not_missing = dataset[~dataset[target_col].isna()]

    # Train a model to predict missing values
    model = RandomForestRegressor()
    X = df_not_missing[feature_columns]
    y = df_not_missing[target_col]
    model.fit(X, y)

    # Predict and fill missing values
    X_missing = df_missing[feature_columns]
    predictions = model.predict(X_missing)

    # Convert predictions to integers and assign to the target column
    dataset.loc[dataset[target_col].isna(), target_col] = predictions.round().astype(int)


