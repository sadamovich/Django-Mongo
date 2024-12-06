from django.shortcuts import render

from .models import Staff, Job

def index(request):
    num_staff=Staff.objects.all().count()
    num_jobs=Job.objects.count()  # Метод 'all()' применён по умолчанию.

    return render(
        request,
        'index.html',
        context={'num_staff':num_staff,'num_jobs':num_jobs},
    )
