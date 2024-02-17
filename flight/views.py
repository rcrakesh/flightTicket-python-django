from django.http import HttpResponse
from django.shortcuts import render , get_object_or_404 , redirect
from .models import BookTickets, Flight




# Create your views here.
def welcome(request):
    if request.method == 'POST' and 'next_button' in request.POST:
        # Perform any necessary processing for the "Next" button click
        # Redirect to the 'home.html' template
        return redirect('main/home1.html')  # Assuming you have a URL pattern named 'home'

    # Render the 'welcome.html' template for the initial GET request
    return render(request, 'main/welcome.html')

def home1(response):
     return render(response,"main/home1.html")

def booking(response):
     
     return render(response,"main/booking.html")


# def sflight(request):
#     if request.method == 'POST':
#         form = FlightSearchForm(request.POST)
#         if form.is_valid():
#             source = form.cleaned_data['source']
#             destination = form.cleaned_data['destination']
#             flights = Flight.objects.filter(source=source, destination=destination)
#             return render(request, "main/aflight.html", {'flights': flights})
#     else:
#         form = FlightSearchForm()

#     return render(request, "main/sflight.html", {'form': form})

# def aflight(request):
#     fly = Flight()
#     fly.source = request.POST['Airport1']
#     fly.destination = request.POST['Airport2']


# def sflight(request):
#     if request.method == 'POST':
#         form = FlightSearchForm(request.POST)
#         if form.is_valid():
#             source = form.cleaned_data['source']
#             destination = form.cleaned_data['destination']
#             flights = Flight.objects.filter(source=source, destination=destination)
#             return render(request, "main/aflight.html", {'flights': flights})
#     else:
#         form = FlightSearchForm()

#     return render(request, "main/sflight.html", {'form': form})

# def aflight(request):
#     if request.method == 'POST':
#         flight = Flight()
#         flight.source = request.POST.get('Airport1', '')
#         flight.destination = request.POST.get('Airport2', '')
#         flight.save()

#         # Assuming you want to redirect to a page showing the details of the added flight
#         return render(request, "main/flight_details.html", {'flight': flight})

#     # If it's a GET request, you may want to redirect to the search form or another page
#     return redirect('sflight')




# def aflight(request):
#     flights = Flight.objects.all()
#     return render(request, "main/aflight.html", {'flights': flights})


# def sflight(request):
#     # flights = []  # Initialize an empty list for flights

#     if request.method == 'POST':
#         form = booking(request.POST)
#         if form.is_valid():
#             From = form.cleaned_data['Airport1']
#             To = form.cleaned_data['Airport2']
#             flights = Flight.objects.filter(source=From, destination=To)

#     else:
#         form = booking()

#     return render(request, "main/sflight.html", {'form': form, 'flights': flights})

# ----------------------------------------------------------------------------------------------------------------------
# def booking(request):
#     dest1 = bookings()
#     dest1.d1='Bangalore'
#     dest1.d2='mumbai'
#     dest1.d3='chennai'
#     dest1.d4='delhi'
   
#     dest2 = bookings()
#     dest2.d11='Bangalore'
#     dest2.d22='mumbai'
#     dest2.d33='chennai'
#     dest2.d44='delhi'

#     return render(request , "main/booking.html",{'dest1':dest1,'dest2':dest2})


def booking(request):
    dest1 = {
        'd1': 'Bangalore',
        'd2': 'Mumbai',
        'd3': 'Chennai',
        'd4': 'Delhi',
    }
    dest2 = {
        'd1': 'Bangalore',
        'd2': 'Mumbai',
        'd3': 'Chennai',
        'd4': 'Delhi',
    }
    return render(request, "main/booking.html", {'dest1': dest1 , 'dest2': dest2})


def sflight(request):
    if request.method == 'POST':
        airport1 = request.POST.get('Airport1', '')
        airport2 = request.POST.get('Airport2', '')
        departing_date = request.POST.get('departing_date', '')
        returning_date = request.POST.get('returning_date', '')

        flight = Flight.objects.create(
            airport1=airport1,
            airport2=airport2,
            departing_date=departing_date,
            returning_date=returning_date
        )

       
        return render(request, "main/sflight.html", {'flight': flight})

    # Handle the case when the form is not submitted or method is not POST
    return HttpResponse('Invalid request method or form not submitted.')

# def plane(request):
#     if request.method =='POST':
#         Email = request.POST.get('register.email','')
#         first_name= request.POST.get('register.first_name','')
#         last_name= request.POST.get('register.last_name','')
#         adults= int(request.POST('adults',''))
#         children=int(request.POST('children',''))
#         price = int(request.POST('tp',''))
#         booking = booking(Email = Email,First_Name = first_name,Last_name = last_name,adults=adults,children=children,price=price)
#         booking.save();
#         print("Booking_successful")
#         return render(request, 'main/plane.html', {'Booking_successful': True})
#     else:
#         print('page_is_notworking')
#         return render(request , 'main/home1.html',{'page_is_notworking': True})

from django.shortcuts import render


# def plane(request):
#     if request.method =='POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         phone = int(request.POST['phone']) 
#         adults = int(request.POST.get('adults', ''))
#         children = int(request.POST.get('children', ''))
#         price = int(request.POST.get('tp', ''))

#         # Create the booking object
#         book_tic = book_tic.objects.create_booking(name= name, email = email, phone= phone , adults=adults, children=children, price=price)
#         book_tic.save()
#         print("Booking_successful")
#         # Render the plane.html template with the Booking_successful context variable
#     return render(request, 'main/plane.html', {'Booking_successful': True} )

    # else:
    #     # Render the home1.html template with the page_is_notworking context variable
    #       return render(request, 'main/home1.html', {'page_is_notworking': True})


# def plane(request):
#     book_tic = None  # Initialize book_tic outside the if block

#     if request.method == 'POST':
#         # Your code to create the 'book_tic' object
#         name = request.POST['name']
#         email = request.POST['email']
#         phone = int(request.POST['phone'])
#         # airport1 = request.POST.get('Airport1', '')
#         # airport2 = request.POST.get('Airport2', '')
#         # departing_date = request.POST.get('departing_date', '')
#         # returning_date = request.POST.get('returning_date', '')
#         flight = get_object_or_404(Flight, id=flight_id)
#         adults = int(request.POST.get('adults', ''))
#         children = int(request.POST.get('children', ''))
#         price = int(request.POST.get('tp', ''))

#         book_tic = book_tic.objects.create(name=name, email=email, phone=phone, airport1=airport1, airport2=airport2, departing_date=departing_date, returning_date=returning_date, adults=adults, children=children, price=price)
#         print("Booking successful")

#         # Render the plane.html template with the Booking_successful context variable
#         return render(request, 'main/plane.html', {'Booking_successful': True})

#     return render(request, 'main/plane.html')

def plane(request, flight_id):
    # book_tic = None  # Initialize book_tic outside the if block

    if request.method == 'POST':
        flight = get_object_or_404(Flight, id=flight_id)
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        # Retrieve the Flight object based on the flight_id
        airport1 = flight.airport1
        airport2 = flight.airport2
        departing_date = flight.departing_date
        returning_date = flight.returning_date
        adults = int(request.POST.get('adults', ''))
        children = int(request.POST.get('children', ''))
        price = int(request.POST.get('tp', ''))
        

        # Create a BookTicket object related to the Flight
        book_ticket = BookTickets.objects.create(
            
            name=name,
            email=email,
            phone=phone,
            airport1=airport1,
            airport2=airport2,
            departing_date=departing_date,
            returning_date=returning_date,
            adults=adults,
            children=children,
            price=price
        )
        context = {
            'Booking_successful': True,
            'ticket_details': {
                'name': name,
                'email': email,
                'phone': phone,
                'airport1': airport1,
                'airport2': airport2,
                'departing_date': departing_date,
                'returning_date': returning_date,
                'adults': adults,
                'children': children,
                'price': price,
            }
        }
        # Render the plane.html template with the 'Booking_successful' context variable
        return render(request, 'main/display_tickets.html', context)

    if  request.method == 'GET':
       flight = get_object_or_404(Flight, id=flight_id)
       return render(request, 'main/plane.html', {'flight': flight})
    else:
       return render(request, 'main/plane.html') 
    
def delete(request, flight_id):
    # book_tic = None  # Initialize book_tic outside the if block

    if request.method == 'POST':
        flight = get_object_or_404(Flight, id=flight_id)
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        # Retrieve the Flight object based on the flight_id
        airport1 = flight.airport1
        airport2 = flight.airport2
        departing_date = flight.departing_date
        returning_date = flight.returning_date
        adults = int(request.POST.get('adults', ''))
        children = int(request.POST.get('children', ''))
        price = int(request.POST.get('tp', ''))
        

        # Create a BookTicket object related to the Flight
        book_ticket = BookTickets.objects.delete(
            
            name=name,
            email=email,
            phone=phone,
            airport1=airport1,
            airport2=airport2,
            departing_date=departing_date,
            returning_date=returning_date,
            adults=adults,
            children=children,
            price=price
        )
        context = {
            'Booking_successful': True,
            'ticket_details': {
                'name': name,
                'email': email,
                'phone': phone,
                'airport1': airport1,
                'airport2': airport2,
                'departing_date': departing_date,
                'returning_date': returning_date,
                'adults': adults,
                'children': children,
                'price': price,
            }
        }
        # Render the plane.html template with the 'Booking_successful' context variable
        return render(request, 'main/display_tickets.html', context)

    if  request.method == 'GET':
       flight = get_object_or_404(Flight, id=flight_id)
       return render(request, 'main/plane.html', {'flight': flight})
    else:
       return render(request, 'main/plane.html')     
    
# def display_tickets(request , ticket_id):
#         if request.method == 'POST':
#                         #    ticket_id = request.POST.get('ticket_id')
#                         booktickets  = get_object_or_404(BookTickets, id=ticket_id)
#                         name = booktickets.name
#                         email = booktickets.email
#                         phone = booktickets.phone
#                                 # Retrieve the Flight object based on the flight_id
#                         airport1 = booktickets.airport1
#                         airport2 = booktickets.airport2
#                         departing_date = booktickets.departing_date
#                         returning_date = booktickets.returning_date
#                         adults = booktickets.adults
#                         children = booktickets.children
#                         price = booktickets.price

#                         print("booked_tickets")
                            
#         return render(request, 'main/display_tickets.html', {
#                 'booked_tickets': True,
#                 'name': name,
#                 'email': email,
#                 'phone': phone,
#                 'airport1': airport1,
#                 'airport2': airport2,
#                 'departing_date': departing_date,
#                 'returning_date': returning_date,
#                 'adults': adults,
#                 'children': children,
#                 'price': price,
#            })

        # elif request.method == 'GET':
        # book_ticket = get_object_or_404(BookTickets, id=ticket_id)
        # return render(request, 'main/error.html', {'ticket': book_ticket})

        # else:
        #    return render(request, 'main/error.html')


# def display_tickets(request):
#     # Retrieve the last stored BookTickets object
#     last_ticket = BookTickets.objects.last()

#     if last_ticket:
#         name = last_ticket.name
#         email = last_ticket.email
#         phone = last_ticket.phone
#         airport1 = last_ticket.airport1
#         airport2 = last_ticket.airport2
#         departing_date = last_ticket.departing_date
#         returning_date = last_ticket.returning_date
#         adults = last_ticket.adults
#         children = last_ticket.children
#         price = last_ticket.price

#         return render(request, 'main/display_tickets.html', {
#             'last_ticket': last_ticket,
#             'name': name,
#             'email': email,
#             'phone': phone,
#             'airport1': airport1,
#             'airport2': airport2,
#             'departing_date': departing_date,
#             'returning_date': returning_date,
#             'adults': adults,
#             'children': children,
#             'price': price,
#         })
#     else:
#         return render(request, 'main/error.html', {'message': 'No tickets found.'})
    
# def display_tickets(request):
#     print('Display tickets view called')
#     # Retrieve the last stored BookTickets object
#     last_ticket = BookTickets.objects.all()

#     if last_ticket:
#         name = last_ticket.name
#         email = last_ticket.email
#         phone = last_ticket.phone
#         airport1 = last_ticket.airport1
#         airport2 = last_ticket.airport2
#         departing_date = last_ticket.departing_date
#         returning_date = last_ticket.returning_date
#         adults = last_ticket.adults
#         children = last_ticket.children
#         price = last_ticket.price

#         print('Name:', name)
#         print('Email:', email)
#         print('Phone:', phone)
#         print('Airport 1:', airport1)
#         print('Airport 2:', airport2)
#         print('Departing Date:', departing_date)
#         print('Returning Date:', returning_date)
#         print('Adults:', adults)
#         print('Children:', children)
#         print('Price:', price)

#         return render(request, 'main/display_tickets.html', {
#             'last_ticket': last_ticket,
#             'name': name,
#             'email': email,
#             'phone': phone,
#             'airport1': airport1,
#             'airport2': airport2,
#             'departing_date': departing_date,
#             'returning_date': returning_date,
#             'adults': adults,
#             'children': children,
#             'price': price,
#         })
#     else:
#         return render(request, 'main/error.html', {'message': 'No tickets found.'})    


# def display_tickets(request):
#     # Fetch all records from the BookTickets model
#     booked_tickets = BookTickets.objects.all()

#     # Render the results in the HTML template
#     return render(request, 'main/display_tickets.html', {'booked_tickets': booked_tickets})



    # tickets = BookTickets.objects.all()

    # # Extract the desired fields for each ticket
    # tickets = []
    # tickets = {
    #         'name': tickets.name,
    #         'email': tickets.email,
    #         'phone': tickets.phone,
    #         'airport1': tickets.airport1,
    #         'airport2': tickets.airport2,
    #         'departing_date': tickets.departing_date,
    #         'returning_date': tickets.returning_date,
    #         'adults': tickets.adults,
    #         'children': tickets.children,
    #         'price': tickets.price,
    #     }
        

    # # Render the results in the HTML template
    # return render(request, 'display_tickets.html', {'tickets': tickets})