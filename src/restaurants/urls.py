from django.conf.urls import url
from . import views

urlpatterns = [
    # ======================================== Home ============================================ #
    url(r'^$', views.HomeView.as_view()),
    url(r'restaurants/$', views.restaurant_listview.as_view()),
    url(r'restaurants/(?P<slug>\w+)/$', views.restaurant_listview.as_view()),
    url(r'about/$', views.AboutView.as_view()),
    url(r'contact/$', views.ContactView.as_view())
    # as_view is necessary because it makes possible to invoke the class based view as a function based view
]
