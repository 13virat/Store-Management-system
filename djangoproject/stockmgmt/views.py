from django.shortcuts import render, redirect
from .models import *
from .forms import StockCreateForm


# Create your views here.
def home(request):
    title = "Welcome to this Page"
    context = {
        "title": title,
    }
    return render(request, "home.html", context)


def list_items(request):
    title = "List of Items"
    queryset = Stock.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "list_items.html", context)


def add_items(request):
    form = StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("list_items")
    content = {"form": form, "title": "Add Items"}
    return render(request, "add_items.html", content)
