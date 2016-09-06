import praw


app_id = 'YOUR_APP_ID_HERE'
app_secret = 'YOUR_APP_SECRET_HERE'
app_url = 'http://127.0.0.1:65010/authorize_callback'
app_scopes = 'account credits edit flair history identity livemanage modconfig modcontributors modflair modlog ' \
             'modothers modposts modself modwiki mysubreddits privatemessages read report save submit subscribe vote wikiedit wikiread'

refresh_token = 'YOUR_REFRESH_TOKEN_HERE'

def login():
    r = praw.Reddit(user_agent="Definitely Correct test by /u/rawkers")
    r.set_oauth_app_info(app_id, app_secret, app_url)
    r.refresh_access_information(refresh_token)
    return r


