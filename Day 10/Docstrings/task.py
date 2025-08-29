def format_name(f_name, l_name):
    """
    this is docstring tutorial and this function takes first name and last name of the user and returns formated name
    :param f_name: first name
    :param l_name: last name
    :return: formatted name
    """
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)



