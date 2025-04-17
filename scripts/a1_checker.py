"""A simple checker for functions in tickets.py."""

from typing import Any
import unittest
import checker_generic
import tickets

FILENAME = 'tickets.py'
PYTA_CONFIG = 'pyta/a1_pyta.txt'
TARGET_LEN = 79
SEP = '='

CONSTANTS = {'YR': 0, 'MON': 4, 'DAY': 6, 'DEP': 8, 'ARR': 11, 'ROW':
             14, 'SEAT': 16, 'FFN': 17, 'SA': 'A', 'SB': 'B', 'SC': 'C', 'SD':
             'D', 'SE': 'E', 'SF': 'F', 'WINDOW': 'window', 'AISLE': 'aisle',
             'MIDDLE': 'middle'}


class CheckTest(unittest.TestCase):
    """Sanity checker for assignment functions."""

    def test_get_date(self) -> None:
        """Function get_date."""

        self._check(tickets.get_date, ['20230915YYZYEG12F'], str)

    def test_get_year(self) -> None:
        """Function get_year."""

        self._check(tickets.get_year, ['20230915YYZYEG12F'], str)

    def test_get_month(self) -> None:
        """Function get_month."""

        self._check(tickets.get_month, ['20230915YYZYEG12F'], str)

    def test_get_day(self) -> None:
        """Function get_day."""

        self._check(tickets.get_day, ['20230915YYZYEG12F'], str)

    def test_get_departure(self) -> None:
        """Function get_departure."""

        self._check(tickets.get_departure, ['20230915YYZYEG12F'], str)

    def test_get_arrival(self) -> None:
        """Function get_arrival."""

        self._check(tickets.get_arrival, ['20230915YYZYEG12F'], str)

    def test_get_row(self) -> None:
        """Function get_row."""

        self._check(tickets.get_row, ['20230915YYZYEG12F'], int)

    def test_get_seat(self) -> None:
        """Function get_seat."""

        self._check(tickets.get_seat, ['20230915YYZYEG12F'], str)

    def test_get_seat_type(self) -> None:
        """Function get_seat_type."""

        self._check(tickets.get_seat_type, ['20230915YYZYEG12F'], str)

    def test_get_ffn(self) -> None:
        """Function get_ffn."""

        self._check(tickets.get_ffn, ['20230915YYZYEG12F1236'], str)

    def test_visits_airport(self) -> None:
        """Function visits_airport."""

        self._check(tickets.visits_airport,
                    ['20230915YYZYEG12F', 'YYZ'], bool)

    def test_connecting(self) -> None:
        """Function connecting."""

        self._check(tickets.connecting,
                    ['20230915YYZYEG12F', '20230915YEGLAS20A'], bool)

    def test_is_valid_seat(self) -> None:
        """Function is_valid_seat."""

        self._check(tickets.is_valid_seat,
                    ['20230915YYZYEG12F', 1, 30], bool)

    def test_is_valid_ffn(self) -> None:
        """Function is_valid_ffn."""

        self._check(tickets.is_valid_ffn, ['20230915YYZYEG12F1236'], bool)

    def test_is_valid_date(self) -> None:
        """Function is_valid_date."""

        self._check(tickets.is_valid_date, ['20230915YYZYEG12F'], bool)

    def test_is_valid_ticket(self) -> None:
        """Function is_valid_ticket."""

        self._check(tickets.is_valid_ticket,
                    ['20230915YYZYEG12F1236', 1, 30], bool)

    def test_adjacent(self) -> None:
        """Function adjacent."""

        self._check(tickets.adjacent,
                    ['20230915YYZYEG12F', '20230915YYZYEG12E1236'], bool)

    def test_behind(self) -> None:
        """Function behind."""

        self._check(tickets.behind,
                    ['20230915YYZYEG11F', '20230915YYZYEG12F'], bool)

    def test_change_seat(self) -> None:
        """Function change_seat."""

        self._check(tickets.change_seat,
                    ['20230915YYZYEG12F', '20', 'A'], str)

    def test_change_date(self) -> None:
        """Function change_date."""

        self._check(tickets.change_date,
                    ['20230915YYZYEG12F', '20', '10', '2024'], str)

    def test_check_constants(self) -> None:
        """Values of constants."""

        print('\nChecking that constants refer to their original values...')
        self._check_constants(CONSTANTS, tickets)
        print('  check complete.')

    def _check(self, func: callable, args: list, ret_type: type) -> None:
        """Check that func called with arguments args returns a value of type
        ret_type. Display the progress and the result of the check.

        """

        print(f'\nChecking {func.__name__}...')
        result = checker_generic.check(func, args, ret_type)
        self.assertTrue(result[0], result[1])
        print('  check complete.')

    def _check_constants(self, name2value: dict[str, Any], mod: Any) -> None:
        """Check that, for each (name, value) pair in name2value, the value of
        a variable named name in module mod is value.
        """

        for name, expected in name2value.items():
            actual = getattr(mod, name)
            msg = (f'The value of constant {name} should be {expected}'
                   f' but is {actual}.')
            self.assertEqual(expected, actual, msg)


print(''.center(TARGET_LEN, SEP))
print(' Start: checking coding style '.center(TARGET_LEN, SEP))
checker_generic.run_pyta(FILENAME, PYTA_CONFIG)
print(' End checking coding style '.center(TARGET_LEN, SEP))

print(' Start: checking type contracts '.center(TARGET_LEN, SEP))
unittest.main(exit=False)
print(' End checking type contracts '.center(TARGET_LEN, SEP))

print('\nScroll up to see ALL RESULTS:')
print('  - checking coding style')
print('  - checking type contract\n')
