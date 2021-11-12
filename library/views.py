from django.db.models.query import QuerySet
from library.models import Job, AppList
from library.serializers import JobSerializer, ApplicationSerializer

#my import
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
)
from rest_framework.viewsets import GenericViewSet

from .serializers import AppList, Job
from .models import Job, AppList


class JobList(GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin, DestroyModelMixin):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class ApplicationList(GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin, DestroyModelMixin):
    queryset = AppList.objects.all()
    serializer_class = ApplicationSerializer