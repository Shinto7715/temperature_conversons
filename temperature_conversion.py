unit_of_temp = input("Is the temperature in Celsius or Farenheight? (C / F): ")
temp = float(input("Please enter the temperature: "))

if unit_of_temp == "C":
  temp = round((temp * (9 / 5)) + 32, 2)
  print(f"The temperature is {temp} deggrees F.")

elif unit_of_temp == "F":
  temp = round((temp - 32) * (5/9), 2)
  print(f"The temperature is {temp} degrees C.")

else:
  print(f"{unit_of_temp} is not a valid option")