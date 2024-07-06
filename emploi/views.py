from datetime import date

from django.shortcuts import render

from emploi.models import Emploi


# sale = 'Sale UvT 1'
# sale_2 = 'Sale UvT 2'
# sale_3 = 'Sale UvT 3'
#
# date_occupe = date.today()
# date_non_occupe = date.today()


def home(request):
    data_title = [d.title for d in Emploi.objects.all()]
    data_occupee = [d.date_emploi_occoupee for d in Emploi.objects.all()]
    data_non_occupee = [d.date_emploi_fixee for d in Emploi.objects.all()]
    data_vide = [d.emploi_vide for d in Emploi.objects.all()]

    return render(request, 'emploi/index.html',
                  {'data_title': data_title, 'data_occupee': data_occupee, 'data_non_occupee': data_non_occupee,
                   'data_vide': data_vide})
