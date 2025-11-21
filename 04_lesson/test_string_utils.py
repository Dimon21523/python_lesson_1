from string_utils import StringUtils

utils = StringUtils()


def test_capitalize_normal():
    assert utils.capitalize("skypro") == "Skypro"


def test_capitalize_empty():
    assert utils.capitalize("") == ""


def test_capitalize_space():
    assert utils.capitalize(" skypro") == " skypro"


def test_capitalize_numbers():
    assert utils.capitalize("123") == "123"


def test_trim_normal():
    assert utils.trim("   skypro") == "skypro"


def test_trim_no_spaces():
    assert utils.trim("python") == "python"


def test_trim_empty():
    assert utils.trim("") == ""


def test_trim_only_spaces():
    assert utils.trim("   ") == ""


def test_contains_true():
    assert utils.contains("SkyPro", "S") is True


def test_contains_false():
    assert utils.contains("SkyPro", "U") is False


def test_contains_empty_string():
    assert utils.contains("", "a") is False


def test_contains_empty_symbol():
    assert utils.contains("SkyPro", "") is False


def test_delete_symbol_one_char():
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"


def test_delete_symbol_substring():
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"


def test_delete_symbol_not_found():
    assert utils.delete_symbol("SkyPro", "X") == "SkyPro"


def test_delete_symbol_empty_string():
    assert utils.delete_symbol("", "a") == ""
