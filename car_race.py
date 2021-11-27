command = ''
started = False
while True:
    command = input('> ').lower()
    if command == 'help':
        print('''start - to start car
stop - to stop car
quit - to exit race''')
    elif command == 'start':
        if started:
            print('car is already started')
        else:
            started = True
            print('car started ...')
    elif command == 'stop':
        if not started:
            print('Car is already stopped')
        else:
            started = False
            print('car stopped ...')
    elif command == 'quit':
        break
    else:
        print('Invalid. Try again ...')
