from django.forms import ModelForm
from api.docModels import CityUploadDoc

class CityUploadForm(ModelForm):
    class Meta:
        model = CityUploadDoc
        exclude = ()