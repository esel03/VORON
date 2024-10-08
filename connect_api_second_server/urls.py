from django.urls import path
from .views import CreateUnderTableAdvertisement


urlpatterns = [
    #path('', Connect.as_view()),
    path('', CreateUnderTableAdvertisement.as_view()),
    

]