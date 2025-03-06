import pandas as pd


def feature_engineering(dataset):
    # New Feature - Month of the movie release
    dataset["Release Month"]=dataset["Movie Release Date"].dt.month

    # New Feature - No of Movies directed by the Director
    dataset["Movie Director"] = dataset["Movie Director"].str.split(',')
    director_counts = dataset.explode("Movie Director")["Movie Director"].value_counts()
    dataset["director_popularity"] = dataset["Movie Director"].apply(
        lambda x: sum(director_counts[director] for director in x))

    # New Feature - Whether movie is in English or not
    dataset['is_english'] = dataset['Language'].apply(lambda x: 1 if 'English' in x else 0)

    # New Feature - No of movies Actors are in
    dataset['Actors'] = dataset['Actors'].str.split(',')
    actor_counts = dataset.explode('Actors')['Actors'].value_counts()
    dataset['actor_popularity'] = dataset['Actors'].apply(
        lambda x: sum(actor_counts[actor] for actor in x))

    return dataset


def features_after_eda(dataset):
    # New Feature - Season of the movie release
    dataset["Season"] = dataset["Release Month"].apply(lambda x: 'Winter' if x in [12, 1, 2] else
    'Spring' if x in [3, 4, 5] else
    'Summer' if x in [6, 7, 8] else 'Fall')

    # New Feature - Whether movie is during holiday season or not
    dataset['is_holiday_release'] = dataset['month'].apply(lambda x: 1 if x in [11, 12] else 0)

    return dataset