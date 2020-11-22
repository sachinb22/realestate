from django.shortcuts import render

# Create your views here.
def register(request):
	if request.method == 'POST':
		print('SUBMITTED REG') 
		return redirect('register')
	else:
	 return render(request,'accounts/register.html')

def login(request):
	if request.method == 'POST':
		print('Login successfully') 
		return redirect('register')
	else:
	 return render(request,'accounts/login.html')

def logout(request):
	return render(request,'accounts/logout.html')

def dashboard(request):
	return render(request,'accounts/dashboard.html')