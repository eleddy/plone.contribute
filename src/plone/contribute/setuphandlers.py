from plone import api
import logging
from zope.securitypolicy.interfaces import IPrincipalRoleManager


def setup_teams(context):
    if context.readDataFile('plone.contribute.various.txt') is None:
        return

    site = context.getSite()
    acl = site.acl_users
    # team mapped to default roles
    teams = {'mentors': ['Mentor', ],
             'DeveloperTeam': ['Contributor', ],
             'agreements': ['Agreement Coordinator', ],
             }
    for team, default_roles in teams.items():
        if not acl.get(team):
            logging.info("Adding group %s for plone.contribute functionality")
            api.group.create(groupname=team)
            for role in default_roles:
                acl.portal_role_manager.assignRoleToPrincipal(role, team)
