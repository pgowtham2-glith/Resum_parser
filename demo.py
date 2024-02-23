import json
import requests

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiODI2OTc5ZDUtNjM1Yy00N2E0LTgyYTgtN2Q0Y2I2Y2NlMjQzIiwidHlwZSI6ImFwaV90b2tlbiJ9.mITxfpq-fwoceUV42XKsezCs_Qf3_opr2Q4gQz-dbQs"}

url = "https://api.edenai.run/v2/ocr/resume_parser"
data = {
    "providers": "affinda",
    "fallback_providers": ""
}
files = {'file': open("C:\\Users\\tejas\\OneDrive\\Documents\\teja3_resume.pdf", 'rb')}

response = requests.post(url, data=data, files=files, headers=headers)

result = json.loads(response.text)

print(result['affinda']['extracted_data'])

def print_resume_data(resume_data):
    # Extracted personal information
    personal_info = resume_data.get('personal_infos', {})
    print("Personal Information:")
    print(f"Name: {personal_info['name']['raw_name']}")
    print(f"Location: {personal_info['address']['formatted_location']}")
    print(f"Phone: {personal_info['phones'][0]}")
    print(f"Email: {personal_info['mails'][0]}")
    print(f"Current Profession: {personal_info['current_profession']}")
    print()

    # Extracted education information
    education_info = resume_data.get('education', {})
    print("Education:")
    for entry in education_info.get('entries', []):
        print(f"Degree: {entry['accreditation']}")
        print(f"Establishment: {entry['establishment']}")
        print(f"Location: {entry['location']['formatted_location']}")
        print(f"Start Date: {entry['start_date']}")
        print(f"End Date: {entry['end_date']}")
        print()

    # Extracted work experience
    work_experience = resume_data.get('work_experience', {})
    print("Work Experience:")
    for entry in work_experience.get('entries', []):
        print(f"Title: {entry['title']}")
        print(f"Company: {entry['company']}")
        print(f"Location: {entry['location']['formatted_location']}")
        print(f"Start Date: {entry['start_date']}")
        print(f"End Date: {entry['end_date']}")
        print(f"Description: {entry['description']}")
        print()

    # Extracted skills
    skills = resume_data.get('skills', [])
    print("Skills:")
    for skill in skills:
        print(f"{skill['name']} ({skill['type']})")
    print()

    # Extracted certifications
    certifications = resume_data.get('certifications', [])
    print("Certifications:")
    for cert in certifications:
        print(f"{cert['name']}")
    print()

    # Extracted languages
    languages = resume_data.get('languages', [])
    print("Languages:")
    for lang in languages:
        print(f"{lang['name']}")
    print()

    # Extracted interests
    interests = resume_data.get('interests', [])
    print("Interests:")
    for interest in interests:
        print(f"{interest}")
    print()

# Call the function with the extracted data
print_resume_data(result['affinda']['extracted_data'])

