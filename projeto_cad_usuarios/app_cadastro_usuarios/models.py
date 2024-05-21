from django.db import models
from django.db import models
from django.utils.translation import gettext_lazy

from django.db import models
from django.utils.translation import gettext_lazy as _

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    email = models.EmailField(_("Email"), max_length=254)

    def __str__(self):
        return self.nome

