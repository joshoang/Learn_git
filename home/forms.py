from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class RegistrationForm(forms.Form):
    username = forms.CharField(label='tài khoản', max_length=30)
    email = forms.EmailField(label='email', max_length=30, widget=forms.TextInput(attrs={'class':"col-md-5", 'id': "email"}))
    password_1 = forms.CharField(label='mật khẩu',widget=forms.PasswordInput())
    password_2 = forms.CharField(label='nhập lại mật khẩu',widget=forms.PasswordInput())

    def clean_password_2(self):
        if 'password_1' in self.cleaned_data:
            pass_1 = self.cleaned_data['password_1']
            pass_2 = self.cleaned_data['password_2']
            if pass_1 == pass_2 and pass_1:
                return pass_2
        raise forms.ValidationError("Mật khẩu không hợp lệ")

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r"^\w+$",username): #kiểm tra username tất cả là kí tự thường
            raise forms.ValidationError("Tài khoản chứa kí tự đặc biệt")
        try:
            User.objects.get(username = username)

        except ObjectDoesNotExist:
            return username

        raise forms.ValidationError("Tài khoản đã tồn tại")
    
    def save(self):
        User.objects.create_user(username = self.cleaned_data['username'],email=self.cleaned_data['email'],password=self.cleaned_data['password_1'])

class LoginForm(forms.Form):
    username = forms.CharField(label='tài khoản', max_length=30)
    password = forms.CharField(label='mật khẩu',widget=forms.PasswordInput())
  
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r"^\w+$",username): #kiểm tra username tất cả là kí tự thường
            raise forms.ValidationError("Tài khoản chứa kí tự đặc biệt")
        try:
            User.objects.get(username = username)
            return username
        except ObjectDoesNotExist:
            raise forms.ValidationError("Tài khoản không tồn tại")
        

