from django import template
from foodapp.models import *
register = template.Library()

@register.filter(name='val')
def val(count):
    return range(count)


@register.filter(name='cart')
def cart_count(user):
    print("jhkdsfhkjsdhfkjdshfkjdfjhk")
    if user.is_authenticated:
        lis=Order.objects.filter(orderedBy=Customer.objects.get(email=user.email),status='Waiting')
        sum=0
        if lis.exists():
            print(lis[0].items.all())
            for i in lis[0].items.all():
                sum+=i.quantity 
            # return lis[0].items.count()
            return sum