def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name("AnGEla", "YU"))

def is_leap_year(year):
    if year%4==0 and (year % 100 !=0 or year % 400==0):
        return True
    return False
print(is_leap_year(2400))
print(is_leap_year(1989))
print(is_leap_year(2000))
print(is_leap_year(2024))