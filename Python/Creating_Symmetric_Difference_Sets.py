user_song_history = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
                     'Stomping Cue': ['country', 'fiddle', 'party'],
                     'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
                     'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

friend_song_history = {'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
                     'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
                     'Wait For Limit': ['rap', 'upbeat', 'romance', 'relationship'],
                     'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

# Write your code below!
user_tags = set()
for key, val in user_song_history.items():
  user_tags.update(set(val))

friend_tags = set()
for key, val in friend_song_history.items():
  friend_tags.update(set(val))

# Method 1
unique_tags = friend_tags.symmetric_difference(user_tags)

# Method 2
unique_tags = friend_tags ^ user_tags

print(unique_tags)
