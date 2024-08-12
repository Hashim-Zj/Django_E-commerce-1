from owner.models import cart

def cart_count(request):
  if request.user.is_authenticated:
    count=cart.objects.filter(user=request.user).count()
    return {"count":count}
  
  else:
    return {"count":0}