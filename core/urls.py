from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

     path('api/predict-character/', views.predict_character, name='predict-character'),
     path('test/', views.testing, name='test'),
     path('upload-image/', views.upload_image, name='upload-image'),
     
    # path('', views.index, name='index'),
    # path('comingsoon/', views.comingsoon, name='comingsoon'),
    # path('index2', views.index2, name='index2'),
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)