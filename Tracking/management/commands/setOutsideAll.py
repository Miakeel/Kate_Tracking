from django.core.management.base import BaseCommand, CommandError

from Tracking.models import Participant

class Command(BaseCommand):
    
    # help = 'Generates a4 size images with unique uuid4 qrcodes'

    # def add_arguments(self, parser):
    #     parser.add_argument('pages', type=int)

    def handle(self, *args, **options):
        victims=Participant.objects.all()
        for i in victims:
            i.inside=False
        
        
