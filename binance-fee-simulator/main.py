

'''
web scrap maker & taker fees from here
https://www.binance.com/de/fee/trading

ask for VIP level and start with calculation
compare current VIP level vs next VIP level in line
'''

# import needed modules
import pip
import locale

# install needeed modules from here
#pip.main(['install','locale'])

# set locale settings for thousand separator handling (i.E. German, English)
locale.setlocale(locale.LC_NUMERIC, 'German')

# user input (!)
# define initial wallet size
wallet = 1800.00

# user input (!)
# define expected daily interest rate
scenario_1 = 1.010
scenario_2 = 1.020
scenario_3 = 1.030
scenario_4 = 1.040

# user input (!)
# define expected time frame for compound invest interest calculation
result_1 = wallet * scenario_1 ** 30
result_2 = wallet * scenario_2 ** 30
result_3 = wallet * scenario_3 ** 30
result_4 = wallet * scenario_4 ** 30

# print calc compound invest interest for each scenario
print("Scenario 1 : Daily Interest Ratio = " + str(scenario_1) +" - Start with $" + locale.format_string('%.2f', wallet, True)  + " and end with $" + locale.format_string('%.2f', result_1, True) + " after X days. Awesome!")
print("Scenario 2 : Daily Interest Ratio = " + str(scenario_2) +" - Start with $" + locale.format_string('%.2f', wallet, True)  + " and end with $" + locale.format_string('%.2f', result_2, True) + " after X days. Awesome!")
print("Scenario 3 : Daily Interest Ratio = " + str(scenario_3) +" - Start with $" + locale.format_string('%.2f', wallet, True)  + " and end with $" + locale.format_string('%.2f', result_3, True) + " after X days. Awesome!")
print("Scenario 4 : Daily Interest Ratio = " + str(scenario_4) +" - Start with $" + locale.format_string('%.2f', wallet, True)  + " and end with $" + locale.format_string('%.2f', result_4, True) + " after X days. Awesome!")