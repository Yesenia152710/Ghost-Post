from django.http.response import HttpResponseRedirect
from django.shortcuts import render, reverse
from ghost_app.models import Posts
from ghost_app.forms import AddPost
# Create your views here.


def index_view(request):
    post = Posts.objects.all().order_by('-time_posted')
    return render(request, 'index.html', {'post': post})


def boast_view(request):
    post = Posts.objects.filter(type_post=False).order_by('-time_posted')
    return render(request, 'boast.html', {'boast': post})


def roast_view(request):
    post = Posts.objects.filter(type_post=True).order_by('-time_posted')
    return render(request, 'roast.html', {'roast': post})


def votes_view(request):
    post = sorted(Posts.objects.all(),
                  key=lambda total: total.total_vote, reverse=True)

    return render(request, 'votes.html', {'votes': post})


def upvote_view(request, post_id):
    upvote = Posts.objects.get(id=post_id)
    upvote.up += 1
    upvote.save()
    return HttpResponseRedirect(reverse('homepage'))


def downvote_view(request, post_id):
    downvote = Posts.objects.get(id=post_id)
    downvote.down += 1
    downvote.save()
    return HttpResponseRedirect(reverse('homepage'))


def subpost_view(request):
    if request.method == "POST":
        to_post = AddPost(request.POST)
        if to_post.is_valid():
            data = to_post.cleaned_data
            new_post = Posts.objects.create(
                text=data['text'], type_post=data['type_post'])
            return HttpResponseRedirect(reverse('homepage'))

    to_post = AddPost()
    return render(request, 'subpost.html', {'to_post': to_post})
