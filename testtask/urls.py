from django.urls import path
from . import views
from django.conf.urls import url
# from testtask.views import TestView
app_name = "testtask"

urlpatterns = [path('', views.index, name='index'),
            #    path('api/', ApiView.as_view(), name='get_api')
                path('api/', views.get_api, name='get_api')
                ]