from django.shortcuts import render

# Create your views here.


def home(request):
    # user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    # context = {
    #   'contacts': user_contacts
    # }
    return render(request, 'index.html')


def missing(request):

    return render(request, 'missing.html')
