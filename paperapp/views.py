from django.db.models import query
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import PaperForm
from .models import Paper
# Create your views here.


'''
def upload(request):
	context = {}
	if request.method == 'POST':
		uploaded = request.FILES['Document']
		fs = FileSystemStorage()
		name = fs.save(uploaded.name,uploaded)
		context['url'] = fs.url(name)
	return render(request,'upload.html',context)
'''
def show_papers(request):
	papers = Paper.objects.all()
	return render(request,'index.html',{'papers':papers})

def upload_paper(request):
	if request.method == 'POST':
		form = PaperForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('paperapp:index')
	else:
		form = PaperForm()
		
	context = {'form':form}
	return render(request,'upload.html',context)

def search(request):
	
	if request.method == 'GET':
		file_names = []
		search_key = request.GET.get("search-key")
		search_key = str(search_key)
		all_files = Paper.objects.all()
		for file in all_files:
			import re
			out = re.search(search_key.lower(),file.title.lower())
			if out:
				file_names.append(file.title)
		return HttpResponse(file_names)

	


