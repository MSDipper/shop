from django.contrib.auth import authenticate, login
from django.views import View
from django.shortcuts import render, redirect
from account.forms import AuthenticationForm
from django.views.generic import TemplateView


class PagesPage(TemplateView):
    ''' Страница отображения формы входа '''
    template_name = 'account/pages.html'
    

class RegisterUser(View):
    """ Регистрация пользователей """
    template_name = 'account/register/register.html'

    def get(self, request):
        context = {
            'form': AuthenticationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = AuthenticationForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('pages')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)