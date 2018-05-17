import random
from django.shortcuts import render
from django.http import HttpResponse


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

def home(request):

    '''In this function based biew, all the templates are stored in the templates folder and Django knows where
    to look for this folder because it was already specified in the base.py from the settings folder.'''
    num = random.randint(0, 1000000)
    some_list = [random.randint(0, 1000000), random.randint(0, 1000000), random.randint(0, 1000000), random.randint(0, 1000000)]
    context_variables = {
        "html_var": True,
        "num": num,
        "some_list": some_list
    }
    return render(request, "home.html", context_variables)


def restaurants(request):

    '''In this function based biew, all the templates are stored in the templates folder and Django knows where
    to look for this folder because it was already specified in the base.py from the settings folder.'''
    num = random.randint(0, 1000000)
    some_list = [random.randint(0, 1000000), random.randint(0, 1000000), random.randint(0, 1000000), random.randint(0, 1000000)]
    context_variables = {
        "html_var": True,
        "num": num,
        "some_list": some_list
    }
    return render(request, "restaurants.html", context_variables)

def about(request):
    context_variables = {}
    return render(request, "about.html", context_variables)


def contact(request):
    context_variables = {}
    return render(request, "contact.html", context_variables)