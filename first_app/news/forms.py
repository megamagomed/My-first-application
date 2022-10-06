from django import forms


class NewsForm(forms.Form):
    article = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)
