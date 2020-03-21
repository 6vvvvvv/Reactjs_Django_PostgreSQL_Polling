from django.contrib import admin
from .models import Pollingoption, Pollingtitle

# Register your models here.
myModels=[Pollingoption, Pollingtitle]
admin.site.register(myModels)
