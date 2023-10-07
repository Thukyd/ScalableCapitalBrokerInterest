# Scalable Capital Subscription Comparison

## Overview

This Python script is designed to compare two different subscription options offered by Scalable Capital. These options are:

1. **Primer Broker**: A subscription that costs €2.99 per month with no interest on savings.
2. **Prime + Broker**: A subscription that costs €4.99 per month and offers an annual interest rate of 2.6%, paid out quarterly.

The script calculates the final amount of money you would have for each option given an initial investment and a specified number of months. It also finds the minimum initial amount at which "Prime + Broker" becomes a more attractive option than "Primer Broker".

## How to Run

1. Clone the repository to your local machine.
2. Navigate to the folder containing the script.
3. Run `python scalable_capital_comparison.py` in your terminal.

## Usage

1. The function `calculate_primer_broker(months, initial_amount)` calculates the final amount for the "Primer Broker" option.
2. The function `calculate_prime_plus_broker(months, initial_amount)` calculates the final amount for the "Prime + Broker" option.
3. The function `find_threshold(months)` finds the initial amount where "Prime + Broker" becomes more financially attractive than "Primer Broker".

## Example Output

When running the script with an initial amount of €10,000 for 12 months, the output might look like this:

```
With €10000 for 12 months:
Final amount with Primer Broker: €9643.88
Final amount with Prime + Broker: €9754.34
The threshold amount for 12 months is €71900
```

## License

Apache-2.0 license
