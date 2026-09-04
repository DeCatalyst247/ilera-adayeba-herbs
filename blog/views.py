# Create your views here.
from django.shortcuts import (
    render,
    get_object_or_404
)

from .models import (BlogPost,BlogCategory)
from django.db.models import Q
from django.core.paginator import Paginator


def blog_list(request):
    featured_posts = BlogPost.objects.filter(
    featured=True,
    published=True
)[:3]

    posts = BlogPost.objects.filter(
    published=True
).order_by('-id')

    paginator = Paginator(
    posts,
    6
)

    page_number = request.GET.get(
    'page'
)

    posts = paginator.get_page(
    page_number
)

    query = request.GET.get('q')

    if query:

        posts = posts.filter(

            Q(title__icontains=query)

            |

            Q(content__icontains=query)

        )

    context = {

        'posts': posts,
        'featured_posts' :featured_posts

    }

    return render(
        request,
        'blog/blog_list.html',
        context
    )

def blog_detail(request, slug):
        

    post = get_object_or_404(
        BlogPost,
        slug=slug,
        published=True
    )
    related_posts = BlogPost.objects.filter(

    category=post.category,

    published=True

    ).exclude(

    id=post.id

)[:3]
    
    context = {
        'post': post,
        'related_posts':related_posts
    }

    return render(
        request,
        'blog/blog_detail.html',
        context
    )

def category_posts(
    request,
    slug
):

    category = BlogCategory.objects.get(
        slug=slug
    )

    posts = BlogPost.objects.filter(
        category=category,
        published=True
    )

    context = {

        'category': category,

        'posts': posts

    }

    return render(
        request,
        'blog/category_posts.html',
        context
    )