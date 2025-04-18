from django.shortcuts import render
from .models import Topic
from django.shortcuts import render
from django.db import connection

def dashboard(request):
    return render(request, 'knowledge_base/dashboard.html', {
        'topics': Topic.objects.all()  # Mantém isso para sua lógica atual!
    })

# View SQLILab
def sqli_lab(request):
    results = []
    if request.method == 'POST':
        user_input = request.POST.get('user_id', '')
        # !! ATENÇÃO: Código vulnerável propositalmente !!
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM auth_user WHERE id = {user_input}")  # SQL Injection óbvia
            results = cursor.fetchall()
    
    return render(request, 'knowledge_base/sqli.html', {'results': results})

# Views XSS_LAB
def xss_lab(request):
    user_input = ""
    if request.method == 'POST':
        user_input = request.POST.get('comment', '')
    return render(request, 'knowledge_base/xss.html', {'user_input': user_input})

#Views SQLi_Details
def sqli_details(request):
    return render(request, 'knowledge_base/sqli_details.html')

#Views XSS_Details
def xss_details(request):
    return render(request, 'knowledge_base/xss_details.html')