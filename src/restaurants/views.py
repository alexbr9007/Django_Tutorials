import random
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .models import RestaurantLocations
from .forms import RestaurantsCreateForm, RestaurantLocationsCreateForm


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


def restaurant_createview(request):
    form = RestaurantLocationsCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        form.save()
        #obj = RestaurantLocations.objects.create(name = form.cleaned_data.get('title'),location = form.cleaned_data.get('location'),category = form.cleaned_data.get('category'))
        return HttpResponseRedirect("restaurants")
    if form.errors:
        errors = form.errors
    template_name = "form.html"
    context = {"form": form, "errors": errors}
    return render(request, template_name, context)


def about(request):
    context_variables = {}
    return render(request, "about.html", context_variables)


'''def contact(request):
    context_variables = {}
    return render(request, "contact.html", context_variables)'''


class RestaurantListview(ListView):
    '''Function list view'''
    template_name = 'restaurants_list.html'

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestaurantLocations.objects.filter(
            Q(category__iexact = slug) | Q(category__icontains=slug))
        else:
            queryset = RestaurantLocations.objects.all()
        return queryset

    '''queryset = RestaurantLocations.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)'''


class RestaurantsView(TemplateView):
    #With the template view you do not have to call the render method anymore. Really?
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

class SearchRestaurantListView(ListView):
    '''This view only displays the results once you type in restaurants/asian or restaurants/mexican'''
    template_name = 'restaurants_list.html'

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestaurantLocations.objects.filter(
            Q(category__iexact = slug) | Q(category__icontains=slug))
        else:
            queryset = RestaurantLocations.objects.all()
        return queryset

class RestaurantsDetailView(DetailView):
    queryset = RestaurantLocations.objects.all()
    template_name = 'restaurants_detail.html'

    '''def get_context_data(self, *args, **kwargs):
        print(self)
        context = super(RestaurantsDetailView, self).get_context_data(*args, **kwargs)
        print(context)

        return context

    def get_object(self, queryset=None):
        rest_id = self.kwargs.get('slug')
        obj = get_object_or_404(RestaurantLocations, id=rest_id) #pk = rest_id
        return obj'''

#def restaurant_detailView(request, slug):

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

class RestaurantsCreateView(CreateView):
    form_class    = RestaurantLocationsCreateForm
    template_name = 'form.html'
    success_url   = "/restaurants/"