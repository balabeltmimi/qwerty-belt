from django.core.management.base import BaseCommand, CommandError
from qwertyindex.models import qwertyindex


class Command(BaseCommand):
    help = 'Help me!'

    def add_arguments(self, parser):
        parser.add_argument('id', nargs=1, type=int)
        parser.add_argument('name', nargs=1, type=str)

    def handle(self, *args, **options):
        print(args)
        print(options)

        try:
            id = options.get('id')[0]
            print(id)
            profile = qwertyindex.objects.get(id=id)
            print(profile.name)
            print(profile.github_url)

        except Exception:
            raise CommandError('Error!')
