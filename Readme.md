Reddit Shell
=========================

This project is just a simple project that provides a command line interface for Reddit.


### Supported Commands

__ls__ - lists reddit submissions for the current subreddit.  Extra parameters are [limit]

__cd__ - change to a different subreddit

__quit__ - quits the application


### Examples

Changes to java subreddit
``` 
cd java
```

Lists submissions for a subreddit
```
ls
```

Lists the top 5 submissions for a subreddit
```
ls 5
```  

#### praw.ini

This application supports the inclusion of a praw.ini file at the top level of the application. An example praw.ini file is:

```ini
[DEFAULT]
# A boolean to indicate whether or not to check for package updates.
check_for_updates=True

# Object to kind mappings
comment_kind=t1
message_kind=t4
redditor_kind=t2
submission_kind=t3
subreddit_kind=t5

# The URL prefix for OAuth-related requests.
oauth_url=https://oauth.reddit.com

# The URL prefix for regular requests.
reddit_url=https://www.reddit.com

# The URL prefix for short URLs.
short_url=https://redd.it

[reddit_shell]
client_id=<CLIENT ID>
client_secret=<CLIENT SECRET>
password=<REDDIT PASSWORD>
username=<REDDIT USERNAME>
```
