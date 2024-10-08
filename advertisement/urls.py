from django.urls import path
from .views import CreateAdvertisementAdd, TakeAdvertisementList, UpdateAdvertisement, DeleteAdvertisement


urlpatterns = [
    path('create_first_table/', CreateAdvertisementAdd.as_view()),
    path('take_list/', TakeAdvertisementList.as_view()),
    path('update/', UpdateAdvertisement.as_view()),
    path('delete/', DeleteAdvertisement.as_view()),
    #path('update/', Update_user.as_view()),
    #path('take_to/', View_data.as_view()),
    #path('delete_acc/', Delete_account.as_view()),


]