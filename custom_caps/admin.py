from django.contrib import admin
from custom_caps.models import Magazine, Manufacturer, Caps, UserCapsRelation

# Добавил все модели в админку
admin.site.register(Magazine),
admin.site.register(Manufacturer)
admin.site.register(Caps)
admin.site.register(UserCapsRelation)
