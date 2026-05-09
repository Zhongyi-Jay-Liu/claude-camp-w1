# Temperatore converter between Celsius and Fahrenheit
def main():

# Get user input for temperature and unit
    
# Check if the input is valid if not float will raise an error and if the unit is not C or F it will print invalid unit
    try:
        temp = float(input("Enter the temperature: "))
        unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").upper().strip()
        if unit == 'C':
            converted_temp = (temp * 9/5) + 32
            print(f"{temp}°C is equal to {converted_temp:.2f}°F")
        elif unit == 'F':
            converted_temp = (temp - 32) * 5/9
            print(f"{temp}°F is equal to {converted_temp:.2f}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")            
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

main()