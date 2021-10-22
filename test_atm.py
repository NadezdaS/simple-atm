"""
This module contains tests for functions in atm.py
"""
import pytest

import atm
import custom_errors

BALANCE_DATA = "balance_for_testing.json"


def test_load_balance():
    """
    Test reading balance data from json file
    """
    actual = atm.load_balance(BALANCE_DATA)
    expected_10= 200
    expected_200 = 50
    assert actual['10']['default'] == expected_10 and actual['200']['default']  == expected_200


def test_withdraw_amount_exception():
    """
    Test that exception is raised when amount is not a multiple of five
    """
    sample_atm = atm.ATM(BALANCE_DATA)
    with pytest.raises(custom_errors.ATMWithdrawalError) as error:
        sample_atm.withdraw_amount("150.43")


def test_withdraw_amount():
    """
    Test how ATM dispence requested amount
    """
    sample_atm = atm.ATM(BALANCE_DATA)
    actual = sample_atm.withdraw_amount("230")
    expected = {
        "10000": 2,
        "2000": 1,
        "1000": 1
    }
    assert actual == expected   


# TO-DO: add more tests
