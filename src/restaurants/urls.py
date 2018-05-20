from django.conf.urls import url
#from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # ======================================== Home ============================================ #

    url(r'^$', views.HomeView.as_view()),
    url(r'restaurants/$', views.RestaurantListview.as_view()),
    #url(r'restaurants/(?P<slug>\w+)/$', views.RestaurantListview.as_view()),
    #url(r'restaurants/(?P<pk>\w+)/$', views.RestaurantsDetailView.as_view()),
    url(r'create/$',views.RestaurantsCreateView.as_view()),
    url(r'restaurants/(?P<slug>[\w-]+)/$', views.RestaurantsDetailView.as_view()), #instead of the pk you can use the rest_id
    url(r'about/$', views.TemplateView.as_view(template_name='about.html')),
    url(r'contact/$', views.TemplateView.as_view(template_name='contact.html'))
    # as_view is necessary because it makes possible to invoke the class based view as a function based view

]
