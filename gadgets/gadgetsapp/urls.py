from django.urls import path
from .import views

urlpatterns = [
    path('', views.index,name='index'),
    path('gadgets/<int:gadgets_id>/', views.detail, name='detail'),
    path('add/',views.add_gadgets,name='add_gadgets'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]