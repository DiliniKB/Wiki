from operator import truediv
import os
from pydoc import describe
from django.shortcuts import render, redirect
import markdown2

from .forms import newEntry

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, page):
    return render(request, "encyclopedia/page.html", {
        "title": {page},
        "content": markdown2.markdown(util.get_entry(page))
    })

def create(request):
    if request.method == "POST":
        form = newEntry(request.POST)
        
        if form.is_valid():
            title = form.cleaned_data.get("title")
            description = form.cleaned_data.get("description")

            util.save_entry(title,f'#{title}\n\n{description}')

            return redirect(f'view/{title}')
    else:
        form = newEntry()
        return render(request, "encyclopedia/create.html",{
            "form": form
        })

