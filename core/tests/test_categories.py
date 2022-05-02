from django.test import TestCase


class CategoryStatusAndContentTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("Adding test categories")
        cls.categories = [
            {"id": 1, "name": "Electronics"},
            {"id": 2, "name": "Furniture"}
        ]

    # def setUp(self) -> None:
    #    print("Setup, run once for each test")
    #    pass

    def test_category_returns_200(self):
        response = self.client.get('/categories')
        self.assertEqual(response.status_code, 200)

    def test_category_contains_category_names(self):
        response = self.client.get('/categories')
        for cat in self.categories:
            self.assertContains(response, f'<p>{cat["name"]}</p>')


