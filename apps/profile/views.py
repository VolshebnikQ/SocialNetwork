from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse

from apps.publications.models import Post
from .models import *


class EditProfileView(LoginRequiredMixin, View):
    """Редактирование профиля"""
    def get(self, request, *args, **kwargs):
        sex = ["---","Мужской","Женский"]
        context = {
            'sex': sex
        }
        return render(request, 'profile/edit.html', context)

    def post(self, request, *args, **kwargs):
        user = request.user.first_name
        user = User.objects.get(username=request.user.username)
        try:
            user.avatar = request.FILES['avatar']
        except:
            pass
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.sex = request.POST['sex']
        user.birthday = request.POST['birthday']
        user.city = request.POST['city']
        user.phone_number = request.POST['phone_number']
        user.about = request.POST['about']
        user.save()
        sex = ["---","Мужской","Женский"]
        posts = Post.objects.filter(user=user)
        context = {
            'profile': user,
            'sex': sex,
            'posts': posts
        }
        return render(request, 'profile/profile.html', context)


class ProfileView(LoginRequiredMixin, View):
    """Информация о пользователе"""
    def get(self, request, *args, **kwargs):
        username = kwargs.get('username')
        profile = User.objects.get(username=username)
        posts = Post.objects.filter(user=profile)
        context = {
            'profile': profile,
            'posts': posts
        }
        return render(request, 'profile/profile.html', context)

    def post(self, request, *args, **kwargs):
        """Опубликовать пост"""
        username = kwargs.get('username')
        profile = User.objects.get(username=username)
        post = Post()
        post.user = profile
        post.content = request.POST['content']
        post.save()
        posts = Post.objects.filter(user=profile)
        context = {
            'profile': profile,
            'posts': posts
        }
        #return JsonResponse(context)
        return render(request, 'profile/profile.html', context)


class PostDelete(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        """Удалить пост"""
        id = kwargs.get('id')
        post = Post.objects.get(id = id)
        if (post.user.username  == request.user.username):
            post.delete()
        return redirect(f'/profile/{ request.user.username }/')


class FriendsListView(LoginRequiredMixin, View):
    """Список друзей"""
    def get(self, request, *args, **kwargs):
        all_users = User.objects.all()                   # Все пользователи
        all_friends = Friend.objects.filter(             # Все заявки в друзья
            user=request.user)
        friends = all_friends.filter(confirmed=True)     # Подтверждённые
        users = all_users.exclude(id__in=all_friends)    # Не друзья
        users = users.exclude(id=request.user.id)        # Исключаем себя
        outgoing = all_friends.filter(confirmed=False)   # Исходящие заявки
        incoming_all = Friend.objects.filter(users_friend=request.user)
        incoming = incoming_all.filter(confirmed=False)  # Входящие заявки
        context = {
            'friends': friends,
            'outgoing': outgoing,
            'incoming': incoming,
            'users': users,
        }
        return render(request, 'profile/friends.html', context)


class AddFriendsView(LoginRequiredMixin, View):
    """Добавление в друзья"""
    pass


class DeleteFriendsView(LoginRequiredMixin, View):
    """Добавление в друзья"""
    pass
