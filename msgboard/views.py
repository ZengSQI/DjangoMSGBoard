from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import MsgPost
from .form import MsgForm


def index(request):
    msg_list = MsgPost.objects.order_by('-pub_date')
    context = {'msg_list': msg_list}
    return render(request, 'index.html', context)


def post(request):
    if request.method == 'POST':
        form = MsgForm(request.POST)
        if form.is_valid():
            newMsg = MsgPost(title=form.cleaned_data['title'],
                             user=form.cleaned_data['name'],
                             content=form.cleaned_data['content'])
            newMsg.save()
        return HttpResponseRedirect('/msgboard')
