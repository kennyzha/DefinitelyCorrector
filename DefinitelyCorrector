import praw
import time
import obot

words_to_match = ["definately", "definatly", "definantly", "definetly", "defiantly"]
cache = []

print("Logging in")
r = obot.login()
print("Logged in successfully")

def run_bot():
    print("Grabbing subreddit")
    subreddit = r.get_subreddit("test")
    print("Grabbing comments")
    comments = subreddit.get_comments()
    for comment in comments:
        comment_text = comment.body.lower()
        is_match = any(string in comment_text for string in words_to_match)
        if comment.id not in cache and is_match:
            print("Match Found! Comment id: " + comment.id)
            comment.reply('I think you meant to say "definitely"')
            print("Reply Successful!")
            cache.append(comment.id)
    print("Comment loop finished, time to sleep")


while True:
    run_bot()
    time.sleep(1)

