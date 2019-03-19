#!/usr/bin/python3 -tt
# -*- coding: utf-8 -*-

__all__ = ['Manager']

from twisted.internet.threads import deferToThread
from twisted.internet import task, reactor
from twisted.python import log

from dovolenkator.elanor import Elanor
class Manager(object):
    def __init__(self, db):
        self.db = db
        self.elanor = Elanor(self)

    def get_zustatek(self, userid, month):
        return {
                'start': self.elanor.get_starting_days(userid), 
                'correction': self.elanor.get_correction(userid, month)
                }

# vim:set sw=4 ts=4 et:
