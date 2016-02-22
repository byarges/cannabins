from django.shortcuts import render

# Create your views here.
def home(request):
	context = {}
	template = 'comingsoon.html'
	return render(request, template, context)