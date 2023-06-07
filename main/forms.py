from django import forms

class UserForm(forms.Form):
    file = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'form-control', 'id': 'formFile'})
    )
    file2 = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'form-control', 'id': 'formFiles'})
    )
    name = forms.CharField(
        widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder': 'Enter Name Of Merged Pdf'})
    )
