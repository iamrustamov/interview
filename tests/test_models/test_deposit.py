import pytest
from pydantic import ValidationError

from app.v1.models.deposit import DepositModel


def test_valid_deposit_model():
    data = {
        "date": "01.01.2023",
        "periods": 3,
        "amount": 10000,
        "rate": 1.5
    }
    deposit = DepositModel(**data)
    assert deposit.date == "01.01.2023"
    assert deposit.periods == 3
    assert deposit.amount == 10000
    assert deposit.rate == 1.5


def test_invalid_date_format():
    data = {
        "date": "2023-01-01",
        "periods": 3,
        "amount": 10000,
        "rate": 1.5
    }
    with pytest.raises(ValidationError) as exc_info:
        DepositModel(**data)
    assert "should be a string in the format 'dd.mm.YYYY'" in str(exc_info.value)


def test_invalid_periods():
    data = {
        "date": "01.01.2023",
        "periods": 100,
        "amount": 10000,
        "rate": 1.5
    }
    with pytest.raises(ValidationError) as exc_info:
        DepositModel(**data)
    assert "invalid value for 'periods'. Should be an integer between 1 and 60" in str(exc_info.value)


def test_invalid_amount():
    data = {
        "date": "01.01.2023",
        "periods": 3,
        "amount": 5000,
        "rate": 1.5
    }
    with pytest.raises(ValidationError) as exc_info:
        DepositModel(**data)
    assert "should be an integer between 10000 and 3000000" in str(exc_info.value)


def test_invalid_rate():
    data = {
        "date": "01.01.2023",
        "periods": 3,
        "amount": 10000,
        "rate": 10
    }
    with pytest.raises(ValidationError) as exc_info:
        DepositModel(**data)
    assert "should be a float between 1 and 8" in str(exc_info.value)
