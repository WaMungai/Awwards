from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url('^$',views.home,name='home'),
]
