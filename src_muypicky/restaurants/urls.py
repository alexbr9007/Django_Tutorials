from django.conf.urls import url
from django.contrib.auth.views import LoginView
from . import views


urlpatterns = [
    # ======================================== Home ============================================ #

    url(r'^$', views.HomeView.as_view(), name="home"), #name = home is reverse url and it helps us to avoid using large url patterns, we try to keep it short
    url(r'login/$',LoginView.as_view(), name='login'),
    url(r'restaurants/$', views.RestaurantListview.as_view(), name="restaurants"), #name is like a shortcut to find something between the RestaurantListview
    #url(r'restaurants/(?P<slug>\w+)/$', views.RestaurantListview.as_view()),
    #url(r'restaurants/(?P<pk>\w+)/$', views.RestaurantsDetailView.as_view()),
    #url(r'create/$',views.RestaurantsCreateView.as_view(), name="create"), #login here is required but this is a class based view
    url(r'create/$',views.restaurant_createview, name="create"), #login here is required but this is a function based view
    url(r'restaurants/(?P<slug>[\w-]+)/$', views.RestaurantsDetailView.as_view()), #instead of the pk you can use the rest_id
    url(r'about/$', views.TemplateView.as_view(template_name='about.html'), name="about"),
    url(r'contact/$', views.TemplateView.as_view(template_name='contact.html'), name="contact")

    # as_view is necessary because it makes possible to invoke the class based view as a function based view

]
