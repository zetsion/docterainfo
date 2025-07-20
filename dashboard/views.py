from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from item.models import Item

@login_required
def index(request):
    items=Item.objects.all()
    context = {
        'myItems':items.filter(created_by=request.user),
        'total_items': items.count(),
        'online_items': items.filter(available_online=True).count(),
        'offline_items': items.filter(available_online=False).count(),
        'recent_items': items.order_by('-id')[:5],  # or use '-created_at' if you have it
    }
    return render(request, "dashboard/index.html",context)
