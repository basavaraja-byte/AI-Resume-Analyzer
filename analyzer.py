def detect_skills(text):

    skills_database = [
        "Python",
        "Java",
        "SQL",
        "Machine Learning",
        "Deep Learning",
        "Artificial Intelligence",
        "Data Science",
        "TensorFlow",
        "LLM",
        "Agentic AI",
        "Streamlit",
        "Git",
        "GitHub"
    ]

    found_skills = []

    for skill in skills_database:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills