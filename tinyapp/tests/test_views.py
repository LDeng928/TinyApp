import datetime
from django.test import TestCase
from tinyapp.models import User, Url


class ViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            first_name="Katherine",
            last_name="Johnson",
            username="KJ",
            email="mathematics@nasa.com",
            password='!P4s5w0*d',
            is_staff=False,
            is_active=True,
            is_superuser=False
        )
        self.url = Url.objects.create(
            shortUrl='bx2Vn2',
            longUrl='https://www.google.com',
            user_id=self.user,
            dateCreated=datetime.datetime.now()
        )
