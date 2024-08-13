from owner.models import cart

def cart_count(request):
  if request.user.is_authenticated:
    count=cart.objects.filter(user=request.user).exclude(status="order-placed").count()
    return {"count":count}
  
  else:
    return {"count":0}