from django.contrib import admin
from django.contrib import admin
from .models import Khachhang, Loaitietkiem, Phieutietkiem, Phieuruttien, Baocaongay, Baocaothang

# Register your models here.


class KhachhangAdmin (admin.ModelAdmin):
    list_display = ["makh", "tenkh", "diachi", "cccd"]
    search_fields = ["makh", "tenkh"]


class LoaitietkiemAdmin (admin.ModelAdmin):
    list_display = ["maltk", "ltk", "kyhan",
                    "sotiengoitoithieu", "thoigiangoitoithieu", "laisuat"]
    search_fields = ["maltk", "ltk", "kyhan"]


class PhieutietkiemAdmin (admin.ModelAdmin):
    list_display = ["maptk", "makh", "maltk", "sotiengoi",
                    "ngaydongphieu", "ngaymophieu", "sodu", "tinhtrang"]
    search_fields = ["maptk", "makh"]
    list_filter = ["ngaymophieu"]
    date_hierarchy = 'ngaymophieu'


class PhieuruttienAdmin (admin.ModelAdmin):
    list_display = ["maprt", "makh", "maptk", "ngayrut", "sotienrut"]
    search_fields = ["maprt", "makh_id", "ngayrut"]
    list_filter = ["ngayrut"]
    date_hierarchy = 'ngayrut'


class BaocaongayAdmin (admin.ModelAdmin):
    list_display = ["ngay", "maltk", "tongthu", "tongchi", "chechlechthuchi"]
    date_hierarchy = 'ngay'
    search_fields = ["ngay", "maltk"],
    list_filter = ['ngay', 'maltk']


class BaocaothangAdmin (admin.ModelAdmin):
    list_display = ["ngaythang", "maltk",
                    "phieugoi", "phieudong", "chenhlechdonggoi"]
    date_hierarchy = 'ngaythang'
    list_filter = ['ngaythang', 'maltk']
    search_fields = ["ngaythang", "maltk"],


# Register your models here.
admin.site.register(Khachhang, KhachhangAdmin)
admin.site.register(Loaitietkiem, LoaitietkiemAdmin)
admin.site.register(Phieutietkiem, PhieutietkiemAdmin)
admin.site.register(Phieuruttien, PhieuruttienAdmin)
admin.site.register(Baocaongay, BaocaongayAdmin)
admin.site.register(Baocaothang, BaocaothangAdmin)

# admin.site.register(KhachhangAdmin)
# admin.site.register(LoaitietkiemAdmin)
# admin.site.register(PhieutietkiemAdmin)
# admin.site.register(PhieuruttienAdmin)
# admin.site.register(BaocaongayAdmin)
# admin.site.register(BaocaothangAdmin)
