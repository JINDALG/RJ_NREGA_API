from rest_framework import viewsets
import rest_framework_filters
from api.serializers import *


class EmployeeFilter(rest_framework_filters.FilterSet):
    id = rest_framework_filters.AllLookupsFilter()

    class Meta:
        model = Employee


class WorkFilter(rest_framework_filters.FilterSet):
    id = rest_framework_filters.AllLookupsFilter()
    district = rest_framework_filters.MethodFilter()
    grampanchayat = rest_framework_filters.MethodFilter()

    class Meta:
        model = Work

    def filter_district(self, name, qs, value):
        return Work.objects.filter(uploaded_by__grampanchayat__district=value)

    def filter_grampanchayat(self, name, qs, value):
        return Work.objects.filter(uploaded_by__grampanchayat=value)


class GramPanchayatFilter(rest_framework_filters.FilterSet):
    id = rest_framework_filters.AllLookupsFilter()

    class Meta:
        model = GramPanchayat


class ProfileFilter(rest_framework_filters.FilterSet):
    id = rest_framework_filters.AllLookupsFilter()
    grampanchayat = rest_framework_filters.RelatedFilter(GramPanchayatFilter)

    class Meta:
        model = Profile


class DistrictFilter(rest_framework_filters.FilterSet):
    id = rest_framework_filters.AllLookupsFilter()

    class Meta:
        model = District


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
    filter_class = GramPanchayatFilter


class WorkViewSet(viewsets.ModelViewSet):
    serializer_class = WorkSerializer
    queryset = Work.objects.all()
    filter_class = WorkFilter


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    filter_class = EmployeeFilter
