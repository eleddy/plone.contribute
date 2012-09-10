#!/usr/bin/python
"""
Helpers for integrating with github.
"""
import requests


DEV_TEAM_ID = 14533


def get_members(token):
    """
    List the members of the dev team
    XXX: Currently not used.
    """
    r = requests.get('https://api.github.com/teams/%s/members' % DEV_TEAM_ID,
        headers={'Authorization': 'Bearer %s' % token})
    if r.status_code != 200:
        return False

    return [user['login'] for user in r.json]


def user_in_devteam(username, token):
    """
    Check to see if a user is already a member of the dev team in github
    """
    url = 'https://api.github.com/teams/%s/members/%s' % (DEV_TEAM_ID,
                                                          username)
    r = requests.get(url, headers={'Authorization': 'Bearer %s' % token,
                                   'content-length': '0'})
    # f*cking brilliant github. 404 means user is not there AND that you
    # are pinging the wrong url. rawr.
    if r.status_code == 204:
        return True
    return False


def add_user_to_devteam(username, token):
    """
    Add a user to the team in github
    """
    if not user_in_devteam(username, token):
        url = 'https://api.github.com/teams/%s/members/%s' % (DEV_TEAM_ID,
                                                              username)
        r = requests.put(url, headers={'Authorization': 'Bearer %s' % token,
                                        'content-length': '0'})
        if r.status_code != 204:
            return False
    return True


if __name__ == '__main__':
    if add_user_to_devteam('digiyouadmin',
                           ''):
        print "Added!"
    else:
        print "Uh oh, something went wrong"
