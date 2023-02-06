import dataclasses
import os
import pytest
import json
import unittest

from homework_10.things_to_test_hw import add_test, search_in_file, add_from_json, Storage


@pytest.fixture
def create_file():
    print('before')
    filename = 'file.txt'
    lines = ['first_line\n', 'second_line\n', 'third_line\n']
    with open(filename, 'w') as file:
        file.writelines(lines)
    # file.close()
    yield
    os.remove(filename)
    print('after')


@pytest.fixture
def create_file_json():
    print('before')
    filename = 'file.txt'
    data = {'a': 3, 'b': 4}
    with open(filename, 'w') as file:
        json.dump(data, file)
    yield
    os.remove(filename)
    print('after')


def test_file_exist(create_file):
    assert os.path.isfile('file.txt')


def test_search_in_file_negative(create_file):
    filename = 'file.txt'
    assert search_in_file(filename, 'pattern') != ['pattern']


def test_search_in_file_positive(create_file):
    filename = 'file.txt'
    assert search_in_file(filename, 'first_line\n') == ['first_line\n']


def test_add_from_json_positive(create_file_json):
    filename = 'file.txt'

    assert add_from_json(filename, ('a', 'b')) == 7


def test_add_from_json_negative(create_file_json):
    filename = 'file.txt'
    with pytest.raises(KeyError):
        add_from_json(filename, ('a', 'b', 'c'))


# @pytest.fixture
class MyClass:
    def __init__(self):
        self.field = str


class TestStorage(unittest.TestCase):

    def setUp(self):
        self.storage = Storage()

    def test_add_table(self):
        self.assertEqual(self.storage.add_table('table_name', MyClass), None)

    def test_get_from_table(self):
        with self.assertRaises(ValueError):
            self.storage.get_from_table('table_name')

    def test_add_to_table(self):
        self.assertEqual(self.storage.add_to_table('table_name', 'a', (2, 3)), 'invalid data')


