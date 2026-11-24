
from django.shortcuts import render
from . import util


def index(request):
    entries = util.list_entries()

    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })


def title(request, title):
    content = util.get_entry(title)

    if content is None:
        return render(request, "encyclopedia/error.html", {
            "message": "Page not found."
        })

    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": content
    })


def search(request):
    query = request.GET.get("q", "")
    entries = util.list_entries()
    results = []

    for entry in entries:
        if query.lower() in entry.lower():
            results.append(entry)

    if len(results) == 1 and results[0].lower() == query.lower():
        return title(request, results[0])

    return render(request, "encyclopedia/search_results.html", {
        "query": query,
        "matching_entries": results
    })


def new_page(request):
    return render(request, "encyclopedia/new_page.html")


def save_page(request):
    if request.method != "POST":
        return render(request, "encyclopedia/error.html", {
            "message": "Invalid request method."
        })

    page_title = request.POST.get("title", "")
    content = request.POST.get("content", "")

    if util.get_entry(page_title) is not None:
        return render(request, "encyclopedia/error.html", {
            "message": "A page with this title already exists."
        })

    util.save_entry(page_title, content)

    return title(request, page_title)
