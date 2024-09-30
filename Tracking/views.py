from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, ParticipantForm, EntryForm
from .models import Participant,QrCodeId, Entry
from PIL import Image, ImageOps, ImageFont, ImageDraw
import qrcode
from django.http import HttpResponse
import os

# Create your views here.

@login_required(login_url='/login')
def index_view(request):
    if not request.user.is_authenticated:       
        return redirect('login')

    participants = Participant.objects.all()
    total = participants.count
    attended=participants.filter(attended=True).count
    notAttended=participants.filter(attended=False).count
    inside = participants.filter(inside=True).count

    return render(request, 'tracking_app/index.html', {
        'totalNr': total,
        'inside': inside,
        'attended': attended,
        'notAttended':notAttended,
    })

    return render(request, 'tracking_app/index.html')


def login_view(request):
    form = LoginForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["username"],
                password=form.cleaned_data["password"])
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error(None, "Invalid username or password")

    return render(request, 'tracking_app/login.html', {
        'form': form
        })

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(redirect_field_name='login',login_url='login')
def participant_info_view(request,id):
    try:
        participant = Participant.objects.get(pk=id)
        path='/QR_Codes/%s_%s_%s.png' % (participant.first_name, participant.last_name, participant.participant_id)
        
        if not os.path.isfile(path):
        
            participant_id=participant.participant_id

            page_width = 2480
            page_height = 3508

            qr_border = 5
            qr_width = 500 - qr_border
            qr_height = 500 - qr_border

            page = Image.new('RGB', (page_width, page_height), (255, 255, 255))

            fontBold=ImageFont.truetype('Tracking/management/commands/Swansea-q3pd.ttf',size=125)
            fontRegular=ImageFont.truetype('Tracking/management/commands/Swansea-q3pd.ttf',size=100)

            qr_img=qrcode.make(participant_id)
            qr_img = qr_img.resize((qr_width, qr_height))
            qr_img = ImageOps.expand(qr_img, border=qr_border, fill='black')

            template = Image.open('Tracking/management/commands/template.png')
            template = template.resize((page_width, page_height))
            page.paste(template,(0,0))
            name=participant.first_name+" "+participant.last_name
                
            page.paste(qr_img,(370,1000))

            draw = ImageDraw.Draw(page)


            draw.text(((page_width/2 - fontBold.getlength(name))/2,550),name,'black',fontBold)

            draw.text(((page_width/2 - fontRegular.getlength(participant.title))/2,750),participant.title,'black',fontRegular)


                
            page.save('Tracking/static/QR_Codes/%s_%s_%s.png' % (participant.first_name, participant.last_name,participant.participant_id))
            

    except Participant.DoesNotExist:
        return HttpResponse("404 Participant with id '%s' does not exist "%id)
    context={
        'participant':participant,
        'badge_url': '/QR_Codes/%s_%s_%s.png' % (participant.first_name, participant.last_name, participant.participant_id)
    }
    return render(request, 'tracking_app/participant_info.html' , context)
    


@login_required(redirect_field_name='login', login_url='/login')
def new_participant_view(request):
    form = ParticipantForm(request.POST or None)
    
    context = {'form': form}

    if request.method == "POST":
        if form.is_valid():
            attendee = form.save()
            
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            institution = form.cleaned_data['institution']
            email=form.cleaned_data['email']
            title=form.cleaned_data['title']
            phone=form.cleaned_data['phone']
            city=form.cleaned_data['city']
            country=form.cleaned_data['country']
            scfhs_number=form.cleaned_data['scfhs_number']

            #Id Generation 
            qrCode=QrCodeId.objects.create()
            qrCode.is_used=True
            qrCode.save()
            participant_id=qrCode.id

            page_width = 2480
            page_height = 3508

            qr_border = 5
            qr_width = 500 - qr_border
            qr_height = 500 - qr_border

            page = Image.new('RGB', (page_width, page_height), (255, 255, 255))

            fontBold=ImageFont.truetype('Tracking/management/commands/Swansea-q3pd.ttf',size=125)
            fontRegular=ImageFont.truetype('Tracking/management/commands/Swansea-q3pd.ttf',size=100)

            qr_img=qrcode.make(participant_id)
            qr_img = qr_img.resize((qr_width, qr_height))
            qr_img = ImageOps.expand(qr_img, border=qr_border, fill='black')

            template = Image.open('Tracking/management/commands/template.png')
            template = template.resize((page_width, page_height))
            page.paste(template,(0,0))
            name=first_name+" "+last_name
            
            page.paste(qr_img,(370,1000))

            draw = ImageDraw.Draw(page)


            draw.text(((page_width/2 - fontBold.getlength(name))/2,550),name,'black',fontBold)

            draw.text(((page_width/2 - fontRegular.getlength(title))/2,750),title,'black',fontRegular)


            
            page.save('Tracking/static/QR_Codes/%s_%s_%s.png' % (first_name, last_name,participant_id))
            attendee.participant_id=participant_id
            attendee.save()
            context['first_name'] = "%d %s" % (participant_id, first_name)
            form = ParticipantForm()
    
    return render(request, 'tracking_app/new_participant.html', context)

@login_required(redirect_field_name='login', login_url='/login')
def participants_view(request):
    participants = Participant.objects.all().order_by('first_name','inside')

    return render(request, 'tracking_app/participants.html', {
        'participants': participants
    })

@login_required(redirect_field_name='login', login_url='/login')
def participant_entry_view(request):
    form = EntryForm(request.POST or None)
    context = {'form': form}

    if request.method == "POST":
        if form.is_valid():
            try:
                participant = Participant.objects.get(participant_id=form.cleaned_data['qrcode_uuid'])
            except Participant.DoesNotExist:
                form.add_error(None, "Invalid code")
                return render(request, 'tracking_app/entry.html', context)
            participant.inside= not participant.inside
            participant.attended=True
            participant.save()
            Entry.objects.create(participant=participant, exit=not participant.inside)
            context['succes'] = '%d %s %s has %s' % (
                participant.id,
                participant.last_name,
                participant.first_name,
                'entered' if participant.inside else 'exited')
            if participant.inside:
                context['succes'] = '<div style="color:green; font-size:1.75em;">' + context['succes'] + '</div>'
            else:
                context['succes'] = '<div style="color:red; font-size:1.75em;">' + context['succes'] + '</div>'

    return render(request, 'tracking_app/entry.html', context)