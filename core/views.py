

# Create your views here.
# core/views.py
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render,redirect
from django.db.models import Q
from item.models import ItemCategory, Item
from .forms import SignupForm, ContactMessageForm


def about(request):
    return render(request,'core/about.html')



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:login')  # or wherever you want to redirect after signup
    else:
        form = SignupForm()
    
    return render(request, 'core/signup.html', {'form': form})

def login(request):
    return render(request, 'core/login.html')

@login_required
def logout_view(request):
    logout(request)  # This clears the session
    return redirect('/')  # Redirect to login or homepage

def contact_view(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            if request.user.is_authenticated:
                message.user = request.user
            message.save()
            return redirect('core:contactsuccess')  # make sure this route exists
    else:
        initial_data = {}
        if request.user.is_authenticated:
            initial_data = {
                'name': request.user.get_full_name() or request.user.username,
                'email': request.user.email,
            }
        form = ContactMessageForm(initial=initial_data)

    return render(request, 'core/contact.html', {'form': form})

def index(request):
    query = request.GET.get('query', '').strip()
    category_id = request.GET.get('category', '').strip()

    categories = ItemCategory.objects.all()
    items = Item.objects.none()  # Show no items by default

    if category_id.isdigit() and int(category_id) != 0:
        items = Item.objects.filter(is_sold=False, category_id=int(category_id))

        if query:
            items = items.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )
    elif query:
        items = Item.objects.filter(
            is_sold=False
        ).filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    return render(request, 'core/index.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id) if category_id.isdigit() else 0,
    })
