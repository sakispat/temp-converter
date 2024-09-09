def celsius_to_fahrenheit(celsius):
    temp_cels = (celsius * 9 / 5) + 32
    return temp_cels


def fahrenheit_to_celsius(fahrenheit):
    temp_fah = (fahrenheit - 32) * 5 // 9
    return temp_fah


print("Convert from:\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius")
choice = input("Choose an option: ")

match choice:
    case '1':
        celsius = float(input("Enter temperature in Celsius: "))
        print(f'{ celsius }°C is equal to { celsius_to_fahrenheit(celsius) }°F')
    case '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f'{ fahrenheit }°F is equal to { fahrenheit_to_celsius(fahrenheit) }°C')
    case _:
        print('Invalid choice, please try again.')
