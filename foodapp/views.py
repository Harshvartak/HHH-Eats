from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.auth.decorators import login_required
from collections import Counter
from django.urls import reverse
from django.db.models import Q
from .models import *
from django.http import HttpResponse


"""
Authentication Starts
"""
def register(request):
    form=UserCreationForm(request.POST)
    print(form.is_valid(),request.method)
    if request.method=="POST" :

        if form.is_valid():
            print(form.data)
            form.save()
            return HttpResponse("Kya haal")
        else:
            print(form.errors)
    return render(request,"signup.html",{'form':form})


def Logout(request):
    logout(request)
    return redirect("login")

def customerRegister(request):
    if request.method=='POST':
        form =CustomerForm(request.POST,request.FILES)
        if form.is_valid():
            print("-------->",form.data)
            Customer=form.save()
            Customer.set_password(Customer.password)
            Customer.is_customer = True
            Customer.is_owner=False
            Customer.is_agree=True
            Customer.save()
            return redirect('customer_home')
        else:
            print(form.errors)
    else:
        form=CustomerForm()
    return render(request,'cust_signup.html',{'form':form})

def createCustomer(request):
	form = CustomerForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		return redirect("profile")
	context={
	'form':form, 
	'title':"Complete Your profile"
	}
	return render(request,'profile_form.html',context)

def RestaurantRegister(request):
    if request.method=='POST':

        form =RestuarantForm(request.POST,request.FILES)
        if form.is_valid():
            print("-------->",form.data)
            Owner=form1.save()
            Owner.set_password(Farmer.password)
            Owner.is_customer = False
            Owner.is_owner=True
            Owner.is_agree=True
            Owner.save()
            return redirect('restaurant_home')
    else:
        form=RestuarantForm()
    return render(request,'rest_signup.html',{'form':form})


@login_required
def createRestaurant(request):
    form = RestuarantForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect("rprofile")
    context = {"form": form, "title": "Complete Your Restaurant profile"}
    return render(request, "webapp/rest_profile_form.html", context)


"""
Authentication Ends
"""

############################################################### Customer Side Stuff ###############################################
def index(request):
    return render(request, "customer_home.html")


def orderplaced(request):
    return render(request, "")


def restuarant(request):
    r_object = Restaurant.objects.all()
    query = request.GET.get("q")
    if query:
        r_object = Restaurant.objects.filter(Q(rname__icontains=query)).distinct()
        return render(request, "", {"r_object": r_object})
    return render(request, "", {"restuarant": r_object})


def customerProfile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    return render(request, "webapp/profile.html", {"user": user})

@login_required
def updateCustomer(request, id):
    form = CustomerForm(request.POST or None, instance=request.user.customer)
    if form.is_valid():
        form.save()
        return redirect("profile")
    context = {"form": form, "title": "Update Your profile"}
    return render(request, "webapp/profile_form.html", context)


def restuarantMenu(request, pk=None):

    menu = Menu.objects.get(r_id=pk)
    rest = Restaurant.objects.get(id=pk)
    items = []
    context={
        'rest':rest,
        'menu':menu
    }
    return render(request, "menu.html", context)


@login_required
def checkout(request):
    if request.POST:
        addr = request.POST["address"]
        ordid = request.POST["oid"]
        Order.objects.filter(id=int(ordid)).update(
            delivery_addr=addr, status=Order.ORDER_STATE_PLACED
        )
        return redirect("/orderplaced/")
    else:
        cart = request.COOKIES["cart"].split(",")
        cart = dict(Counter(cart))
        items = []
        totalprice = 0
        uid = User.objects.filter(username=request.user)
        oid = Order()
        oid.orderedBy = uid[0]
        for x, y in cart.items():
            item = []
            it = Menu.objects.filter(id=int(x))
            if len(it):
                oiid = orderItem()
                oiid.item_id = it[0]
                oiid.quantity = int(y)
                oid.r_id = it[0].r_id
                oid.save()
                oiid.ord_id = oid
                oiid.save()
                totalprice += int(y) * it[0].price
                item.append(it[0].item_id.fname)
                it[0].quantity = it[0].quantity - y
                it[0].save()
                item.append(y)
                item.append(it[0].price * int(y))

            items.append(item)
        oid.total_amount = totalprice
        oid.save()
        context = {"items": items, "totalprice": totalprice, "oid": oid.id}
        return render(request, "webapp/order.html", context)


########################################################### Restaurant side stuff ###################################################

# creating restuarant account
def rest_index(request):
    return render(request,'rest_home.html')


# restaurant profile view
def restaurantProfile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    return render(request, "webapp/rest_profile.html", {"user": user})


# create restaurant detail



# Update restaurant detail
@login_required
def updateRestaurant(request, id):
    form = RestuarantForm(
        request.POST or None, request.FILES or None, instance=request.user.restaurant
    )
    if form.is_valid():
        form.save()
        return redirect("rprofile")
    context = {"form": form, "title": "Update Your Restaurant profile"}
    return render(request, "webapp/rest_profile_form.html", context)


# add  menu item for restaurant
@login_required
def menuManipulation(request):
    if not request.user.is_authenticated:
        return redirect("rlogin")

    rest = Restaurant.objects.filter(id=request.user.restaurant.id)
    rest = rest[0]
    if request.POST:
        type = request.POST["submit"]
        if type == "Modify":
            menuid = int(request.POST["menuid"])
            memu = Menu.objects.filter(id=menuid).update(
                price=int(request.POST["price"]), quantity=int(request.POST["quantity"])
            )
        elif type == "Add":
            itemid = int(request.POST["item"])
            item = Item.objects.filter(id=itemid)
            item = item[0]
            menu = Menu()
            menu.item_id = item
            menu.r_id = rest
            menu.price = int(request.POST["price"])
            menu.quantity = int(request.POST["quantity"])
            menu.save()
        else:
            menuid = int(request.POST["menuid"])
            menu = Menu.objects.filter(id=menuid)
            menu[0].delete()

    menuitems = Menu.objects.filter(r_id=rest)
    menu = []
    for x in menuitems:
        cmenu = []
        cmenu.append(x.item_id)
        cmenu.append(x.price)
        cmenu.append(x.quantity)
        cmenu.append(x.id)
        menu.append(cmenu)

    menuitems = Item.objects.all()
    items = []
    for y in menuitems:
        citem = []
        citem.append(y.id)
        citem.append(y.fname)
        items.append(citem)

    context = {
        "menu": menu,
        "items": items,
        "username": request.user.username,
    }
    return render(request, "webapp/menu_modify.html", context)


def orderlist(request):
    if request.POST:
        oid = request.POST["orderid"]
        select = request.POST["orderstatus"]
        select = int(select)
        order = Order.objects.filter(id=oid)
        if len(order):
            x = Order.ORDER_STATE_WAITING
            if select == 1:
                x = Order.ORDER_STATE_PLACED
            elif select == 2:
                x = Order.ORDER_STATE_ACKNOWLEDGED
            elif select == 3:
                x = Order.ORDER_STATE_COMPLETED
            elif select == 4:
                x = Order.ORDER_STATE_DISPATCHED
            elif select == 5:
                x = Order.ORDER_STATE_CANCELLED
            else:
                x = Order.ORDER_STATE_WAITING
            order[0].status = x
            order[0].save()

    orders = Order.objects.filter(r_id=request.user.restaurant.id).order_by(
        "-timestamp"
    )
    corders = []

    for order in orders:

        user = User.objects.filter(id=order.orderedBy.id)
        user = user[0]
        corder = []
        if user.is_restaurant:
            corder.append(user.restaurant.rname)
            corder.append(user.restaurant.info)
        else:
            corder.append(user.customer.f_name)
            corder.append(user.customer.phone)
        items_list = orderItem.objects.filter(ord_id=order)

        items = []
        for item in items_list:
            citem = []
            citem.append(item.item_id)
            citem.append(item.quantity)
            menu = Menu.objects.filter(id=item.item_id.id)
            citem.append(menu[0].price * item.quantity)
            menu = 0
            items.append(citem)

        corder.append(items)
        corder.append(order.total_amount)
        corder.append(order.id)

        x = order.status
        if x == Order.ORDER_STATE_WAITING:
            continue
        elif x == Order.ORDER_STATE_PLACED:
            x = 1
        elif x == Order.ORDER_STATE_ACKNOWLEDGED:
            x = 2
        elif x == Order.ORDER_STATE_COMPLETED:
            x = 3
        elif x == Order.ORDER_STATE_DISPATCHED:
            x = 4
        elif x == Order.ORDER_STATE_CANCELLED:
            x = 5
        else:
            continue

        corder.append(x)
        corder.append(order.delivery_addr)
        corders.append(corder)

    context = {
        "orders": corders,
    }

    return render(request, "webapp/order-list.html", context)

def listRestaurant(request):
    data=Restaurant.objects.all()
    print(data)

    return render(request,"restaurant.html",{"Restaurants":data})



def new_order(request,pk,rid):
    item=get_object_or_404(MenuItem,pk=pk)
    order=Order.objects.filter(orderedBy=Customer.objects.get(email=request.user.email),status='Waiting').first()
    
    
    print("----------",order,item)
    if order is not None:
        print("The value",order.items.filter(item_id__id=pk))
        if order.items.filter(item_id__pk=pk).exists():
            print("Yes existssssssssss")
            fooditem=order.items.filter(item_id__pk=pk).first()
            fooditem.quantity+=1
            fooditem.save()
        else:
            new,created=orderItem.objects.get_or_create(item_id=item,orderedBy=Customer.objects.get(email=request.user.email))
            new.quantity=1
            order.items.add(new)
            new.save()

    else:
        order=Order.objects.create(orderedBy=Customer.objects.get(email=request.user.email),r_id=Restaurant.objects.get(id=rid))
        new,created=orderItem.objects.get_or_create(item_id=item,orderedBy=Customer.objects.get(email=request.user.email))
        new.quantity=1
        new.save()
        order.items.add(new)
        order.save()

    return redirect('restuarantMenu',pk=rid)



def test(request):
    print("---------------------",   (request.user.email))