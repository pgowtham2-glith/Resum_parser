
# models.py

import json
import os
import requests
import datetime

# models.py

from django.db import models

class StudentForm(models.Model):
    file = models.FileField(null=True)
    name = models.CharField(max_length=255, default='Not available', null=True)
    location = models.CharField(max_length=255, default='Not available', null=True)
    phone = models.CharField(max_length=20, default='Not available', null=True)
    email = models.EmailField(default='Not available', null=True)
    urls = models.CharField(max_length=255, default='Not available', null=True)
    current_profession = models.CharField(max_length=255, default='Not available', null=True)

    # Additional fields based on your resume data structure
    education_details = models.CharField(max_length=255, default='Not available', null=True)
   # establishment = models.CharField(max_length=255, default='Not available', null=True)
    work_title = models.CharField(max_length=255, default='Not available', null=True)
    company = models.CharField(max_length=255, default='Not available', null=True)
    skill_name = models.CharField(max_length=255, default='Not available', null=True)
    certification_name = models.CharField(max_length=255, default='Not available', null=True)
    language_name = models.CharField(max_length=255, default='Not available', null=True)
    interest = models.CharField(max_length=255, default='Not available', null=True)

def save_resume_data_to_db(resume_data):
    print('hi')
    print(resume_data)
    personal_info = resume_data.get('personal_infos', {})
    education_info = resume_data.get('education', {})
    work_experience = resume_data.get('work_experience', {})
    skills = resume_data.get('skills', [])
    certifications = resume_data.get('certifications', [])
    languages = resume_data.get('languages', [])
    interests = resume_data.get('interests', [])

    skill_names = [skill.get('name', 'Not available') for skill in skills]
    certifications_name = [certi.get('name', 'Not available') for certi in certifications]
    accreditations = [entry.get('accreditation', 'Not available') for entry in education_info.get('entries', [])]
    establishments = [entry.get('establishment', 'Not available') for entry in education_info.get('entries', [])]
    marks = [entry.get('gpa', 'Not available') for entry in education_info.get('entries', [])]
    
    resume_data_instance = StudentForm(
        name=personal_info.get('name', {}).get('raw_name', 'None'),
        location=personal_info.get('address', {}).get('formatted_location', 'None'),
        phone=personal_info.get('phones', [])[0] if personal_info.get('phones', []) else 'Not available',
        email=personal_info.get('mails', [])[0] if personal_info.get('mails', []) else 'Not available',
        current_profession=personal_info.get('current_profession', 'Not available'),
        urls = personal_info.get('urls','Not available'),

        # Additional fields based on your resume data structure
        # degree=education_info.get('entries', [])[0].get('accreditation', 'Not available') if education_info.get('entries', []) else 'Not available',
        education_details = ', '.join(filter(None, accreditations + establishments + marks)) if accreditations or establishments or marks else 'Not available',

       # establishment=education_info.get('entries', [])[0].get('establishment', 'Not available') if education_info.get('entries', []) else 'Not available',
        
        work_title=work_experience.get('entries', [])[0].get('title', 'Not available') if work_experience.get('entries', []) else 'Not available',
        company=work_experience.get('entries', [])[0].get('company', 'Not available') if work_experience.get('entries', []) else 'Not available',
        skill_name=', '.join(skill_names) if skill_names else 'Not available',
        #certification_name=certifications[0].get('name', 'Not available') if certifications else 'Not available',
        certification_name = ', '.join(certifications_name) if certifications_name else 'Not available',
        language_name=languages[0].get('name', 'Not available') if languages else 'Not available',
        interest=interests[0] if interests else 'Not available',
    )

    resume_data_instance.save()
    
