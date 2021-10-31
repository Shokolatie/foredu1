from django.forms import ModelForm

from .models import AddClient

class AddClientForm(ModelForm):
    class Meta:
        model = AddClient
        fields = ('Name', 'Second_Name', 'Company', 'Work_field', 'content', 'email', 'vectorWork')
