from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

from allauth.account import views as allauth_views

from forwarder import views

urlpatterns = [
    url(r'^$', allauth_views.login, name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, admin.site.urls),

    # User management
    url(r'^users/', include('arrow.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),

    #arrow urls start here
    url(r'^createApplication', views.ApplicationCreate.as_view()) ,
    url(r'^listApplication', views.ListApplicationView.as_view(), name="list-application"),
    url(r'^application/(?P<pk>\d+)/$', views.ApplicationDetailView.as_view(), name="application"),
    url(r'^pdf_dl/(?P<pk>\d+)/$', views.pdf_dl),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
