from django.shortcuts import render, Http404, get_object_or_404, redirect
from django.contrib.auth .decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
from .forms import BlogPostModelForm
from .models import BlogPost


def blog_post_detail_page(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_app/detail.html'
    context = {"object": obj}
    # The context object extracted form the BlogPost is transferred to the template and then we can get the
    # title and contents.
    return render(request, template_name, context)

def blog_post_list_view(request):
    # list out objects
    # could be search
    qs = BlogPost.objects.published().published()
    template_name = 'blog_app/list.html'
    context = {'object_list':qs}
    return render(request, template_name, context)


@staff_member_required
def blog_post_create_view(request):

    form = BlogPostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        print(form.cleaned_data)
        # create the new object and save it because of the ModelForm
        obj = form.save(commit=False)
        # associate the user that creates the blog post
        obj.user = request.user
        obj.save()
        form = BlogPostModelForm()
    # it's loading the form.html from the templates, not from the blog_app
    template_name = 'form.html'
    context = {'form' : form}
    return render(request, template_name, context)

def blog_post_detail_view(request, slug):

    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_retrieve.html'
    context = {'object': obj}
    return render(request, template_name, context)

@staff_member_required
def blog_post_update_view(request, slug):

    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'form.html'
    context = {'form': form, "title": f"Update {obj.title}"}
    return render(request, template_name, context)

@staff_member_required
def blog_post_delete_view(request, slug):

    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_app/delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect("/blog")
    context = {'object': obj}
    return render(request, template_name, context)


