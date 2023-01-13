from django.urls import path
from providers.views import providers_list, providers_create

urlpatterns = [
    path('providers-list/', providers_list, name='providers_list'),
    path('providers-create/', providers_create, name='providers_create')

]