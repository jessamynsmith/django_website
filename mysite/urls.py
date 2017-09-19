from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin

from core import views as core_views


urlpatterns = [
url(r'^admin/', include(admin.site.urls)),
url(r'^home/$', core_views.home, name='home'),
url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
url(r'^signup/$', core_views.signup, name='signup'),
url(r'^wnba_directory/$', core_views.wnba_directory, name='wnba_directory'),
url(r'^$', core_views.index, name='index'),
url(r'^account_activation_sent/$', core_views.account_activation_sent, name='account_activation_sent'),
url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
	core_views.activate, name='activate'),
url(r'^articles/$', core_views.articles, name='articles'),
url(r'^testimonials/$', core_views.testimonials, name='testimonials'),
url(r'^small_ball/$', core_views.small_ball, name='small_ball'),
url(r'^wnba_fd/$', core_views.wnba_fd, name='wnba_fd'),
url(r'^wnba_dk/$', core_views.wnba_dk, name='wnba_dk'),
url(r'^wnba_teams/$', core_views.wnba_teams, name='wnba_teams'),
url(r'^wnba_cheat_sheet/$', core_views.wnba_cheat_sheet, name='wnba_cheat_sheet'),
url(r'^contact/',    include('envelope.urls')),
]

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )