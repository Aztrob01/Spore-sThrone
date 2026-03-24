def sk_filter(skills):
    try:
        line = []
        for skill in skills:
            if skill is not None:
                line.append(skill)
    
        return line, len(line)

    except AttributeError:
        print(f'SK_FILTER ERROR: {skills} is not an list.')

    
