from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from administrativo.serializers import UserSerializer, GroupSerializer, \
    EdificioSerializer, DepartamentoSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class EdificioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Edificio.objects.all()
    serializer_class = EdificioSerializer
    permission_classes = [permissions.IsAuthenticated]


class DepartamentoViewSet(viewsets.ModelViewSet):
    # class DepartamentoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    # permission_classes = [permissions.IsAuthenticated]
