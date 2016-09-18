def edit(option):
    try:
        option = option.title()
        return option
    except AttributeError:
        return option
