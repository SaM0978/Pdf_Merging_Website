from django.shortcuts import render, redirect
from .forms import UserForm
from pdfmerger import settings
import os
from PyPDF2 import PdfMerger

def merge(pdf1, pdf2, name='Default'):
    merger = PdfMerger()
    for i in [f"media/files/{pdf1}", f"media/files/{pdf2}"]:
        merger.append(i)
    
    merger.write(f"media/merged/{name}.pdf")
    merger.close()
    return f"{name}.pdf"



def process_file(data, filename1, filename2, name='Default'):
    with open(f"media/files/{filename1}", 'wb') as file1:
        file1.write(data)

    return merge(filename1, filename2, name)


def success(request, filename1, filename2, name='Default'):
    merged = process_file(data=request.FILES['file'].read(), filename1=filename1, filename2=filename2, name=name)
    return render(request, 'success.html', {'merged': merged})


def index(request):
    uploaded_file = None  # Variable to store the uploaded file temporarily
    uploaded_file2 = None  # Variable to store the uploaded file temporarily

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']  # Store the uploaded file
            uploaded_file2 = request.FILES['file2']  # Store the uploaded file
            file_name = uploaded_file.name
            file_name2 = uploaded_file2.name
            data2 = uploaded_file2.read()
            with open(f"media/files/{file_name2}", '+wb') as file2:
                     file2.write(data2)

            # Process the file or perform any other actions
            return success(request, filename1=file_name, filename2=file_name2, name=request.POST['name'])  # Redirect to success page
    else:
        form = UserForm()

    return render(request, 'home.html', {"form": form, "uploaded_file": uploaded_file})
