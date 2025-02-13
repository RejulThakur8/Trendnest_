from django.contrib import admin
from .models import brand,banners,menban,brandbnnr,wbanner,hwomencard,hwomencard2,shoes,category,category2,product,mbanner,card,sign,logo,Cartitem,Contactus,wishlist,Shippingaddress
# Register your models here.


class cardAdmin(admin.ModelAdmin):
    list_display=['id','title','price','rating','brand_name','pro_name','category_name']

class bannersAdmin(admin.ModelAdmin):
    list_display=['brand_name','banner_name','banner']

class menbanAdmin(admin.ModelAdmin):
    list_display=['brand_name','menban_name','men_ban']

class brandbnnrAdmin(admin.ModelAdmin):
    list_display=['brand_name','brnd_bn','s_card']

class CartitemAdmin(admin.ModelAdmin):
    list_display=['user','Card','qyt','Size','price']

class wishlistAdmin(admin.ModelAdmin):
    list_display=['user','product_name','price']

admin.site.register(brand)#
admin.site.register(banners, bannersAdmin)#
admin.site.register(menban,menbanAdmin)#
admin.site.register(brandbnnr,brandbnnrAdmin)#
admin.site.register(wbanner)#
admin.site.register(hwomencard)#
admin.site.register(hwomencard2)#
admin.site.register(shoes)#
admin.site.register(category) #
admin.site.register(category2) #
admin.site.register(product)#
admin.site.register(mbanner)#
admin.site.register(card, cardAdmin)#
admin.site.register(sign)
admin.site.register(logo)
admin.site.register(Cartitem,CartitemAdmin)
admin.site.register(Contactus)
admin.site.register(wishlist,wishlistAdmin)
admin.site.register(Shippingaddress)