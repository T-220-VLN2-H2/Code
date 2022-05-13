from django.http import JsonResponse
from django.shortcuts import render
from core.services.search_service import SearchService


def search_result(request):
    try:
        sort = request.GET["sort"]
        query = request.GET["query"]
    except:
        sort = "default"
    if request.method == "POST" and sort == "default":
        query = request.POST.get("search", "")
        ctx = {"items": SearchService.item_search(q=query, sort=sort), "query": query}
        return render(request, "../templates/search_result.html", context=ctx)
    if request.method == "GET":
        item_list = list(SearchService.item_search(sort=sort, q=query))
        ctx = {"items": item_list}
        return render(request, "../templates/search_result.html", context=ctx)


def get_search_items(request):
    if request.method == "GET":
        item_list = list(SearchService.item_search(sort="default"))
        return JsonResponse(item_list, safe=False)
