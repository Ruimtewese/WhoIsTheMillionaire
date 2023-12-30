'''
_______________________________________________________________________________
_______________________________________________________________________________
File:       funksies.py  
Developer:  Ruimteman
Date:       12/08/2023
Description:
    Who Wants to Be a Millionaire game   
_______________________________________________________________________________
_______________________________________________________________________________
'''

from src.funksies import *
from src.variables import *

#-------------START OF MY PROGRAM------------
welkom_boodskap()


#-------------INDIVIDUAL QUESTION------------
vraag_no = -1
gekose_vraag, oorblywende_vrae = kry_vrae(vrae_lys) 
min_money = millionaire_money[0]
while True:
    vraag_no += 1
    gewen_of_nie = 0
    print_vraag_en_opsies(gekose_vraag)  # Print vraag en opsies
    gewen_of_nie, hulpmiddel_lys, opgehou = kies_opsie(gekose_vraag, hulpmiddel_lys)  # maak n vraag en/of hulpmiddel keuse

    if opgehou == 1:
          print("You have won %s!"%(millionaire_money[vraag_no]))
          exit()

    if gewen_of_nie == 1 and vraag_no == 4:
        #-----------------------sit nuwe vashaak plek hier im-----------------
        # Jy sal 'n variable moet inbou wat die vashaak bedrag is, indien die gebruik verkeerd raai 
        # voor hierdie punt, verloor hulle alles tot op die punt
        min_money = millionaire_money[5]
          
    elif gewen_of_nie == 1 and vraag_no == 9:
        #-----------------------sit nuwe vashaak plek hier im-----------------
        # Jy sal 'n variable moet inbou wat die vashaak bedrag is, indien die gebruik verkeerd raai 
        # voor hierdie punt, verloor hulle alles tot op die punt
        min_money = millionaire_money[10]
          
    elif gewen_of_nie == 1 and vraag_no < 15:
            print("Your answer is correct!")
            print("Now you are guaranteed %s!"%(millionaire_money[vraag_no+1]))
            print("You can now move on to the next question.")
            gekose_vraag, oorblywende_vrae = kry_vrae(oorblywende_vrae) 

            

    elif gewen_of_nie == 1 and vraag_no == 15:
        print("You have won $1 000 000!")
        break
    
    elif gewen_of_nie != 1:
        print("Your answer is incorrect!")
        print("But don't worry, you still get %s!"%(min_money))
        exit()
    
    
