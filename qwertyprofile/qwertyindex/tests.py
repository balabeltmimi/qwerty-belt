from django.test import TestCase

from qwertyindex.models import qwertyindex, Subscibemodel


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
    def test_index_view_should_see_my_name(self):
        # Given
        qwertyindex.objects.create(name='Belt')
        # When
        response = self.client.get('/')
        # Then
        assert response.status_code == 200
        assert 'Belt' in str(response.content)

    def test_index_view_should_save_subscriber_email_when_input_form(self):
        qwertyindex.objects.create(name='Belt')
        data = {
            'email': 'thanaporn.jira@odds.team'
        }
        response = self.client.post('/', data=data)
        sub_email = Subscibemodel.objects.last()
        assert sub_email.email == 'thanaporn.jira@odds.team'
        assert 'thanaporn.jira@odds.team' in str(response.content)
