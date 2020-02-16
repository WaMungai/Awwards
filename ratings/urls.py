from django.conf.urls import url
from django.conf.urls.static import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url('^$',views.home,name='home'),
    url(r'^new/project$',views.new_project,name='new-project'),
    url(r'^search/',views.search_by_title,name='search_by_title'),
    url(r'^project/(\d+)',views.single_project,name='project'),
    url(r'^new/profile$',views.new_profile,name='new-profile'),
    url(r'rate$',views.add_rating,name='rate'),
    url(r'displayprofile/(?P<user_id>\d+)$',views.display_profile,name='displayprofile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
