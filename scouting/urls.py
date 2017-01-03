
from django.conf.urls import include, url
from django.contrib import admin
from collection import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', views.login), 
    url(r'^accounts/auth/$', views.auth_view),
    url(r'^accounts/logout/$', views.logout), 
    url(r'^accounts/loggedin/$', views.loggedin), 
    url(r'^accounts/invalid/$', views.invalid_login), 
    
    url(r'^report$', views.report,name='report'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'), 
    url(r'^labelle/scouting/mature$', views.labelleMature,name='mature'),
    url(r'^labelle/scouting/young$', views.labelleYoung,name='young'),
    url(r'^labelle/scouting/mature_form$', views.labelleMatureForm,name='mature_form'),
    url(r'^labelle/scouting/young_form$', views.labelleYoungForm,name='young_form'),
    
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
