import pandas as pd
import requests
from bs4 import BeautifulSoup
from src.data_gathering.box_office_mojo_movie_scraper import scrape_highest_grossing_movies
from src.data_gathering.imdb_movie_scraper import get_imdb_movies
from src.utils.helper_functions import concat_dataframes, save_df_to_csv
from src.utils.helper_functions import remove_duplicates
from src.data_gathering.omdb_api_fetcher import fetch_omdb_api_data

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

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Completed !")


# Preprocessing Functions


# Analysis Functions


# Modeling Functions


if __name__ == "__main__":
    main()