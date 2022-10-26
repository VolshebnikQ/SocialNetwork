from django.urls import path

from .views import *


urlpatterns = [
    path('<slug:city>/', CityChatView.as_view(), name='city'),
    path('', PageChatsView.as_view(), name='chat'),
    path('<slug:city>/Add', MessageAddView.as_view(), name='add_message'),
]
