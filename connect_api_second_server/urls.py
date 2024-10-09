from django.urls import path
from .views import CreateUnderTableAdvertisement, TakeMarketingSpecific, UpdateUnderTableAdvertisement


urlpatterns = [
    #path('', Connect.as_view()),
    path('create_under_table_advertisement/', CreateUnderTableAdvertisement.as_view()),
    path('take_marketing_specific/',TakeMarketingSpecific.as_view()),
    path('update_under_table_advertisement/',UpdateUnderTableAdvertisement.as_view()),

]