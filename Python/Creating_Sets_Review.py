music_tags = {'pop', 'warm', 'happy', 'electronic', 'synth', 'dance', 'upbeat'}

# Write your code below!
my_tags = frozenset(['pop', 'electronic', 'relaxing', 'slow', 'synth'])

# Union
frozen_tag_union = my_tags | music_tags

# Intersection
regular_tag_intersect = music_tags & my_tags

# Difference
frozen_tag_difference = my_tags - music_tags

# Symmetric Difference
regular_tag_sd = music_tags ^ my_tags
