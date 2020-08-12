from django import forms
from .models import StudentInfo
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class RegisterUserForm(UserCreationForm):
    # username = forms.CharField(required='True', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # , widget=forms.EmailInput(attrs={'class': 'form-control'})
    # password = forms.CharField(required='True', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # password_repeat = forms.CharField(required='True', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )
        widgets = {

            'user_name': forms.TextInput(attrs={'class': 'form-control', "placeholder": "User Name *"}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', "placeholder": "First Name *"}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Last Name *"}),
            'email': forms.EmailInput(attrs={'class': 'form-control', "placeholder": "Email *"}),
            'password1': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Password *"}),
            'password2': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Password Confirmation *"}),

        }

    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user

class StudentInfoForm(ModelForm):

    class Meta:
        model = StudentInfo
        fields = "__all__"
        widgets = {
            'First_name': forms.TextInput(attrs={'class': 'form-control is_valid', "placeholder": "First Name *",
                                                 'id': 'ValidationCustom01'}),
            'Last_name': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Last Name *"}),
            'Email': forms.EmailInput(attrs={'class': 'form-control', "placeholder": "Email *"}),
            'Mobile_number': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Mobile Number *"}),
            'id': forms.TextInput(attrs={'class': 'form-control', "placeholder": "ID *", 'id': 'ID'}),
            'Gender': forms.Select(attrs={'class': 'form-control'}),
            'Date_of_birth': forms.DateInput(attrs={'class': 'form-control'}),
            'Address': forms.Textarea(attrs={'class': 'form-control', "placeholder": "Address *"}),
            'Pin_code': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Pincode *"}),
            'City': forms.TextInput(attrs={'class': 'form-control', "placeholder": "City *"}),
            'State': forms.TextInput(attrs={'class': 'form-control', "placeholder": "State *"}),
            'Country': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Country *"}),
            'Hobbies': forms.Textarea(attrs={'class': 'form-control', "placeholder": "Hobbies *"}),
            'Course_applied': forms.Select(attrs={'class': 'form-control'}),
        }
