"""CSCA08 Assignment 3: arxiv.org"""

from copy import deepcopy
import unittest
from arxiv_functions import get_most_published_authors as get_mpas


class TestGetMostPublishedAuthors(unittest.TestCase):

    def setUp(self):
        self.example = {
            '008': {
                'identifier': '008',
                'title': 'Intro to CS is the best course ever',
                'created': '2021-09-01',
                'modified': None,
                'authors': [('Ponce', 'Marcelo'), ('Tafliovich', 'Anya Y.')],
                'abstract': 'Intro to CS rocks.'},
            '031': {
                'identifier': '031',
                'title': 'Calculus is the best course ever',
                'created': None,
                'modified': '2021-09-02',
                'authors': [('Breuss', 'Nataliya')],
                'abstract': 'Calculus is amazing.'},
            '067': {
                'identifier': '067',
                'title': 'Discrete Math is the best course ever',
                'created': '2021-09-02',
                'modified': '2021-10-01',
                'authors': [('Bretscher', 'Anna'), ('Pancer', 'Richard')],
                'abstract': 'Discrete math is great.'},
            '827': {
                'identifier': '827',
                'title': 'UofT is the best university',
                'created': '2021-08-20',
                'modified': '2021-10-02',
                'authors': [('Bretscher', 'Anna'),
                            ('Ponce', 'Marcelo'),
                            ('Tafliovich', 'Anya Y.')],
                'abstract': 'UofT rules.'},
            '042': {
                'identifier': '042',
                'title': None,
                'created': '2021-05-04',
                'modified': '2021-05-05',
                'authors': [],
                'abstract': 'No title, no authors.'}
        }

        self.examples = {
            "tie_two": {
                '001': {'identifier': '001', 'title': '', 'created': '', 'modified': '',
                        'authors': [('A', 'X')], 'abstract': ''},
                '002': {'identifier': '002', 'title': '', 'created': '', 'modified': '',
                        'authors': [('B', 'Y')], 'abstract': ''},
                '003': {'identifier': '003', 'title': '', 'created': '', 'modified': '',
                        'authors': [('A', 'X')], 'abstract': ''},
                '004': {'identifier': '004', 'title': '', 'created': '', 'modified': '',
                        'authors': [('B', 'Y')], 'abstract': ''}
            },
            "no_authors": {
                '001': {'identifier': '001', 'title': '', 'created': '', 'modified': '',
                        'authors': [], 'abstract': ''}
            },
            "one_author": {
                '001': {'identifier': '001', 'title': '', 'created': '', 'modified': '',
                        'authors': [('A', 'X')], 'abstract': ''}
            },
            "empty": {}
        }

    def test_handout_example(self):
        expected = [('Bretscher', 'Anna'),
                    ('Ponce', 'Marcelo'),
                    ('Tafliovich', 'Anya Y.')]
        actual = get_mpas(self.example)
        self.assertEqual(actual, expected, message(self.example, expected, actual))

    def test_two_authors_tie(self):
        data = self.examples["tie_two"]
        expected = [('A', 'X'), ('B', 'Y')]
        actual = get_mpas(data)
        self.assertEqual(sorted(actual), sorted(expected), message(data, expected, actual))

    def test_no_authors(self):
        data = self.examples["no_authors"]
        expected = []
        actual = get_mpas(data)
        self.assertEqual(actual, expected, message(data, expected, actual))

    def test_one_author(self):
        data = self.examples["one_author"]
        expected = [('A', 'X')]
        actual = get_mpas(data)
        self.assertEqual(actual, expected, message(data, expected, actual))

    def test_empty_input(self):
        data = self.examples["empty"]
        expected = []
        actual = get_mpas(data)
        self.assertEqual(actual, expected, message(data, expected, actual))

    def test_mutation(self):
        original = deepcopy(self.example)
        get_mpas(self.example)
        self.assertEqual(self.example, original,
                         "Function mutated the original input dictionary.")


def message(test_case: dict, expected: list, actual: object) -> str:
    return (f"When we called get_most_published_authors({test_case})\n"
            f"we expected: {expected},\nbut got: {actual}")


if __name__ == '__main__':
    unittest.main(exit=False)
