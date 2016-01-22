from django import forms


class MsgForm(forms.Form):
    name = forms.CharField(max_length=20)
    title = forms.CharField(max_length=50)
    content = forms.CharField(widget=forms.Textarea)


class CommentForm(forms.Form):
    name = forms.CharField(max_length=20)
    content = forms.CharField(widget=forms.Textarea)
