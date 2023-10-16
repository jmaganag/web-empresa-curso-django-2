from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    # print("tipo de peticion: {}".format(request.method))
    contact_form=ContactForm()

    if request.method == "POST":
        contact_form=ContactForm(data=request.POST)
        if contact_form.is_valid():
            name=request.POST.get('name', '')
            email=request.POST.get('email', '')
            content=request.POST.get('content', '')
            # Enviamos el correo y redirecionamos
            email=EmailMessage (
                "la cafetera:Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name,email,content),
                "no-constetar@inbox.mailtrap.io",
                ["jmagana.go"],
                reply_to=[email]
            )

            try:
                email.send()
                 # Todo ha ido bien, redireccionamos a OK
                return redirect(reverse('contact')+"?ok")
            except:
            #    import traceback
            #    traceback.print_exc()
            #    #algo no ha ido bien, redireccionamos al FAIL
                return redirect(reverse('contact')+"?fail")


    return render(request,"contact/contact.html", {'form': contact_form})