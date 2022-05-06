from django.http import JsonResponse
from core.services.search_service import SearchService

def search_result(request):
    search = SearchService()
    item_list = list(search.item_search())
    return JsonResponse(item_list, safe=False)
