from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^project/(\d+)',views.project,name ='project'),
    url(r'^new/project$', views.new_project, name='new-project'),
    url(r'^new/profile$', views.update_profile, name='new-profile'),
    url(r'^accounts/profile/',views.profile,name ='profile'),
    url(r'^search/', views.search_results, name='search_results'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)