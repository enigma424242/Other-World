def edit(per):
    try:
        per = per.title()
        return per
    except AttributeError:
        return per
