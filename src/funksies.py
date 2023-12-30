'''
_______________________________________________________________________________
_______________________________________________________________________________
File:       funksies.py  
Developer:  Ruimteman
Date:       12/08/2023
Description:
    Al die funksies wat ek nodig het om Who Wants to Be a Millionaire te speel    
_______________________________________________________________________________
_______________________________________________________________________________
'''

import random

def welkom_boodskap():
    """welcome message to start the program
    """

    print("Welcome at Ruimteman's Who Wants to Be a Millionaire! ")
    print("Today you stand the change to win R1'000'000 in price money.")
    print("Are you ready to play!")
    print()



def kry_vrae(vrae_lys: dict)->dict:
    """Hierdie funksie kry die random vraag en oorblywende vrae

    Args:
        vrae_lys (dict): Hierdie is die lys van vrae soos in die veranderlike in 'variebles.py'

    Returns:
        dict: Hierdie funksie gee die volgende terug:
        'gekose_vraag', 'oorblywende_vrae'
    """
    index_vraag = random.randint(0, len(vrae_lys)-1)
    verwyderde_vraag = vrae_lys.pop(index_vraag)

    # Create a new list without the randomly removed item
    oorblywende_vrae = vrae_lys[:index_vraag-1] + vrae_lys[index_vraag:]
    print()
    print("Question no.%i"%(14-len(oorblywende_vrae)))
    gekose_vraag = vrae_lys[index_vraag-1]
    antwoord = vrae_lys[index_vraag-1]["answer"]
    opsies = vrae_lys[index_vraag-1]["options"]
    gekose_vraag["posisie"] = opsies.index(antwoord) 

    return gekose_vraag, oorblywende_vrae

def print_vraag_en_opsies(gekose_vraag: str)->None:
    """Print vraag en opsies

    Args:
        gekose_vraag (str): Str met vraag inligting - gekose_vraag["question"], gekose_vraag["options"]
    """

    print(gekose_vraag["question"])
    for index, i in enumerate(gekose_vraag["options"], start=1):
        print(f"{index}. {i}")


def antwoord_vraag(gekose_vraag:str)->int:
    """nou gaan die gebruiker die vraag antwoord

    Args:
        gekose_vraag (str): Str met vraag inligting

    Returns:
        int: 1 = gewen, 0 = verloor
    """
    opsies = gekose_vraag["options"]
    antwoord = gekose_vraag["answer"]
    answer_position: int = opsies.index(antwoord)
    while True:
        gekiesde_antwoord = int(input("The answer is: "))
        seker = input("Are you sure about your answer? (y/n)").lower()
        if seker == "y":
            break

    if gekiesde_antwoord - 1 == answer_position:
        return 1
    else:
        return 0

def kies_hulpmiddel(gekose_vraag: str, hulpmiddel_lys:str):
    """Kies 'n hulp middel om te help om die vraag te antwoord

    Args:
        vraag_inligting (str): Str met vraag inligting
        hulpmiddel_lys (str): Str met hulpmiddel inligting
    """
    phone_responses = gekose_vraag["phone me"]
    random_index = random.randint(0, len(gekose_vraag["phone me"]))
    random_phone_a_friend = phone_responses[random_index-1]

    opsies = gekose_vraag["options"]
    antwoord = gekose_vraag["answer"]
    answer_position: int = opsies.index(antwoord)

    ##################### bou check in om te kyk of daar nog geldige hulpmiddel oor is om van te kies, ander
    ##################### skryf boodskap dat jou kans klaar is, en jy nou moet antwoord, BREAK
    
    while True:
        if "1. Phone a friend" in hulpmiddel_lys or "2. 50/50" in hulpmiddel_lys or "3. Audiance" in hulpmiddel_lys:
            for element in hulpmiddel_lys:
                print(element)
            hulpmiddel = input("Choice a live line:")

            if hulpmiddel == "1" and "1. Phone a friend" in hulpmiddel_lys:
                # Phone a friend
                print(random_phone_a_friend)
                for i in range(3):
                    hulpmiddel_lys[i] = hulpmiddel_lys[i].replace("1. Phone a friend", "1. ----")
                break
            
            elif hulpmiddel == "2"and "2. 50/50" in hulpmiddel_lys:
                # 50/50
                for a in range(2):
                    rand_no1 = -1
                    while True:
                        random_no = random.randint(0, 3)
                        if random_no != answer_position and rand_no1 != random_no:
                            rand_no1 = random_no
                            gekose_vraag["options"][random_no] = "-----------"
                            break
            
                for i in range(3):
                    hulpmiddel_lys[i] = hulpmiddel_lys[i].replace("2. 50/50", "2. ----")
                break

            elif hulpmiddel == "3"and "3. Audiance" in hulpmiddel_lys:
                # Gehoor
                rand = []
                sum_rand_getal = 0
                if "2. 50/50" in hulpmiddel_lys:
                    for v in range(4):
                        rand_getal = random.randint(1, 10)
                        sum_rand_getal += rand_getal
                        rand.append(rand_getal)
                    for d in range(4):
                        print(int(rand[d]/sum_rand_getal*100))
                
                else:
                    for v in range(2):
                        rand_getal = random.randint(1, 10)
                        sum_rand_getal += rand_getal
                        rand.append(rand_getal)
                    for d in range(2):
                        print(int(rand[d]/sum_rand_getal*100))


                for i in range(3):
                    hulpmiddel_lys[i] = hulpmiddel_lys[i].replace("3. Audiance", "3. ----")
                break
            else:
                print("%s is not a valid option!"%(hulpmiddel))              
        else:
            print("All of your live lines are used up!")
            break
    return gekose_vraag, hulpmiddel_lys



def kies_opsie(gekose_vraag, hulpmiddel_lys):   
    """kies tussen twee opsies, 1) antwoord vraag , en 2) kies n hulpmiddel

    Args:
        gekose_vraag (str): gekose vraag se besonderhede
        hulpmiddel_lys (str): lys van al die oorblywende hulpmiddels

    Returns:
        list(int, str): gewen_of_nie, hulpmiddel_lys
    """
    while True:
        opgehou = 0
        gewen_of_nie = 0
        keuse = int(input("Do you want to answer the question(1), use a life line(2) or bank your money(3):"))
        if keuse == 1:   # As jy direk die vraag wil antwoord
            gewen_of_nie = antwoord_vraag(gekose_vraag)
            return gewen_of_nie, hulpmiddel_lys, opgehou

        elif keuse == 2:    # As jy 'n hulpmiddel soek
            gekose_vraag, hulpmiddel_lys = kies_hulpmiddel(gekose_vraag, hulpmiddel_lys)
        
        elif keuse == 3: # Bank jou geld
            gewen_of_nie = 1
            opgehou = 1
            return gewen_of_nie, hulpmiddel_lys, opgehou 
        else:
            print("%s is not a valid option!"%(keuse))
            break

        print_vraag_en_opsies(gekose_vraag)



   



