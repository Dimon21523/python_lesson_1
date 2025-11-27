import pytest
from string_utils import StringUtils

utils = StringUtils()


def test_capitalize_normal():
    assert utils.capitalize("skypro") == "Skypro"


def test_capitalize_empty():
    assert utils.capitalize("") == ""


def test_capitalize_space_begin():
    assert utils.capitalize(" skypro") == " skypro"


def test_capitalize_numbers():
    assert utils.capitalize("123") == "123"


def test_capitalize_already_capitalized():
    assert utils.capitalize("Sky") == "Sky"


def test_capitalize_none():
    with pytest.raises(AttributeError):
        utils.capitalize(None)  # type: ignore[arg-type]


def test_trim_normal():
    assert utils.trim("   skypro") == "skypro"


def test_trim_no_spaces():
    assert utils.trim("python") == "python"


def test_trim_empty():
    assert utils.trim("") == ""


def test_trim_only_spaces():
    assert utils.trim("   ") == ""


def test_trim_with_inner_spaces():
    assert utils.trim("  sky pro  ") == "sky pro  "


def test_trim_none():
    with pytest.raises(AttributeError):
        utils.trim(None)  # type: ignore[arg-type]


def test_contains_true_first_char():
    assert utils.contains("SkyPro", "S") is True


def test_contains_true_middle_char():
    assert utils.contains("SkyPro", "y") is True


def test_contains_false_not_found():
    assert utils.contains("SkyPro", "U") is False


def test_contains_empty_string():
    assert utils.contains("", "a") is False


def test_contains_empty_symbol():
    assert utils.contains("SkyPro", "") is False


def test_contains_none_string():
    with pytest.raises(TypeError):
        utils.contains(None, "a")


def test_contains_none_symbol():
    with pytest.raises(TypeError):
        utils.contains("SkyPro", None)


def test_delete_symbol_one_char():
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"


def test_delete_symbol_substring():
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"


def test_delete_symbol_not_found():
    assert utils.delete_symbol("SkyPro", "X") == "SkyPro"


def test_delete_symbol_empty_string():
    assert utils.delete_symbol("", "a") == ""


def test_delete_symbol_all_chars():
    assert utils.delete_symbol("aaa", "a") == ""


def test_delete_symbol_empty_symbol():
    assert utils.delete_symbol("SkyPro", "") == "SkyPro"


def test_delete_symbol_none_string():
    with pytest.raises(TypeError):
        utils.delete_symbol(None, "a")


def test_delete_symbol_none_symbol():
    with pytest.raises(TypeError):
        utils.delete_symbol("SkyPro", None)
