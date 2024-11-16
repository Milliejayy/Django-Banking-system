#Here we are going to import 2 things; the django form and the models we created cos we'd be using them
from django import forms
from . models import UserForm
from django.core.exceptions import ValidationError

#create our django form by using the fields/attributes we listed in our models page
class FormData(forms.ModelForm):
   
    class Meta:
        model = UserForm #Here, we just linked/mapped our model fields to this django inbuilt form
        fields = ["firstname", "lastname", "email", "password"]

    def clean_email(self):
        email = self.cleaned_data['email']

        if UserForm.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered")
        return email
            
#NOTEThis: Any validation done in the models works only for database.To validate a users input before it is pushed to the database, we do it in the Forms.Py file