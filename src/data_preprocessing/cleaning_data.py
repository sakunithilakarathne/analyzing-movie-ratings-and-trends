import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer

def removing_duplicates(dataset):
    # Check for duplicates
    duplicates = dataset.duplicated(subset=['IMDb ID'], keep=False)
    duplicate_rows = dataset[duplicates]

    # Check if there are any duplicates
    if duplicate_rows.empty:
        print("No Duplicates")
    else:
        print("Duplicates found:")
        dataset.drop_duplicates(subset=['IMDb ID'], keep='first', inplace=True)
        print("Duplicated Removed")

    return dataset

def converting_data_types(dataset):

    # Removing min and converting to int type from "Movie Runtime" column
    dataset["Movie Runtime"] = dataset["Movie Runtime"].str.split(" ").str[0].astype(int)
    # Removing $ and , and converting to int type from "Domestic Gross" column
    dataset["Domestic Gross"] = dataset["Domestic Gross"].str.replace("$", "")
    dataset["Domestic Gross"] = dataset["Domestic Gross"].str.replace(",", "")
    dataset["Domestic Gross"] = pd.to_numeric(dataset["Domestic Gross"], errors='coerce').astype("Int64")
    # Converting the IMDb rating from 7.9/10 to 7.9 and to float type
    dataset["IMDB Rating"] = dataset["IMDB Rating"].str.split("/").str[0]
    dataset["IMDB Rating"] = pd.to_numeric(dataset["IMDB Rating"], errors="coerce")
    # Changing RT Rating from 80% to 80 and Converting to int type
    dataset["RT Rating"] = dataset["RT Rating"].str.replace("%", "")
    dataset["RT Rating"] = pd.to_numeric(dataset["RT Rating"], errors="coerce").astype("Int64")
    # Changing Metacritic rating from 83/100 to 83 and Converting to int type
    dataset["Metacritic Rating"] = dataset["Metacritic Rating"].str.split("/").str[0]
    dataset["Metacritic Rating"] = pd.to_numeric(dataset["Metacritic Rating"], errors="coerce").astype("Int64")
    # Removing , from IMDB vote count and converting to int type
    dataset["IMDB Vote Count"] = dataset["IMDB Vote Count"].str.replace(",", "")
    dataset["IMDB Vote Count"] = pd.to_numeric(dataset["IMDB Vote Count"], errors='coerce').astype("Int64")

    # Convert Movie Release Date datetime type
    dataset["Movie Release Date"] = pd.to_datetime(dataset["Movie Release Date"], format='%d-%b-%y')

    return dataset


def handling_categorical_data(dataset):

    # ------------- 1. Handling Movie Genres Column ---------------

    # Split genres into individual genres
    dataset["Movie Genre"] = dataset["Movie Genre"].str.split(',')
    # Initializing
    mlb = MultiLabelBinarizer()
    # One hot encoding for genre values
    genre_encoded = pd.DataFrame(mlb.fit_transform(dataset["Movie Genre"]), columns=mlb.classes_)
    # Adding the encoded values to the dataset
    dataset = pd.concat([dataset, genre_encoded], axis=1)

    # Drop movie genre column
    #dataset.drop("Movie Genre", axis=1, inplace=True)

    # ------------- 2.  ---------------
    return dataset
