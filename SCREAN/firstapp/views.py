from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from .forms import LoginUserForm
from django.contrib.auth.decorators import login_required
from django.urls.base import reverse_lazy
from .import UDALENIE
from .import LICHO
import os


class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "firstapp/register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)


def index(request):
    return render(request, 'firstapp/BLUR.html')


@login_required
def password(request):
    return render(request, 'firstapp/NOBLUR.html')


def TIR(request):
    images, blurimages = LICHO.VIDEO()
    context = {
        'images': images,
        "blurimages": blurimages
    }
    return render(request, 'firstapp/blur_img.html', context=context)


def DELETE(request):
    UDALENIE.all_img_delete()
    return render(request, 'firstapp/BLUR.html')


def Log(request):
    return render(request, 'firstapp/Logaut.html')


class LoginUser(LoginView):
    template_name = "firstapp/AVT.html"
    form_class = LoginUserForm
    success_url = reverse_lazy('home')

    def get_success_url(self) -> str:
        return self.success_url
