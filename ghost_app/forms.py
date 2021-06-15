from django import forms
from ghost_app.models import Posts


class AddPost(forms.Form):
    Choices = ((True, 'Roast'), (False, 'Boast'))
    text = forms.CharField(widget=forms.Textarea)
    type_post = forms.ChoiceField(choices=Choices)
