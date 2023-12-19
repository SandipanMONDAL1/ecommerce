from django.contrib import admin
from home.models import contact
from home.models import product
from home.models import dilivary

from home.models import card
# Register your models here.
admin.site.register(contact)
admin.site.register(product)
admin.site.register(dilivary)

admin.site.register(card)