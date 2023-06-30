from django.shortcuts import render, get_object_or_404
from .models import Post


#all_posts = [
#]


def get_date(post):
    return post['date']


# Create your views here.

def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    # sorted_posts = sorted(all_posts, key=get_date)
    # latest_posts = sorted_posts[-3:]
    return render(request, "Feature_Blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "Feature_Blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "Feature_blog/post-detail.html", {
        "post": identified_post,
        "post_tags": identified_post.tags.all()
    })
