genre_results = ['rap', 'classical', 'rock', 'rock', 'country', 'rap', 'rock', 'latin', 'country', 'k-pop', 'pop', 'rap', 'rock', 'k-pop',  'rap', 'k-pop', 'rock', 'rap', 'latin', 'pop', 'pop', 'classical', 'pop', 'country', 'rock', 'classical', 'country', 'pop', 'rap', 'latin']

# Write your code below!
survey_genres = set(genre_results)
print(survey_genres)

survey_abbreviated = {genre[0:3] for genre in survey_genres}
print(survey_abbreviated)

#------------------------------
# Creating a Frozenset

top_genres = ['rap', 'rock', 'pop']

# Write your code below!
frozen_top_genres = frozenset(top_genres)
print(frozen_top_genres)

#------------------------------
# Adding to a Set

song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electric']}

user_tag_1 = 'warm'
user_tag_2 = 'exciting'
user_tag_3 = 'electric'

# Write your code below!
tags = (user_tag_1, user_tag_2, user_tag_3)

tag_set = set(song_data['Retro Words'])
tag_set.update(tags)

song_data = {'Retro Words': tag_set}

print(song_data)
