from django.conf.urls import patterns, url
from rango import views

# urlpatterns = patterns('',
#         url(r'^$', views.index, name='index'))

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),    
    #url(r'^about/$', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'), # NEW MAPPING!
    url(r'^category/(?P<category_name_url>\w+)/add_page/$', views.add_page, name='add_page'), 
    url(r'^register/$', views.register, name='register'), # ADD NEW PATTERN! 
    url(r'^login/$', views.user_login, name='login'),  
    url(r'^category/(?P<category_name_url>\w+)/$', views.category, name='category'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^goto/$', views.track_url, name='track_url'),
    # url(r'^search/$', views.search, name='search'),
    ) 