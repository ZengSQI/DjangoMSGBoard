from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


from .models import MsgPost, Comment
from .form import MsgForm, CommentForm

import re


def index(request):
    msg_list = MsgPost.objects.order_by('-pub_date')
    form = MsgForm()
    context = {'msg_list': msg_list,
               'msg_form': form}
    return render(request, 'index.html', context)


@login_required
def post(request):
    if request.method == 'POST':
        form = MsgForm(request.POST)
        if form.is_valid():
            _newMsg = MsgPost(title=form.cleaned_data['title'],
                              user=request.user,
                              content=re.sub(r'\n', '<br/>',
                                             form.cleaned_data['content']))
            _newMsg.save()
        return HttpResponseRedirect('/msgboard')


def detail(request, msg_id):
    msg = get_object_or_404(MsgPost, pk=msg_id)
    return render(request, 'detail.html', {'msg': msg})


@login_required
def comment(request, msg_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            _newComment = Comment(msg_id=get_object_or_404(MsgPost,
                                                           pk=msg_id),
                                  user=request.user,
                                  content=re.sub(r'\n', '<br/>',
                                                 form.cleaned_data['content']))
            _newComment.save()
        return HttpResponseRedirect(reverse('msgboard:detail',
                                            args=(msg_id,)))
