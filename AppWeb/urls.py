from django.urls import path
from .views import index, by_VectorWork, AddClientCreateView

urlpatterns = [
    path('<int:VectorWork_id>/', by_VectorWork, name='by_VectorWork'),
    path('', index, name='index'),
    path('AppWeb/', AddClientCreateView.as_view(), name='add')
]
