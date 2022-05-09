from core.models.category import Category


class CategoryService:
    def create_category(self, request):
        print("Do something")
        # TODO validate category request and store in DB

    def delete_category(self, request):
        print("Do something")
        # TODO remove category from DB, some validation is required here?

    def update_category(category_id, **kwargs):
        print("Do something")
        # TODO update information in DB

    @staticmethod
    def get_all_category_items():
        categories = Category.objects.all().order_by("id")
        return categories

    def categories_with_parents(self):
        categories = self.get_all_category_items()
        sub_categories = {}
        for cat in categories:
            if cat.parent is not None:
                if cat.parent in sub_categories:
                    sub_categories[cat.parent].append(cat)
                else:
                    sub_categories[cat.parent] = [cat]
        return sub_categories
