# step 1. asks the user for a temperature in Fahrenheit degrees and reads the number
number = float(input("please enter Fahrenheit temperature: "))

# step 2. computes the correspodning temperature in Celsius degrees
number = (number - 32.0) * 5.0 / 9.0

# step 3. prints out the temperature in the Celsius scale.
print("Celsius temperature is %f"%(number))