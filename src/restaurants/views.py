import random
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

from .models import RestaurantLocations


'''def home(request):
    # Basic function based view
    html_var = 'f strings new feature only in Python 3.6'

    html = f"""<!DOCTYPE html>
    <html lang=en>
    <head>
    </head>
    
    <body>
        <h1>Hello Alex!</h1>
        <p>This is {html_var} (somthing new!)</p>
    </body>
    
    </html>
    """

    return HttpResponse(html)
    #return render(request, "template",{})'''

'''def home(request):

    #In this function based biew, all the templates are stored in the templates folder and Django knows where
    #to look for this folder because it was already specified in the base.py from the settings folder.
    num = random.randint(0, 1000000)
    some_list = [random.randint(0, 1000000), random.randint(0, 1000000), random.randint(0, 1000000), random.randint(0, 1000000)]
    context_variables = {
        "html_var": True,
        "num": num,
        "some_list": some_list
    }
    return render(request, "home.html", context_variables)'''


class HomeView(TemplateView):
    #With the template view you do not have to call the render method anymore.
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):

        context = super(HomeView, self).get_context_data(*args, **kwargs)
        num = random.randint(0, 1000000)
        some_list = [random.randint(0, 1000000), random.randint(0, 1000000), random.randint(0, 1000000),
                     random.randint(0, 1000000)]
        context = {
            "html_var": True,
            "num": num,
            "some_list": some_list
        }

        '''The variable context defined at the very beginning initializes the template for rendering
        and the second variable named context sets the dictionary of variables that will be used in 
        that same template.'''

        return context


def about(request):
    context_variables = {}
    return render(request, "about.html", context_variables)


'''def contact(request):
    context_variables = {}
    return render(request, "contact.html", context_variables)'''


def restaurant_listview(request):
    template_name = 'restaurants.html'
    queryset = RestaurantLocations.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)

class RestaurantsView(TemplateView):
    #With the template view you do not have to call the render method anymore.
    template_name = 'restaurants.html'

    def get_context_data(self, *args, **kwargs):

        context = super(RestaurantsView, self).get_context_data(*args, **kwargs)
        num = random.randint(0, 1000000)
        some_list = [random.randint(0, 1000000), random.randint(0, 1000000), random.randint(0, 1000000),
                     random.randint(0, 1000000)]
        context = {
            "html_var": True,
            "num": num,
            "some_list": some_list
        }

        '''The variable context defined at the very beginning initializes the template for rendering
        and the second variable named context sets the dictionary of variables that will be used in 
        that same template.'''

        return context

class AboutView(TemplateView):
    template_name = 'about.html'

'''class ContactView(View):
    # Class based view
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, "contact.html", context)'''

class ContactView(TemplateView):
    #Template based view
    template_name = 'contact.html'

def restaurant_listview(request):
    template_name = ''
    context = {
        "object_list":[]

    }
    return render(request, template_name, context )
