
from django.contrib import admin
from django.urls import path
from home import  views 


admin.site.site_header="sandipan mondal"
admin.site.site_title="sandipan is great"
admin.site.index_title="welcome to my page"

urlpatterns = [
    path('',views.index, name='index'),
    path('home',views.home, name='home'),
    path('login',views.login, name='login'),
    path('sineup',views.sineup, name='sineup'),
    path('product',views.item, name='product'),
    path('order',views.order, name='order'),
    path('addcard',views.addcard, name='addcard'),
    path('aboutus',views.aboutus, name='aboutus'),
    path('mycard',views.mycard, name='mycard'),
    path('electronics',views.electronics, name='electronics'),
    path('fmcg',views.fmcg, name='fmcg'),
    path('buity',views.buity, name='buity'),
]
