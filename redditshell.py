from datetime import datetime
import praw

USER_AGENT = '/u/elihusmails Reddit Shell 0.1'


def list_subreddit2(reddit, subreddit, max=25):
    submissions = reddit.subreddit(subreddit).hot(limit=max)
    print('{0}\t{1}\t{2: <17}\t{3: <16}\t{4}'.format('ID', 'SCORE', 'CREATED', 'AUTHOR', 'TITLE'))
    print('-------------------------------------------------------------------------')
    for submission in submissions:
        title = submission.title
        id = submission.id
        author = submission.author.name
        utc = submission.created_utc
        created = datetime.utcfromtimestamp(utc).isoformat()
        score = str(submission.score)
        print( '{0}\t{1}\t{2}\t{3: <16}\t{4}'.format(id, score, created, author, title))

if __name__ == "__main__":

    reddit = praw.Reddit('reddit_shell', user_agent=USER_AGENT)

    subreddit = ''

    while True:

        cmd_input = input('reddit/' + subreddit + ' :')
        cmds = cmd_input.split()

        if len(cmds) is 0:
            continue

        if cmds[0] == 'quit':
            exit(0)
        elif cmds[0] == 'cd':
            subreddit = cmds[1]
        elif cmds[0] == 'ls':
            if len(cmds) == 2:
                list_subreddit2(reddit, subreddit, int(cmds[1]))
            else:
                list_subreddit2(reddit, subreddit)

