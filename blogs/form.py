from django.forms import ModelForm
from blogs.models import people


class peopleModelForm(ModelForm) :
    class Meta:
        model = people
        fields = ['name' , 'age' , 'phone']