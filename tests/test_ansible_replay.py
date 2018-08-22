#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_ansible_replay
----------------------------------

Tests for `ansible_replay` module.
"""

import unittest

import ansible_replay


class TestAnsible_replay(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        assert(ansible_replay.__version__)

    def tearDown(self):
        pass
