def get_suggestions(found_skills, target_skills):
    missing = list(set(target_skills) - set(found_skills))
    return f"Consider adding or highlighting: {', '.join(missing)}"
