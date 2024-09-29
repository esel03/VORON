from django.urls import path
from .views import CreateUserCustomAdd


urlpatterns = [
    path('create_first_table/', CreateUserCustomAdd.as_view()),
    #path('registration/', Registration.as_view()),
    #path('update/', Update_user.as_view()),
    #path('take_to/', View_data.as_view()),
    #path('delete_acc/', Delete_account.as_view()),


]