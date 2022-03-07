from django.forms import ModelForm
from BazaFakeKont.models import Webpage

class PageForm(ModelForm):
    class Meta:
        model = Webpage
        fields = ['name', 'description', 'link']