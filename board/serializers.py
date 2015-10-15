from datetime import date
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Chat


User = get_user_model()

#modificado serializer
class ChatSerializer(serializers.ModelSerializer):    

    nome = serializers.SlugRelatedField(
        slug_field=User.USERNAME_FIELD, required=False, allow_null=True,
        queryset=User.objects.all())

    class Meta:
        model = Chat
        fields = ('id', 'nome', 'mensagem', )

    def create(self, validated_data):

        return Chat.objects.create(**validated_data)
