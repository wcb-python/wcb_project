from django.shortcuts import render

# Create your views here.

def show_manage(request):
   login = request.session.get('login')
   print('login',login)
   return render(request, 'manage_system/持明法洲管理界面.html',{"login",login})