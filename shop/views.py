from django.shortcuts import render
from django.http import HttpResponse
from . models import Product,Contact,Banner,Order, OrderUpdate
from math import ceil
import json

def shop(req):
   
    allproducts = []
    catofproducts = Product.objects.values('category','id')
    cats = {item['category'] for item in catofproducts}
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        noofslides = n//4 + ceil((n/4) - (n//4))
        allproducts.append([prod,noofslides])

    banners = Banner.objects.all()

    params = {
        "allproducts": allproducts,
        "banners": banners
    }
    return render(req,'index.html',params)


def about(req):
    return render(req,'about.html')


def contact(req):
    if req.method == "POST":
        print(req)
        name = req.POST.get('name','')
        email = req.POST.get('email','')
        phone = req.POST.get('phone','')
        query = req.POST.get('query','')
        contact = Contact(name=name,email=email,phone=phone,query=query)
        contact.save()
    return render(req,'contact.html')


def productview(req,pid):

    product = Product.objects.filter(id = pid)
    print(product)

    return render(req,'productview.html',{'product':product[0]})


def search(req):
    return render(req,'search.html')


def tracker(req):
    if req.method == "POST":
        order_id = req.POST.get('order_id','')
        phone = req.POST.get('phone','')

        try:
            order = Order.objects.filter(order_id= order_id, phone=phone)
            if len(order)> 0:
                order_update = OrderUpdate.objects.filter(order_id= order_id)
                updates = []
                for i in order_update:
                    updates.append({'update_id': i.update_id , 'order_id': i.order_id , 'update_desc':i.update_desc, 'time': i.timestamp})    
                    response = json.dumps(updates,default=str)
                    return HttpResponse(response)
            else:
                return HttpResponse("error")
        
        except expression as identifier:
            return HttpResponse(f"Found {identifier}")

    return render(req,'tracker.html')


def checkout(req):
    if req.method == "POST":
        item_json = req.POST.get('item_json','')
        name = req.POST.get('name','')
        phone = req.POST.get('phone','')
        address = req.POST.get('address','')
        city = req.POST.get('city','')
        state = req.POST.get('state','')
        pincode = req.POST.get('pincode','')

        order = Order(item_json=item_json,name=name,phone=phone,address=address,state=state,city=city,pincode=pincode)  
        order.save()  
        orderupdate = OrderUpdate(order_id = order.order_id, update_desc="Your order has been placed Successfully")
        orderupdate.save()
        status = True ## success
        order_id = order.order_id
        params = {
            'order_id': order_id,
            'status': status
        }
        return render(req,'checkout.html',params)


    return render(req,'checkout.html')

