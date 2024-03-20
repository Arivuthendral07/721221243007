from django.urls import path,include
from .import views
urlpatterns=[
    path('get/',views.getData),
    path('post/',views.postData),
    path('',views.companies,name='companies'),
]