from django.urls import path
from agenda.views import listagem, create, delete

urlpatterns = [
    path('', listagem, name='listagem'),
    path('create/', create, name='create'),
    path('<int:compromisso_id>/', delete, name='delete')
]