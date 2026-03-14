import pdfplumber

skills = [
    "python","java","sql","machine learning",
    "react","javascript","html","css"
]

def extract_text(pdf):

    text = ""

    with pdfplumber.open(pdf) as pdf_file:

        for page in pdf_file.pages:
            text += page.extract_text()

    return text


def find_skills(text):

    found = []

    for skill in skills:

        if skill in text.lower():
            found.append(skill)

    return found


resume = "resume.pdf"

text = extract_text(resume)

found_skills = find_skills(text)

score = len(found_skills)

print("Detected Skills:",found_skills)

print("Resume Score:",score,"/10")
