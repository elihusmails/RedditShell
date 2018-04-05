import requests
from datetime import datetime

def list_subreddit(subreddit):

    url = 'http://www.reddit.com/.json'
    if subreddit is not '':
        url = 'http://www.reddit.com/r/' + subreddit + '/.json'

    response = requests.get(url, headers = {'User-agent': '/u/elihusmails Reddit Shell 0.1'})
    response_json = response.json()

    print('ID\t' + ('{0: <16}'.format('AUTHOR')) + '\tTITLE')
    print('-------------------------------------------------------------------------')
    for thing in response_json['data']['children']:
        title = thing['data']['title']
        id = thing['data']['id']
        author = thing['data']['author']
        utc = thing['data']['created_utc']
        created = datetime.utcfromtimestamp(utc).isoformat()
        print(id + '\t' + created + '\t' + ('{0: <16}'.format(author)) + '\t' + title)


if __name__ == "__main__":

    subreddit = ''

    while True:

        cmd_input = input('reddit/' + subreddit + ' :')
        cmds = cmd_input.split()

        if cmds[0] == 'quit':
            exit(0)
        elif cmds[0] == 'cd':
            subreddit = cmds[1]
        elif cmds[0] == 'ls':
            list_subreddit(subreddit)

