#!/usr/bin/env python3

import os
import requests
import sys


def download_image(url, destination_dir):
    filename = os.path.join(destination_dir, os.path.basename(url))
    if not os.path.exists(filename):
        try:
            response = requests.get(url, headers={"User-Agent": "HotImagesDownloader"})
            if response.status_code == 200:
                with open(filename, 'wb') as f:
                    f.write(response.content)
                print(f"Downloaded: {url}")
            else:
                print(f"Failed to download: {url} (Status code: {response.status_code})")
        except Exception as e:
            print(f"Error while downloading: {url} - {e}")
    else:
        print(f"Skipped (Already Exists): {url}")


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 get_hot_images.py <destination_dir> <subreddit1,subreddit2,...>")
        sys.exit(1)

    destination_dir = sys.argv[1]
    subreddits = sys.argv[2].split(',')

    for subreddit in subreddits:
        # Fetch the top 15 hot posts from the subreddit using Reddit API
        url = f"https://www.reddit.com/r/{subreddit}/hot/.json?limit=15"
        headers = {"User-Agent": "HotImagesDownloader"}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Check for any request errors
            data = response.json()

            if "data" in data and "children" in data["data"]:
                for post in data["data"]["children"]:
                    if "data" in post and "url" in post["data"] and post["data"]["url"].endswith(('.jpg', '.png', '.jpeg', '.gif')):
                        download_image(post["data"]["url"], destination_dir)
            else:
                print(f"Failed to retrieve data from /r/{subreddit}.")

        except requests.exceptions.RequestException as re:
            print(f"API Request Error for /r/{subreddit}: {re}")
        except Exception as e:
            print(f"Unexpected Error for /r/{subreddit}: {e}")


if __name__ == "__main__":
    main()
