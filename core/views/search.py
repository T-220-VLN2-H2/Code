from django.http import JsonResponse
from django.shortcuts import render
from core.services.search_service import SearchService


def search_result(request):
    try:
        sort = request.GET["sort"]
    except:
        sort = "default"
    if request.method == "POST" and sort == "default":
        query = request.POST.get("search", "")
        ctx = {"items": SearchService.item_search(q=query, sort=sort)}
        return render(request, "../templates/search_result.html", context=ctx)
    if request.method == "GET":
        item_list = list(SearchService.item_search(sort=sort))
        return JsonResponse(item_list, safe=False)
