"""CSCA08 Fall 2023 Assignment 1.

This code is provided solely for the personal and private use of
students taking the CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2020-2023 Jacqueline Smith and Anya Tafliovich.

"""

from constants import (YR, MON, DAY, DEP, ARR, ROW, SEAT, FFN,
                       WINDOW, AISLE, MIDDLE, SA, SB, SC, SD, SE, SF)


# We provide this function solution as an example of correct
# documentation, as well as a function that uses constants.
def get_year(ticket: str) -> str:
    """Return the year of ticket 'ticket'.

    Precondition: 'ticket' is in valid format

    >>> get_year('20230915YYZYEG12F')
    '2023'
    >>> get_year('20240915YYZYEG12F1236')
    '2024'
    >>> get_year('')
    ''
    """

    return ticket[YR:YR + 4]


# We provide this function solution as an example of correct
# documentation, as well as a function that uses other functions as
# helpers.
def get_date(ticket: str) -> str:
    """Return the date of ticket 'ticket' in YYYYMMDD format.

    Precondition: 'ticket' is in valid format

    >>> get_date('20230915YYZYEG12F')
    '20230915'
    >>> get_date('20240915YYZYEG12F1236')
    '20240915'
    >>> get_date('')
    ''
    """

    return get_year(ticket) + get_month(ticket) + get_day(ticket)


# We provide the docstring for this function to help you get started.
def get_month(ticket: str) -> str:
    """Return the month of ticket 'ticket'.

    Precondition: 'ticket' is in valid format

    >>> get_month('20230915YYZYEG12F')
    '09'
    >>> get_month('20241215YYZYEG12F1236')
    '12'
    >>> get_month('')
    ''
    """

    return ticket[MON:MON + 2]


def get_day(ticket: str) -> str:
    """Return the day of ticket 'ticket'.

    Precondition: 'ticket' is in valid format

    >>> get_day('20230915YYZYEG12F')
    '15'
    >>> get_day('20241223YYZYEG12F1236')
    '23'
    >>> get_day('')
    ''
    """

    return ticket[DAY:DAY + 2]


# We provide the docstring for this function to help you get started.
def visits_airport(ticket: str, airport: str) -> bool:
    """Return True if and only if either departure or arrival airport on
    ticket 'ticket' is the same as 'airport'.

    Precondition: 'ticket' is a valid ticket.

    >>> visits_airport('20230915YYZYEG12F1236', 'YEG')
    True
    >>> visits_airport('20230915YEGYYZ12F1236', 'YEG')
    True
    >>> visits_airport('20230915YYZYEG12F1236', 'YVR')
    False
    >>> visits_airport('', '')
    False
    """

    if ticket == '' or airport == '':
        return False

    return (get_departure(ticket) == airport
            or get_arrival(ticket) == airport)


def get_departure(ticket: str) -> str:
    """Returns the departure of the ticket 'ticket' through airport code.

    Precondition: 'ticket' is a valid ticket.

    >>> get_departure('20230915YYZYEG12F1236')
    'YYZ'
    >>> get_departure('20230915YEGYYZ12F1236')
    'YEG'
    >>> get_departure('')
    ''
    """

    return ticket[DEP:DEP + 3]


def get_arrival(ticket: str) -> str:
    """Returns the departure of the ticket 'ticket' through airport code.

    Precondition: 'ticket' is a valid ticket.

    >>> get_arrival('20230915YYZYEG12F1236')
    'YEG'
    >>> get_arrival('20230915YEGYYZ12F1236')
    'YYZ'
    >>> get_arrival('')
    ''
    """

    return ticket[ARR:ARR + 3]


def get_row(ticket: str) -> int:
    """Returns the row of the ticket 'ticket'.

       Precondition: 'ticket' is a valid ticket.

    >>> get_row('20230915YYZYEG12F1236')
    12
    >>> get_row('20230915YEGYYZ12F1236')
    12
    """

    return int(ticket[ROW:ROW + 2])


def get_seat(ticket: str) -> str:
    """Returns the seat number of the ticket 'ticket'.

    Precondition: 'ticket' is a valid ticket.

    >>> get_seat('20230915YYZYEG12F1236')
    'F'
    >>> get_seat('20230915YYZYEG12E1236')
    'E'
    """

    return ticket[SEAT]


def get_ffn(ticket: str) -> str:
    """Return the frequent flyer number from the given ticket.

    >>> get_ffn('20230915YYZYEG12F1236')
    '1236'
    >>> get_ffn('20230915YYZYEG12F')
    ''
    >>> get_ffn('')
    ''
    """

    return ticket[FFN:FFN + 4]


# We provide the docstring for this function to help you get started.
def get_seat_type(ticket: str) -> str:
    """Return WINDOW, AISLE, or MIDDLE depending on the type of seat in
    ticket 'ticket'.

    Precondition: 'ticket' is a valid ticket.

    >>> get_seat_type('20230915YYZYEG12F1236')
    'window'
    >>> get_seat_type('20230915YYZYEG08B')
    'middle'
    >>> get_seat_type('20230915YYZYEG12C1236')
    'aisle'
    >>> get_seat_type('')
    'Invalid'
    
    """
    if not ticket or len(ticket) <= SEAT:
        return 'Invalid'
    seat = ticket[SEAT]
    if seat in {SA, SF}:
        return WINDOW
    if seat in {SB, SE}:
        return MIDDLE
    if seat in {SC, SD}:
        return AISLE
    return 'Invalid'


# We provide the docstring for this function to help you get started.
def is_valid_seat(ticket: str, first_row: int, last_row: int) -> bool:
    """Return True if and only if ticket 'ticket' has a valid seat. That
    is, if the seat row is between 'first_row' and 'last_row',
    inclusive, and the seat is SA, SB, SC, SD, SE, or SF.

    Precondition: 'ticket' is in valid format.

    >>> is_valid_seat('20230915YYZYEG12F1236', 1, 30)
    True
    >>> is_valid_seat('20230915YYZYEG42F1236', 1, 30)
    False
    >>> is_valid_seat('20230915YYZYEG21Q1236', 1, 30)
    False
    """

    row = get_row(ticket)
    seat = get_seat(ticket)
    if seat in {SA, SB, SC, SD, SE, SF}:
        return first_row <= row <= last_row

    return False


def is_valid_ffn(ticket: str) -> bool:
    """Returns True if and only if the last four digits follow the conditions:
    The FFN numbers are the last 4 numbers of the ticket where 
    the sum of the first 3 numbers modulo 10 is equal to the last digit. 
    A ticket will still valid if there are no FFN numbers, and will result 
    in True. 

    >>> is_valid_ffn('20230915YYZYEG12F1236')
    True
    >>> is_valid_ffn('20230915YYZYEG12F5678')  
    True
    >>> is_valid_ffn('20230915YYZYEG12F')
    True
    """
    ffn = get_ffn(ticket)

    if len(ffn) < 4 or not ffn.isdigit():
        return True

    first_three_sum = sum(int(digit) for digit in ffn[:3])

    return first_three_sum % 10 == int(ffn[3])


def is_valid_date(ticket: str) -> bool:
    """Return True if the date in 'ticket' is valid.

    The date is valid if:
    - The month is between 1 and 12.
    - The day is valid for the given month, considering leap years.

    >>> is_valid_date('20240229YYZYEG12F1236')
    True
    >>> is_valid_date('20230229YYZYEG12F1236')
    False
    >>> is_valid_date('20231232YYZYEG12F1236')  
    False
    """

    year = int(get_year(ticket))
    month = int(get_month(ticket))
    day = int(get_day(ticket))

    if not 1 <= month <= 12:
        return False

    days_in_month = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days_in_month[2] = 29

    return 1 <= day <= days_in_month[month]


def is_valid_ticket(ticket: str, first_row: int, last_row: int) -> bool:
    """Return True if and only if 'ticket' is valid.

    A ticket is valid if:
      It has the correct format.
      The seat is valid.
      The date is valid.
      The frequent flyer number is valid.

    Parameters:
    first_row (int): The smallest valid row number.
    last_row (int): The largest valid row number.

    >>> is_valid_ticket('20230915YYZYEG12F1236', 1, 30)
    True
    >>> is_valid_ticket('20230230YYZYEG12F1236', 1, 30)  
    False
    >>> is_valid_ticket('20230915YYZYEG99G1236', 1, 30)  
    False
    """
    return (is_valid_ticket_format(ticket)
            and is_valid_seat(ticket, first_row, last_row)
            and is_valid_date(ticket)
            and is_valid_ffn(ticket))


def behind(ticket1: str, ticket2: str) -> bool:
    """Return True if ticket2 is directly behind ticket1 in the same seat.

    >>> behind('20230915YYZYEG12A1236', '20230915YYZYEG13A1236')
    True
    >>> behind('20230915YYZYEG12C1236', '20230915YYZYEG13C1236')
    True
    >>> behind('20230915YYZYEG12B1236', '20230915YYZYEG14B1236')
    False
    """

    return (
        get_seat(ticket1) == get_seat(ticket2)
        and int(get_row(ticket2)) == int(get_row(ticket1)) + 1
    )


def connecting(ticket1: str, ticket2: str) -> bool:
    """Return True if ticket1 and ticket2 represent connecting flights.

    Flights are connecting if:
      The arrival airport of ticket1 matches the departure airport of ticket2.
      The flights are on the same date.

    >>> connecting('20230915YYZYEG12F1236', '20230915YEGLAX15A1236')
    True
    >>> connecting('20230915YYZYEG12F1236', '20230916YEGLAX15A1236')  
    False
    >>> connecting('20230915YYZYEG12F1236', '20230915LAXYEG15A1236')
    False
    """
    return (
        get_arrival(ticket1) == get_departure(ticket2)
        and get_date(ticket1) == get_date(ticket2)
    )


# We provide the docstring for this function to help you get started.


def adjacent(ticket1: str, ticket2: str) -> bool:
    """Return True if and only if the seats in tickets 'ticket1' and
    'ticket2' are adjacent (next to each other). Seats across an aisle
    are not considered to be adjacent.

    Precondition: 'ticket1' and 'ticket2' are valid tickets.

    >>> adjacent('20230915YYZYEG12D1236', '20230915YYZYEG12E1236')
    True
    >>> adjacent('20230915YYZYEG12B1236', '20230915YYZYEG12A1236')
    True
    >>> adjacent('20230915YYZYEG12C1236', '20230915YYZYEG12D1236')
    False
    >>> adjacent('20230915YYZYEG12A1236', '20230915YYZYEG11B1236')
    False
    """

    ticket1_seat, ticket2_seat = get_seat(ticket1), get_seat(ticket2)

    adjacent_row1 = {SA, SB, SC}
    adjacent_row2 = {SD, SE, SF}
    if get_row(ticket1) != get_row(ticket2):
        return False
    if ticket1_seat == ticket2_seat:
        return False

    return (
        (ticket1_seat in adjacent_row1 and ticket2_seat in adjacent_row1)
        or (ticket1_seat in adjacent_row2 and ticket2_seat in adjacent_row2)
    )


def change_date(ticket: str, day: str, month: str, year: str) -> str:
    """Return new tickets with the same details as 'ticket' but with a new date.

    Precondition:
    - 'day', 'month', 'year' are valid date values.
    - The input 'ticket' is a valid ticket.

    >>> change_date('20230915YYZYEG12F1236', '20', '10', '2024')
    '20241020YYZYEG12F1236'
    >>> change_date('20230228YYZYEG14B', '01', '03', '2023')
    '20230301YYZYEG14B'
    """
    return year + month + day + ticket[DEP:]


def change_seat(ticket: str, row_number: str, seat: str) -> str:
    """Return a new ticket with the updated row number and seat.

    The departure, arrival, date, and frequent flyer number stay the same.
    Parameters:
        ticket (str): The original ticket string.
        row_number (str): The new row number for the seat.
        seat (str): The new seat letter
        
    >>> change_seat('20230915YYZYEG12F1236', '24', 'A')
    '20230915YYZYEG24A1236'
    >>> change_seat('20230915YYZYEG08C', '13', 'E')
    '20230915YYZYEG13E'
    """
    return ticket[YR: ROW] + row_number + seat + ticket[FFN:FFN + 4]


# We provide this function for you to use as a helper.
def is_valid_ticket_format(ticket: str) -> bool:
    """Return True if and only if ticket 'ticket' is in valid format:

    - year is 4 digits
    - months is 2 digits
    - day is 2 digits
    - departure is 3 letters
    - arrival is 3 letters
    - row is 2 digits
    - seat is a characters
    - frequent flyer number is either empty or 4 digits, and
      it is the last record in 'ticket'

    >>> is_valid_ticket_format('20241020YYZYEG12C1236')
    True
    >>> is_valid_ticket_format('20241020YYZYEG12C12361236')
    False
    >>> is_valid_ticket_format('ABC41020YYZYEG12C1236')
    False
    """

    return (FFN == 17
            and (len(ticket) == 17
                 or len(ticket) == 21 and ticket[FFN:FFN + 4].isdigit())
            and ticket[YR:YR + 4].isdigit()
            and ticket[MON:MON + 2].isdigit()
            and ticket[DAY:DAY + 2].isdigit()
            and ticket[DEP:DEP + 3].isalpha()
            and ticket[ARR:ARR + 3].isalpha()
            and ticket[ROW:ROW + 2].isdigit()
            and len(ticket[SEAT]) == 1)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
