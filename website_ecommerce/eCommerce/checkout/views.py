from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
import stripe
from django.core.urlresolvers import reverse
from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def payment_done(request):
    return render(request , 'done.html')

@csrf_exempt
def payment_canceled(request):
    return render(request , 'canceled.html')


def paymentProcess(request):
    # What you want the button to do.
    paypal_dict = {
        "business": "hj03111996@gmail.com",
        "amount": "1000.00",
        "item_name": "name of the item",
        "invoice": "unique-invoice-id",
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return_url": request.build_absolute_uri(reverse('payment:done')),
        "cancel_return": request.build_absolute_uri(reverse('payment:canceled')),
        "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, "process.html", context)
