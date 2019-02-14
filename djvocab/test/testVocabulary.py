'''
Test Vocabulary

Created on  2019-02-14

@author: Aaron Kitzmiller <aaron_kitzmiller@harvard.edu>
@copyright: 2019 The Presidents and Fellows of Harvard College.
All rights reserved.
@license: GPL v2.0
'''

import unittest
from django.db import IntegrityError
from djvocab.models import Vocabulary

class TestVocabulary(unittest.TestCase):
    '''
    Test of vocabulary
    '''
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUniqueness(self):
        '''
        Ensure that duplicates cannot be entered
        '''
        vdata = {
            'key': 'akey',
            'value': 'avalue'
        }
        v = Vocabulary(**vdata)
        v.save()
        v2 = Vocabulary(**vdata)

        try:
            v2.save()
            self.assertTrue(False, 'Saved a duplicate record!')
        except IntegrityError:
            self.assertTrue(True, 'Duplicate prevented')