import pandas as pd
import requests
from bs4 import BeautifulSoup
from src.data_gathering.box_office_mojo_movie_scraper import scrape_highest_grossing_movies
from src.data_gathering.imdb_movie_scraper import get_imdb_movies
from src.utils.helper_functions import *
from src.data_gathering.omdb_api_fetcher import fetch_omdb_api_data
from src.data_preprocessing.cleaning_data import *
from src.data_preprocessing.handling_missing_values import *
from src.data_preprocessing.feature_engineering import *
from src.data_visualization.creating_plots import *
from src.data_visualization.generating_report import *
from src.data_preprocessing.splitting_dataset import *
from src.model_creation.linear_regression_model import *
from src.model_creation.random_forest_model import *
from src.model_creation.xg_boost_model import *

# Configuration

def main():
    try:
        # ---------- Step 1 - Data Gathering Functions ----------
        # Extracting data from Box Office Mojo
        highest_grossed_movies_df = scrape_highest_grossing_movies()
        save_df_to_csv(highest_grossed_movies_df,"data/raw/box_mojo_data.csv")

        # Extracting data from IMDB site
        highest_rated_movies_df = get_imdb_movies("user_rating,desc")
        most_voted_movies_df = get_imdb_movies("num_votes,desc")
        most_popular_movies_df = get_imdb_movies("moviemeter,desc")
        longest_runtime_movies_df = get_imdb_movies("runtime,desc")
        shortest_runtime_movies_df = get_imdb_movies("runtime,asc")
        latest_released_movies_df = get_imdb_movies("year,desc")
        # Combining and Removing the duplicates from the IMDB datasets
        all_imdb_movies_df = concat_dataframes(highest_rated_movies_df,most_voted_movies_df,most_popular_movies_df,
                                               longest_runtime_movies_df,shortest_runtime_movies_df,latest_released_movies_df)
        imdb_movies_df = remove_duplicates(all_imdb_movies_df,"IMDb ID")
        save_df_to_csv(imdb_movies_df,"data/raw/imdb_data.csv")

        # Combining box office mojo and IMDb data
        all_movie_data = concat_dataframes(highest_grossed_movies_df,imdb_movies_df)
        all_movie_data_cleaned = remove_duplicates(all_movie_data,"IMDb ID")
        save_df_to_csv(all_movie_data_cleaned,"data/raw/imdb_bom_combined.csv")

        # Fetching extensive movie details from OMDb API
        complete_movie_data_df = fetch_omdb_api_data(all_movie_data_cleaned)
        save_df_to_csv(complete_movie_data_df, "data/raw/complete_movie_data.csv")

        #---------- Step 2 - Data Preprocessing Functions ----------
        movie_data = pd.read_csv("data/raw/complete_movie_data.csv")
        movie_data = removing_duplicates(dataset=movie_data)
        movie_data = cleaning_data(dataset=movie_data)
        movie_data = converting_data_types(dataset=movie_data)

        movie_data = mean_median_mode_imputation(dataset=movie_data)

        columns_to_impute = ['Domestic Gross', 'Metacritic Rating']
        feature_cols = ['IMDB Rating', 'Movie Runtime', 'IMDB Vote Count', 'Movie Year']
        for col in columns_to_impute:
            statistical_imputation(movie_data, col, feature_cols)

        movie_data = feature_engineering(dataset=movie_data)
        movie_data = feature_encoding(dataset=movie_data)
        # movie_data = feature_scaling(dataset=movie_data)
        movie_data = dropping_unnecessary_columns(dataset=movie_data)
        save_df_to_csv(movie_data, "src/data_visualization/dataset1.csv")
        movie_data = feature_scaling(dataset=movie_data)
        save_df_to_csv(movie_data, "data/processed/dataset_for_clustering.csv")
        movie_data = movie_data.drop(columns='IMDb ID')
        save_df_to_csv(movie_data, "data/processed/preprocessed_movie_data.csv")

        # Analysis Functions

        dataset = pd.read_csv("src/data_visualization/dataset.csv")
        generate_pdf_report(dataset)

        final_dataset = pd.read_csv("data/processed/preprocessed_movie_data.csv")
        X_test,X_train,y_test,y_train = splitting_dataset(final_dataset)

        linear_regression_model(X_test,X_train,y_test,y_train)
        random_forest_model(X_test,X_train,y_test,y_train)
        xg_boost_model(X_test,X_train,y_test,y_train)


    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Completed !")





# Modeling Functions


if __name__ == "__main__":
    main()