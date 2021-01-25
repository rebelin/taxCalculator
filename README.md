Tax Calculator
==============

The primary goal of this python program is to take the user's income and determine the amount of income tax the user would pay under three different tax plans. 

The user enters an income, which is then used to calculate the total taxes owed, the percent of gross income paid to taxes, and their net income for each plan.

Taxes are Complicated
---------------------
This program ignores write-offs, credits, deductions, dependents, and all the other stuff that make income tax so complex. This will calculate taxes for a single taxpayer, claiming only him or herself, taking the standard deduction. The standard deduction is currently $5,800 and a single exemption is $3,700. So each income you can assume will be $9,500 lower than the entered amount, for tax purposes.

The Tax Plans
-------------

###2000 Tax Plan (Final year of Clinton administration)

OVER | NOT OVER | AMOUNT OF TAX
---|---|---
$0 | $2,650 | 0%
$2,650 | $27,850 | 15%
$27,850 | $59,900 |28%
$59,900 | $134,200 | 31%
$134,200 | $289,950 36%
$289,950 | AND OVER | 39.6%


###2008 Tax Plan (Final year of Bush administration)

OVER | NOT OVER | AMOUNT OF TAX
---|---|---
$0|$8,025|10%
$8,025|$32,550|15%
$32,550|$78,850|25%
$78,850|$164,550|28%
$164,550|$357,700|33%
$357,700|AND OVER|35%


###2014 Tax Plan (The most recent data)

OVER | NOT OVER | AMOUNT OF TAX
---|---|---
$0|$8,700|10%
$8,700|$35,350|15%
$35,350|$85,650|25%
$85,650|$178,650|28%
$178,650|$388,350|33%
$388,350|AND OVER|35%


A Worked Example
----------------
Imagine Jose made $30,000. After subtracting the standard deduction and single exemption, his adjusted income is $20,500. Now according to the year 2000 plan, the first $2650 are taxed at 0%, and dollars 2,651-20,500 are taxed at 15%.

```
Welcome to the tax calculator.
How much gross income did you earn last year?  $30000

Results for the 2000 plan.
Taxes owed: $2677.5
Percent of gross: 9%
Net income: $27322.5

Results for the 2008 plan.
Taxes owed: $2673.75
Percent of gross: 9%
Net income: $27326.25

Results for the 2014 plan.
Taxes owed: $2640.0
Percent of gross: 9%
Net income: $27360.0
```

Author
------
Rebecca Lin

License
-------
unlicense.org
