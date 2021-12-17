from django.contrib import admin
from app.models import TODO,sp,kp


@admin.register(TODO)
class TODOdisp(admin.ModelAdmin):
    list_display=['id','title','status','user','date','priority']

@admin.register(sp)
class sssp(admin.ModelAdmin):
    list_display=['ssp']



@admin.register(kp)
class kssp(admin.ModelAdmin):
    list_display=['kkp']