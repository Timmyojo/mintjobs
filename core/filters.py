import django_filters
from django_filters import CharFilter

from .models import *

class JobFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', label='Job Title', lookup_expr='icontains')
    location = CharFilter(field_name='location', label='Location', lookup_expr='icontains')
    class Meta:
        model = Job
        fields = ['jobtype', 'level', 'workplace']