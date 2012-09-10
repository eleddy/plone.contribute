# -*- coding: utf-8 -*-
from five import grok
from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from plone.contribute import gitintegration
import logging
from plone import api
import random
from Products.CMFCore.interfaces import ISiteRoot


class SetupNewContributor(grok.View):
    """
    This view will add a user to the github repo, add them to the right
    groups in active directory, send off some emails, and party like its
    1999 all with one click. This is a browser view because there are
    probably cases when we may not be in workflow and will still need to
    make someone a contributor.
    """
    grok.context(ISiteRoot)
    grok.require('plone.contribute.approveAgreement')
    grok.name('setup_contributor')

    def render(self):
        """
        returns plone.org id of new mentor
        """
        plone_id = self.request.form.get('plone_id')
        github_id = self.request.form.get('github_id')
        email = self.request.form.get('email')

        # add to github group
        registry = getUtility(IRegistry)
        token = registry['plone.contribute.githubtoken']
        if not token:
            logging.error("There is no token on file for github integration -" +
                           "please add plone.contribute.githubtoken")
            api.portal.show_message(message='Github is not configured. ' +
                                            'Please manually add to dev team.',
                                    request=self.request,
                                    type='error')
        else:
            if gitintegration.add_user_to_devteam(github_id, token):
                api.portal.show_message(message='Added to github!',
                                        request=self.request)
            else:
                api.portal.show_message(message='Unknown error adding to github.',
                                        request=self.request,
                                        type='error')
        # add to proper plone group
        try:
            api.group.add_user(groupname='DeveloperTeam', username=plone_id)
            api.portal.show_message(message='Added to plone.org developer team!',
                                    request=self.request)
        except ValuError, e:
            logging.error("Could not add contributor %s to DeveloperTeam: " %
                          (plone_id, e))
            api.portal.show_message(message='Unknown error adding to plone.org ' +
                                    'DeveloperTeam.',
                                    request=self.request,
                                    type='error')

        # send welcome email to user
        api.portal.send_email(
            recipient=email,
            sender="assignments@plone.org",
            subject="Welcome to the Plone Core Developer Team!",
            body="""Something to welcome the chump with contact info for mentor""",
        )

        # send email to mentor. we will rand this shit for now
        mentors = api.user.get_users(groupname='mentors')
        new_mentor = random.choice(mentors)

        api.portal.send_email(
            recipient=new_mentor.email,
            sender="assignments@plone.org",
            subject="New Member of the Plone Core Developer Team!",
            body="""Hey mentor, please contact this person and help them get going""",
        )

        # party like it's 1999

