from django import forms

class NewsForm(forms.Form) :
    news = forms.CharField()