from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render, get_object_or_404,redirect
from .models import Item ,ItemCategory # make sure this import is correct
from .forms import NewItemForm, EditItemForm

def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', '')
    show_mine = request.GET.get('mine') == 'true'

    categories = ItemCategory.objects.all()

    # Start with base queryset
    items = Item.objects.filter(is_sold=False)

    # Filter by user if "mine" is set
    if show_mine:
        items = items.filter(created_by=request.user)

    # Apply category filter if given
    if category_id:
        items = items.filter(category_id=category_id)

    # Apply search query filter if given
    if query:
        items = items.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id) if category_id.isdigit() else 0,
        'mylistings': Item.objects.filter(created_by=request.user)
    })




def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
        # Start with related items by category, excluding itself
    related_items = Item.objects.filter(category=item.category).exclude(pk=pk)[:3]

    # related_items = related_items[:3]
    return render(request, 'item/detail.html', {'item': item, 'related_items':related_items})

@login_required
def new(request):
 if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user  # if your model has this field
            item.save()
            return redirect('item:detail', pk=item.id)
 else:
    form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New Item'
    })
 
 

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect('dashboard:index')

 
@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return HttpResponse("✅ Updated successfully")  # Force simple response
        else:
            return HttpResponse(f"❌ Errors: {form.errors}")
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit Item'
    })
