from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required = False , max_length = 120)
    email = forms.EmailField(required = True)
    comment = forms.CharField(required = True , widget = forms.Textarea)
    fields = ['name','email','comment']