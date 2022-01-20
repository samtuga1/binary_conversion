def conversion_process():
    num_to_convert = int(input('What number do you want to convert ? : '))
    print('\n')

    list_of_types = ['bin', 'oct', 'hex']

    conversion_type = input(f'Convert to ? {list_of_types}: ')
    print('\n')

    if conversion_type == 'bin':
        print(f'The answer is {bin(num_to_convert)}')
        print('\n')
    elif conversion_type == 'oct':
        print(f'The answer is {oct(num_to_convert)}')
        print('\n')
    elif conversion_type == 'hex':
        print(f'The answer is {hex(num_to_convert)}')
        print('\n')
    else:
        print('Invalid conversion type')
    restart_process = input('Do you want to re-run the code again? y/n : ')
    print('\n')
    if restart_process == 'y':
        conversion_process()
    elif restart_process == 'n':
        quit()


conversion_process()