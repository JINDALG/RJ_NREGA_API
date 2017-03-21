from __future__ import unicode_literals

from django.db import models
from django_extensions.db.models import TimeStampedModel

ROLE_TYPES = (
    ('District Officer', 'District Officer'),
    ('Gram Panchayat Officer', 'Gram Panchayat Officer')
)

BLOCK_TYPES = (
    ('District', 'District'),
    ('Gram Panchayat', 'Gram Panchayat')
)

GENDER_TYPES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
)


class Profile(TimeStampedModel):
    userid = models.CharField(max_length=12)
    password = models.CharField(max_length=20)
    role = models.CharField(choices=ROLE_TYPES, max_length=20)

    def __str__(self):
        return '-'.join([self.userid, self.role])


class District(TimeStampedModel):
    district_id = models.CharField(max_length=20)
    name = models.CharField(max_length=25)
    officer = models.ForeignKey(Profile)

    def __str__(self):
        return '-'.join([self.district_id, self.name])


class GramPanchayat(TimeStampedModel):
    gp_id = models.CharField(max_length=10)
    name = models.CharField(max_length=25)
    officer = models.ForeignKey(Profile)
    district = models.ForeignKey(District)

    def __str__(self):
        return '-'.join([self.gp_id, self.name])


class Work(TimeStampedModel):
    emp_aadhar = models.CharField(max_length=12)
    description = models.CharField(max_length=100)
    photo = models.TextField(null=True, blank=True)
    timestamp = models.CharField(max_length=50, blank=True, null=True)
    uploaded_by = models.ForeignKey(Profile, null=True, blank=True, related_name='uploaded_by',
                                    related_query_name='work')
    verified_by = models.ForeignKey(Profile, null=True, blank=True, related_name='verified_by')
    payment_done = models.BooleanField(default=False)

    def __str__(self):
        return '-'.join([self.emp_aadhar, self.timestamp])


class Employee(TimeStampedModel):
    emp_aadhar = models.CharField(max_length=12)
    name = models.CharField(max_length=30)
    district = models.ForeignKey(District, null=True, blank=True)
    gender = models.CharField(choices=GENDER_TYPES, max_length=10)
    start_date = models.DateField(null=True, blank=True)
    employement_days = models.IntegerField(default=0, null=True, blank=True)
    registered_by = models.ForeignKey(Profile, null=True, blank=True)
