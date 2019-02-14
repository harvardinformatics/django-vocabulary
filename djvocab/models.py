# -*- coding: utf-8 -*-

'''
models djvocab

Created on  2019-02-14

@author: Aaron Kitzmiller <aaron_kitzmiller@harvard.edu>
@copyright: 2019 The Presidents and Fellows of Harvard College.
All rights reserved.
@license: GPL v2.0
'''

from django.db import models


class Vocabulary(models.Model):
    """
    Vocabulary to hold all lookup values where key is the table name
    """
    class Meta:
        db_table = 'vocabulary'
        unique_together = ('key', 'value')
        verbose_name_plural = 'vocabularies'

    key = models.CharField(max_length=100)
    value = models.CharField(max_length=1000)
    description = models.CharField(max_length=2000, blank=True)
    order = models.IntegerField(default=0)
