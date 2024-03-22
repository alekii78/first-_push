from django.urls import path
from  . import views
from  . import view
urlpatterns=[
    path('hello/',views.hello,name='hello'),
    path('hello/details/<int:id>',view.details,name='details'),
    path('hello/details/<int:id>',views.details,name='details'),
]