skills = [
"python","java","sql","machine learning",
"data analysis","react","javascript","html","css"
]

def find_skills(text):

    found = []

    for skill in skills:

        if skill in text.lower():
            found.append(skill)

    return found


def score_resume(found):

    score = len(found) * 1.2

    if score > 10:
        score = 10

    return round(score,2)
