from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    """ Setup function need to be run before the tests, since there are some tasks that need to be completed before the test runs"""

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(email='admin@example.com',
                                                                    password='password123')
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(email='test@example.com',
                                                         password='password123', name='test')

    def test_users_listed(self):
        """ Test that users are listed on the user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        # checks if the response is HTTP 200 OK or not
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    """" Tests if the edit page is working for the users or not since it wont work directly we have to add it to our user model """

    def test_user_change_page(self):
        """Tests that the user edit page renders correctly"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        # /admin/core/user/<user_id>
        # since we already made client in our setup function thus we can directly use it here
        res = self.client.get(url)

        # To test if the page rendered correctly match its response status code to 200
        self.assertEqual(res.status_code, 200)

    def test_user_add_page(self):
        """Test that the create user page works correctly"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
