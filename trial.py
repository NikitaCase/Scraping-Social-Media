from keys import clientid, usr, pw, token, usa
import praw

reddit = praw.Reddit(
    client_id = clientid,
    client_secret = token, 
    user_agent = usa, 
    username = usr,     
    password = pw
)

subreddit = reddit.subreddit('wallstreetbets')

top_subreddit = subreddit.new(limit=10)

title_list = []

for post in top_subreddit:
    title = post.title
    title_text = title.split()
    title_list.append(title_text)

print(title_list)

### it works!! 