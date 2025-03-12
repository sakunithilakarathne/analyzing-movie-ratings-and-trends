import pandas as pd


def removing_duplicates(dataset):
    """
    Checks for the missing values in dataset and removes them.
    """
    # Check for duplicates
    duplicates = dataset.duplicated(subset=['IMDb ID'], keep=False)
    duplicate_rows = dataset[duplicates]

    # Check if there are any duplicates
    if duplicate_rows.empty:
        print("\n No Duplicates found !\n")
    else:
        print("Duplicates found:")
        dataset.drop_duplicates(subset=['IMDb ID'], keep='first', inplace=True)
        print("Duplicated Removed")

    return dataset

def cleaning_data(dataset):
    """
    Clean the dataset of unnecessary suffixes, prefixes and symbols.
    """
    # Removing min suffix from Movie Runtime column
    dataset["Movie Runtime"] = dataset["Movie Runtime"].str.split(" ").str[0]

    # Removing $ prefix and . from Domestic Gross column
    dataset["Domestic Gross"] = dataset["Domestic Gross"].str.replace("$", "")
    dataset["Domestic Gross"] = dataset["Domestic Gross"].str.replace(",", "")

    # Turning IMDB Rating column from x/10 into x
    dataset["IMDB Rating"] = dataset["IMDB Rating"].str.split("/").str[0]

    # Turning RT Rating column from x% to x
    dataset["RT Rating"] = dataset["RT Rating"].str.replace("%", "")

    # Turning Metacritic Column from x/100 to x
    dataset["Metacritic Rating"] = dataset["Metacritic Rating"].str.split("/").str[0]

    # Removing , from IMDB Vote Count column
    dataset["IMDB Vote Count"] = dataset["IMDB Vote Count"].str.replace(",", "")
    print("\n Unnecessary symbols and spaces removed from dataset! \n")
    return dataset


def converting_data_types(dataset):
    """
    Convert the data into correct types from object type.
    """

    # Converting "Movie Runtime" column to int
    dataset["Movie Runtime"] = pd.to_numeric(dataset["Movie Runtime"], errors="coerce").astype("Int64")
    # Converting "Domestic Gross" column to int
    dataset["Domestic Gross"] = pd.to_numeric(dataset["Domestic Gross"], errors='coerce').astype("Int64")
    # Converting the IMDb rating column to float
    dataset["IMDB Rating"] = pd.to_numeric(dataset["IMDB Rating"], errors="coerce")
    # Converting "RT Rating" column to int type
    dataset["RT Rating"] = pd.to_numeric(dataset["RT Rating"], errors="coerce").astype("Int64")
    # Converting "Metacritic Rating" column to int type
    dataset["Metacritic Rating"] = pd.to_numeric(dataset["Metacritic Rating"], errors="coerce").astype("Int64")
    # Removing , from IMDB vote count and converting to int type
    dataset["IMDB Vote Count"] = pd.to_numeric(dataset["IMDB Vote Count"], errors='coerce').astype("Int64")

    # Convert Movie Release Date datetime type
    dataset["Movie Release Date"] = pd.to_datetime(dataset["Movie Release Date"], format='%d %b %Y')

    # Ensuring Movie Genre is in str format
    dataset['Movie Genre'] = dataset['Movie Genre'].astype(str)
    dataset['Language'] = dataset['Language'].astype(str)
    dataset['Country'] = dataset['Country'].astype(str)

    print("\n Data converted to appropriate type ! \n")
    return dataset

def dropping_unnecessary_columns(dataset):
    # Columns to drop
    columns_to_drop = [
        'Movie Year','Movie Title', 'Movie Release Date', 'Movie Genre',
        'Movie Director', 'Writers', 'Actors', 'Language', 'Country'
    ]

    # Drop unnecessary columns
    dataset = dataset.drop(columns=columns_to_drop)


    print("\n Unnecessary columns dropped! \n")
    return dataset
