from django.contrib import admin
from .models import Authors , Users ,Categories , Books , BookAudioFiles ,BookReviews
# Register your models here.
admin.site.register(Authors)
admin.site.register(Users)
admin.site.register(Categories)
admin.site.register(Books)
admin.site.register(BookReviews)
admin.site.register(BookAudioFiles)


