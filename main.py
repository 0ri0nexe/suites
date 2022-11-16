from suite import ArithmeticSuite

import questionary

def question(message:str):
    return questionary.text(message).ask()  

def create_suite():
    print("------------- NOUVELLE SUITE -------------")
    valid = False
    while not valid:
        try:
            suite_type = questionary.select(
            "Quel est le genre de la suite ?",
            choices=[
                "arithmétique",
                "géométrique"
            ]).ask()
            
            first_term = int(question("quel est l'indice du premier terme ? (u...)"))
            
            first_term_value = int(question(f"quel est la valeur du premier terme ? u({first_term})"))
            
            if suite_type == "arithmétique":
                raison = int(question("r ="))
                return ArithmeticSuite(raison, first_term, first_term_value)
            else:
                raison = int(question("q ="))
            valid = True    
        except ValueError:
            print("merci de mettre une valeure numérique.")

def dev_menu(dev):
    response = questionary.select(
    "Que voulez-vous faire ? ?",
    choices=[
        "Afficher le développement",
        "Revenir au panel de gestion de la suite"
    ]).ask()
    if response == "Afficher le développement":
        for i, step in enumerate(dev, start=1):
            print(i, ") ", step, sep="")
    return

running = True
created = False

while running:
    
    if not created:
        suite = create_suite()
        created = True
    
    response = questionary.select(
    "Que voulez-vous ?",
    choices=[
        "terme d'indice u...",
        "Somme",
        "Nouvelle suite",
        "Stop"
    ]).ask()
    
    if response == "terme d'indice u...":
        valid = False
        while not valid:
            try:
                indice = int(question("terme d'indice :"))
                valid = True
            except ValueError:
                print("merci de mettre une valeure valide.")
        
        answer, dev = suite.get_term(indice)
        print(f"Le terme u({indice}) =", answer)
        dev_menu(dev)
    
    elif response == "Stop":
        raise(SystemError("Program stoped"))
    
    elif response == "Nouvelle suite":
        created = False
        
    else:
        valid = False
        while not valid:
            try:
                first_indice = int(question("Indice du premier terme de la somme :"))
                last_indice = int(question("Indice du dernier terme de la somme :"))
                
                if not first_indice >= suite.get_first_term():
                    print("merci de mettre un indice suppérieur à celui du premier terme de la liste.")
                    
                elif not last_indice >= first_indice:
                    print("merci de respecter la condition Indice du premier terme de la somme < ou = au dernier terme de la somme.")
                else:
                    answer, dev = suite.get_somme(first_indice, last_indice)
                    print(f"Somme des indices allant de {first_indice} à {last_indice} = {answer}")
                    dev_menu(dev)
                valid = True
            except ValueError:
                print("merci de ne mettre que des valeures numériques.")
            
