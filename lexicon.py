def edit(per):
    try:
        per = per.capitalize()
        return per
    except AttributeError:
        return per
