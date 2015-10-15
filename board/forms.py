import django_filters
from django.contrib.auth import get_user_model
from .models import Chat
      
      
User = get_user_model()       

#modificado form
class ChatFilter(django_filters.FilterSet):
    
    data_min = django_filters.DateFilter(name='data', lookup_type='gte')
    data_max = django_filters.DateFilter(name='data', lookup_type='lte')
    
    class Meta:
        model = Chat
        fields = ('data_min', 'data_max', )

