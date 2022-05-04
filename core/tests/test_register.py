from django.test import TestCase


class CategoryStatusAndContentTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("Adding test categories")

    # def setUp(self) -> None:
    #    print("Setup, run once for each test")
    #    pass

    def test_get_login_is_200(self):
        response = self.client.get("/register")
        self.assertEqual(response.status_code, 200)

    def test_post_login_returns_200(self):
        response = self.client.post("/register")
        self.assertEqual(response.status_code, 200)
