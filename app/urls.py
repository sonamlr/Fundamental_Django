from django.urls import path
from . import views

urlpatterns = [
    path('',views.main_app, name='main' ),
    path('<int:chai_id>/', views.chai_detail, name='chai_detail'),
]
