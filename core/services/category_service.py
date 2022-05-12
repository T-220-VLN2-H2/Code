from core.models.category import Category


class CategoryService:
    @classmethod
    def create_category(cls, request):
        print("Do something")
        # TODO validate category request and store in DB

    @classmethod
    def delete_category(cls, request):
        print("Do something")
        # TODO remove category from DB, some validation is required here?

    @classmethod
    def update_category(cls, category_id, **kwargs):
        print("Do something")
        # TODO update information in DB

    @classmethod
    def get_all_category_items(cls):
        categories = Category.objects.all().order_by("id")
        return categories

    @classmethod
    def get_category(cls, id):
        categorie = Category.objects.get(id=id)
        return categorie

    @classmethod
    def categories_with_parents(cls):
        categories = cls.get_all_category_items()
        sub_categories = {}
        for cat in categories:
            if cat.parent is not None:
                if cat.parent in sub_categories:
                    sub_categories[cat.parent].append(cat)
                else:
                    sub_categories[cat.parent] = [cat]
        return sub_categories
