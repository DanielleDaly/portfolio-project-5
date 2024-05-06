from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import CustomerEnquiryForm

def customer_enquiry(request):
#     """
#     Add a Customer Enquiry to the database
#     """
    if request.method == 'POST':
        form = CustomerEnquiryForm(request.POST)
        if form.is_valid():
            customer_enquiry = form.save()
            messages.success(request, 'Thank you. Your enquiry was sent successfully. We will contact you within the next 24 hours.')
            # return redirect(reverse('customer_enquiry', args=[customer_enquiry.enquiry_number]))
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

# def add_customer_enquiry(request):
#     """
#     Add a Customer Enquiry to the database
#     """
#     if request.method == 'POST':
#         form = CustomerEnquiryForm(request.POST)
#         if form.is_valid():
#             customer_enquiry = form.save()
#             messages.success(request, 'Enquiry sent successfully. Your enquiry number is {customer_enquiry.enquiry_number}')
#             return redirect(reverse('customer_enquiry', args=[customer_enquiry.enquiry_number]))
#         else:
#             messages.error(request, 'Failed to send your enquiry. Please check that the form is valid.')
#     else:
#         form = CustomerEnquiryForm()

#     template = 'customer_enquiries/customer_enquiry.html'
#     context = {
#         'form': form,
#     }

#     return render(request, template, context)