from django.shortcuts import render
from django.http import HttpResponse
import os
global list
list = {}
def show_name(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        list[username] = [email]
        return HttpResponse(f'<h1> Successsfully added <ins>{username}</ins></h1><h4>Email: {email}</h4>')

    return render(
        request,
        template_name='form.html',
    )

def show_all(request):
    data = ""
    for b in list:
        data += "<div><h3><li>" + b + "</li></h3></div>"
        for c in list[b]:
            data += "<p> E-mail:" + c + "</p>"
    with open("show.html", "w", encoding="utf-8") as file:
        file.write(data)
    os.startfile("show.html")