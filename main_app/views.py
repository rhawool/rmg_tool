from django.contrib import messages
from django.http import FileResponse, HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import DetailView, ListView
from tablib import Dataset

from main_app.forms import AddAssociateForm
from main_app.models import Associate
from main_app.resources import AssociateResource


def home_page(request):
    return render(request, "home_page.html")


def add_associate_home(request):
    form = AddAssociateForm()
    if request.method == 'GET':
        return render(request, "add_associate_home.html", {'form': form})

    elif request.method == 'POST':
        form = AddAssociateForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Associate added successfully.")
                return redirect("add_associate_home")
            except Exception as e:
                messages.error(request, f"Error Adding Associate. Error code/message: {e}")
                return redirect("add_associate_home")
    else:
        messages.error(request, "Invalid entries found. Please check and try again.")
        return redirect("add_associate_home")


def associate_list(request):
    associates = Associate.objects.all()
    context = {
        'associates': associates,
    }

    return render(request, "associate_list.html", context)


def bulk_import_associates(request):
    try:
        associate_resource = AssociateResource()
        dataset = Dataset()
        new_associate = request.FILES['bulk_file']

        dataset.load(new_associate.read())
        result = associate_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            associate_resource.import_data(dataset, dry_run=False)  # Actually import now

            messages.success(request, "Associates added successfully")
            return redirect("add_associate_home")

        else:
            messages.error(request,
                           "Error adding Associates, please input the data according to the sample format provided.")
            return redirect("add_associate_home")
    except Exception as e:
        messages.error(request, f"Something went wrong, Error code/message: {e}")
        return redirect("add_associate_home")


def download_sample_format(request):
    try:
        response = FileResponse(open('media/files/sample_formats/associates_sample_format.xlsx', 'rb'))
        return response

    except Exception as e:
        messages.error(request, f"Something went wrong, Error code/message: {e}")
        return redirect("home_page")


def export_associate_data(request):
    try:
        associate_resource = AssociateResource()
        dataset = associate_resource.export()
        response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="associate_data.xls"'
        return response

    except Exception as e:
        messages.error(request, f"Something went wrong, Error code/message: {e}")
        return redirect("associate_list")


def about_page(request):
    return render(request, "about_page.html")
