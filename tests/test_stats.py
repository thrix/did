#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "Chris Ward" <cward@redhat.com>

from __future__ import unicode_literals, absolute_import


def test_Stats():
    # simple test that import works
    from did.stats import Stats
    assert Stats


def test_StatsGroup():
    # simple test that import works
    from did.stats import StatsGroup
    assert StatsGroup


def test_UserStats():
    # simple test that import works
    from did.stats import UserStats
    assert UserStats


def test_EmptyStats():
    # simple test that import works
    from did.stats import EmptyStats
    assert EmptyStats


def test_EmptyStatsGroup():
    # simple test that import works
    from did.stats import EmptyStatsGroup
    assert EmptyStatsGroup
