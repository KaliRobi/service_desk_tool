from django.contrib import admin
from django.urls import path, include


urlpatterns  = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('reporting_tool.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('landing_page.urls'))
]


