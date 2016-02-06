from django import forms


class MsgForm(forms.Form):
    title = forms.CharField(max_length=50)
    content = forms.CharField(widget=forms.Textarea)


class CommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)
