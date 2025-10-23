# fetch data from reddit
import praw 
from .config import REDDIT_CLIENT_ID, REDDIT_SECRET, REDDIT_USER_AGENT

# api wrapper
def init_reddit():
    return praw.Reddit(
        client_id= REDDIT_CLIENT_ID,
        client_secret= REDDIT_SECRET,
        user_agent= REDDIT_USER_AGENT,
        )

# fetch posts
def fetch_posts(subreddit, keyword, limit=100):
    reddit = init_reddit()
    posts = reddit.subreddit(subreddit).search(keyword, limit=limit)
    return posts

