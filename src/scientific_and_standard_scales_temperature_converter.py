#   License and Author
__author__ = "Faycal Kilali"
__copyright__ = "Copyright (C) 2021 Faycal Kilali"
__license__ = "\nGNU GENERAL PUBLIC LICENSE"
__license_version__ = "3.0"

#   Purpose and version of program
purpose = "This program converts to multiple different temperature scales using an input from any of the temperature scales."
__version__ = "\nProgram Version: 1.1"

#   Display purpose and version, license and version of license.
print(purpose, __version__)
print(__copyright__, __license__, __license_version__)

def errormessage_function():
    print("Please follow the directions in the program")
    
def abs_error():
    print("Your input temperature is below the absolute zero of %s by the Law of Thermodynamics, try plugging in a realistic temperature." % choice)
    
class Temp_conversion:
    
    def __init__(self, temperature = 0):
        self.temperature = temperature
        
    def conversion_to_celsius(self, choice):
        if   choice == "Fahrenheit":
                celsius = (self.temperature - 32) * 5 / 9
        elif choice == "Kelvin":
                celsius = self.temperature - 273.15
        elif choice == "Rankine":
                celsius = (self.temperature - 491.67) * 5 / 9
        elif choice == "Delisle":
                celsius =  100 - self.temperature * 2/3 
        elif choice == "Newton":
                celsius = self.temperature * 100 / 33
        elif choice == "Reaumur":
                celsius =  self.temperature * 5 / 4
        elif choice == "Romer":
                celsius =  (self.temperature - 7.5) * 40/21
        elif choice == "Celsius":
                celsius = (self.temperature) # When Celsius is standardized unit, switch this to kelvin later honestly
        else: 
            print("Conversion failed, argument match not found")
        return celsius # Return Kelvin later once I make Kelvin the standard unit of measure
    
    def conversion_from_celsius(self, celsius, convert):
            if convert == "Fahrenheit":
                return celsius * 9/5 + 32
            elif convert == "Kelvin":
                return celsius + 273.15
            elif convert == "Rankine":
                return (celsius + 273.15) * 9/5
            elif convert == "Delisle":
                return (100 - celsius) * 3/2
            elif convert == "Newton":
                return celsius * 33/100
            elif convert == "Reaumur":
                return  celsius * 4/5
            elif convert == "Romer":
                return celsius * 21/40 + 7.5
            else:
                print("Error encountered, convert argument match not found")
            
# Scientific absolute zero temperatures for the different temperature scales (for convenience)
abs_celsius = -273.15
abs_kelvin = 0
abs_fahrenheit = -459.67
abs_rankine = 0
abs_delisle = 559.73
abs_newton = -90.14
abs_Reaumur = -218.52
abs_Romer = -135.90

deadend = False
while deadend == False:
    try:
        user_input = input("Input the unit of measure you would like to convert from.\n0 for Celsius, 1 for Fahrenheit, 2 for Kelvin, 3 for Rankine, 4 for Delisle, 5 for Newton, 6 for Reaumur, 7 for Romer: ")
        try: 
            float(user_input)
        except ValueError:
            errormessage_function()
            continue
        if len(user_input) == 0:
            errormessage_function()
            continue
        else:
            user_input_float = float(user_input)
            if user_input_float not in range(0,8):
                errormessage_function()
                continue
            else:
                if user_input_float == 0:
                    choice = "Celsius"
                elif user_input_float == 1:
                    choice = "Fahrenheit"
                elif user_input_float == 2:
                    choice = "Kelvin"
                elif user_input_float == 3:
                    choice = "Rankine"
                elif user_input_float == 4:
                    choice = "Delisle"
                elif user_input_float == 5:
                    choice = "Newton"
                elif user_input_float == 6:
                    choice = "Reaumur"
                elif user_input_float == 7:
                    choice = "Romer"
                    
                user_input_pt2 = input("Plug in the %s temperature to convert it: " % choice)
                
                try:
                    float(user_input_pt2)
                except ValueError:
                    errormessage_function()
                    continue
                user_input_pt2_float = float(user_input_pt2)
                try: 
                    if choice == "Celsius" and user_input_pt2_float < abs_celsius:
                        abs_error()
                        continue
                    elif choice == "Fahrenheit" and user_input_pt2_float < abs_fahrenheit:
                        abs_error()
                        continue
                    elif choice == "Kelvin" and user_input_pt2_float < abs_kelvin:
                        abs_error()
                        continue
                    elif choice == "Rankine" and user_input_pt2_float < abs_rankine:
                        abs_error()
                        continue
                    elif choice == "Delisle" and user_input_pt2_float > abs_delisle:
                        abs_error()
                        continue
                    elif choice == "Newton" and user_input_pt2_float < abs_newton:
                        abs_error()
                        continue
                    elif choice == "Reaumur" and user_input_pt2_float < abs_Reaumur:
                        abs_error()
                        continue
                    elif choice == "Romer" and user_input_pt2_float < abs_Romer:
                        abs_error()
                        continue
                    else:
                        Temp_conversionObject = Temp_conversion() # Assigns the object to Temp_conversionObject
                        Temp_conversionObject.temperature = user_input_pt2_float  # Assigns the integer value of user_input_pt2_float as an attribute to the object's temperature property
                        #The code below prints all the temperature conversions, utilizing formulas based upon the user's choice of temperature (that they input)
                        celsius = Temp_conversionObject.conversion_to_celsius(choice)
                        print("Celsius: %.2f°C" % celsius)
                        print("Fahrenheit: %.2f°F" % Temp_conversionObject.conversion_from_celsius(celsius, "Fahrenheit"))
                        print("Kelvin: %.2fK" % Temp_conversionObject.conversion_from_celsius(celsius, "Kelvin"))
                        print("Rankine: %.2f°R" % Temp_conversionObject.conversion_from_celsius(celsius, "Rankine"))
                        print("Delisle: %.2f°De" % Temp_conversionObject.conversion_from_celsius(celsius, "Delisle"))
                        print("Newton: %.2f°N" % Temp_conversionObject.conversion_from_celsius(celsius, "Newton"))
                        print("Reaumur: %.2f°Ré" % Temp_conversionObject.conversion_from_celsius(celsius, "Reaumur"))
                        print("Romer: %.2f°Rø" % Temp_conversionObject.conversion_from_celsius(celsius, "Romer"))
                except EOFError as e:
                    print(e)
                    deadend = True
    except EOFError as d:
        print(d)
        deadend = True