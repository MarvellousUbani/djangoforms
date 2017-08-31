from django.shortcuts import render
from .forms import ContactForm
# Create your views here.

def home(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			pass
	else:
		form = ContactForm()
	return render(request, 'home.html', {'form' : form})
