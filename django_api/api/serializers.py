from rest_framework import serializers
from api.models import *


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile


class DistrictSerializer(serializers.ModelSerializer):

    class Meta:
        model = District


class GramPanchayatSerializer(serializers.ModelSerializer):

    class Meta:
        model = GramPanchayat


class WorkSerializer(serializers.ModelSerializer):
    uploaded_by_detail = ProfileSerializer(read_only=True, source='uploaded_by')

    class Meta:
        model = Work


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee