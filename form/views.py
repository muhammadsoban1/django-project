from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                phone_number=form.cleaned_data['phone_number']
            )
            return redirect('contact')  
    else:
        form = ContactForm()
    
    return render(request, "contacts/contact.html", {"form": form})


def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, "contacts/contact_list.html", {"contacts": contacts})

def contact_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect("contact_list")
    else:
        form = ContactForm(instance=contact)
    return render(request, "contacts/contact_edit.html", {"form": form, "contact": contact})

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()  
    return redirect("contact_list")


