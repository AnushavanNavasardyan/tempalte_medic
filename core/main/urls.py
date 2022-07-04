from django.urls import path
from .views import IndexListView, about, timeline, testimonials, booking, contact

urlpatterns = [
    path('', IndexListView.as_view(), name='IndexPage' ),
    path('about/', about, name='about' ),
    path('timeline/', timeline, name='timeline' ),
    path('testimonials/', testimonials, name='testimonials' ),
    path('booking/', booking, name='booking' ),
    path('contact/', contact, name='contact' ),

]