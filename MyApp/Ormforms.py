from django.forms import ModelForm
from MyApp.models import Student

class Studentform(ModelForm):
    class Meta:
        model=Student
        fields="__all__"
        # fields=["name","qualification","persentage"]
        