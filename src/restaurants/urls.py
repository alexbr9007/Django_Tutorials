from django.conf.urls import url
from . import views

urlpatterns = [
    # ======================================== Home ============================================ #
    url(r'^$', views.home),
    url(r'restaurants/$', views.RestaurantsView.as_view()),
    url(r'about/$', views.AboutView.as_view()),
    url(r'contact/$', views.ContactView.as_view())
    # as_view is necessary because it makes possible to invoke the class based view as a function based view

]
