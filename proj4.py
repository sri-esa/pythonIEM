import random
import string
import matplotlib.pyplot as plt

# Function to generate OTP
def generate_otp(length, alphanumeric=True):
    if alphanumeric:
        characters = string.ascii_letters + string.digits  # Alphanumeric characters
    else:
        characters = string.digits  # Only numeric characters
    
    otp = ''.join(random.choice(characters) for _ in range(length))
    return otp

# Function to plot OTP length statistics
def plot_otp_lengths(lengths):
    unique_lengths = list(set(lengths))
    frequency = [lengths.count(length) for length in unique_lengths]

    plt.figure(figsize=(8, 6))
    plt.bar(unique_lengths, frequency, color='blue')
    plt.xlabel("OTP Length")
    plt.ylabel("Frequency")
    plt.title("Frequency of OTP Lengths Generated")
    plt.xticks(unique_lengths)
    plt.grid(axis='y')
    plt.show()

# Main Program
if __name__ == "__main__":
    print("Welcome to the OTP Generator Application!")
    generated_otps = []  # List to store generated OTPs
    otp_lengths = []     # List to store OTP lengths for statistics

    while True:
        try:
            otp_length = int(input("\nEnter the desired OTP length (e.g., 4, 6): "))
            otp_lengths.append(otp_length)

            otp_type = input("Do you want an alphanumeric OTP? (yes/no): ").strip().lower()
            alphanumeric = True if otp_type == 'yes' else False

            # Generate OTP
            otp = generate_otp(otp_length, alphanumeric)
            generated_otps.append(otp)

            print(f"Your Generated OTP: {otp}")

            # Ask user if they want to generate another OTP
            another = input("Do you want to generate another OTP? (yes/no): ").strip().lower()
            if another != "yes":
                break
        except ValueError:
            print("Invalid input! Please enter a positive integer for OTP length.")

    # Display all generated OTPs
    print("\nAll Generated OTPs:")
    for i, otp in enumerate(generated_otps, start=1):
        print(f"OTP {i}: {otp}")

    # Ask if the user wants to visualize statistics
    visualize = input("\nDo you want to visualize OTP length statistics? (yes/no): ").strip().lower()
    if visualize == "yes":
        plot_otp_lengths(otp_lengths)
