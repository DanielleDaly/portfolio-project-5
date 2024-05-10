from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import CustomerEnquiry, CustomerEnquiryForm

def customer_enquiry(request):
#     """
#     Add a Customer Enquiry to the database
#     """
    if request.method == 'POST':
        form = CustomerEnquiryForm(request.POST)
        if form.is_valid():
            customer_enquiry = form.save()
            messages.success(request, f'Thank you. Your enquiry was sent successfully. \
                             We will contact you within the next 24 hours. \
                             Your enquiry number is: {customer_enquiry.enquiry_number}')
            return redirect(reverse('customer_enquiry'))
        else:
            messages.error(request, 'Failed to send your enquiry. Please check that the form is valid.')
    else:
        form = CustomerEnquiryForm()

    template = 'customer_enquiries/customer_enquiry.html'
    context = {
        'form': form,
    }

    return render(request, template, context)