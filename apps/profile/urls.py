from django.urls import include, path

from . import views


urlpatterns = [
    path('add-friends/', views.AddFriendsView.as_view(), name='add_friends'),
    path('edit/', views.EditProfileView.as_view(), name='edit'),
    path('friends/', views.FriendsListView.as_view(), name='friends'),
    path('<str:username>/', views.ProfileView.as_view(), name='username_page'),
    path('post-<int:id>/delete', views.PostDelete.as_view(), name='delete_post'),
]
