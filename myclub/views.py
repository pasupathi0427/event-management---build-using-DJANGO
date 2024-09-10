from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Events ,Venue
from .forms import AddEventForm , AddVenueForm
from django.http import HttpResponse
import csv  
#lockdown
from django.contrib.auth.decorators import login_required

#import for PDF
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from .models import Venue


#Generate PDF file --> .pdf
@login_required
def venue_pdf(request):
    # Create Bytestream buffer
    buf = io.BytesIO()
    # Create a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # Create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    # Designate The Model
    venues = Venue.objects.all()

    # Create blank list
    lines = []

    for venue in venues:
        lines.append(venue.name)
        lines.append(venue.address)
        lines.append(venue.phone)
        lines.append(venue.pincode)  # Append pincode after phone
        lines.append(venue.web)
        lines.append(venue.email)
        lines.append(" ")

    # Loop through the lines list and add each line to the PDF
    for line in lines:
        textob.textLine(line)

    # Finish up the PDF
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    # Return the PDF as a file response
    return FileResponse(buf, as_attachment=True, filename='venue.pdf')

# Generate CSV file --> .CSV
@login_required
def venue_CSV(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachments ; filename="venue-list.csv"'
    venues = Venue.objects.all()
    # create a csv writer
    writer = csv.writer(response)
    # Designate the Model i.e column names
    writer.writerow(['Venue Name' , 'Address','phone' ,'pincode' ,'Web Address','Email Address'])
    # print detail as rows
    for venue in venues:
        writer.writerow([venue.name,venue.address,venue.phone,venue.pincode,venue.web,venue.email])
    return response

# Generate Text file --> .txt
@login_required
def venue_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachments ; filename="venue-list.txt"'
    venues = Venue.objects.all()
    line = [ ]
    for  venue in venues:
        line.append(f'{venue.name}\n{venue.address}\n{venue.phone}\n{venue.pincode}\n{venue.web}\n{venue.email}\n\n\n')

    response.writelines(line)
    return response
    

def update_event(request , event_id):
    event = Events.objects.get(pk=event_id)
    form = AddEventForm(request.POST or None , instance=event)
    if form.is_valid():
        form.save()
        return redirect('list-events')
    
    return render(request , 'myclub/update_event.html', {'form':form ,'event':event})

def delete(request , venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('list-venues')

def update(request , venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = AddVenueForm(request.POST or None , request.FILES or None , instance=venue)
    if form.is_valid():
        form.save()
        return redirect('list-venues')
    
    return render (request, 'myclub/update.html',{'form':form ,'venue':venue})

@login_required
def add_venue(request):
    if request.method=='POST':
        form = AddVenueForm(request.POST , request.FILES)
         # request.Files to handle images/files , since there is file/image add  "enctype" in the html form to process images
         #  while submission
        if form.is_valid():
            form.save()
            return redirect('list-venues')
    else:
        form= AddVenueForm()
    return render(request , 'myclub/add_venues.html', {'form':form})
@login_required
def show_venue(request , venue_id):
    # event = Events.objects.get(pk=venue_id)
    venues= Venue.objects.get(pk=venue_id)
    return render(request , 'myclub/show_venue.html',{'venues' : venues })

@login_required
def venues(request):
    query = request.POST.get('search')
    if query:
        venues =Venue.objects.filter(name__contains=query).order_by('name')
    else:
        venues= Venue.objects.all().order_by('name')
    return render(request , 'myclub/venues.html',{'venues' : venues})

@login_required
def add_events(request):
    if request.method =='POST':
        form =AddEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-events')
    else:
        form =AddEventForm()

    return render( request , 'myclub/add_events.html' ,{'form':form})

@login_required
def events(request):
    events = Events.objects.all().order_by('event_date')
    return render (request , 'myclub/events.html' ,{'events':events})

def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    month = month.capitalize()
    # Convert the month name to its corresponding number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    # Create an HTMLCalendar instance
    cal = HTMLCalendar()
    
    # Generate the HTML calendar for the given year and month
    html_calendar = cal.formatmonth(year, month_number)
    
    # Get the current date for highlighting purposes
    current_date = datetime.today()

    return render(request, 'myclub/home.html', {
        'year': year, 
        'month': month,
        'calendar': html_calendar,
        'current_year': year,
        'current_month': month_number,
        'current_date': current_date,
    })
