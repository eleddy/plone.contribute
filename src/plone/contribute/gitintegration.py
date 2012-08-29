#!/usr/bin/python
"""
Helpers for integrating with github.
"""
import requests


TOKEN = 'dfd'
DEV_TEAM_ID = 14533


def get_members():
    r = requests.get('https://api.github.com/teams/%s/members' % DEV_TEAM_ID,
        headers={'Authorization': 'Bearer %s' % TOKEN})
    if r.status_code != 200:
        return False

    return [user['login'] for user in r.json]


def user_in_devteam(username):
    """
    Check to see if a user is already a member of the dev team in github
    """
    url = 'https://api.github.com/plone/teams/%s/members/%s' % (DEV_TEAM_ID, username)
    r = requests.get(url, headers={'Authorization': 'Bearer %s' % TOKEN, 'content-length' : '0'})
    # f*cking brilliant github. 404 means user is not there AND that you
    # are pinging the wrong url. rawr.
    if r.status_code == 200:
        return True
    return False


def get_user_id_from_login(login):
    """
    User login != id in plone. Lookup the id given the human
    username that we have all adjusted to
    """
    r = requests.get('https://api.github.com/users/%s' % login,
                     headers={'Authorization': 'Bearer %s' % TOKEN})
    if r.status_code != 200:
        return False
    return r.json['id']


def add_user_to_devteam(username):
    """
    Add a user to the team in github
    """
    import pdb;pdb.set_trace()
    if not user_in_devteam(username):
        url = 'https://api.github.com/plone/teams/%s/members/%s' % (DEV_TEAM_ID, username)
        r = requests.put(url, headers={'Authorization': 'Bearer %s' % TOKEN, 'content-length' : '0'})
        if r.status_code != 204:
             return False
    return True


if __name__ == '__main__':
    if add_user_to_devteam('ericof'):
        print "Added!"
