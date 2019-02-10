from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=200)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
