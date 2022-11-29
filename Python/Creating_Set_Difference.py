song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
             'Wait For Limit': ['rap', 'upbeat', 'romance', 'relationship'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
             'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
             'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
             'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional'],
             'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_liked_song = {'Back To Art': ['pop', 'sad', 'emotional', 'relationship']}
user_disliked_song = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth']}

# Write your code below!

# Method 1
tag_diff = set(user_liked_song['Back To Art']).difference(user_disliked_song['Retro Words'])

# Method 2
tag_diff = set(user_liked_song['Back To Art']) - set(user_disliked_song['Retro Words'])

recommended_songs = {}
for key, val in song_data.items():
  for tags in val:
    if tags in tag_diff:
      if key not in user_liked_song and key not in user_disliked_song:
        recommended_songs[key] = val
print(recommended_songs)
