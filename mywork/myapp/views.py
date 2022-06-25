from django.shortcuts import render

from myapp.models import Main


def main(request):
    baza = Main.objects.all()
    print('------')
    print(baza)
    print('------')
    return render(request, 'base.html')



