from django.shortcuts import render
from .forms import ContactForm
from django.views.generic import View
from django.conf import settings
from django.core.mail import send_mail



# Create your views here.
class ContactFormView(View):
    form_class = ContactForm
    template_name = 'contact.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request , self.template_name , {'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            comment = form.cleaned_data['comment']
            subject = 'Message from ' + form.cleaned_data['email']
            message = 'Comment:{} Name:{}'.format(comment, name)
            emailFrom = form.cleaned_data['email']
            emailTo = [settings.EMAIL_HOST_USER]
            send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
            confirm_message = 'Thanks'
            print("sent")
        return render(request, self.template_name, {'form': form, 'confirm_message': confirm_message})

