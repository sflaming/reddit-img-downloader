#!/bin/bash

# Step 1: Create the slideshow directory if it doesn't exist
mkdir -p ~/Users/username/bin/slideshow2

# Step 2: Get the top 15 hot images from the /fujfilm subreddit using the Python script
python3 get_hot_images.py ~/Users/username/bin/slideshow2
