from django.contrib.auth import views
from django.conf.urls import url,include
from django.contrib import admin



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^kbstack/', include('kbstack.urls')),
    url(r'^', include('kbstack.urls')),

]
