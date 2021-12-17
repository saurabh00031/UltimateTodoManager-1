from django.forms import ModelForm
from app.models import TODO



class TODOForm(ModelForm): #inherited model form
    class Meta:
        model = TODO
        fields = ['id' ,'title' , 'status' , 'priority'] 

        
        