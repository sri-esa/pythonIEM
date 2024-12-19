import matplotlib.pyplot as plt

def convert_temperature(value, unit):
    if unit.upper() == 'C':
        celsius = value
        fahrenheit = (value * 9/5) + 32
        kelvin = value + 273.15
    elif unit.upper() == 'F':
        celsius = (value - 32) * 5/9
        fahrenheit = value
        kelvin = celsius + 273.15
    elif unit.upper() == 'K':
        celsius = value - 273.15
        fahrenheit = (celsius * 9/5) + 32
        kelvin = value
    else:
        raise ValueError("Invalid unit! Use 'C', 'F', or 'K'.")
    return celsius, fahrenheit, kelvin

def plot_temperature_conversion(start, end, unit):
    temperatures = range(start, end + 1)
    c_values, f_values, k_values = [], [], []

    for temp in temperatures:
        c, f, k = convert_temperature(temp, unit)
        c_values.append(c)
        f_values.append(f)
        k_values.append(k)

    plt.figure(figsize=(10, 6))
    plt.plot(temperatures, c_values, label="Celsius", color="blue")
    plt.plot(temperatures, f_values, label="Fahrenheit", color="red")
    plt.plot(temperatures, k_values, label="Kelvin", color="green")
    plt.title(f"Temperature Conversion from {unit.upper()}")
    plt.xlabel(f"Input Temperature ({unit.upper()})")
    plt.ylabel("Converted Temperatures")
    plt.legend()
    plt.grid()
    plt.show()

# Main Program
try:
    value = float(input("Enter the temperature value: "))
    unit = input("Enter the unit (C, F, or K): ").strip()

    celsius, fahrenheit, kelvin = convert_temperature(value, unit)
    print(f"Temperature in Celsius: {celsius:.2f} °C")
    print(f"Temperature in Fahrenheit: {fahrenheit:.2f} °F")
    print(f"Temperature in Kelvin: {kelvin:.2f} K")

    plot = input("Do you want to plot the temperature conversion graph? (yes/no): ").strip().lower()
    if plot == "yes":
        start = int(input(f"Enter the starting temperature in {unit.upper()}: "))
        end = int(input(f"Enter the ending temperature in {unit.upper()}: "))
        plot_temperature_conversion(start, end, unit)
except ValueError as e:
    print(e)
