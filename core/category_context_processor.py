from core.services.category_service import CategoryService


def categories(request):
    return {
        "categories": CategoryService.get_all_category_items(),
    }
