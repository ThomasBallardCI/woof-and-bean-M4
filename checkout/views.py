from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your shopping bag at this time")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OUSxkICzqrS0JpbK4KpRMFASef515QK4CZMR1BpmReQFPLPd6zpN7u0HUSlHoUjhuG9yLPGTprrzV3ZtfIYVcMD00O6r1gtWw',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
