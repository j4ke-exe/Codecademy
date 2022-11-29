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

#-----------------------------
# Removing From a Set

song_data_users = {'Retro Words': ['pop', 'onion', 'warm', 'helloworld', 'happy', 'spam', 'electric']}

# Write your code below!
tag_set = set(song_data_users['Retro Words'])
tag_set.remove('onion')
tag_set.remove('helloworld')
tag_set.remove('spam')

song_data_users = {'Retro Words': tag_set}
print(song_data_users)

#----------------------------
# Finding Elements in a Set

allowed_tags = ['pop', 'hip-hop', 'rap', 'dance', 'electronic', 'latin', 'indie', 'alternative rock', 'classical', 'k-pop', 'country', 'rock', 'metal', 'jazz', 'exciting', 'sad', 'happy', 'upbeat', 'party', 'synth', 'rhythmic', 'emotional', 'relationship', 'warm', 'guitar', 'fiddle', 'romance', 'chill', 'swing']

song_data_users = {'Retro Words': ['pop', 'explosion', 'hammer', 'bomb', 'warm', 'due', 'writer', 'happy', 'horrible', 'electric', 'mushroom', 'shed']}

# Write your code below!
tag_set = set(song_data_users['Retro Words'])

bad_tags = []
for tag in tag_set:
  if tag not in allowed_tags:
    bad_tags.append(tag)

for tag in bad_tags:
  tag_set.remove(tag)

song_data_users = {'Retro Words': tag_set}
print(song_data_users)
