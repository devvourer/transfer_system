from django.urls import path
from .views import register, activate, UserEditView, UpdateWalletView

urlpatterns = [
    path('register/', register, name='register'),
    path('activate/<slug:uidb64>/<slug:token>', activate, name='activate'),
    path('detail/<int:pk>', UserEditView.as_view(), name='user_detail'),
    path('currency_choice/<int:pk>', UpdateWalletView.as_view(), name='currency_choice')
]