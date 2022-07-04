from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import IndexPage, About, Timeline, Testimonials
# Create your views here.



class IndexListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        inddexPage = IndexPage.objects.all()

        return render(request, self.template_name, {
            'inddexPage':inddexPage,

        })


def about(request):
    template_name = 'about.html'
    contexet = About.objects.all()
    return render(request, template_name, {'contexet':contexet} )


def timeline(request):
    template_name = 'timeline.html'
    contexet = Timeline.objects.all()

    return render(request, template_name, {'contexet':contexet})



def testimonials(request):
    template_name = 'testimonials.html'
    testimonialsPage = Testimonials.objects.all()

    return render(request, template_name, {
            'testimonialsPage':testimonialsPage,

        })



def booking(request):
    return render(request, 'booking.html') 


def contact(request):
    return render(request, 'contact.html') 