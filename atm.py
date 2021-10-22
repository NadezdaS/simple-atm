"""
This module contains class that emulates simplified ATM that dispenses Australian notes and coins
"""
import json

import custom_errors

class ATM:
    """
    Simplified ATM that dispenses Australian notes and coins
    """
    def __init__(self, file_with_balance_data):
        self.cash_balance = load_balance(file_with_balance_data)

    def withdraw_amount(self, amount):
        """
        Withdraw amount from ATM

        Returns dictionary with number of dispenced notes and coins
        Raises custom exception if not enough money in ATM, if there are no notes or coins to fulfill exact amount,
        or if requestes amount is not a multiple of five
        """
        cents = int(float(amount)*100)
        withdraw_count = {}
        total_available_amount = self.calculate_total_available_amount()

        if cents > total_available_amount:
            raise custom_errors.ATMWithdrawalError(
                "Error: Not enough cash in ATM to service your request. "  \
                f"Available balance - {format_balance(total_available_amount)}.")

        if (cents % 5) != 0:
            raise custom_errors.ATMWithdrawalError(
                f"Error: ATM don't have 1c and 2c coins to dispence requested amount.")

        for denomination in self.cash_balance.keys():
            current_denom_balance = int(self.cash_balance[denomination]["current"])
            number_of_notes_or_coins = cents // int(denomination)

            if current_denom_balance == 0 or number_of_notes_or_coins == 0:
                continue

            withdraw_num = current_denom_balance if number_of_notes_or_coins > current_denom_balance else number_of_notes_or_coins

            cents -= withdraw_num * int(denomination)
            self.cash_balance[denomination]["current"] -= withdraw_num
            withdraw_count[denomination] = withdraw_num

            if cents == 0:
                break

        if cents == 0:
            return withdraw_count

        raise custom_errors.ATMWithdrawalError(
            "Error: Not enough coins or notes to dispence requested amount.")

    def print_available_balance(self):
        """
        Print the current balance to the screen
        """
        total_amount_cents = self.calculate_total_available_amount()
        print(f"Available balance: {format_balance(total_amount_cents)}")

    def refill_atm(self, file_with_balance_data):
        """
        Restore balance data to default (original amount)
        """
        for denominations in self.cash_balance.keys():
            self.cash_balance[denominations]["current"] = self.cash_balance[denominations]["default"]
        self.save_current_balance(file_with_balance_data)
        print("ATM has been refilled.")

    def get_current_balance(self):
        """
        Return current available ATM balance
        """
        return {value: amount["current"] for value, amount in self.cash_balance.items()}

    def calculate_total_available_amount(self):
        """
        Return total available amount in cents
        """
        return sum([int(denominations)*amount for denominations, amount in self.get_current_balance().items()])

    def save_current_balance(self, file_with_balance_data):
        """
        Save current balance to json file
        """
        with open(file_with_balance_data, 'w') as json_file:
            json.dump(self.cash_balance, json_file, indent=4)


# helper functions
def format_balance(balance_cents):
    """
    Return balance as string in the decimal format (ex. $1000.15)
    """
    return f"${balance_cents // 100}.{balance_cents % 100}"


def load_balance(balance_json):
    """
    Load balance data from json file
    """
    with open(balance_json) as file:
        json_dict = json.load(file)
    return json_dict


def print_withdraw_result(withdraw_result):
    """
    Print how many notes and coins has been dispenced
    """
    result_text = "Withdrawing: "
    for denomination, amount in withdraw_result.items():
        if int(denomination) >= 100:
            result_text += f"{amount}x ${int(denomination) // 100} Note, "
        else:
            result_text += f"{amount}x {denomination}c coin, "
    print(result_text[:-2])
