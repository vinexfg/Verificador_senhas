from verificador_de_senhas import verificador_de_senhas


print('type your passaword')
passaword_entered = input(': ')

checker_passaword = verificador_de_senhas.Password()

if checker_passaword.checker(passaword_entered):
    if checker_passaword.checker_especial(passaword_entered):
        print('Passaword valid')
    else:
        print('Passaword invalid')

