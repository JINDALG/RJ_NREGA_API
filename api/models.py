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

    def __str__(self):
        return '-'.join([self.userid, self.role])


class District(models.Model):
    district_id = models.CharField(max_length=20)
    name = models.CharField(max_length=25)
    officer = models.ForeignKey(Profile)

    def __str__(self):
        return '-'.join([self.district_id, self.name])


class GramPanchayat(models.Model):
    gp_id = models.CharField(max_length=10)
    name = models.CharField(max_length=25)
    officer = models.ForeignKey(Profile)
    district = models.ForeignKey(District)

    def __str__(self):
        return '-'.join([self.gp_id, self.name])


class Work(models.Model):
    emp_aadhar = models.CharField(max_length=12)
    description = models.CharField(max_length=100)
    photo = models.TextField(null=True, blank=True)
    timestamp = models.CharField(max_length=50, blank=True, null=True)
    uploaded_by = models.ForeignKey(Profile, null=True, blank=True, related_name='uploaded_by')
    verified_by = models.ForeignKey(Profile, null=True, blank=True, related_name='verified_by')

    def __str__(self):
        return '-'.join([self.emp_aadhar, self.timestamp])
