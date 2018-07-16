from django import forms

choices = (
    ("choice.id", "choice.choice_name")
)


class MyForm(forms.Form):
    choice = forms.ChoiceField(widget=forms.RadioSelect, choices=choices)
