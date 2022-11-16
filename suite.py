class Suite:
    
    def __init__(self, raison, first_term, first_term_value) -> None:
        self.raison = raison
        self.first_term = first_term
        self.first_term_value = first_term_value
        
class ArithmeticSuite(Suite):
    def __init__(self, raison, first_term, first_term_value) -> None:
        super().__init__(raison, first_term, first_term_value)
    
    def get_term(self, term:int):
        valid = True
        
        first_part = (term - self.first_term) * self.raison
        answer = self.first_term_value + first_part
        
        dev = ["RAPPEL DE LA FORMULE : u(n) = u(p) + r(n - p)",
                f"u({term}) = u({self.first_term}) + {self.raison} x ({term} - {self.first_term})",
                f"= {self.first_term_value} + {first_part}",
                f"= {answer}"
        ]
        return answer, dev
    
    def get_somme(self, first_ind, last_ind):
        
        term1 = self.get_term(first_ind)[0]
        term2 = self.get_term(last_ind)[0]
        totals_terms = last_ind - first_ind + 1
        first_part = (term1 + term2) / 2
        answer = totals_terms * first_part
        
        dev = ["""RAPPEL DE LA FORMULE : Somme = (nombre de termes de la somme) x (1er terme de la somme +dernier terme de la somme) / 2\n/!\ nombre de termes de la somme = indice du dernier terme de la somme - indice du dernier + 1""",
               f"Somme = ({last_ind} - {first_ind} + 1) x (({term1} + {term2}) / 2)",
               f"= {totals_terms} * {first_part}",
               f"= {answer}"
        ]
        return answer, dev
    
class GeometricalSuite(Suite):
    def __init__(self, raison, first_term, first_term_value) -> None:
        super().__init__(raison, first_term, first_term_value)
        
    def get_term(self, term:int):
        
        first_part = self.raison ** (term - self.first_term)
        answer = self.first_term_value * first_part
        
        dev = ["""RAPPEL DE LA FORMULE : u(n) = u(p) x q^(n-p)""",
            f"u({term}) = u({self.first_term}) x {self.raison}^({term} - {self.first_term})",
            f"= {self.first_term_value} x {first_part}",
            f"= {answer}"       
        ]
        return answer, dev
    
    def get_somme(self, first_ind, last_ind):
        
        term1 = self.get_term(first_ind)[0]
        multiplier = last_ind - first_ind + 1
        diviser = 1 - self.raison
        first_part = (1 - self.raison ** multiplier) / diviser
        answer = term1 * first_part
        
        dev = ["""RAPPEL DE LA FORMULE : (1er terme de la somme) x (1 - q^(nb de termes de la somme) / 1 - q)\n/!\ nombre de termes de la somme = indice du dernier terme de la somme - indice du dernier + 1""",
               f"Somme = u({first_ind}) x ((1 - {self.raison}^({last_ind} - {first_ind} + 1) / 1 - {self.raison})",
               f"= {term1} x (1 - {self.raison}^{multiplier} / {diviser})",
               f"= {term1} x {first_part}",
               f"= {answer}"
        ]
        
        return answer, dev