from verificador_de_senhas import Password

print('Type your password')

while True:
    password_entered = input(': ')

    checker_password = Password()

    if checker_password.checker(password_entered):
        if checker_password.checker_especial(password_entered):
            if checker_password.cheker_char(password_entered):
                print('Password valido')
    else:
        print('Password invalid')