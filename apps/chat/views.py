from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import View

from apps.profile.models import User
from .models import City, Message
from .slugify import slugify
from datetime import datetime, timedelta

class CityChatView(LoginRequiredMixin, View):
    """Страница чата"""
    def get(self, request, *args, **kwargs):
        """Загрузить страницу чата"""
        last_day = datetime.now() - timedelta(days=2)
        slug = self.kwargs.get('city')
        city = City.objects.get(slug=slug)
        messages = Message.objects.filter(city=city,date__range=[last_day, datetime.now()])
        profile = User.objects.all()
        
        context = {
                'city': city,
                'messages': messages,
                'city_sug': slug,
                'profile': profile
            }
        return render(request, 'chat/page.html', context)
        
    def post(self, request, *args, **kwargs):
        """Отправить сообщение в чат"""
        slug = self.kwargs.get('city')
        city = City.objects.get(slug=slug)
        user = User.objects.get(id=request.user.id)

        message = Message(user = user,city = city)
        message.message_text = request.POST['message_text']
        message.save()

        return redirect(f'/chat/{ slug }/')

class PageChatsView(LoginRequiredMixin, View):
    """Страница с всеми чатами"""
    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        cities = City.objects.values_list('slug', flat=True).distinct()
        if (slugify(user.city) not in cities):
            new_city = City(title = user.city)
            new_city.save()
        messages = Message.objects.filter(user = user).distinct()
        i = ""
        s = []
        if City.objects.get(title=user.city) not in s:
                s.append(City.objects.get(title=user.city))
        for message in messages:
            i = message.city
            if i not in s:
                s.append(City.objects.get(title=i))
        cities = City.objects.all().order_by('title').distinct()
        context = {
                'city_user': user.city,
                'cities_user': s,
                'cities': cities
            }
        return render(request, 'chat/index.html', context)

class MessageAddView(LoginRequiredMixin, View):
    pass