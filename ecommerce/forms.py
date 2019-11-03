from django import forms
from django.contrib.auth import get_user_model

User=get_user_model()
class ContactForm(forms.Form):
    fullname=forms.CharField(
        widget=forms.TextInput(
            attrs={"class":"form-control",
            "placeholder":"Your name"})
            )
    email=forms.EmailField( widget=forms.EmailInput(
            attrs={"class":"form-control",
            "placeholder":"Your email"})
           
            
            
        )
    content=forms.CharField( widget=forms.Textarea(
            attrs={"class":"form-control",
            "placeholder":"Content"})
            )
    def clean_email(self):
        email=self.cleaned_data.get('email')
        if not "gmail.com" in email:
            raise forms.ValidationError("Youe email id is incorrect")
        return email


class Login_Form(forms.Form):
    username= forms.CharField(widget=forms.TextInput())
        
    
    password= forms.CharField(widget=forms.PasswordInput())

    

class Register_Form(forms.Form):
    username= forms.CharField()
    email=forms.EmailField( widget=forms.EmailInput())
    password =forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(label='confirm password',widget=forms.PasswordInput())
    
    def clean_username(self):
        username=self.cleaned_data.get('username')
        qs=User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("username already taken")
        return username
    def clean_email(self):
        email=self.cleaned_data.get('email')
        qs=User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email already taken")
        return email


    def clean(self):

        data=self.cleaned_data
        password=self.cleaned_data.get('password')
        password2=self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError("passwords doesn't match")
        return data


  

    