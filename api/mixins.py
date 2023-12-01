from pprint import pprint
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from src.account.serializers import StaffSerializer

from src.account.staff import Staff
from src.administration.serializers import QuestionSerializer, Question


class CreateListRetrieveViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.DestroyModelMixin,
                                mixins.UpdateModelMixin,
                                viewsets.GenericViewSet):
    allowed_methods = ['GET', 'PUT', 'POST', 'DELETE', 'PATCH']


class StaffListRetrieveMixin(CreateListRetrieveViewSet):
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        _staff = Staff.objects.get(pk=serializer.data['staff'])
        _staff_data = StaffSerializer(_staff)
        _serializer = serializer.data
        _serializer["staff"] = _staff_data.data
        return Response(_serializer)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        _serializer = serializer.data
        for obj in _serializer:
            try:
                _staff = Staff.objects.get(pk=obj['staff'])
            except:
                _staff = Staff.objects.get(pk=obj['owner'])
            _staff_data = StaffSerializer(_staff)
            obj['staff'] = _staff_data.data
        return Response(_serializer)


class SurveyCreateListRetrieveViewSet(CreateListRetrieveViewSet):
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        _question = Question.objects.get(pk=serializer.data['question'])
        _questionSerializer = QuestionSerializer(_question)
        _serializer = serializer.data
        _serializer["question"] = _questionSerializer.data
        return Response(_serializer)
