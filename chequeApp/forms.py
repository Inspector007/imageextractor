from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField()
    loginId = forms.HiddenInput()

class UccDataForm(forms.Form):
    uccfile = forms.FileField()

class BoDataForm(forms.Form):
    bofile = forms.FileField()


class MutualDataForm(forms.Form):
    mutualfile = forms.FileField()