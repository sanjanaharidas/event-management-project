from django import forms
from eventapp.models import Booking

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'Booking_date': DateInput(),
        }
        labels = {
            'Customer_name': "Customer Name:",
            'Customer_phone': "Customer Phone:",
            'Event_name': "Event Name:",
            'Booking_date': "Booking Date:",
        }
