from django.urls import path, include
from . import views as vi 

urlpatterns= [
path('test/reporter_tool/', vi.ExecuteSQLQuery.as_view(), name='reporter_tool')
]