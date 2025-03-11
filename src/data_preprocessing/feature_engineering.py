import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer

def feature_engineering(dataset):
    """
    Create new features using the existing features.
    """
    # New Feature - Month of the movie release
    dataset["Release Month"]=dataset["Movie Release Date"].dt.month

    # New Feature - Season of the movie release
    dataset["Season"] = dataset["Release Month"].apply(lambda x: 'Winter' if x in [12, 1, 2] else
    'Spring' if x in [3, 4, 5] else
    'Summer' if x in [6, 7, 8] else 'Fall')

    # New Feature - Whether movie is during holiday season or not
    dataset['is_holiday_release'] = dataset['Release Month'].apply(lambda x: 1 if x in [11, 12] else 0)

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

    # New Feature - No of movies written by the writers
    dataset['Writers'] = dataset['Writers'].str.split(',')
    writer_counts = dataset.explode('Writers')['Writers'].value_counts()
    dataset['writer_popularity'] = dataset['Writers'].apply(
        lambda x: sum(writer_counts[writer] for writer in x))

    # New Feature - No of Languages movie is release in
    dataset['Language_Count'] = dataset['Language'].apply(lambda x: len(x.split(',')))

    # New Feature - No of Countries movie is release in
    dataset['Country_Count'] = dataset['Country'].apply(lambda x: len(x.split(',')))

    # New Feature - One Hot encoding for movie genre
    dataset['Movie Genre'] = dataset['Movie Genre'].apply(
        lambda x: [genre.strip().strip("'") for genre in x.strip('[]').split(',')])
    #dataset['Movie Genre'] = dataset['Movie Genre'].str.split(',')
    mlb = MultiLabelBinarizer()
    genre_encoded = pd.DataFrame(mlb.fit_transform(dataset['Movie Genre']), columns=mlb.classes_)
    dataset = pd.concat([dataset, genre_encoded], axis=1)

    return dataset
