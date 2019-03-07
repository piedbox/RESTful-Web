from rest_framework import status
from mainapp.models import Toy
from mainapp.serializers import ToySerializer, UserSerializer
# from rest_framework.authentication import SessionAuthentication,                                             BasicAuthentication
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView


class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class ToysList(generics.ListCreateAPIView):
    """Показать список элементов. Или загрузить свой."""

    queryset = Toy.objects.all()
    serializer_class = ToySerializer
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ToyDetail(generics.RetrieveUpdateDestroyAPIView):
    """Показать/изменить/удалить элемент."""

    queryset = Toy.objects.all()
    serializer_class = ToySerializer
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (permissions.IsAuthenticated,)


class UserList(generics.ListAPIView):
    """Все пользователи."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (permissions.IsAuthenticated,)



class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (permissions.IsAuthenticated,)
