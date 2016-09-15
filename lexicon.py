def edit(par):
    try:
        par = par.capitalize()
        return par
    except AttributeError:
        return par
