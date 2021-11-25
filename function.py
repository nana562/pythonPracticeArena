def greet_user(first_name, last_name):  # parameter
    print(f'Hi {first_name} {last_name}')
    print('Welcome on board')


print('start')
greet_user('Gideon', 'Opoku')  # positional argument
greet_user(last_name="Opoku", first_name="Gideon")  # keyword argument - improves readability of code
print('finish')
