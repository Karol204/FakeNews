from django.shortcuts import render, redirect
from django.views import View
from .models import Webpage
from .forms import PageForm
# Create your views here.


class FirstPage(View):

    def get(self, request):
        all_pages = Webpage.objects.all()

        ctx = {
            'all_paged': all_pages
        }
        return render(request, 'LandingPage.html', ctx)

class FormPage(View):

    def get(self, request):
        form = PageForm()

        ctx = {
            'form': form,
        }
        return render(request, 'FormPage.html', ctx)

    def post(self, request):
        name = request.POST.get('name')
        description = request.POST.get('description')
        link = request.POST.get('link')
        newWebpage = Webpage()
        newWebpage.name = name
        newWebpage.description = description
        newWebpage.link = link
        print(newWebpage)
        newWebpage.save()
        return redirect('/')
