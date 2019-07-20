from django import forms
class UploadFileForm(forms.Form):
    # title = forms.CharField(max_length=50)
    file = forms.FileField()


class LoginForm(forms.Form):
    userId = forms.CharField(label="Usre Id",max_length=50)
    userPassword = forms.CharField(label="User Password", max_length=15)