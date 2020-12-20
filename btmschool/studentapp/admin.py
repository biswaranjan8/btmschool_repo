from django.contrib import admin
from studentapp.models import *


@admin.register(registerModel)
class registretion(admin.ModelAdmin):
    list_display = ['name', 'ad_class', 'DOB', 'place_birth', 'nation', 'state', 'religion', 'gender', 'caste',
                    'permanent_address', 'pin_code', 'blood_group', 'identification_mark', 'other_info']
