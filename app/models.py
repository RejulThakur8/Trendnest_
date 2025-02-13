from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class sign(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    def __str__(self):
        return self.username

class logo(models.Model):
    logo_image=models.ImageField(upload_to='statics/image',default='Trendnest')


class brand(models.Model):
    brand_name = models.CharField(max_length=50)
    def __str__(self):
        return self.brand_name

class banners(models.Model):
    brand_name = models.ForeignKey(brand,related_name='a',on_delete=models.CASCADE,default="men")
    banner_name = models.CharField(max_length=50)
    banner = models.ImageField(upload_to='statics/image',default='bn')
    def __str__(self):
        return self.banner_name
    
    
class menban(models.Model):
    brand_name = models.ForeignKey(brand, related_name='b',on_delete=models.CASCADE)
    menban_name = models.CharField(max_length=50,default="kids")
    men_ban = models.ImageField(upload_to='statics/image',default='cs')       
    def __str__(self):
        return self.menban_name
    
    
class brandbnnr(models.Model):
    brand_name = models.ForeignKey(brand,related_name='c',on_delete=models.CASCADE,default="women")
    brnd_bn=models.CharField(max_length=50,)
    s_card = models.ImageField(upload_to='statics/image',default='s')       # wait
    def __str__(self):
        return self.brnd_bn
    

class mbanner(models.Model):
    brand_name = models.ForeignKey(brand,related_name='h',on_delete=models.CASCADE,default="men")
    mbanner_name = models.CharField(max_length=110,default='frag')
    mbanner_image = models.ImageField(upload_to='statics/image')
    def __str__(self):
        return self.mbanner_name
    
    

class wbanner(models.Model):
    brand_name = models.ForeignKey(brand,related_name='d',on_delete=models.CASCADE,default="levis")
    wbanner_name = models.CharField(max_length=50)
    women_banner = models.ImageField(upload_to='statics/image',default='Ab')
    def __str__(self):
        return self.wbanner_name
    
class hwomencard(models.Model):
    brand_name = models.ForeignKey(brand,related_name='e',on_delete=models.CASCADE,default="polo")
    wcard_name = models.CharField(max_length=50,default="women")
    wcard_image = models.ImageField(upload_to='statics/image',default="kj")
    def __str__(self):
        return self.wcard_name
    

class hwomencard2(models.Model):
    brand_name = models.ForeignKey(brand,related_name='f',on_delete=models.CASCADE,default="trend")
    wcard2_name = models.CharField(max_length=50,default="boys")
    wcard2_image = models.ImageField(upload_to='statics/image',default="b")
    def __str__(self):
        return self.wcard2_name
    

class shoes(models.Model):
    brand_name = models.ForeignKey(brand,related_name='g',on_delete=models.CASCADE,default="asian")
    shoes_cat = models.CharField(max_length=22)
    shoes_banner = models.ImageField(upload_to='statics/image',default='sho')
    def __str__(self):
        return self.shoes_cat
    
class category(models.Model):
    category_name = models.CharField(max_length=20,default='Male')
    def __str__(self):
        return self.category_name
    
class category2(models.Model):
    category2_name = models.CharField(max_length=39)
    def __str__(self):
        return self.category2_name
    
    
class product(models.Model):
    pro_name = models.CharField(max_length=100,default="products")
    def __str__(self):
        return self.pro_name
    

    
SIZE_CHOICE=(
    ('NA', 'NA'),
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL','Xtra Large'),
    ('XXl','Double Xtra Lagre'),
    ('UK','5'),
    ('UK','6'),
    ('UK','7'),
    ('UK','8'),
    ('UK','9'),
    ('UK','10'),
    ('UK','11'),
)



class card(models.Model):
    image = models.ImageField(upload_to='statics/image',default="ab")
    title = models.TextField()
    size = models.CharField(choices=SIZE_CHOICE,max_length=20)
    product_title = models.CharField(max_length=103,default='women') 
    rating = models.CharField(max_length=31, null=True)
    price = models.IntegerField(null=True)
    brand_name = models.ForeignKey(brand,related_name='brand',on_delete=models.CASCADE)
    pro_name = models.ForeignKey(product,related_name="prod",on_delete=models.CASCADE)
    shoes_cat = models.ForeignKey(shoes,related_name='shoes',on_delete=models.CASCADE)
    category_name = models.ForeignKey(category,related_name='categoriesname',on_delete=models.CASCADE)
    category2_name = models.ForeignKey(category2,related_name='cat2name',on_delete=models.CASCADE)
    banner_name = models.ForeignKey(banners,related_name='i',on_delete=models.CASCADE)
    menban_name = models.ForeignKey(menban,related_name='j',on_delete=models.CASCADE)
    wbanner_name = models.ForeignKey(wbanner, related_name='l',on_delete=models.CASCADE)
    shoes_cat = models.ForeignKey(shoes, related_name='m',on_delete=models.CASCADE)
    wcard_name = models.ForeignKey(hwomencard, related_name='n',on_delete=models.CASCADE)
    wcard2_name = models.ForeignKey(hwomencard2,related_name='o',on_delete=models.CASCADE)
    brnd_bn = models.ForeignKey(brandbnnr, related_name='bbnr',on_delete=models.CASCADE)
    mbanner_name = models.ForeignKey(mbanner, related_name='mb',on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='statics/image')
    image2 = models.ImageField(upload_to='statics/image')
    image3 = models.ImageField(upload_to='statics/image')
    image4 = models.ImageField(upload_to='statics/image')
    image5 = models.ImageField(upload_to='statics/image')
    image6 = models.ImageField(upload_to='statics/image')
    def __str__(self):
        return self.title
    
# class product_card(models.Model):
#     image = models.ImageField(upload_to="statics/image")
#     title = models.TextField()
#     product_title = models.CharField(max_length=100,default="AB")

class Cartitem(models.Model):
    Card = models.ForeignKey(card, on_delete=models.CASCADE)
    qyt = models.CharField(max_length=100,default=0)
    Size = models.CharField(max_length=50,default="s")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.Size
    

class wishlist(models.Model):
    product_name = models.ForeignKey(card, on_delete=models.CASCADE)
    price = models.IntegerField(null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    

class Contactus(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField(default='There is good service')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
   

class Shippingaddress(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    address1 = models.TextField()
    address2 = models.TextField()
    Phoneno1 = models.CharField(max_length=15,default=0)
    alterPhone = models.CharField(max_length=15,default=0)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.IntegerField()

    def __str__(self):
        return self.f_name