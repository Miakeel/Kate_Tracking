from django.core.management.base import BaseCommand, CommandError
from Tracking.models import Participant, QrCodeId


first_names=["Dr Richard", "Dr Karen", "Prof Turgay", "Prof Marc", "Dr Hend", "Dr Hind", "Dr Sakra", "Dr Al Johara", "Dr Laila", "Dr Mansour", "Dr Consuela", "Dr Sara", "Dr Abdulrazaq", "Dr Ziad", "Dr Mohammed", "Dr Catherine", "Dr Roaa", "Dr Ibrahim", "Dr Hadeel", "Dr Naveed", "Dr Mohammed", "Dr Ibtisam", "Prof Mohammad", "Dr Abdulrahman", "Dr Fatma", "Dr Ahmed", "Bob", "Costi", "Khaled", "Asma", "Dr Ali Faris"]
last_names=["Chapman", "Facey", "Ayer", "Evans", "Metwali", "Almodaimegh", "Balhareth", "Al Koraishi", "Abu Esba", "Khan", "Yousef", "Al Dallal", "Al-Jazairi", "Al Malki", "Al Muqbil", "Eileen Zeilinger", "Al Gain", "Al Homod", "Samarkandi", "Ahmad", "Ahmad", "Al Harbi", "Arafa", "Al Turaiki", "Maraiki", "Hattan", "Stratone", "Bogdan", "El Toukhy", "Syed", "H. Altebainaw"]
institutions=["Center for Innovation & Value Research, Alexandria, VA, USA", "University of Utrecht, Amsterdam, Netherlands", "Georgia Institute of Technology", "University Hospital Llandough", "King Abdulaziz Medical City - Jeddah", "Ministry of Health Affairs", "King Faisal Specialist Hospital & Research Centre", "King Saud University Medical City", "Ministry of Health Affairs", "Ministry of Health Affairs", "Ministry of Health Affairs", "Emirates Health Economisc Association", "King Faisal Specialist Hospital & Research Centre", "Prince Sattam Bin Abdulaziz University", "King Abdulaziz Medical City", "King Fahd Medical City", "King Faisal Specialist Hospital & Research Centre", "King Fahd Medical City", "King Faisal Specialist Hospital & Research Centre", "King Abdullah Specialized Children’s Hospital", "King Faisal Specialist Hospital & Research Centre", "King Fahd Armed Forces Hospital", "Dallah Hospital", "Ministry of Health Affairs", "King Faisal Specialist Hospital & Research Centre", "King Abdullah Bin Abdulaziz University Hospital", "Eurolink Alliance", "Eurolink Alliance", "Eurolink Alliance", "Eurolink Alliance", "Hail Cardiac Center - Hail Health Cluster"]
emails=["rick.chapman@valueresearch.org", "k.facey@btinternet.com","" ,"" , "metwalihe@nhga.med.sa", "modaimeghH@mngha.med.sa", "sbalhareth@kfshrc.edu.sa", "aalkoraishi@ksu.edu.sa", "abuesbala@ngha.med.sa", "khanma1@ngha.med.sa", "yousefco@mngha.med.sa","" , "ajazairi@kfshrc.edu.sa", "z.almalki@psau.edu.sa", "","" ,"" ,"" , "hsamarkandi61@kfshrc.edu.sa","" , "mahmed@kfshrc.edu.sa", "e.alharby@live.com","" ,"" , "f_maraiki@hotmail.com","" ,"" ,"" ,"" ,"" ,"" ]
titles=["Speaker", "Speaker", "Speaker", "Speaker", "Scientific Committee", "Scientific Committee", "Scientific Committee", "Scientific Committee", "Scientific Committee", "Scientific Committee", "Scientific Committee", "Speaker", "Speaker", "Speaker", "Speaker", "Speaker", "Speaker", "Speaker", "Speaker", "Speaker", "Speaker", "Speaker", "Speaker", "Speaker", "Moderator", "Moderator", "Managing Director", "MICE Tamer", "Project Manager", "Sponsorship Manager", "Speaker"]
phones=["1-703-772-2453", "44 789 414 3931","" ,"" , "503375728","" , "504129758","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ]
cities=["Alexandria", "Glasgow","" ,"" , "Jeddah", "Riyadh", "Riyadh", "Riyadh", "Riyadh", "Riyadh","" , "Dubai", "Riyadh", "Riyadh","" , "Riyadh", "Riyadh", "Riyadh", "Riyadh", "", "Riyadh", "Riyadh","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ]
countries=["USA", "UK","" ,"" , "KSA", "KSA", "KSA", "KSA", "KSA", "KSA", "KSA", "UAE", "KSA", "KSA", "", "KSA", "KSA", "KSA", "KSA","" , "KSA", "KSA","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ]
scfhs_numbers=["", "","" ,"" , "09JP0281626", "04RP11997", "04RP3446", "10RP0351188", "05RP44352", "09JP0284330", "10RP0343901", "", "02RP3345", "09RP0274281","" ,"" , "04RP3372","" , "14RP0031262","" , "10RP0307561", "09JP0280879","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ]



class Command(BaseCommand):
    
    # help = 'Generates a4 size images with unique uuid4 qrcodes'

    # def add_arguments(self, parser):
    #     parser.add_argument('pages', type=int)

    def handle(self, *args, **options):
    
        for i in range (len(first_names)):
            attendee=Participant.objects.create()
            attendee.first_name=first_names[i]
            attendee.last_name=last_names[i]
            attendee.institution=institutions[i]
            attendee.email=emails[i]
            attendee.title=titles[i]
            attendee.phone=phones[i]
            attendee.city=cities[i]
            attendee.country=countries[i]
            attendee.scfhs_number=scfhs_numbers[i]
            
            qrCode=QrCodeId.objects.create()
            qrCode.is_used=True
            qrCode.save()
            
            attendee.participant_id=qrCode.id
            attendee.save()
        

    