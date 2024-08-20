from owner.models import cart,orders

def cart_count(request):
  if request.user.is_authenticated:
    count=cart.objects.filter(user=request.user).exclude(status="order-placed").count()
    return {"count":count}
  else:
    return {"count":0}
  
def order_count(request):
  if request.user.is_authenticated:
    ordercount=orders.objects.filter(user=request.user).count()
    return {"order_count":ordercount}
  else:
    return {"order_count":0}