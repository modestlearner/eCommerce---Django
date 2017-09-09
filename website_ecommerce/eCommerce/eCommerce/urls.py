from django.conf.urls import url
from django.contrib import admin
from profiles import views as profile_views
from contact import views as contact_views
from django.conf import settings
from django.conf.urls import url , include
from django.conf.urls.static import static
from checkout import views as checkout_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', profile_views.home, name='home'),
    url(r'^about/$', profile_views.about, name='about'),
    url(r'^contact/$', contact_views.ContactFormView.as_view(), name='contact'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^profile/$', profile_views.userProfile, name='profile'),
    url(r'^checkout/', include('checkout.urls' , namespace='payment')),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),



]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)