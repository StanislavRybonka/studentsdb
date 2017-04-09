from django.conf.urls import url, include

from .views import HomePageView

urlpatterns = [
    # Students urls
    url(r'^$', HomePageView.as_view(), name='home-page'),

]
