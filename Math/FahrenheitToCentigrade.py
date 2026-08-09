# Run: python FahrenheitToCentigrade.py

def fahrenheit_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.
    Formula: C = (F - 32) * 5 / 9
    """
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def main():
    print("--- Fahrenheit to Celsius Converter ---")
    
    try:
        # Get input from the user
        temp_f = float(input("Enter temperature in Fahrenheit: "))
        
        # Calculate conversion
        temp_c = fahrenheit_to_celsius(temp_f)
        
        # Display output formatted to 2 decimal places
        print(f"{temp_f:.2f}°F is equal to {temp_c:.2f}°C")
        
    except ValueError:
        print("Error: Please enter a valid numerical value.")

if __name__ == "__main__":
    main()