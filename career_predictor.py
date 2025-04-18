from textblob import TextBlob

def predict_career(interests):
    blob = TextBlob(interests)
    keywords = blob.noun_phrases

    # Expanded mapping with 10+ career paths
    career_suggestions = {
        'programming': ['Software Developer', 'Backend Developer', 'Full Stack Developer'],
        'ai': ['AI Engineer', 'Machine Learning Engineer', 'Deep Learning Engineer'],
        'data': ['Data Analyst', 'Data Engineer', 'Data Scientist'],
        'web': ['Frontend Developer', 'Backend Developer', 'Web Developer'],
        'development': ['Software Developer', 'App Developer', 'Web Developer'],
        'cloud': ['Cloud Engineer', 'DevOps Engineer', 'AWS Solutions Architect'],
        'cybersecurity': ['Cybersecurity Analyst', 'Security Engineer', 'Penetration Tester'],
        'iot': ['IoT Developer', 'Embedded Systems Engineer'],
        'robotics': ['Robotics Engineer', 'Automation Engineer'],
        'design': ['UI/UX Designer', 'Graphic Designer'],
        'database': ['Database Administrator', 'SQL Developer'],
        'networking': ['Network Engineer', 'Systems Administrator'],
        'electronics': ['Embedded Systems Developer', 'VLSI Engineer'],
        'mechanical': ['CAD Engineer', 'Mechanical Design Engineer'],
        'civil': ['Site Engineer', 'Structural Engineer'],
        'management': ['Product Manager', 'Project Manager'],
        'mobile': ['Android Developer', 'iOS Developer'],
        'game': ['Game Developer', 'Game Designer'],
        'bio': ['Bioinformatics Specialist', 'Biomedical Engineer']
    }

    # Search for relevant careers
    suggestions = []
    for keyword in keywords:
        for key in career_suggestions:
            if key in keyword.lower():
                suggestions.extend(career_suggestions[key])

    # Remove duplicates and return
    return list(set(suggestions))
