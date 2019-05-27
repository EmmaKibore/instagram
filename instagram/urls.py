from django.conf.urls import url, include
from  .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.home, name='home'),
    url(r'^new_image$', views.new_image, name='new_image'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^comment/(?P<image_id>\d+)', views.comment, name='comments'),
    url(r'^profiles/(\d+)',views.profiles,name='profiles'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    # url(r'^signup/$', views.signup, name='signup'),
    # url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     views.activate, name='activate'),
]