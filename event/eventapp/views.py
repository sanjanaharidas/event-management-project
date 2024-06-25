from django.shortcuts import render,redirect
from eventapp.models import Event,Booking
from eventapp.forms import BookingForm
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')

@login_required
def events(request):
    e=Event.objects.all()
    return render(request,'events.html',{'e':e})

@login_required
def details(request,p):
    e = Event.objects.filter(name=p)
    return render(request, 'details.html', {'e':e})


@login_required
def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('eventapp:booking')  # Redirect to a success page or another view
    else:
        form = BookingForm()

    return render(request, 'booking.html', {'form': form})


@login_required
def confirm(request):
    k=Booking.objects.all()
    return render(request,'confirm.html',{'k':k})


@login_required
def edit(request,p):
    b = Booking.objects.get(id=p)
    if (request.method == "POST"):  # after submission
        form = BookingForm(request.POST,instance=b)
        if form.is_valid():
            form.save()  # saves the form object inside Db table
        return redirect('eventapp:confirm')
    else:
        form=BookingForm(instance=b)
    return render(request,'edit.html',{'form':form})


@login_required
def delete(request,p):
    b=Booking.objects.get(id=p)
    b.delete()
    return redirect('eventapp:confirm')


@login_required
def submit(request):
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        booking = Booking.objects.get(id=booking_id)
        booking.delete()
        msg = "Booking confirmed successfully!"
        return render(request, 'submit.html', {'msg': msg})
    else:
        return redirect('eventapp:confirm')

@login_required
def contact(request):
    return render(request,'contact.html')
