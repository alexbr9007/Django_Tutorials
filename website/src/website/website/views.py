from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .forms import ContactForm
from blog_app.models import BlogPost

# Django uses the Model View Template instead of the MVC

#def home_page(request):
#    my_title = "Hello there"
#    context  = {"title" : my_title, "my_list" : [1, 2, 3, 4, 5]}
#    return render(request, "home.html", context)

#Render an external file, a .txt file
def home_page(request):
    #my_title        = "Hello there!"

    qs = BlogPost.objects.all()[:5]
    context = {'title':'Welcome to your blog','blog_list': qs}
    #context         = {"title": my_title}
    #template_name   = "title.txt"
    #template_obj    = get_template(template_name)
    #rendered_string = template_obj.render(context)
    # print(rendered_string)
    #return render(request, "home.html", {"title": rendered_string})
    return render(request, "home.html", context)

def about_page(request):
    my_about_msg = "About us"
    return render(request, "about.html", {"title": my_about_msg})

def contact_page(request):
    # template_name = "form.html"
    # template_obj  = get_template(template_name)
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        "title": "Contact us",
        "form": form
    }
    return render(request, "form.html", context)


