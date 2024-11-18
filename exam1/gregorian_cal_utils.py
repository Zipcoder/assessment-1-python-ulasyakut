def is_leap_year(year: int) -> bool:
    """
    Given a year, this function returns a boolean indicating whether or not it is a leap year.

    :param year: an integer indicating a year.
    :return: A boolean indicating whether or not the year parameter is a leap year.
    """
    boolean = False
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0 :
            boolean = True

        elif year % 100 == 0 and year % 400 != 0:
            boolean = False
        
        else:
            boolean = True

    return boolean  # implement me
