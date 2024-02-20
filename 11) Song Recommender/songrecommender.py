import numpy as np
import pandas as pd
import gensim
from gensim.models import Word2Vec
from urllib import request
import warnings
warnings.filterwarnings('ignore')

# Get the playlist dataset
data = open('train.txt', "r")

# Parse the playlist and skip the first two lines
# they contain metadata
lines = data.read().split('\n')[2:]

# Remove the playlist with only one song
playlists = [s.rstrip().split() for s in lines if len(s.split()) > 1]
##print('\n there are ', len(playlists), ' number of playlists')
##print('Playlist #1:\n', playlists[0], '\n')
##print('Playlist #2:\n', playlists[1], '\n')

# Our dataset is now in the shape that the Word2Vec model expects as input
# Here are the keyword parameters:
# vector_size: embedding size for the songs
# window: Word2Vec algorithm parameter, which is the max distance between the current
#          value and the predicted value (where value is the song)
# negative: Word2Vec number of negative examples to use at each training step - the model
#          needs to identify as "noise"

model = Word2Vec(playlists, vector_size=32, window=20, negative=50, min_count=1)

# The model is now trained
# We have only song IDs
# Load the song info in form of titles and artists
songs_file = open("song_hash.txt", "r")
songs_file = songs_file.read().split("\n")
songs = [s.rstrip().split('\t') for s in songs_file]
##print('\n\nA song sample from the input file:', songs[:3])
##print('\nThere are ', len(songs), ' number of songs\n')

songs_df = pd.DataFrame(data= songs, columns=['id', 'title', 'artist'])
songs_df = songs_df.set_index('id')
##print()
##print('A sample of songs when we reorganized them as a DataFrame with id as index:')
##print(songs_df.head())

# Pandas dataframes give us the ability to search through columns of our dataset
# For example, we can look at the songs of a certain artist:
##print()
##print('A sample of songs for specific artist usher:')
##print(songs_df[songs_df.artist == 'Usher'].head())
##
### Pandas also gives us the ability to retrieve info for multiple items (songs)
##print('Song of choice:')
##print(songs_df.iloc[2344])
song_id = 2344
##
### Ask the model for songs similar to this song
##print('Similar songs from the model are:\n')
##similar_songs = np.array(model.wv.most_similar(positive=str(song_id)))[:,0]
##print(songs_df.iloc[similar_songs]) # iloc = index location

def print_recommendations(song_id):
    print('\n\nRecommendations based on the song:')
    print(songs_df.iloc[song_id])
    print('\nAnd the songs recommended by the model')
    similar_songs = np.array(model.wv.most_similar(positive=str(song_id)))[:,0]
    return songs_df.iloc[similar_songs]

print(print_recommendations(1011))
print(print_recommendations(4000))
