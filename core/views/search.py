from django.http import JsonResponse
from django.shortcuts import render
from core.services.search_service import SearchService


def search_result(request):
    search = SearchService()
    if request.method == "POST":
        query = request.POST.get("search", "")
        ctx = {"items": search.item_search(query)}
        return render(request, "../templates/search_result.html", context=ctx)
    if request.method == "GET":
        item_list = list(search.item_search())
        return JsonResponse(item_list, safe=False)
