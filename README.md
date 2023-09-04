# Reddit Images Downloader

This script allows you to download images from Reddit subreddits using various options.

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
        ./get_reddit_images.py -s fujifilm photography -d ~/Pictures/RedditScreensaver -c -n 20 --type top --time all
        ```

## Options

- `-s`, `--subreddits`: Specify one or more subreddit names. (default: fujifilm)
- `-d`, `--destination`: Set the destination path to save downloaded images. (default: ~/Pictures/RedditScreensaver)
- `-c`, `--clear`: Clear the destination folder before fetching new images.
- `-n`, `--num-images`: Number of images to retrieve. (default: 15)
- `-t`, `--title-as-filename`: Save image files with titles as filenames.
- `--type`: Choose the post type: hot or top. (default: hot)
- `--time`: Choose the time range for top posts: hour, day, week, month, year, all. (default: day)

## Examples

- Fetch 15 hot images from the "fujifilm" subreddit and save them in the default destination:
    ```bash
    ./get_reddit_images.py
    ```

- Fetch top images of the week from the "photography" subreddit and save them with their titles as filenames:
    ```bash
    ./get_reddit_images.py -s photography -d ~/Desktop/Images -n 10 --type top --time week -t
    ```

## License

This script is licensed under the [MIT License](LICENSE).
