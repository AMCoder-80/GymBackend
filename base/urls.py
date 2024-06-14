from django.urls import path, include


urlpatterns = [
    path('accounts/', include('base.accounts.urls')),
    path('general/', include('base.general.urls')),
]