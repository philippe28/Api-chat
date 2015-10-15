from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from django.contrib.auth.models import User


#modificado models
class Chat(models.Model):
    """Development iteration period."""
    
    nome = models.ForeignKey(settings.AUTH_USER_MODEL, 
	null=True, blank=True)
    mensagem = models.TextField(blank=True, default='')
    data = models.DateTimeField(default=datetime.now)
    
    #assigned = models.ForeignKey(settings.AUTH_USER_MODEL, 
	#null=True, blank=True)
    
    def __str__(self):
        return self.name or _('Chat ending %s') % self.end
