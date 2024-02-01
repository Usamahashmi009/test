from django.shortcuts import render,redirect
from .models import Stock,ItemSize,Company,Vender
from .forms import StockCreateForm,AddItemSizeForm,AddItemCompanyForm,StockCreateFormSet,AddVenderForm
from django.forms import formset_factory
from django.db import transaction


# Create your views here.
def home(request):
	title = 'Welcome to our HomePage'
	context = {
	"title": title,
	}
	return render(request, "home.html",context)




def list_items(request):
    title = 'List of Items'
    queryset = Stock.objects.all()
    context = {
        "title": title,
        "queryset": queryset, 
    }
    return render(request, "list_items.html", context)


def add_items(request):
    if request.method == 'POST':
        formset = StockCreateFormSet(request.POST, prefix='stock')
        if formset.is_valid():
            for form in formset:
                # Process each form individually
                instance = form.save(commit=False)
                instance.quantity = form.cleaned_data.get('quantity')
                instance.rate = form.cleaned_data.get('rate')
                instance.save()
    else:
        formset = StockCreateFormSet(prefix='stock')

    context = {
        "formset": formset,
        "title": "Add Items",
    }
    return render(request, "add_items.html", context)

def add_itemsize(request):
    if request.method == 'POST':
        form = AddItemSizeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('items_size')  # Assuming 'items_size' is the URL pattern name

    else:
        form = AddItemSizeForm()

    item_sizes = ItemSize.objects.all()

    context = {
        'form': form,
        'item_sizes': item_sizes,
    }

    return render(request, 'add_itemsize.html', context)

def add_itemcompany(request):
    if request.method == 'POST':
        form = AddItemCompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addcompany')
    else:
        form = AddItemCompanyForm()

    add_companies = Company.objects.all()

    context = {
        'form': form,
        'add_companies': add_companies
    }

    return render(request, 'add_company.html', context)

def Settings_app (request):
    return render(request, 'settings.html')

def add_vender(request):
    if request.method == 'POST':
        form = AddVenderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addvender')  # Redirect to the same page after adding a vendor
    else:
        form = AddVenderForm()

    vendors = Vender.objects.all()  # Fetch the list of vendors from the database

    context = {
        'form': form,
        'vendors': vendors,  # Add the vendors list to the context
    }

    return render(request, 'add_vender.html', context)
