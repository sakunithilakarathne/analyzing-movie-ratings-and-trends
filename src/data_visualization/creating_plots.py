import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from jinja2 import Environment, FileSystemLoader
import os



def generate_visualizations(movie_data):

    # Creating file to save graphs
    if not os.path.exists('reports/plots'):
        os.makedirs('reports/plots')

    # Histograms for numerical columns
    numerical_columns = ['Movie Runtime', 'Domestic Gross', 'IMDB Rating', 'RT Rating', 'Metacritic Rating',
                         'IMDB Vote Count', 'director_popularity', 'actor_popularity', 'writer_popularity',
                         'Language_Count', 'Country_Count']
    movie_data[numerical_columns].hist(bins=20, figsize=(20, 15))
    plt.suptitle('Distribution of Numerical Features')
    plt.savefig('reports/plots/histograms_for_NumericalColumns.png')
    plt.close()

    # Plot bar charts for categorical features
    categorical_features = ['Release Month', 'Season', 'is_holiday_release', 'is_english']
    plt.figure(figsize=(15, 8))
    for i, feature in enumerate(categorical_features, 1):
        plt.subplot(2, 2, i)
        movie_data[feature].value_counts().plot(kind='bar')
        plt.title(f'Frequency of {feature}')
        plt.xlabel(feature)
        plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig('reports/plots/bar_charts_for_CategoricalData.png')
    plt.close()

    # Scatter plots for numerical features vs Domestic Gross
    plt.figure(figsize=(15, 10))
    for i, feature in enumerate(numerical_columns, 1):
        plt.subplot(3, 4, i)
        sns.scatterplot(x=movie_data[feature], y=movie_data['Domestic Gross'])
        plt.title(f'{feature} vs Domestic Gross')
    plt.tight_layout()
    plt.savefig('reports/plots/scatterplots_against_DomesticGross.png')
    plt.close()

    # Create bar graphs for categorical features vs Domestic Gross
    plt.figure(figsize=(15, 8))
    for i, feature in enumerate(categorical_features, 1):
        plt.subplot(2, 2, i)

        # Plot the bar graph
        sns.barplot(x=feature, y='Domestic Gross', data=movie_data, errorbar=None)
        plt.title(f'Average Domestic Gross by {feature}')
        plt.xlabel(feature)
        plt.ylabel('Domestic Gross')
    plt.tight_layout()
    plt.savefig('reports/plots/bargraphs_against_DomesticGross.png')
    plt.close()

    # Correlation heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(movie_data[numerical_columns].corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Heatmap')
    plt.tight_layout()
    plt.savefig('reports/plots/correlation_heatmap.png')
    plt.close()

    # Number of movies by release month
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Release Month', data=movie_data, palette='coolwarm')
    plt.title('Number of Movies by Release Month')
    plt.tight_layout()
    plt.savefig('reports/plots/no_of_movies_by_month.png')
    plt.close()

    # Average Domestic Gross by release month
    mean_gross = movie_data.groupby('Release Month')['Domestic Gross'].sum().reset_index()

    plt.figure(figsize=(10, 6))
    sns.barplot(x='Release Month', y='Domestic Gross', data=mean_gross, palette='coolwarm')
    plt.title('Domestic Gross by Release Month')
    plt.tight_layout()
    plt.savefig('reports/plots/average_domestic_gross_by_month.png')
    plt.close()

    # Count of movies by genre
    genre_columns = ['Action', 'Adventure', 'Biography', 'Comedy', 'Crime', 'Drama', 'Family', 'Fantasy', 'History',
                     'Horror', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller']
    genre_counts = movie_data[genre_columns].sum().sort_values(ascending=False)

    # Plot the number of movies by genre
    plt.figure(figsize=(12, 6))
    sns.barplot(x=genre_counts.index, y=genre_counts.values, palette='viridis')
    plt.title('Number of Movies by Genre')
    plt.xlabel('Genre')
    plt.ylabel('Number of Movies')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('reports/plots/no_of_movies_by_genre.png')
    plt.close()

    melted_data = movie_data.melt(id_vars=['Domestic Gross'], value_vars=genre_columns, var_name='Genre',
                                  value_name='Is_Genre')
    filtered_data = melted_data[melted_data['Is_Genre'] == 1]
    genre_gross = filtered_data.groupby('Genre')['Domestic Gross'].mean().reset_index()
    genre_gross['Genre'] = pd.Categorical(genre_gross['Genre'], categories=genre_counts.index, ordered=True)
    genre_gross = genre_gross.sort_values('Genre')

    # Create the bar plot for average Domestic Gross by genre
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Genre', y='Domestic Gross', data=genre_gross, palette='Set2')
    plt.title('Average Domestic Gross by Genre')
    plt.xlabel('Genre')
    plt.ylabel('Average Domestic Gross')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('reports/plots/average_domestic_gross_by_genre.png')
    plt.close()

    return movie_data


