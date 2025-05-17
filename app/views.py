from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth import hashers
from .models import * 
import os

# Create your views here.


# User Register Section  ------>

def registration(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password1=hashers.make_password(password)
        user = User.objects.filter(email=email)

        if user.exists():
            messages.info(request, 'Email already exist! Use different mail')
            return redirect('/regis/')
        
        User.objects.create(username=username,email=email,password=password1)
        
        messages.success(request, 'Account Created succesfully')

    category1=category.objects.all()
    categories=category2.objects.all()
    brands=brand.objects.all()
    products=product.objects.all()
    return render(request,'registration.html',{'category':category1,'categories':categories,'brand':brands,'product':products})


#   Login Section   ----------->

def signin_user(request):
    category1=category.objects.all()
    categories=category2.objects.all()
    brands=brand.objects.all()
    products=product.objects.all()
    bnr=banners.objects.exclude(banner_name='default')
    homecard=menban.objects.exclude(menban_name='default')
    smcard=brandbnnr.objects.exclude(brnd_bn="default")
    menbnr=mbanner.objects.exclude(mbanner_name="default")
    womenbnr=wbanner.objects.exclude(wbanner_name="default")
    womencard=hwomencard.objects.exclude(wcard_name='default')
    shoess=shoes.objects.exclude(shoes_cat='default')
    womencard2=hwomencard2.objects.all()[:10]
    for b in bnr:
        b.banner=os.path.basename(b.banner.url)
    for hcrd in homecard:
        hcrd.men_ban=os.path.basename(hcrd.men_ban.url)
    for scard in smcard:
        scard.s_card=os.path.basename(scard.s_card.url)
    for mbnr in menbnr:
        mbnr.mbanner_image=os.path.basename(mbnr.mbanner_image.url)
    for wbnr in womenbnr:
        wbnr.women_banner=os.path.basename(wbnr.women_banner.url)
    for wcrd in womencard:
        wcrd.wcard_image=os.path.basename(wcrd.wcard_image.url)
    for wcrd2 in womencard2:
        wcrd2.wcard2_image=os.path.basename(wcrd2.wcard2_image.url)
    for s in shoess:
        s.shoes_banner=os.path.basename(s.shoes_banner.url)
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.warning(request, 'Invalid Username')
            return redirect('/signin/',{'banner':bnr,'hcard':homecard,'smallcard':smcard,'mbnr':menbnr,'wmnbnr':womenbnr,'womencard':womencard,'womencard2':womencard2,'shoes':shoess,'category':category1,'categories':categories[:2],'brand':brands,'product':products})
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('/signin/',{'banner':bnr,'hcard':homecard,'smallcard':smcard,'mbnr':menbnr,'wmnbnr':womenbnr,'womencard':womencard,'womencard2':womencard2,'shoes':shoess,'category':category1,'categories':categories[:2],'brand':brands,'product':products})
        
        else:
            login(request ,user)
            messages.success(request,'successfully login Countinue shopping!')
            return render(request,'index.html',{'banner':bnr,'hcard':homecard,'smallcard':smcard,'mbnr':menbnr,'wmnbnr':womenbnr,'womencard':womencard,'womencard2':womencard2,'shoes':shoess,'category':category1,'categories':categories[:2],'brand':brands,'product':products})
        
    return render(request,'signin.html',{'banner':bnr,'hcard':homecard,'smallcard':smcard,'mbnr':menbnr,'wmnbnr':womenbnr,'womencard':womencard,'womencard2':womencard2,'shoes':shoess,'category':category1,'categories':categories[:2],'brand':brands,'product':products})



# Logout Section  ------->

def signout_user(request):
    category1=category.objects.all()
    categories=category2.objects.all()
    brands=brand.objects.all()
    products=product.objects.all()
    bnr=banners.objects.exclude(banner_name='default')
    homecard=menban.objects.exclude(menban_name='default')
    smcard=brandbnnr.objects.exclude(brnd_bn="default")
    menbnr=mbanner.objects.exclude(mbanner_name="default")
    womenbnr=wbanner.objects.exclude(wbanner_name="default")
    womencard=hwomencard.objects.exclude(wcard_name='default')
    shoess=shoes.objects.exclude(shoes_cat='default')
    womencard2=hwomencard2.objects.all()[:10]
    for b in bnr:
        b.banner=os.path.basename(b.banner.url)
    for hcrd in homecard:
        hcrd.men_ban=os.path.basename(hcrd.men_ban.url)
    for scard in smcard:
        scard.s_card=os.path.basename(scard.s_card.url)
    for mbnr in menbnr:
        mbnr.mbanner_image=os.path.basename(mbnr.mbanner_image.url)
    for wbnr in womenbnr:
        wbnr.women_banner=os.path.basename(wbnr.women_banner.url)
    for wcrd in womencard:
        wcrd.wcard_image=os.path.basename(wcrd.wcard_image.url)
    for wcrd2 in womencard2:
        wcrd2.wcard2_image=os.path.basename(wcrd2.wcard2_image.url)
    for s in shoess:
        s.shoes_banner=os.path.basename(s.shoes_banner.url)
    logout(request)
    return render(request,'index.html',{'banner':bnr,'hcard':homecard,'smallcard':smcard,'mbnr':menbnr,'wmnbnr':womenbnr,'womencard':womencard,'womencard2':womencard2,'shoes':shoess,'category':category1,'categories':categories[:2],'brand':brands,'product':products})


# Profile Section --->

def profile(request):
    if request.user.is_authenticated:
        category1=category.objects.all()
        categories=category2.objects.all()
        brands=brand.objects.all()
        products=product.objects.all()
        return render(request, 'profile.html',{'category':category1,'categories':categories,'brand':brands,'product':products})
    else:
        messages.error(request,"Please login First")
        return render(request,'index.html',{'category':category1,'categories':categories,'brand':brands,'product':products})

    
# Home Template   ----->

def home(request):
    category1=category.objects.all()
    categories=category2.objects.all()
    brands=brand.objects.all()
    products=product.objects.all()
    bnr=banners.objects.exclude(banner_name='default')
    homecard=menban.objects.exclude(menban_name='default')
    smcard=brandbnnr.objects.exclude(brnd_bn="default")
    menbnr=mbanner.objects.exclude(mbanner_name="default")
    womenbnr=wbanner.objects.exclude(wbanner_name="default")
    womencard=hwomencard.objects.exclude(wcard_name='default')
    shoess=shoes.objects.exclude(shoes_cat='default')
    womencard2=hwomencard2.objects.all()[:10]
    for b in bnr:
        b.banner=os.path.basename(b.banner.url)
    for hcrd in homecard:
        hcrd.men_ban=os.path.basename(hcrd.men_ban.url)
    for scard in smcard:
        scard.s_card=os.path.basename(scard.s_card.url)
    for mbnr in menbnr:
        mbnr.mbanner_image=os.path.basename(mbnr.mbanner_image.url)
    for wbnr in womenbnr:
        wbnr.women_banner=os.path.basename(wbnr.women_banner.url)
    for wcrd in womencard:
        wcrd.wcard_image=os.path.basename(wcrd.wcard_image.url)
    for wcrd2 in womencard2:
        wcrd2.wcard2_image=os.path.basename(wcrd2.wcard2_image.url)
    for s in shoess:
        s.shoes_banner=os.path.basename(s.shoes_banner.url)
        
    return render(request,'index.html',{'banner':bnr,'hcard':homecard,'smallcard':smcard,'mbnr':menbnr,'wmnbnr':womenbnr,'womencard':womencard,'womencard2':womencard2,'shoes':shoess,'category':category1,'categories':categories[:2],'brand':brands,'product':products})


# Category -->

def cards(request):
        if request.method=="POST":
            title1=request.POST.get("category")
            card1=category.objects.get(category_name=title1.title())
            print(title1.title())
            category1=category.objects.all()
            categories=category2.objects.all()
            brands=brand.objects.all()
            products=product.objects.all()
            if card1:
                data=card.objects.filter(category_name=card1)
                print(data)
                for i in data:
                    i.image=os.path.basename(i.image.name)
                    print(i.category_name)
            return render(request,'product.html',{'data':data,'category':category1,'categories':categories,'brand':brands,'product':products})
        return render(request,'index.html',{'category':category1,'categories':categories,'brand':brands,'product':products})



#  Brand-Name  --->

def br_card(request):
    if request.method=="POST":
        title2=request.POST.get("brand_name")
        c_ard=brand.objects.get(brand_name=title2)
        category1=category.objects.all()[:4]
        categories=category2.objects.all()
        brands=brand.objects.all()
        products=product.objects.all()
        if c_ard:
            data=card.objects.filter(brand_name=c_ard)
            for i in data:
                i.image=os.path.basename(i.image.name)
        return render(request,"product.html",{'data':data,'brand':brands,'product':products,'category':category1,'categories':categories})
    return render(request,'index.html',{'data':data,'brand':brands,'product':products,'category':category1,'categories':categories})



#  Product Card --->

def product_cart(request):
    category1=category.objects.all()[:4]
    categories=category2.objects.all()
    brands=brand.objects.all()
    products=product.objects.all()
    if request.method=="POST":
        product_name=request.POST.get("pro_names")
        pro_d_cart=product.objects.get(pro_name=product_name)
        if pro_d_cart:
            data=card.objects.filter(pro_name=pro_d_cart)
            for i in data:
                i.image=os.path.basename(i.image.name)
        return render(request,"product.html",{'data':data,'brand':brands,'product':products,'category':category1,'categories':categories})
    return render(request,'index.html',{'data':data,'brand':brands,'product':products,'category':category1,'categories':categories})




# Product Details ---->

def product_det(request,iid,ititle):
    category1=category.objects.all()
    categories=category2.objects.all()
    brands=brand.objects.all()
    products=product.objects.all()
    prod=card.objects.get(id=iid)
    
    SIZE_CHOICE = card._meta.get_field('size').choices
    if prod:
        data=card.objects.filter(title=prod)
    for i in data:
        i.image1=os.path.basename(i.image1.name)
        i.image2=os.path.basename(i.image2.name)
        i.image3=os.path.basename(i.image3.name)
        i.image4=os.path.basename(i.image4.name)
        i.image5=os.path.basename(i.image5.name)
        i.image6=os.path.basename(i.image6.name)
    return render(request,'product_detail.html',{'data':data,'category':category1,'categories':categories,'brand':brands,'product':products,'size_choice':SIZE_CHOICE})



# Banners Section    ------>

def baners(request):
    if request.method=="POST":
        baner = request.POST.get("banners")
        baner1 = banners.objects.get(banner_name=baner)
        category1=category.objects.all()
        categories=category2.objects.all()
        brands=brand.objects.all()
        products=product.objects.all()
        if baner1:
            data=card.objects.filter(banner_name=baner1)
            for i in data:
                i.image=os.path.basename(i.image.name)
        return render(request,'product.html',{'data':data,'category':category1,'categories':categories,'brand':brands,'product':products})
    return render(request,'index.html',{'category':category1,'categories':categories,'brand':brands,'product':products})


# Brand Banners  -------->

def Trends(request):
    if request.method=="POST":
        trend = request.POST.get("trends")
        trend1 = brandbnnr.objects.get(brnd_bn=trend)
        category1=category.objects.all()
        categories=category2.objects.all()
        brands=brand.objects.all()
        products=product.objects.all()
        if trend1:
            data=card.objects.filter(brnd_bn=trend1)
            for i in data:
                i.image=os.path.basename(i.image.name)
        return render(request,'product.html',{'data':data,'category':category1,'categories':categories,'brand':brands,'product':products})
    return render(request,'index.html',{'category':category1,'categories':categories,'brand':brands,'product':products})


# Men Brand Banner Section --------->

def Menclothing(request):
    if request.method=="POST":
        m_clothing = request.POST.get("Men-clothing")
        m_clothing1 = mbanner.objects.get(mbanner_name=m_clothing)
        category1=category.objects.all()
        categories=category2.objects.all()
        brands=brand.objects.all()
        products=product.objects.all()
        if m_clothing1:
            data = card.objects.filter(mbanner_name=m_clothing1)
            for i in data:
                i.image=os.path.basename(i.image.url)
        return render(request,'product.html',{'data':data,'category':category1,'categories':categories,'brand':brands,'product':products})
    return render(request,'index.html',{'category':category1,'categories':categories,'brand':brands,'product':products})



# Women Brand Banner Section --------->

def Wenclothing(request):
    if request.method=="POST":
        w_clothing = request.POST.get("Women-clothing")
        w_clothing1 = wbanner.objects.get(wbanner_name=w_clothing)
        category1=category.objects.all()
        categories=category2.objects.all()
        brands=brand.objects.all()
        products=product.objects.all()
        if w_clothing1:
            data = card.objects.filter(wbanner_name=w_clothing1)
            for i in data:
                i.image=os.path.basename(i.image.url)
        return render(request,'product.html',{'data':data,'category':category1,'categories':categories,'brand':brands,'product':products})
    return render(request,'index.html',{'category':category1,'categories':categories,'brand':brands,'product':products})



# Top Brand Banners Section   ---------->

def Topbrand(request):
    try:
         category1=category.objects.all()
         categories=category2.objects.all()
         brands=brand.objects.all()
         products=product.objects.all()
         if request.method=="POST":
                topbrand = request.POST.get("top-brand")
                topbrand1 = menban.objects.get(menban_name=topbrand)
                if topbrand1:
                    data = card.objects.filter(menban_name=topbrand1)
                    for i in data:
                        i.image=os.path.basename(i.image.url)
                return render(request,'product.html',{'data':data,'category':category1,'categories':categories,'brand':brands,'product':products})
         return render(request,'index.html',{'category':category1,'categories':categories,'brand':brands,'product':products})
    except ObjectDoesNotExist:
        return None
    

# # Women Brand Banner Section --------->

def Womenbrand(request):
    try:
         category1=category.objects.all()
         categories=category2.objects.all()
         brands=brand.objects.all()
         products=product.objects.all()
         if request.method=="POST":
                womenbrand = request.POST.get("women-brands")
                womenbrand1 = hwomencard.objects.get(wcard_name=womenbrand)
                if womenbrand1:
                    data = card.objects.filter(wcard_name=womenbrand1)
                    for i in data:
                        i.image=os.path.basename(i.image.url)
                return render(request,'product.html',{'data':data,'category':category1,'categories':categories,'brand':brands,'product':products})
         return render(request,'index.html',{'category':category1,'categories':categories,'brand':brands,'product':products})
    except ObjectDoesNotExist:
        return None
    

# Star Women Brand Banner Section --------->

def Starbrand(request):
    try:
        category1=category.objects.all()
        categories=category2.objects.all()
        brands=brand.objects.all()
        products=product.objects.all()
        if request.method=="POST":
            star = request.POST.get("star-brands")
            star1 = hwomencard2.objects.get(wcard2_name=star)
            if star1:
                data = card.objects.filter(wcard2_name=star1)
                for i in data:
                    i.image=os.path.basename(i.image.url)
            return render(request,'product.html',{'data':data,'category':category1,'categories':categories,'brand':brands,'product':products})
        return render(request,'index.html',{'category':category1,'categories':categories,'brand':brands,'product':products})
    except ObjectDoesNotExist:
        return None


# Shoes Brand Banner Section --------->        

def Shoesbanner(request):
    try:
        category1=category.objects.all()
        categories=category2.objects.all()
        brands=brand.objects.all()
        products=product.objects.all()
        if request.method=="POST":
            shoesb = request.POST.get("shoes-banner")
            shoesb1 = shoes.objects.get(shoes_cat=shoesb)
            if shoesb1:
                data = card.objects.filter(shoes_cat=shoesb1)
                for i in data:
                    i.image=os.path.basename(i.image.url)
            return render(request,'product.html',{'data':data,'category':category1,'categories':categories,'brand':brands,'product':products})
        return render(request,'index.html',{'category':category1,'categories':categories,'brand':brands,'product':products})
    except ObjectDoesNotExist:
        return None


# Search Functionality --->

def search(request):
    category1=category.objects.all()
    categories=category2.objects.all()
    brands=brand.objects.all()
    products=product.objects.all()
    query = request.GET['query']
    Product_title = card.objects.filter(product_title__icontains=query)
    Brand_Name = card.objects.filter(brand_name__brand_name__icontains=query)
    Product_name = card.objects.filter(pro_name__pro_name__icontains=query)
    data = Product_title.union(Brand_Name,Product_name)
    for i in data:
        i.image=os.path.basename(i.image.url)
    return render(request,'search.html',{'category':category1,'categories':categories,'brand':brands,'product':products,'data':data,'query':query})


#   Cart ----->

def car_t(request):
    category1=category.objects.all()
    categories=category2.objects.all()
    brands=brand.objects.all()
    products=product.objects.all()
    if request.user.is_authenticated:
        if request.method=="POST":
            Card_info = card.objects.get(id=request.POST['iid'])
            qyt1 = request.POST['quantity']
            si_ze = request.POST['si-ze']
            tprice = int(Card_info.price) * int(qyt1)
            Cartitem.objects.create(Card=Card_info,qyt=qyt1,user=request.user,price=tprice,Size=si_ze)

        cartData = Cartitem.objects.filter(user=request.user)
        Subtotal = 0
        for cd in cartData:
            Subtotal+=int(cd.price)

        return render(request,'cart.html',{'cartData':cartData,'Subtotal':Subtotal,'category':category1,'categories':categories,'brand':brands,'product':products})
    else:
        messages.warning(request,'If you want to add product! Please login first')
        return render(request,'cart.html',{'category':category1,'categories':categories,'brand':brands,'product':products})
    

# Remove Items from cart Section ------->

def remove(request):
    if request.method=="POST":
        name1 = request.POST.get('Card')

        data = Cartitem.objects.filter(Card=name1,user=request.user)
        data.delete()

        
        cartData = Cartitem.objects.filter(user=request.user)
        Total=0
        for cd in cartData:
            Total+=int(cd.price)

    return redirect('/cart/')



#   Wishlist ---->

def wish(request):
    category1=category.objects.all()
    categories=category2.objects.all()
    brands=brand.objects.all()
    products=product.objects.all()
    if request.user.is_authenticated:
        if request.method=="POST":
            Wish = card.objects.get(id=request.POST['wiid'])
            tprice1 = int(Wish.price)
            wishlist.objects.create(product_name=Wish,price=tprice1,user=request.user)
        wishdata = wishlist.objects.filter(user=request.user)
        return render(request,'wishlist.html',{'wishdata':wishdata,'category':category1,'categories':categories,'brand':brands,'product':products})
    else:
        messages.warning(request,'If You want to add product in your wishlist! Please login first')
        return render(request, 'wishlist.html',{'category':category1,'categories':categories,'brand':brands,'product':products})
    

# Remove Items from wishlist Section ------->    

@login_required
def wremove(request):
    if request.method == "POST":
        item_id = request.POST.get('product_name')

        data1 = wishlist.objects.filter(product_name=item_id,user = request.user)
        data1.delete()
        
        return redirect('/wishlist')
    


# Contact Us Section ----->

def contact(request):
    category1=category.objects.all()
    categories=category2.objects.all()
    brands=brand.objects.all()
    products=product.objects.all()
    logo1=logo.objects.all()
    if request.method=="POST":
        name = request.POST.get('name1')
        email = request.POST.get('email1')
        message = request.POST.get('message')
        Contactus.objects.create(name=name,email=email,message=message,user=request.user)
    for l in logo1:
        l.logo_image=os.path.basename(l.logo_image.url)
    return render(request,'contact.html',{'logo':logo1,'category':category1,'categories':categories,'brand':brands,'product':products})   



#   Profile update section    ---------->

def updateprofile(request):
    if request.method=="POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        # username = request.POST.get("username")
        user_id = request.user.id

        user = User.objects.get(id=user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        user.save()

        messages.success(request,"Your Profile has been updated successfully")
        return redirect("/profileupdate/") 
    else:
        messages.error(request,"Something wrong")   
        return redirect("/profile/") 



#  Order address --------->

def shipping_address(request):
    category1=category.objects.all()
    categories=category2.objects.all()
    brands=brand.objects.all()
    products=product.objects.all()
    logo1=logo.objects.all()
    bnr=banners.objects.exclude(banner_name='default')
    homecard=menban.objects.exclude(menban_name='default')
    smcard=brandbnnr.objects.exclude(brnd_bn="default")
    menbnr=mbanner.objects.exclude(mbanner_name="default")
    womenbnr=wbanner.objects.exclude(wbanner_name="default")
    womencard=hwomencard.objects.exclude(wcard_name='default')
    shoess=shoes.objects.exclude(shoes_cat='default')
    womencard2=hwomencard2.objects.all()[:10]
    for b in bnr:
        b.banner=os.path.basename(b.banner.url)
    for hcrd in homecard:
        hcrd.men_ban=os.path.basename(hcrd.men_ban.url)
    for scard in smcard:
        scard.s_card=os.path.basename(scard.s_card.url)
    for mbnr in menbnr:
        mbnr.mbanner_image=os.path.basename(mbnr.mbanner_image.url)
    for wbnr in womenbnr:
        wbnr.women_banner=os.path.basename(wbnr.women_banner.url)
    for wcrd in womencard:
        wcrd.wcard_image=os.path.basename(wcrd.wcard_image.url)
    for wcrd2 in womencard2:
        wcrd2.wcard2_image=os.path.basename(wcrd2.wcard2_image.url)
    for s in shoess:
        s.shoes_banner=os.path.basename(s.shoes_banner.url)

    if request.method =="POST":
        first_name = request.POST.get("f_name")
        last_name = request.POST.get("l_name")
        phone_no = request.POST.get("phone_no")
        alternate_no = request.POST.get("Alternate_phone")
        address1 = request.POST.get("address1")
        address2 = request.POST.get("address2")
        city = request.POST.get("city")
        state = request.POST.get("state")
        zip = request.POST.get("zip")
        Shippingaddress.objects.create(f_name=first_name, l_name=last_name,address1=address1,address2=address2,Phoneno1=phone_no,alterPhone=alternate_no,city=city,state=state,pincode=zip)
        messages.success(request,"Your Order is Successfully Place")
        return render(request,'index.html',{'logo':logo1,'banner':bnr,'hcard':homecard,'smallcard':smcard,'mbnr':menbnr,'wmnbnr':womenbnr,'womencard':womencard,'womencard2':womencard2,'shoes':shoess,'category':category1,'categories':categories[:2],'brand':brands,'product':products})
    else:
        return render(request,'Shipping_address.html',{'logo':logo1,'banner':bnr,'hcard':homecard,'smallcard':smcard,'mbnr':menbnr,'wmnbnr':womenbnr,'womencard':womencard,'womencard2':womencard2,'shoes':shoess,'category':category1,'categories':categories[:2],'brand':brands,'product':products})
    

def order(request):
    category1=category.objects.all()
    categories=category2.objects.all()
    brands=brand.objects.all()
    products=product.objects.all()
    logo1=logo.objects.all()
    shipping=Shippingaddress.objects.all()
    return render(request,'order.html',{'logo':logo1,'category':category1,'categories':categories,'brand':brands,'product':products,'orders':shipping})