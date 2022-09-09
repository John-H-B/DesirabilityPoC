# DesirabilityPoC
A proof of concept for a stakeholder preference acquisition algorithm.

To use, clone this repo and run main.py, this will guide you through setup for a desirability function.

I suggest copy and pasting your generated quick setup save_string that will be printed for future use to a text file. An example desirability function save_string is included in save_strings.txt.

The example reflects an employer of a large company that sells a high value object that is attempting to determine there most and least effective senior salespeople.

The employer values those that can make a large number of sales, expecting greater than 10 per year and believing the average employer should make 20 sales. They do not believe that move that 100 sales a year are possible.

The employer values those that use minimal sick days, expecting less than 28 sick days per year and believing the average employer should take on average 5. Taking 3 or less sick days is conisdered optimal.

The employer values those that manage juniors, prefering there seniors to manage 5 juniors each. The employer believes that those managing no juniors are undesirable. Similarly, managing 15 or more juniors is undesirable as the employer believes that the senior would be inable to provide adequate attention to each. Between 2 and 7 would be preffered.

To generate this from running main.py I typed:

N

b

Yearly_Sales

10

100

20

Yearly_sick_days

3

28

5

Juniors

0

5

15

2

7

end

15

12

end

This desirability function can be built using the above steps or using the quick setyp, and will then ask for values to get desirability.

An employee made 12 sales (far less than the 20 that is considered expected), took 4 sick days (near optimal) and manages 5 juniors (the optimal amount). Typing

12, 4, 5

gives an overall employee desirability of 0.52, which is greater than 0.5 and hence the employee is overall slightly exceeding expectations.

An employee made 80 sales (far more than the 20 that is considered expected), took 6 sick days (slightly more than preferable) and manages 0 juniors (which is unacceptable). Typing

80, 6, 0

gives an overall employee desirability of 0.00, hence the employee is presently not acceptable under the emploer's standards. If this employee then took on 5 juniors, reducing their sales to 30, the new desirability would be 0.67, which is very desirable.
