from django.contrib.auth import get_user_model
from rest_framework import authentication, permissions, viewsets, filters
from .forms import ChatFilter
from .models import Chat
from .serializers import ChatSerializer


User = get_user_model()

#modificado views
class ChatViewSet( viewsets.ModelViewSet):

    queryset = Chat.objects.order_by('data')
    serializer_class = ChatSerializer
    filter_class = ChatFilter
    search_fields = ('nome', )
    ordering_fields = ('data', )
    
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,    
    )
    permission_classes = (
        permissions.IsAuthenticated,
        #permissions.IsAuthenticatedOrReadOnly,
    )
