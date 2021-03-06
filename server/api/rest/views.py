from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.rest.serializers import *
from api.rest.models import *
from url_filter.integrations.drf import DjangoFilterBackend


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class HomeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Home.objects.all()
    serializer_class = HomeSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['agencyId']

class AgentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

class AgencyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Agency.objects.all()
    serializer_class = AgencySerializer
