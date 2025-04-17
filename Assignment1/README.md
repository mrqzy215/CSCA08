### The Airline Ticket
The typical airplane boarding pass contains many different pieces of information, including passenger information, seat, flight number, flight time, and so on. In this assignment, we'll work with our own version of information you might find on a boarding pass.


The date the ticket is for, including year, month, and day.
Departure and arrival airport codes of the flight the ticket is for.
The seat assigned to the ticket, including the row number and the seat within that row.
The passenger's frequent flyer number, if applicable.
A valid ticket will have either 17 or 21 characters.


#### Task 1: Getting the Information
Advice: Start working on these functions as soon as the assignment is released. You have already learned all material needed to complete them.

Functions to write for A1: Getting Ticket Info
Function name:
(Parameter types) -> Return type	Full Description (paraphrase to get a proper docstring description)
get_date:
(str) -> str	
The parameter represents the ticket. The function should return the date on the given ticket in the format YYYYMMDD. You may assume the input ticket is valid.

For example, if the constants have values YR = 0, MON = 4, DAY = 6, and the input ticket string is '20231221YYZYEG25F4442', this function should return '20231221'.

As another example, if the constants have values YR = 10, MON = 8, DAY = 6, and the input ticket string is 'YYZLAS2009202416D4420', this function should return '20240920'.

get_year:
(str) -> str	
The parameter represents the ticket. The function should return the year on the given ticket in the format YYYY. You may assume the input ticket is valid.

See function get_date for examples.

get_month:
(str) -> str	
The parameter represents the ticket. The function should return the month on the given ticket in the format MM. You may assume the input ticket is valid.

See function get_date for examples.

get_day:
(str) -> str	
The parameter represents the ticket. The function should return the day on the given ticket in the format DD. You may assume the input ticket is valid.

See function get_date for examples.

get_departure:
(str) -> str	
The parameter represents the ticket. The function should return the departure airport code on the given ticket. You may assume the input ticket is valid.

For example, if the constant DEP has value 8, and the input ticket string is '20231221YYZYEG25F4442', this function should return 'YYZ'.

As another example, if the constant DEP has value 0, and the input ticket string is 'YYZLAS2009202416D4420', this function should return 'YYZ'.

get_arrival:
(str) -> str	
The parameter represents the ticket. The function should return the arrival airport code on the given ticket. You may assume the input ticket is valid.

For example, if the constant ARR has value 11, and the input ticket string is '20231221YYZYEG25F4442', this function should return 'YEG'.

As another example, if the constant ARR has value 3, and the input ticket string is 'YYZLAS2009202416D4420', this function should return 'LAS'.

get_row:
(str) -> int	
The parameter represents the ticket. The function should return the row number on the given ticket. You may assume the input ticket is valid.

For example, if the constant ROW has value 14, and the input ticket string is '20231221YYZYEG25F4442', this function should return 25.

get_seat:
(str) -> str	
The parameter represents the ticket. The function should return the seat on the given ticket. You may assume the input ticket is valid.

For example, if the constant SEAT has value 16, and the input ticket string is '20231221YYZYEG25F4442', this function should return 'F'.

get_ffn:
(str) -> str	
The parameter represents the ticket. The function should return the frequent flyer number on the given ticket. You may assume the input ticket is valid.

For example, if the input ticket string is '20231221YYZYEG25F4442', this function should return '4442'. If the input ticket string is '20231221YYZYEG25F', this function should return ''.

 

#### Task 2: Validating the Information
Advice: Start working on these functions as soon as the assignment is released. You can complete the headers and docstrings for all of them now, and then complete the implementations a week after.

Functions to write for A1: Validating Ticket Info
Function name:
(Parameter types) -> Return type	Full Description (paraphrase to get a proper docstring description)
is_valid_seat:
(str, int, int) -> bool	
The first parameter represents the ticket. The second parameter represents the number of the first row in the plane. The third parameter represents the number of the last row in the plane. The function should return True if and only if the seat, including the row number and the seat within that row, of this ticket is valid. See above for explanations of ticket validity. You may assume that the format of the ticket string is valid: see provided helper function is_valid_ticket_format.

For example, if the values of the constants are ROW = 14 and SEAT = 16, and the input ticket string is '20230915YYZYEG12F1236', the second argument is 1, and the third argument is 30, then the function should return True.

If, however, the input ticket string is '20230915YYZYEG32F1236', the second argument is 1, and the third argument is 30, then the function should return False.

Similarly, if the input ticket string is '20230915YYZYEG12H1236', the second argument is 1, and the third argument is 30, then the function should return False.

is_valid_ffn:
(str) -> bool	
The parameter represents the ticket. The function should return True if and only if the frequent flyer number of this ticket is valid. See above for explanations of ticket validity. You may assume that the format of the ticket string is valid: see provided helper function is_valid_ticket_format.

is_valid_date:
(str) -> bool	
The parameter represents the ticket. The function should return True if and only if the date of this ticket is valid. See above for explanations of ticket validity. You may assume that the format of the ticket string is valid: see provided helper function is_valid_ticket_format.

Hint: this is possibly the most challenging function in this assignment. You may want to implement it last.

is_valid_ticket:
(str, int, int) -> bool	
The first parameter represents the ticket. The second parameter represents the number of the first row in the plane. The third parameter represents the number of the last row in the plane. The function should return True if and only if the ticket is in valid format and all of the ticket information on this ticket is valid. See above for explanations of ticket validity. Hint: use the provided helper function is_valid_ticket_format.

 

#### Task 3: Analysing the Information
Advice: Start working on these functions as soon as the assignment is released. You can complete the headers and docstrings for all of them now, and then complete the implementations a week after.

Functions to write for A1: Analysing Ticket Info
Function name:
(Parameter types) -> Return type	Full Description (paraphrase to get a proper docstring description)
visits_airport:
(str, str) -> bool	
The first parameter represents the ticket. The second parameter represents the airport code. The function should return True if and only if this flight either begins or ends in the given airport. You may assume the ticket is valid.

connecting:
(str, str) -> bool	
The parameters represent two tickets. The function should return True if and only if the two flights are connecting: the first flight arrives in the same airport as the departure point of the second flight, and the two flights are on the same dates. You may assume the tickets are valid.

adjacent:
(str, str) -> bool	
The parameters represent two tickets. The function should return True if and only if the seats on the two tickets are adjacent, i.e. they are next to each other in the same row. Seats that are across an aisle are not considered adjacent. You do not need to check the date, nor the departure/arrival airports in this function. You may assume the tickets are valid.

behind:
(str, str) -> bool	
The parameters represent two tickets. The function should return True if and only if the seats on the two tickets are one immediately behind another. You do not need to check the date, nor the departure/arrival airports in this function. You may assume the tickets are valid.

get_seat_type:
(str) -> str	
The parameter represents the ticket. The function should return the type of the seat on the given ticket: WINDOW, MIDDLE, or AISLE. You may assume the ticket is valid.

 

#### Task 4: Changing the Information
Functions to write for A1: Changing Ticket Info
Function name:
(Parameter types) -> Return type	Full Description (paraphrase to get a proper docstring description)
change_seat:
(str, str, str) -> str	
Note: this function is not required; completing it will earn you bonus marks.

The first parameter represents the ticket. The second parameter represents the row number. The third parameter represents the seat within that row. The function should return a new ticket that is in the same format as the input ticket, has the same departure, arrival, date, and frequent flyer number as the input ticket, and has a new seat information with the given row and seat. You may assume the ticket and the new seat information are valid.

For example, if the values of the constants are ROW = 14 and SEAT = 16, and the input ticket string is '20230915YYZYEG12F1236', the second argument is '24', and the third argument is 'A', then the function should return '20230915YYZYEG24A1236'.

change_date:
(str, str, str, str) -> str	
Note: this function is not required; completing it will earn you bonus marks.

The first parameter represents the ticket. The second parameter represents the day. The third parameter represents the months. The last parameter represents the year. The function should return a new ticket that is in the same format as the input ticket, has the same departure, arrival, seat information, and frequent flyer number as the input ticket, and has a new date. You may assume the ticket and the new date information are valid.

For example, if the values of the constants are YEAR = 0, MON = 4, and DAY = 6, and the input ticket string is '20230915YYZYEG12F1236', the second argument is '20', the third argument is '10', and the last argument is '2024', then the function should return '20241020YYZYEG12F1236'.
