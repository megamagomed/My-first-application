from django import forms


class NewsForm(forms.Form):
    article = forms.CharField()