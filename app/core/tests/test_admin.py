from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@londonappdev.com',
            password='password123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@londonappdev.com',
            password='password123',
            name='Test User Full Name',
        )

    def test_users_listed(self):
        """Test that users are listed on the user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url) #res == response

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_page_change(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id]) #reverse 다시 이해하기
        res = self.client.get(url) # url에서 http를 가져옴?

        self.assertEqual(res.status_code, 200) # 응답상태가 http response 200인지를 확인함

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add') #사용자 모델의 추가 페이지 별칭
        res = self.client.get(url) # 테스트 클라이언트는 HTTP가 이 URL에 도달 하도록 하고

        self.assertEqual(res.status_code, 200) # 상태가 200인지 확인함