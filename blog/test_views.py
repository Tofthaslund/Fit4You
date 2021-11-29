from django.test import TestCase


class TestViews(TestCase):

    def test_get_blog_list_view(self):
        # Any site user can view the main blog page
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')

    def test_get_add_blog_view(self):
        """ If not logged in, user will be redirected
        if they try to access the add article page """
        response = self.client.get('/blog/add/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/accounts/login/?next=/blog/add/')

    def Test_edit_blog_view(self):
        """ If not looged in, user will be redirected
        if thet try to edit a blog article """
        response = self.client.get('/blog/edit/1')
        self.assertEqual(response.status_code, 301)
