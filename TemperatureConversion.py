#!/usr/bin/env python3

# This is a pactice file for temperature conversion in Python.
# This program will demonstrate the input and print functions.
# It will also demonstrate the use of variables and mathematical expressions.

# Convert Fahrenheit to Celsius
def farenheit_to_celsius(temperature):
    return (temperature - 32) * 5 / 9

# Convert Celsius to Fahrenheit
def celsius_to_farenheit(temperature):
    return (temperature * 9 / 5) + 32

# Convert Kelvin to Celsius
def kelvin_to_celsius(temperature):
    return temperature - 273.15

# Convert Celsius to Kelvin
def celsius_to_kelvin(temperature):
    return temperature + 273.15

def conversion():
    print("Welcome to the Temperature Conversion Program!")
    print("This program will convert temperatures between Fahrenheit, Celsius, and Kelvin.")
    input_temp = (input("What is temperature do you want to convert?: "))
    input_unit = input("What is the unit of the temperature you entered? (F, C, K)?: ").strip().upper()
    output_unit = input("What unit do you want to convert to? (F, C, K)?: ").strip().upper()
    try:
        input_temp = float(input_temp)
        
        if input_unit == 'F':
            
            if output_unit == 'C':
                converted_temp = farenheit_to_celsius(input_temp)
                print(f"{input_temp}°F is {converted_temp:.2f}°C")
            
            elif output_unit == 'K':
                converted_temp = celsius_to_kelvin(farenheit_to_celsius(input_temp))
                print(f"{input_temp}°F is {converted_temp:.2f}K")
            
            else:
                print("Invalid output unit.")
        
        elif input_unit == 'C':
           
            if output_unit == 'F':
                converted_temp = celsius_to_farenheit(input_temp)
                print(f"{input_temp}°C is {converted_temp:.2f}°F")
           
            elif output_unit == 'K':
                converted_temp = celsius_to_kelvin(input_temp)
                print(f"{input_temp}°C is {converted_temp:.2f}K")
            
            else:
                print("Invalid output unit.")
        
        elif input_unit == 'K':
            
            if output_unit == 'C':
                converted_temp = kelvin_to_celsius(input_temp)
                print(f"{input_temp}K is {converted_temp:.2f}°C")
            
            elif output_unit == 'F':
                converted_temp = celsius_to_farenheit(kelvin_to_celsius(input_temp))
                print(f"{input_temp}K is {converted_temp:.2f}°F")
            
            else:
                print("Invalid output unit.")
        
        elif input_unit not in ['F', 'C', 'K'] or output_unit not in ['F', 'C', 'K']:
            print("Invalid input. Please enter F, C, or K for temperature units.")
        
        elif input_unit == output_unit:
            print(f"The temperature is already in {input_unit}. No conversion needed.")
        
        elif input_temp < 0 and input_unit == 'K':
            print("Kelvin cannot be negative. Please enter a valid temperature.")
        
        elif input_temp < -273.15 and input_unit == 'C':
            print("Celsius cannot be below absolute zero. Please enter a valid temperature.")
        
        elif input_temp < -459.67 and input_unit == 'F':
            print("Fahrenheit cannot be below absolute zero. Please enter a valid temperature.")
        
        else:
            print("Invalid input. Please try again.")
    
    except ValueError:
        print("Invalid temperature input. Please enter a numeric value.")

if __name__ == "__main__":
    conversion()
    print("Thank you for using the Temperature Conversion Program!")
