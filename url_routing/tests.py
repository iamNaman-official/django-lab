from django.test import SimpleTestCase


class URLRoutingTests(SimpleTestCase):

    def test_home(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)

    def test_about(self):
        response = self.client.get("/about/")

        self.assertEqual(response.status_code, 200)

    def test_missing_url(self):
        response = self.client.get("/does-not-exist/")

        self.assertEqual(response.status_code, 404)

    def test_get_method(self):
        response = self.client.get("/methods/")

        self.assertEqual(response.status_code, 200)

    def test_post_method(self):
        response = self.client.post("/methods/")

        self.assertEqual(response.status_code, 200)

    def test_put_method(self):
        response = self.client.put("/methods/")

        self.assertEqual(response.status_code, 405)