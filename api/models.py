from __future__ import unicode_literals

from django.db import models

ROLE_TYPES = (
    ('District Officer', 'District Officer'),
    ('Gram Panchayat Officer', 'Gram Panchayat Officer')
)

BLOCK_TYPES = (
    ('District', 'District'),
    ('Gram Panchayat', 'Gram Panchayat')
)


class Profile(models.Model):

    userid = models.CharField(max_length=12)
    password = models.CharField(max_length=20)
    role = models.CharField(choices=ROLE_TYPES, max_length=20)


class Block(models.Model):
    type = models.CharField(choices=BLOCK_TYPES, max_length=10)
    block_id = models.CharField(max_length=10)
    name = models.CharField(max_length=25)
    officer = models.ForeignKey(Profile)


class Work(models.Model):
    emp_aadhar = models.CharField(max_length=12)
    description = models.CharField(max_length=100)
    photo = models.TextField(null=True, blank=True)
    timestamp = models.CharField(max_length=20, blank=True, null=True)
    uploaded_by = models.ForeignKey(Profile, null=True, blank=True, related_name='uploaded_by')
    verified_by = models.ForeignKey(Profile, null=True, blank=True, related_name='verified_by')
