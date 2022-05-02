from django.test import TestCase


class StatusCodeTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("Creates correct test data ")
        pass

    def setUp(self) -> None:
        print("Setup, run once for each test")
        pass

    def test_catalog_returns_200(self):
        response = self.client.get('/checkout')
        self.assertEqual(response.status_code, 200)

