numToConvert = int(input('What number do you want to convert ? : '))
print('\n')

listOfTypes = ['bin', 'oct', 'hex']

conversionType = input(f'Convert to ? {listOfTypes}: ')
print('\n')

if conversionType == 'bin':
    print(f'The answer is {bin(numToConvert)}')
elif conversionType == 'oct':
    print(f'The answer is {oct(numToConvert)}')
elif conversionType == 'hex':
    print(f'The answer is {hex(numToConvert)}')
else:
    print('Invalid conversion type')