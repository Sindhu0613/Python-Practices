from django.contrib import admin  
from django.urls import path       
from django.conf import settings   
from django.conf.urls.static import static  
from django.contrib.staticfiles.urls import staticfiles_urlpatterns  
from members.views import AudioRecordingListCreate




urlpatterns = [
  
    path('members/', AudioRecordingListCreate.as_view(), name='recording-list-create'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()