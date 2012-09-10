# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from plone.contribute.tests.base import IntegrationTestCase
from plone import api

import unittest2 as unittest


class TestInstall(IntegrationTestCase):

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']

    def test_product_installed(self):
        """Test if tutorial.todoapp is installed in portal_quickinstaller."""
        installer = api.portal.get_tool('portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('plone.contribute'))

    def test_dependencies_installed(self):
        """Test that all dependencies are installed."""
        installer = api.portal.get_tool('portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('plone.app.dexterity'))

    def test_contributor_agreement_installed(self):
        """
        Test that contributor agreement content type
        is listed in portal_types.
        """
        types = api.portal.get_tool('portal_types')
        self.assertIn('contributor_agreement', types.objectIds())

    def test_contributor_agreement_workflow_installed(self):
        """"Test that contributor_agreement_workflow is listed in portal_workflow."""
        workflow = api.portal.get_tool('portal_workflow')
        self.assertIn('contributor_agreement_workflow', workflow.objectIds())

    def test_contributor_agreement_workflow(self):
        """Test if workflow Contributor Agreement content type."""
        workflow = api.portal.get_tool('portal_workflow')
        for portal_type, chain in workflow.listChainOverrides():
            if portal_type in ('contributor_agreement', ):
                self.assertEquals(('contributor_agreement_workflow',), chain)

    def test_team_setup(self):
        """ Validate that the teams are installed as expected """
        acl = self.portal.acl_users
        self.assertIsNotNone(acl.getGroup('mentors'))


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above."""
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
