from . import jalali
from django.utils import timezone


def persian_converter(mystr):
    numbers = {
        "0" : "0",
        "1" : "1",
        "2" : "2",
        "3" : "3",
        "4" : "4",
        "5" : "5",
        "6" : "6",
        "7" : "7",
        "8" : "8",
        "9" : "9",
    }
    for e,p in numbers.items():
        mystr = mystr.replace(e,p)
        return(mystr)


def jalali_converter(time):
    jmonth = ["farvardin", "ordibehesht", "khordad", "tir", "mordad", "shahrivar", "mehr", "aban", "azaz", "dey", "bahman", "esfand"]

    time = timezone.localtime(time)
    time_to_str = "{},{},{}".format(time.year,time.month,time.day)
    time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()
    time_to_list = list(time_to_tuple)

    for index, month in enumerate(jmonth):
        if time_to_list[1] == index+1:
            time_to_list[1] = month
            break
    output = "{} {} {} , hour: {}:{}".format(
        time_to_list[2],
        time_to_list[1],
        time_to_list[0],
        time.hour,
        time.minute
    )
    return persian_converter(output)