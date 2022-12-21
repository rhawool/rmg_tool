from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import DetailView, ListView
from tablib import Dataset

from main_app.forms import AddAssociateForm
from main_app.models import Associate
from main_app.resources import AssociateResource


def home_page(request):
    form = AddAssociateForm()
    if request.method == 'GET':
        return render(request, "home_page.html", {'form': form})

    elif request.method == 'POST':
        form = AddAssociateForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Associate added successfully.")
                return redirect("home_page")
            except Exception as e:
                messages.error(request, f"Error Adding Associate. Error code/message: {e}")
                return redirect("home_page")
    else:
        messages.error(request, "Invalid entries found. Please check and try again.")
        return redirect("home_page")


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
            return redirect("home_page")

        else:
            messages.error(request,
                           "Error adding Associates, please input the data according to the sample format provided.")
            return redirect("home_page")
    except Exception as e:
        messages.error(request, f"Something went wrong, Error code/message: {e}")
        return redirect("home_page")



# def bulk_import_associates(request):
#     if request.method == "POST":
#         associate_resource = AssociateResource()
#         dataset = Dataset()
#         associates = Associate.objects.all()
#         try:
#             new_associate = request.FILES['bulk_file']
#             if not new_associate.name.endswith('xlsx'):
#                 messages.warning(request, 'Wrong File Format, Please Select a xlsx file type!')
#                 return redirect("home_page")
#             try:
#                 dataset.load(new_associate.read())
#                 result = associate_resource.import_data(dataset, dry_run=True)  # Test the data import
#
#                 if not result.has_errors():
#                     associate_resource.import_data(dataset, dry_run=False)  # Actually import now
#
#                     messages.success(request, "Associates added successfully")
#                     return redirect("home_page")
#
#             except Exception as e:
#                 messages.error(request, f'Error message: {e}')
#         except Exception as e:
#             messages.error(request, 'Did you forget to select a file? Please Select the file...!')
#
#     return redirect("home_page")
