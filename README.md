# Reddit Image Downloader

This fetches popular images from the Reddit subreddit(s) specified by `-s (--subreddits)` flag. Provide one or more space-separated subreddits to download the top 15 "hot" images.

Set the save location, the number of posts to check for images, and whether to clear the folder before downloading new images.

For example, you can run the script with the `-l` option to specify the limit for the number of hot posts to retrieve. For example:

```bash
chmod +x get_hot_images.py
./get_hot_images.py -s fujifilm fujix -d ~/Pictures/RedditScreensaver -c -l 20
```

This will fetch hot images from the "r/fujifilm" and "r/fujix" subreddits, store them in the "~/Pictures/RedditScreensaver" directory, clear the folder before fetching new images, and retrieve a maximum of 20 hot posts from each subreddit.

If you don't provide the `--limit` option, the default limit of 15 will be used.

Feel free to customize the script further based on your needs. If you have any more questions or need further assistance, please let me know!

## Version notes
0.1
