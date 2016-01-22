from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


from .models import MsgPost, Comment
from .form import MsgForm, CommentForm


def index(request):
    msg_list = MsgPost.objects.order_by('-pub_date')
    form = MsgForm()
    context = {'msg_list': msg_list,
               'msg_form': form}
    return render(request, 'index.html', context)


def post(request):
    if request.method == 'POST':
        form = MsgForm(request.POST)
        if form.is_valid():
            __newMsg = MsgPost(title=form.cleaned_data['title'],
                               user=form.cleaned_data['name'],
                               content=form.cleaned_data['content'])
            __newMsg.save()
        return HttpResponseRedirect('/msgboard')


def detail(request, msg_id):
    msg = get_object_or_404(MsgPost, pk=msg_id)
    return render(request, 'detail.html', {'msg': msg})


def comment(request, msg_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            __newComment = Comment(msg_id=get_object_or_404(MsgPost,
                                                            pk=msg_id),
                                   user=form.cleaned_data['name'],
                                   content=form.cleaned_data['content'])
            __newComment.save()
        return HttpResponseRedirect(reverse('msgboard:detail',
                                            args=(msg_id,)))
