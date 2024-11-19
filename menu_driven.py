temperature_data = [65, 112, 76, 54, 59, 92, 82]
ph_data = [8.2, 6.3, 7.6, 5.9, 8.2, 4.9, 6.8]
# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit_data):
    return [(5/9) * (temp - 32) for temp in fahrenheit_data]

# Function to classify soil pH values
def classify_soil_ph(ph_data):
    neutral = []
    alkaline = []
    acidic = []
    
    for ph in ph_data:
        if 6.5 <= ph <= 7.5:
            neutral.append(ph)
        elif ph > 7.5:
            alkaline.append(ph)
        else:
            acidic.append(ph)
    
    return neutral, alkaline, acidic

# Menu driven program
def menu():
   
    while True:
        print("\nSmart Apple Farm Menu:")
        print("1. Convert temperature data from Fahrenheit to Celsius")
        print("2. Classify soil pH data into neutral, alkaline, and acidic")
        print("3. Exit")
        choice = int(input("Enter your choice (1-3): "))
        
        if choice == 1:
            celsius_data = fahrenheit_to_celsius(temperature_data)
            print("Temperature data in Celsius:", celsius_data)
        
        elif choice == 2:
            neutral, alkaline, acidic = classify_soil_ph(ph_data)
            print("Neutral pH values:", neutral)
            print("Alkaline pH values:", alkaline)
            print("Acidic pH values:", acidic)
        
        elif choice == 3:
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please choose a valid option.")

# Run the menu
menu()