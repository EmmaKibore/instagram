from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index, name = 'sign'),
    url(r'^home/$',views.index, name='index'),
    url(r'^new/image$', views.new_image, name='new-image'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^comment/(?P<image_id>\d+)', views.comment, name='comment'),
    url(r'^profiles/(\d+)',views.profiles,name='profiles'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]