# program: Financial, Interest & Budgeting calculator
# written by: Master80059
# date: 9-25-2018
# description: The program will be designed to determine what should be withheld for your 1099 IRS taxed income. After determine what your in-hand cash is after
#   with-holdings for taxes. Determine how much should go to housing, savings/investing, donations,  free spending money. This will be a helpful tool for a person 
#   who is investing or trying to save and make money on investments. #challenges: context to what the assinment was looking  for. plus mising more advanced knolege into it.
# time spent: 4 hours research on wrong question solution idea. 10 min once I found out what the intent was of the question.  and removed everything but what i new.
#


# Import list

import configparser
config = configparser.RawConfigParser()
import secrets
from time import sleep
import os


# instantiate

# parse existing file

config.read('config.ini')

# Global fixed Variables

ProgramTitle = "Financial, Interest & Budgeting calculator"
author =  "Steve W. Cornell"
Copyright = "Copyright (C) <2018>"
    # fica tax rate
RUN = True

#tax Rate configs information Edit here if changes to tax rates may change or relocate to config
social_security_Trate = config.getfloat('tax_rates', 'social_security_Trate')
social_security_MTI = config.getfloat('tax_rates', 'social_security_MTI')
medicare_TrateBase = config.getfloat('tax_rates', 'medicare_TrateBase')
medicare_MaxBase_MFJ = config.getfloat('tax_rates', 'medicare_MaxBase_MFJ')
medicare_MaxBase_S = config.getfloat('tax_rates', 'medicare_MaxBase_S')
medicare_MaxBase_MFS = config.getfloat('tax_rates', 'medicare_MaxBase_MFS')
Medicare_BaseOverRate = config.getfloat('tax_rates', 'Medicare_BaseOverRate')
ss_filling_status = config.getint('config','ss_filling_status')
federal_filling_status = config.getint('config','federal_filling_status')


# Get and repeated code    
def clear(): # used to clear screen
   return os.system('cls')


def dollar(amount): # used in print command to format floats to us currency format for easy read.
   return("${0:,.2f}".format(amount))


def get_bool(prompt): #used to get a bool input and add different entries or answers not case sensitive 
    while True:
        try:
            return {"true":True,"t":True,"yes":True,"y":True,"false":False,"f":False,"no":False,"n":False}[input(prompt).lower()]
        except KeyError:
            print ("Invalid input: please enter true, t, yes, y or false, f, no, n. not case sensitive")


def get_int(prompt): # used to get a int input
    while True:
        try:
           return int(input(prompt))
        except ValueError:
           print ("invalid input must be in 000 format!")


def get_float(prompt): #used to get a float input
    while True:
        try:
           return float(input(prompt))
        except ValueError:
           print ("invalid input must be in 000.00 format!")



class income: # calculation class functions

    def calculate_SSTaxes(taxable_ammount):
        while True:
            if taxable_ammount > social_security_MTI :
                return (social_security_MTI * social_security_Trate)
            else:
                return (taxable_ammount * social_security_Trate)
            

    def calculate_MCTaxes(taxable_ammount):
        while True:
            if ss_filling_status == 1 : # Single filling or head of household
                MCMrate = ss_filling_status
            elif ss_filling_status == 2 : # married filling joint
                MCMrate = medicare_MaxBase_MFJ
            elif ss_filling_status == 3 : # married filling seperatly
                MCMrate = medicare_MaxBase_MFS


            if taxable_ammount > MCMrate :
                return(taxable_ammount * Medicare_BaseOverRate)
            else:
                return(taxable_ammount * medicare_TrateBase)


    def calculate_federalTaxes(federal_taxable_ammount):
        while True:
            if federal_filling_status == 1: #single filling status
                if federal_taxable_ammount > 500000.00:
                    return(((federal_taxable_ammount-500000.00)*.37)+150689.50)
                elif federal_taxable_ammount > 200000.00:
                    return(((federal_taxable_ammount-200000.00)*.35)+45689.50)
                elif federal_taxable_ammount > 157500.00:
                    return(((federal_taxable_ammount-157500.00)*.32)+32089.50)
                elif federal_taxable_ammount > 82500.00:
                    return(((federal_taxable_ammount-82500.00)*.24)+14089.50)
                elif federal_taxable_ammount > 38700.00:
                    return(((federal_taxable_ammount-38700.00)*.22)+4453.50)
                elif federal_taxable_ammount > 9525.00:
                    return(((federal_taxable_ammount-9525.00)*.12)+952.50)
                elif federal_taxable_ammount > 0.00:
                    return(federal_taxable_ammount*.10)
                else:
                    return(0)
            elif federal_filling_status == 2: #married Filling Joint
                if federal_taxable_ammount > 600000.00:
                    return(((federal_taxable_ammount-600000.00)*.37)+161379.00)
                elif federal_taxable_ammount > 400000.00:
                    return(((federal_taxable_ammount-400000.00)*.35)+91379.00)
                elif federal_taxable_ammount > 315000.00:
                    return(((federal_taxable_ammount-315000.00)*.32)+64179.00)
                elif federal_taxable_ammount > 165000.00:
                    return(((federal_taxable_ammount-165000.00)*.24)+28179.00)
                elif federal_taxable_ammount > 77400.00:
                    return(((federal_taxable_ammount-77400.00)*.22)+8907.00)
                elif federal_taxable_ammount > 19050.00:
                    return(((federal_taxable_ammount-19050.00)*.12)+1905.00)
                elif federal_taxable_ammount > 0.00:
                    return(federal_taxable_ammount*.10)
                else:
                    return(0)
            elif federal_filling_status == 3: #married Filling seperately
                if federal_taxable_ammount > 600000.00/2:
                    return(((federal_taxable_ammount-600000.00/2)*.37)+161379.00/2)
                elif federal_taxable_ammount > 400000.00:
                    return(((federal_taxable_ammount-400000.00/2)*.35)+91379.00/2)
                elif federal_taxable_ammount > 315000.00:
                    return(((federal_taxable_ammount-315000.00/2)*.32)+64179.00/2)
                elif federal_taxable_ammount > 165000.00:
                    return(((federal_taxable_ammount-165000.00/2)*.24)+28179.00/2)
                elif federal_taxable_ammount > 77400.00:
                    return(((federal_taxable_ammount-77400.00/2)*.22)+8907.00/2)
                elif federal_taxable_ammount > 19050.00:
                    return(((federal_taxable_ammount-19050.00/2)*.12)+1905.00/2)
                elif federal_taxable_ammount > 0.00:
                    return(federal_taxable_ammount*.10)
                else:
                    return(0)
            elif federal_filling_status == 4: #Head Of House hold
                if federal_taxable_ammount > 500000.00:
                    return(((federal_taxable_ammount-500000.00)*.37)+149298.00)
                elif federal_taxable_ammount > 200000.00:
                    return(((federal_taxable_ammount-200000.00)*.35)+44298.00)
                elif federal_taxable_ammount > 157500.00:
                    return(((federal_taxable_ammount-157500.00)*.32)+30698.00)
                elif federal_taxable_ammount > 82500.00:
                    return(((federal_taxable_ammount-82500.00)*.24)+12698.00)
                elif federal_taxable_ammount > 52800.00:
                    return(((federal_taxable_ammount-52800.00)*.22)+5944.00)
                elif federal_taxable_ammount > 13600.00:
                    return(((federal_taxable_ammount-13600.00)*.12)+1360.00)
                elif federal_taxable_ammount > 0.00:
                    return(federal_taxable_ammount*.10)
                else:
                    return(0)
            else:
                print("error in filling status for federal")
                main.CRnotice()
            
    def calculate_stateTaxes(taxable_ammount):
        return (taxable_ammount * 0.052 ) 
    

    def print_taxes(ss_tax_witheld,Medicare_Tax_witheld,Federal_Tax_withheld,state_taxes_withheld,take_home_income,Gincome_ammount):
       clear()
       print("table of what will be withheld from your gross income and what you will be takeing home:")
       print("\tGross Income:",dollar(Gincome_ammount),"\nSocial Security Taxes:-",dollar(ss_tax_witheld),"\tMedicare Taxes:-",dollar(Medicare_Tax_witheld))   
       print("\tFederal Taxes:-",dollar(Federal_Tax_withheld),"\tstate taxes:-",dollar(Federal_Tax_withheld))
       total_taxes = ss_tax_witheld + Medicare_Tax_witheld + Federal_Tax_withheld + Federal_Tax_withheld
       print("total income taxes:-",dollar(total_taxes),"\tTake Home Income:",dollar(take_home_income))
       sleep(20)
       input("\npress any key to return to main menu")
       clear()

                
    def tax_calculation():
        TForm = get_bool("Is this going to be a W2 form payment calculation?")
        Gincome_ammount = income.Get_income()
        taxable_ammount = Gincome_ammount
        ss_tax_witheld = income.calculate_SSTaxes(taxable_ammount)  
        Medicare_Tax_witheld = income.calculate_MCTaxes(taxable_ammount)
        if TForm == True:
            ss_tax_witheld = ss_tax_witheld / 2
            Medicare_Tax_witheld = Medicare_Tax_witheld / 2
        

        federal_taxable_ammount = Gincome_ammount - ss_tax_witheld - Medicare_Tax_witheld
        Federal_Tax_withheld = income.calculate_federalTaxes(federal_taxable_ammount)  
        state_taxes_withheld = income.calculate_stateTaxes(taxable_ammount)
        take_home_income = Gincome_ammount - ss_tax_witheld - Medicare_Tax_witheld - Federal_Tax_withheld - state_taxes_withheld
        income.print_taxes(ss_tax_witheld,Medicare_Tax_witheld,Federal_Tax_withheld,state_taxes_withheld,take_home_income,Gincome_ammount)
        
    def Get_income():
        clear()
        HourlyIncome = get_bool("Is this an hourly rate job?")
        if HourlyIncome == True:
            clear()
            normal_time = get_float("How many hours did you work at regular time?")
            clear()
            over_time = get_float("How many hours did you work overtime?")
            clear()            
            over_time_multiplier = get_float("What is the overtime hourly pay rate multiplier? example for time and a half = 1.5")
            clear()
            hours_worked = normal_time + (over_time * over_time_multiplier)
            clear()
            hourly_pay = get_float("What is the base hourly pay rate?")
            Gincome_ammount = float(hours_worked * hourly_pay)
            return Gincome_ammount
        elif HourlyIncome == False:
            clear()
            Gincome_ammount = get_float("what is the gross income/salary rate you want to calculate?")
            return Gincome_ammount

class main: # Main menu class and other items 
    termsserviceg = config.getboolean('config','termsserviceg')
    ttry = 0

    def Filing_Status():
        list_file_status = ("1. Single filling Default","2. Married filling jointly or Widow(er)",
        "3. Married filing Seperatly","4. Head Of HouseHold","10. Cancel and quit")
        print("\n\nHello wellcome to the configs and set up of your",
        "form 1099. \n Note: The information provided is not legal advice. Please consult a lawyer.")
        LFS = False # resets if you decide to redo the form may change to a option later on.
        while LFS == False:
            clear()
            print('\n'.join(map(str, list_file_status)))   # prints list
            Federal_taxFilling = get_int("Please select how you will be filing your taxes. Note: for S.S. taxes head of household will auto convert to single filling.")
            if Federal_taxFilling == 1:
                federal_filling_status = 1
                SS_filling_status = 1
                LFS = True
            elif Federal_taxFilling == 2:
                federal_filling_status = 2
                SS_filling_status = 2
                LFS = True
            elif Federal_taxFilling == 3:                
                federal_filling_status = 3
                SS_filling_status = 3
                LFS = True  
            elif Federal_taxFilling == 4:
                federal_filling_status = 4
                SS_filling_status = 1
                LFS = True
            elif Federal_taxFilling == 10:
                exit()
            else:
                clear()
                print("\nInvalid  Entry!!! please try again thank you.")
                
        ### save configs set ###          
        print("saving please wait")
        config.set('config','federal_filling_status', federal_filling_status )
        config.set('config','SS_filling_status', SS_filling_status )
        with open('config.ini', 'w') as update_config:
            config.write(update_config)
        clear()
        print("saving please wait.....")
        sleep(3)
        clear()
        input("press any key to return to main menu.")

    def CRnotice():
        while main.termsserviceg != True and main.ttry < 4 :
            print("\t",ProgramTitle,"\n")
            print("\t",Copyright,"<",author,">\n")  
            print("\n\tCreative Commons Attribution-NonCommercial-NoDerivatives 4.0 International Public License\n")
            print("""By exercising the Licensed Rights (defined below), You accept and agree to be bound by the terms and conditions of this Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International Public License ("Public License"). To the extent this Public License may be interpreted as a contract, You are granted the Licensed Rights in consideration of Your acceptance of these terms and conditions, and the Licensor grants You such rights in consideration of benefits the Licensor receives from making the Licensed Material available under these terms and conditions.""")
            print("\n you have attempted to accept the terms",main.ttry,"times.")
            main.termsserviceg = get_bool("\n\tDo you aree with the terms of  the Copy Right? yes or no")
            main.ttry = main.ttry + 1
        else:
            if main.termsserviceg == True:
                clear()
                print("\nTerms of Copy Right has been accepted. thank you please wait")
                config.set('config','termsserviceg', main.termsserviceg )
                with open('config.ini', 'w') as update_config:
                    config.write(update_config)
                clear()
                print("saving and loading. please wait.....")
                sleep(3)
                input("press any key to go to the main menu")
                main.menu()
            else:
                clear()
                print("you have failed to accept the terms of service. the program will close now.")
                sleep(30)
                exit()

    def menu():
        Main_menu = ( "1. Set up IRS tax filling status info.","2. calculate payment taxes", "8. reset config.ini file to defaults",
        "9. CopyRight Notice", "10. Exit") #main menu
       
        while RUN == True : #menu loop
            clear()
            print("Main Menu\n")
            print('\n'.join(map(str, Main_menu))) # prints list
            target = get_int("Pick an option from the menu:")
            if target == 1:
                clear()
                main.Filing_Status()
            elif target == 2:
                clear()
                income.tax_calculation()
            elif target == 8:
                federal_filling_status = 1
                SS_filling_status = 1
                main.termsserviceg = False
                config.set('config','federal_filling_status', federal_filling_status )
                config.set('config','SS_filling_status', SS_filling_status )
                config.set('config','termsserviceg', main.termsserviceg )
                with open('config.ini', 'w') as update_config:
                    config.write(update_config)
                clear()
                print("saving configs. please wait.....")
                sleep(5)
            elif target == 9:
                clear()
                main.termsserviceg = False
                main.ttry = 0
                main.CRnotice()
            elif target == 10:
                exit()
            else:
                clear()
                print("\nInvalid  Entry!!! please try again thank you.") # catch all
    
main.CRnotice()
