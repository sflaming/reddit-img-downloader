~~# Reddit Images Downloader with Metadata

This script downloads popular images from any Reddit subreddit.

## Features

- Download images from one or more subreddits.
- Images are saved with the URL, username, and title of the original post in EXIF metadata.
- Supports either hot or top posts, with all time range options for top posts.
- Customize the destination folder, number of images, and more.

## Usage

1. Make the script executable:
    ```bash
    chmod +x get_reddit_images.py
    ```

2. Run the script with desired options. For example:

    - Fetch 20 hot images from the "fujifilm" and "photography" subreddits:
        ```bash
        ./get_reddit_images.py -s fujifilm photography -d ~/Pictures/RedditScreensaver -c -n 20
        ```

    - Fetch 20 top images of all time from the "fujifilm" and "photography" subreddits:
        ```bash
        ./get_reddit_images.py -s fujifilm photography -d ~/Pictures/RedditScreensaver -c -n 20 -f top -r all
        ```

## Options

- `-s`, `--subreddits`: Specify one or more subreddit names. (default: fujifilm)
- `-d`, `--destination`: Set the destination path to save downloaded images. (default: ~/Pictures/RedditScreensaver)
- `-c`, `--clear`: Clear the destination folder before fetching new images.
- `-n`, `--num-images`: Number of images to retrieve. (default: 15)
- `-t`, `--title-as-filename`: Save image files with titles as filenames.
- `-f`, `--filter`: Choose the post filter: hot or top. (default: hot)
- `-r`, `--range`: Choose the time range for top posts: hour, day, week, month, year, all. (default: day)

## Examples

- Fetch hot images from the "fujifilm" subreddit and save them in the default destination:
    ```bash
    ./get_reddit_images.py
    ```

- Fetch top images of the day from the "photography" subreddit and save them with titles as filenames:
    ```bash
    ./get_reddit_images.py -s photography -d ~/Desktop/Images -n 10 -f top -r day -t
    ```

## Metadata

- The URL is saved to the File Source EXIF field.
- The username and post title are saved to the User Comment EXIF field. 

## License

This script is licensed under the [MIT License](LICENSE).~~
