import pandas as pd
import os

def concat_dataframes(*args,axis=0,ignore_index=True):
    """
    Concatenates any number of DataFrames.

    Parameters:
        *args: Variable-length argument list of DataFrames.
        axis: Axis to concatenate along (0 for row-wise, 1 for column-wise). Default is 0.
        ignore_index: If True, the resulting DataFrame will have a new index. Default is Ture.

    Returns:
        A single concatenated DataFrame.
    """
    combined_df = pd.concat([args], axis=axis, ignore_index=ignore_index)
    return combined_df


def remove_duplicates(data_frame,subset):
    """
    Concatenates any number of DataFrames.

    Parameters:
        data_frame: Data Frame to remove duplicates from.
        subset: List of column names to consider for identifying duplicates

    Returns:
        A single DataFrame with no duplicate values.
    """
    cleaned_df = data_frame.drop_duplicates(subset=[subset]).reset_index(drop=True)
    return cleaned_df

def save_df_to_csv(dataframe,file_path):
    dataframe.to_csv(file_path, index=False)
    print("Dataframe Saved!")
