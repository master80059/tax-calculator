Notes:
1. Program will not run if file config.ini does not exist.
2. program requires the config.ini to be in the program folder properly formated.
3. to run the program you use run.py changeing the name of the program will cause it no nolonger run... security feature.
4. licence.ini is the code licence with out it the program will not run...
5. licence.ini, config_default.ini, run.py, should not be modified or will cause failer of program... security check of code built in.
6. licence.ini is only a hash check of the files that are used for the code. prevent tampering and unatherized modifications.

what i am using in the code.

	1. im using if-else statements to navigate the program.
	2. using boolean true falses to check valid answers inputs and to reset menu's
	3. exceptions  are used for error checking in the opening of configs and import also to error check values inputed. example my get functions.
	4. lists are used for memu creation and organization of information. helping in organization of the information
	5. file read/right reading and writing to configs.ini 

inputs default config expected outputs
	inputs
Pick an option from the menu:3
what is the amount of gross income: 10000
pay period: 1

	output
dailly gross $10000.00
Social Security Taxes: $1450.00
Medicare Taxes: $380.00
Federal Taxes: $817.00
state taxes: $520.00
Take Home Income: $6833.00

	inputs	
Pick an option from the menu:3
what is the amount of gross income: 150000
pay period: 1
	output
dailly gross $150000.00
Social Security Taxes: $18661.50
Medicare Taxes: $5700.00
Federal Taxes: $24442.74
state taxes: $7800.00
Take Home Income: $93395.76

	inputs	
Pick an option from the menu:3
what is the amount of gross income: 500000
pay period: 1
	output
dailly gross: $ 500000.00
Social Security Taxes: $18661.50
Medicare Taxes: $19000.00
Federal Taxes: $137507.97
state taxes: $26000.00
Take Home Income: $298830.53


	inputs	
Pick an option from the menu:3
what is the amount of gross income: 1000000
pay period: 1
	output
dailly gross : $1000000.00
Social Security Taxes: $18661.50
Medicare Taxes: $38000.00
Federal Taxes: $314724.74
state taxes: $52000.00
Take Home Income: $576613.76

pseudocode

copy right notice once
and code verification

main menu while true loop
	get int( nemu option)
		1. set up configs
		2. calculator
		8. reset config file to defaulst.
		9. copyright notice
		10. exit()
set up config
	sellect filling status
	save config.ini
calculator
	get income
	calculate taxes
	print to screen
	give option to save to file.
