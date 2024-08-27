class Password:
    def __init__(self):
        self.caracteres_permitidos = 25
        self.minimo_caracteres = 6
        self.caracteres_necessarios = ['!', '@', '#', '%', '&', '*']
        
    def checker(self, password):
        if len(password) > self.caracteres_permitidos:
            print('Máximo de caracteres atingido')
            return False
        elif len(password) < self.minimo_caracteres:
            print('A senha deve ter no mínimo 6 caracteres')
            return False
        else:
            return True
        
    def checker_especial(self, password):
        if not any(char in password for char in self.caracteres_necessarios):
            print('A senha deve conter pelo menos um caractere especial: !, @, #, %, &, *')
            return False
        return True

    def cheker_char(self, password):
        if any(char.isupper() for char in password):
            return True
        else:
            return False
        