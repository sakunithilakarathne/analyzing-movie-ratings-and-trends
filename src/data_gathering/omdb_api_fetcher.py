import requests
import pandas as pd

API_KEY = "70b73d8d"

def fetch_omdb_api_data(dataframe):

    all_movie_data = []

    for each_value in dataframe["IMDb ID"]:
        url = f"http://www.omdbapi.com/?i={each_value}&apikey={API_KEY}"
        omdb_response = requests.get(url).json()

        # Check if the response contains an error
        if omdb_response.get("Response") == "False":
            print(f"Error fetching data for IMDb ID {each_value}: {omdb_response.get('Error')}")
            continue

        # Extract required data
        try:
            movie_title = omdb_response.get("Title", "N/A")
            movie_runtime = omdb_response.get("Runtime", "N/A")
            movie_genre = omdb_response.get("Genre", "N/A")
            movie_box_office = omdb_response.get("BoxOffice", "N/A")
            movie_director = omdb_response.get("Director", "N/A")
            movie_actors = omdb_response.get("Actors", "N/A")

            ratings = omdb_response.get("Ratings", [])
            imdb_rating = ratings[0]["Value"] if len(ratings) > 0 else "N/A"
            rt_rating = ratings[1]["Value"] if len(ratings) > 1 else "N/A"
            metacritic_rating = ratings[2]["Value"] if len(ratings) > 2 else "N/A"

            imdb_votes = omdb_response.get("imdbVotes", "N/A")

            # Append the movie data to the list
            all_movie_data.append({
                "Movie Title": movie_title,
                "IMDb ID": each_value,
                "Movie Runtime": movie_runtime,
                "Movie Genre": movie_genre,
                "Domestic Gross": movie_box_office,
                "Movie Director": movie_director,
                "Actors": movie_actors,
                "IMDB Rating": imdb_rating,
                "RT Rating": rt_rating,
                "Metacritic Rating": metacritic_rating,
                "IMDB Vote Count": imdb_votes
            })
        except Exception as e:
            print(f"Error processing data for IMDb ID {each_value}: {e}")
            continue

    # Convert the list of dictionaries to a DataFrame
    omdb_df = pd.DataFrame(data=all_movie_data)
    return omdb_df
