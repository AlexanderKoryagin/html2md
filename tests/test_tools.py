"""
Tests
"""
# pylint: disable=invalid-name

import pytest

from converter.tools import FileReader
from converter.tools import HTMLToMD
from tests import examples


@pytest.mark.parametrize(
    'initial, expected',
    (
        ('tests/example_1.html', examples.examples_1_md),
        ('tests/example_2.html', examples.examples_2_md),
    ),
    ids=['example_1', 'example_2']
)
def test_generation(initial, expected):
    """Test generation and expected result"""
    reader = FileReader(file_path=initial)
    html_str = reader.read_file()
    conv = HTMLToMD()
    conv.feed(html_str)
    result = conv.out
    assert result == expected


@pytest.mark.parametrize(
    'file_path',
    (
        'test_1_en.html',
        pytest.mark.xfail('fake_file.html', strict=True, raises=IOError)
    ),
)
def test_file_open(file_path):
    """Test files opening"""
    reader = FileReader(file_path=file_path)
    reader.read_file()


@pytest.mark.xfail(strict=True, raises=ValueError)
def test_file_open_unsupported_tag():
    """Test handling of unsupported tags"""
    file_path = 'tests/example_3_err.html'
    html_reader = FileReader(file_path=file_path)
    html_str = html_reader.read_file()
    conv = HTMLToMD()
    conv.feed(html_str)
