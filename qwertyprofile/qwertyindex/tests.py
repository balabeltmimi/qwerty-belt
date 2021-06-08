from django.test import TestCase

from qwertyindex.models import qwertyindex

# Create your tests here.
class TestProfile(TestCase):
    def test_profile_should_have_defined_fields(self):
        profile = qwertyindex.objects.create(
            name='Beltrt',
            github_url='https://github.com/balabeltmimi',
            github_project_url='https://github.com/balabeltmimi/qwerty-belt',
        )

        assert profile.name == 'Beltrt'
        assert profile.github_url == 'https://github.com/balabeltmimi'
        assert profile.github_project_url == 'https://github.com/balabeltmimi/qwerty-belt'

class TestIndexView(TestCase):
    def test_index_view_should_be_accessible(self):
        response = self.client.get('/')
        assert response.status_code == 200