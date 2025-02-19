#import required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_highest_grossing_movies():
    # Values used to paginate through the website
    offset_values = [0, 200, 400, 600, 800]

    # List used to store the scraped data
    all_movie_data = []

    for value in offset_values:
        # URL for scraping worldwide highest grossing movies
        url = f"https://www.boxofficemojo.com/chart/ww_top_lifetime_gross/?area=XWW&offset={value}"

        # Set headers to avoid blocking
        headers = {"User-Agent": "Mozilla/5.0"}

        # Fetch the page content
        page_to_scrape = requests.get(url, headers=headers)
        soup = BeautifulSoup(page_to_scrape.text, "html.parser")

        # Find all <tr> elements
        movie_details = soup.find_all('tr')[1:]

        # Extracting the movie title and movie id using class attributes
        for each_movie in movie_details:
            movie_title = each_movie.find('td', class_='a-text-left mojo-field-type-title').text
            movie_id = each_movie.find('a', class_='a-link-normal').get('href').split('/')[2]
            # Adding the extracted data to the list
            all_movie_data.append({
                "Title": movie_title,
                "IMDb ID": movie_id
            })

    df = pd.DataFrame(data=all_movie_data)
    #print(df)

    return df


# Call the function
# scrape_highest_grossing_movies()

# Save the DataFrame to a CSV file
# movies_df.to_csv("highest_grossing_films.csv", index=False)