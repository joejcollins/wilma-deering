"""Confirm that the extract_manufacturer function works as expected."""

from my_pkg.cars import add_features


def test_extract_manufacturer():
    """Test the extract_manufacturer function."""
    assert add_features.extract_manufacturer("Toyota Camry") == "Toyota"
    assert add_features.extract_manufacturer("Bingo Bongo") == "Bingo"
    assert add_features.extract_manufacturer("AMC Javelin") == "AMC"
    assert add_features.extract_manufacturer("") == ""


def test_add_manufacturer():
    """Test the add_manufacturer function."""
    car = {"name": "Toyota Camry"}
    car_with_manufacturer = add_features.add_manufacturer(car)
    assert car_with_manufacturer["manufacturer"] == "Toyota"
