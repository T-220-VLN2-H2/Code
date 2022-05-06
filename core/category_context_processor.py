from core.services.category_service import CategoryService
cat_service = CategoryService()

def categories(request):
    return {
        "categories": cat_service.get_all_category_items(),
        "sub_categories": cat_service.categories_with_parents(),
    }
