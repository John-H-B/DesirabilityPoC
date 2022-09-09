from classes import Combined_Desirability
import ast

cd = Combined_Desirability()
cont = True
while cont:
    values = input(f'Type a comma seperated set of values or end')
    if values == 'end':
        cont = False
    else:
        values = ast.literal_eval(values)
        print(f'desirability is {cd.get_desirability(values)}')
        print('I am sorry, I do not know that one!')
print(f'save_string: {cd.get_quick_setup()} ')
