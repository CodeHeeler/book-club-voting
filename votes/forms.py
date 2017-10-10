from django.forms import ModelForm

from .models import Election


class ElectionForm(ModelForm):
    class Meta:
        model = Election
        fields = ['name', 'open', 'close', 'candidates']