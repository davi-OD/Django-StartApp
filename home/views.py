from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

# Create your views here.


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.htm'
    success_url = '/smart/notes'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)


class LoginInterfaceView(LoginView):
    template_name = "home/login.htm"


class LogoutInterfaceView(LogoutView):
    template_name = "home/logout.htm"


class HomeView(TemplateView):
    template_name = 'home/welcome.htm'
    extra_context = {'today': datetime.today()}

# The function based view below has been replaced by the classed base view above
# def home(request):
#     return render(request, 'home/welcome.htm', {'today': datetime.today()})


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.htm'
    login_url = '/admin'


# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, 'home/authorized.htm', {})


# What is a mixin class?
# These are helper classes that can be used along with other classes to provide additional features
