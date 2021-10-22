"""
This module contains script that runs simplified ATM that dispenses Australian notes and coins
"""
import sys
import argparse

import custom_errors
import atm

BALANCE_DATA = "balance.json"

def main():
    """
    Run simplified ATM that dispenses Australian notes and coins
    """
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-a', '--amount',
                            help="The amount to withdraw as a decimal number",
                            default=None)
        parser.add_argument('-b', '--balance',
                            help="Print the current balance to the screen",
                            action="store_true",
                            default=False)
        parser.add_argument('-r', '--refill',
                            help="Refill the ATM to hold the original setting of notes and coins",
                            action="store_true",
                            default=False)
        args = parser.parse_args()

        if (args.amount and len(sys.argv) != 3) or (not args.amount and len(sys.argv) != 2):
            print("Please supply exactly one argument per script execution.")
            parser.print_help()
            sys.exit()

        sample_atm = atm.ATM(BALANCE_DATA)
        if args.amount:
            dispenced = sample_atm.withdraw_amount(args.amount)
            atm.print_withdraw_result(dispenced)
            sample_atm.save_current_balance(BALANCE_DATA)
        elif args.balance:
            sample_atm.print_available_balance()
        elif args.refill:
            sample_atm.refill_atm(BALANCE_DATA)

    except (KeyError, TypeError, ValueError, OSError, custom_errors.ATMWithdrawalError) as error:
        print(error)


if __name__ == '__main__':
    main()
