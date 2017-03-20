from rest_framework import viewsets
import rest_framework_filters
from api.serializers import *


class ProfileFilter(rest_framework_filters.FilterSet):
    id = rest_framework_filters.AllLookupsFilter()

    class Meta:
        model = Profile


class DistrictFilter(rest_framework_filters.FilterSet):
    id = rest_framework_filters.AllLookupsFilter()

    class Meta:
        model = District


class GramPanchayatFilter(rest_framework_filters.FilterSet):
    id = rest_framework_filters.AllLookupsFilter()

    class Meta:
        model = GramPanchayat


class WorkFilter(rest_framework_filters.FilterSet):
    id = rest_framework_filters.AllLookupsFilter()

    class Meta:
        model = Work


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    filter_class = ProfileFilter


class DistrictViewSet(viewsets.ModelViewSet):
    serializer_class = DistrictSerializer
    queryset = District.objects.all()
    filter_class = DistrictFilter


class GramPanchayatViewSet(viewsets.ModelViewSet):
    serializer_class = GramPanchayatSerializer
    queryset = GramPanchayat.objects.all()
    filter_class = GramPanchayat


class WorkViewSet(viewsets.ModelViewSet):
    serializer_class = WorkSerializer
    queryset = Work.objects.all()
    filter_class = WorkFilter

