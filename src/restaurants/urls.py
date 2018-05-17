from django.conf.urls import url
from . import views

urlpatterns = [
    # ======================================== Home ============================================ #
    url(r'^$', views.home),
    url(r'restaurants/$', views.restaurants), #'home2 is a slug'
    url(r'about/$', views.about), #'home2 is a slug'
    url(r'contact/$', views.contact) #'home2 is a slug'

]
