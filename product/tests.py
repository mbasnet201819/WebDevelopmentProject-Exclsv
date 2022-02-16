from django.contrib.auth.models import User
from django.test import TestCase
from django.test import SimpleTestCase
from django.test import Client
from django.urls import reverse, resolve

from exclusive.models import Customer
from exclusive.views import login, show, logout, signup, signin, Index, cdelete


# Create your tests here.
class TestUrls(SimpleTestCase):
    # Home page Testing, and It is Customer/User and Admin Signin Testing as well
    def test_case_login_url(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login)

        # Create Contact Us Testing

    def test_case_signin_url(self):
        url = reverse('signin')
        self.assertEquals(resolve(url).func, signin)

        # Create Contact Us Testing

    def test_case_index_url(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, Index)
    def test_case_logout_url(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logout)

        # Delete Contact Us Testing

    def test_case_delete_url(self):
        url = reverse('cdelete', args=[1])
        self.assertEquals(resolve(url).func, cdelete)

        # Creating Signup or Customer registration Testing

    def test_case_signup_url(self):
        url = reverse('signup')
        self.assertEquals(resolve(url).func, signup)

        # Delete Registered Customer Testing



class TestViews(TestCase):
    # Testing User Authentication in home view
    def test_case_home_views(self):
        user = User.objects.create(username='testcase')
        user.set_password('12345')
        user.save()
        client = Client()
        logged_in = client.login(username='testcase', password="12345")
        url = reverse('login')
        response = client.get(url)
        print(response)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/index.html')

        # Testing Contact Create in Contact us view

    def test_case_CreateContact_views(self):
        client = Client()
        url = reverse('signup')
        response = client.post(url, {
            'name': 'name',
            'email': 'email',
            'password': 'password',
        })

        print(response)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

        # Testing Contact Delete in Contact us view

    def test_case_DeleteContact_views(self):
            client = Client()

            newlycreated = Customer.objects.create(
                {
                    'name': 'name',
                    'email': 'email',
                    'password': 'password',
                })
            print(newlycreated.id)
            url = reverse('cdelete', newlycreated.id)
            response = client.delete(url)

            print(response)
            self.assertEquals(response.status_code, 200)
            self.assertRedirects(response, '/show')
