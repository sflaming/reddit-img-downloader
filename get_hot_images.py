#!/usr/bin/env python3

import os
import requests
import sys
import argparse
import shutil


def download_image(url, title, destination_dir, use_title_as_filename):
    if use_title_as_filename:
        filename = os.path.join(destination_dir, f"{title}.jpg")
    else:
        filename = os.path.join(destination_dir, os.path.basename(url))

    if not os.path.exists(filename):
        try:
            response = requests.get(url, headers={"User-Agent": "RedditImagesDownloader"})
            if response.status_code == 200:
                with open(filename, 'wb') as f:
                    f.write(response.content)
                print(f"Downloaded: {title}")
            else:
                print(f"Failed to download: {title} (Status code: {response.status_code})")
        except Exception as e:
            print(f"Error while downloading: {title} - {e}")
    else:
        print(f"Skipped (Already Exists): {title}")


def fetch_reddit_images(subreddits, destination_dir, num_images, use_title_as_filename, post_filter, time_range):
    for subreddit in subreddits:
        posts_processed = 0
        after = None

        while posts_processed < num_images:
            # Build the URL based on user's choices
            if post_filter == "hot":
                url = f"https://www.reddit.com/r/{subreddit}/hot/.json?limit=100"
            elif post_filter == "top":
                url = f"https://www.reddit.com/r/{subreddit}/top/.json?t={time_range}&limit=100"
            else:
                print(f"Invalid post filter: {post_filter}")
                break

            if after:
                url += f"&after={after}"
            headers = {"User-Agent": "RedditImagesDownloader"}

            try:
                response = requests.get(url, headers=headers)
                response.raise_for_status()  # Check for any request errors
                data = response.json()

                if "data" in data and "children" in data["data"]:
                    for post in data["data"]["children"]:
                        if "data" in post and "url" in post["data"] and post["data"]["url"].endswith(('.jpg', '.png', '.jpeg', '.gif')):
                            title = post["data"]["title"]
                            download_image(post["data"]["url"], title, destination_dir, use_title_as_filename)
                            posts_processed += 1
                            if posts_processed >= num_images:
                                break
                else:
                    print(f"Failed to retrieve data from subreddit: {subreddit}")
                    break

                if "data" in data and "after" in data["data"]:
                    after = data["data"]["after"]
                else:
                    break
            except requests.exceptions.RequestException as re:
                print(f"API Request Error for subreddit {subreddit}: {re}")
                break
            except Exception as e:
                print(f"Unexpected Error for subreddit {subreddit}: {e}")
                break


def main():
    parser = argparse.ArgumentParser(description="Fetch images from subreddits.")
    parser.add_argument("-s", "--subreddits", nargs="+", default=["fujifilm"], help="Subreddit name(s) (default: fujifilm)")
    parser.add_argument("-d", "--destination", default="~/Pictures/RedditImageDownloader", help="Destination path (default: ~/Pictures/RedditImageDownloader)")
    parser.add_argument("-c", "--clear", action="store_true", help="Clear the folder before fetching new images")
    parser.add_argument("-n", "--num-images", type=int, default=15, help="Number of images to retrieve (default: 15)")
    parser.add_argument("-t", "--title-as-filename", action="store_true", help="Save image files with titles as filenames")
    parser.add_argument("-f", "--filter", choices=["hot", "top"], default="hot", help="Post filter: hot or top. (default: hot)")
    parser.add_argument("-r", "--range", choices=["hour", "day", "week", "month", "year", "all"], default="day", help="Time range for top posts. (default: day)")

    args = parser.parse_args()

    # Resolve the destination path
    destination_dir = os.path.expanduser(args.destination)

    # Clear the folder if the --clear option is provided
    if args.clear:
        try:
            shutil.rmtree(destination_dir)
        except FileNotFoundError:
            pass  # The folder doesn't exist yet

    # Create the destination directory if it doesn't exist
    os.makedirs(destination_dir, exist_ok=True)

    # Fetch the specified number of images using the user's choices
    fetch_reddit_images(args.subreddits, destination_dir, args.num_images, args.title_as_filename, args.filter, args.range)


if __name__ == "__main__":
    main()
