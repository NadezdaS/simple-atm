# simple-atm
Contains script that represents simplified ATM that dispenses Australian notes and coins.

## How to run the script?
Be sure that you have Python3.8 installed.

Clone this repository into your environment. Run the script and pass one of the 3 available arguments:
- --amount, -a: The amount to withdraw as a decimal number
- --balance, -b: Print the current balance to the screen
- --refill, -r: Refill the ATM to hold the original setting of notes and coins.

Examples:
```
# python3.8 run_atm.py -a 110.50
# python3.8 run_atm.py -b
# python3.8 run_atm.py -r
```

## How to run tests?
This project uses pytest for running tests. Install it by rinning:
```
pip install pytest
```

After that run go to the folder that contains this repository and run the tests:
```
# pytest
```
