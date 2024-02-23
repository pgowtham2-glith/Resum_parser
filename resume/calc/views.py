from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import time
from .forms import UploadForm
from .models import save_resume_data_to_db
import json
import os
import requests
import logging
from win32com import client as wc
import pythoncom


# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def upload(request):
    # if request.method == 'POST':
    # #    form = UploadForm(request.POST, request.FILES)
    #     upload_file=request.FILES['document']
    # #    if form.is_valid():
    # #         form.save(upload_file)
    # #         return HttpResponse('/thanks/')
    #     print(upload_file.name)
    #     fs=FileSystemStorage()
    #     fs.save(upload_file.name,upload_file)
    #     time.sleep(2)
    #     return render(request, 'upload.html')
    # else:
    #     form=UploadForm()
    # return render(request, 'upload.html')

    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        # upload_file=request.FILES['document']
        # fs=FileSystemStorage()
        # fs.save(upload_file.name,upload_file)
        if form.is_valid():
            form.save()
            file_name = str(request.FILES['file'])
            sanitized_file_name = file_name.replace(' ', '_')
            path = os.path.join('C:\\Users\\tejas\\OneDrive\\Desktop\\Css\\resume\\media', sanitized_file_name)
            temp=0
            if file_name.lower().endswith('.docx'):
                # Convert .docx to .doc
                doc_path = os.path.join('C:\\Users\\tejas\\OneDrive\\Desktop\\Css\\resume\\media', sanitized_file_name.replace('.docx', '.doc'))
                temp=1
                convert_docx_to_doc(path, doc_path)
            headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMmQ2OTlhODctOTIxMC00YWE3LThhYmEtMjdlYjkyNGYyNzc3IiwidHlwZSI6ImFwaV90b2tlbiJ9.drNIW3vajSMe7jITN3vxdglzhm1SxXIxeIa_58bmOWY"}

            url = "https://api.edenai.run/v2/ocr/resume_parser"
            data = {
                "providers": "affinda",
                "fallback_providers": ""
            }


# Sanitize the file name (replace spaces with underscores, for example)

# Create the full path using os.path.join
            if temp==1:
                files = {'file': open(doc_path,'rb')}
            else:
                files = {'file': open(path,'rb')}

            response = requests.post(url, data=data, files=files, headers=headers)

            result = json.loads(response.text)

            # Example
            affinda_data = result.get('affinda', {}).get('extracted_data', {})
            save_resume_data_to_db(affinda_data)


            time.sleep(1)  # This will save the form data including the file in the database
            return render(request, 'home.html')# You can redirect to a success page
        else:
            logging.error(form.errors)
            time.sleep(1)
            return render(request, 'home.html') 
            # If the form is not valid, you can handle errors or simply render the form again with errors
            #return render(request, 'home.html')
    else:
        form = UploadForm()
    return render(request,'home.html')
def convert_docx_to_doc(docx_path, doc_path):
    pythoncom.CoInitialize()
    word = wc.Dispatch('Word.Application')
    word.Visible = 0  # Hide the Word application
    doc = word.Documents.Open(docx_path)
    doc.SaveAs(doc_path, FileFormat=0)  # FileFormat=0 corresponds to .doc format
    doc.Close()
    word.Quit()
    pythoncom.CoUninitialize()