from operator import truediv
import os
from pydoc import describe
from django.shortcuts import render, redirect
import markdown2
import random

from .forms import editEntry, newEntry

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, page):
    return render(request, "encyclopedia/page.html", {
        "title": page,
        "content": markdown2.markdown(util.get_entry(page))
    })

def create(request):
    if request.method == "POST":
        form = newEntry(request.POST)
        
        if form.is_valid():
            title = form.cleaned_data.get("title")
            description = form.cleaned_data.get("description")

            util.save_entry(title,f'#{title}\n\n{description}')

            return redirect(f'view', page=title)
    else:
        form = newEntry()
        return render(request, "encyclopedia/create.html",{
            "form": form
        })

def randomP (request):
    randomPage =  random.choice(util.list_entries())
    # randomPage = random.ch
    return redirect(f'view/{randomPage}')

def editP(request, page):

    if request.method == 'POST':
        form = editEntry(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']

            os.rename(f'./entries/{page}.md', f'./entries/{title}.md')
            util.save_entry(title, f'# {title}\n\n{description}')

            return redirect(f'view/page')
    else:
        with open(f'./entries/{page}.md') as ef:
            ef_content = ef.readlines()

        data = {
            'title': page,
            'description': ''.join(ef_content[1:])
        }

        form = editEntry(data)

    context = {'form': form}

    return render(request, 'encyclopedia/edit.html', context)
