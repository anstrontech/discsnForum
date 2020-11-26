from django.forms import ModelForm
from .models import *


class CreateInDiscussion(ModelForm):
    class Meta:
        model= Discussion
        fields = "__all__"