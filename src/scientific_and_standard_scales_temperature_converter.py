# By Faycal Kilali 07-Mar-21, this project is covered by the GNU General Public License V3.0.

def errormessage_function():
    print("Please follow the directions in the program")
    
def abs_error():
    print("Your input temperature is below the absolute zero of %s by the Law of Thermodynamics, try plugging in a realistic temperature." % choice)
    
class Temp_conversion:
    
    def __init__(self, temperature = 0):
        self.temperature = temperature
        
    def conversion_to_celsius(self, choice):
        if choice == "Fahrenheit":
            celsius = (self.temperature - 32) * 5 / 9
        elif choice == "Kelvin":
            celsius = (self.temperature - 273.15)
        elif choice == "Rankine":
            celsius = (self.temperature - 491.67) * 5 / 9
        elif choice == "Delisle":
            celsius =  (100 - self.temperature) * 2/3 
        elif choice == "Newton":
            celsius = (self.temperature * 100 / 33)
        elif choice == "Réaumur":
            celsius =  (self.temperature) * 5 / 4
        elif choice == "Rømer":
            celsius =  (self.temperature - 7.5) * 40/21
        else:
            celsius = user_input_pt2_int
        return celsius            
    
    def conversion_from_celsius(self, celsius, convert):
            if convert == "Fahrenheit":
                return (celsius * 1.8) + 32
            elif convert == "Kelvin":
                return (celsius) + 273.15
            elif convert == "Rankine":
                return (celsius + 273.15) * 9/5
            elif convert == "Delisle":
                return (100 - celsius) * 3/2
            elif convert == "Newton":
                return celsius * 33/100
            elif convert == "Réaumur":
                return  celsius * 4/5
            elif convert == "Rømer":
                return celsius * 21/40 + 7.5
            else:
                return user_input_pt2_int
 
# Scientific absolute zero temperatures for the different temperature scales (for convenience)
abs_celsius = -273.15
abs_kelvin = 0
abs_fahrenheit = -459.67
abs_rankine = 0
abs_delisle = 559.73
abs_newton = -90.14
abs_Réaumur = -218.52
abs_Rømer = -135.90

deadend = False
while deadend == False:
    try:
        user_input = input("Input the unit of measure you would like to convert from:\n 0 for Celsius, 1 for Fahrenheit, 2 for Kelvin, 3 for Rankine, 4 for Delisle, 5 for Newton, 6 for Réaumur, 7 for Rømer: ")
        try: 
            float(user_input)
        except ValueError:
            errormessage_function()
            continue
        if len(user_input) == 0:
            errormessage_function()
            continue
        else:
            user_input_int = int(user_input)
            if user_input_int > 7 or user_input_int < 0:
                errormessage_function()
                continue
            else:
                if user_input_int == 0:
                    choice = "Celsius"
                elif user_input_int == 1:
                    choice = "Fahrenheit"
                elif user_input_int == 2:
                    choice = "Kelvin"
                elif user_input_int == 3:
                    choice = "Rankine"
                elif user_input_int == 4:
                    choice = "Delisle"
                elif user_input_int == 5:
                    choice = "Newton"
                elif user_input_int == 6:
                    choice = "Réaumur"
                elif user_input_int == 7:
                    choice = "Rømer"
                    
                user_input_pt2 = input("Plug in the %s temperature to convert it: " % choice)
                
                try:
                    float(user_input_pt2)
                except ValueError:
                    errormessage_function()
                    continue
                user_input_pt2_int = int(user_input_pt2)
                try: 
                    if choice == "Celsius" and user_input_pt2_int < abs_celsius:
                        abs_error()
                        continue
                    elif choice == "Fahrenheit" and user_input_pt2_int < abs_fahrenheit:
                        abs_error()
                        continue
                    elif choice == "Kelvin" and user_input_pt2_int < abs_kelvin:
                        abs_error()
                        continue
                    elif choice == "Rankine" and user_input_pt2_int < abs_rankine:
                        abs_error()
                        continue
                    elif choice == "Delisle" and user_input_pt2_int < abs_delisle:
                        abs_error()
                        continue
                    elif choice == "Newton" and user_input_pt2_int < abs_newton:
                        abs_error()
                        continue
                    elif choice == "Réaumur" and user_input_pt2_int < abs_Réaumur:
                        abs_error()
                        continue
                    elif choice == "Rømer" and user_input_pt2_int < abs_Rømer:
                        abs_error()
                        continue
                    else:
                        Temp_conversionObject = Temp_conversion() # Assigns the object to Temp_conversionObject
                        Temp_conversionObject.temperature = user_input_pt2_int  # Assigns the integer value of user_input_pt2_int as an attribute to the object's temperature property
                        #The code below prints all the temperature conversions, utilizing formulas based upon the user's choice of temperature (that they input)
                        celsius = Temp_conversionObject.conversion_to_celsius(choice)
                        print("Celsius: %.2f°C" % Temp_conversionObject.conversion_from_celsius(celsius, "placeholder"))
                        print("Fahrenheit: %.2f°F" % Temp_conversionObject.conversion_from_celsius(celsius, "Fahrenheit"))
                        print("Kelvin: %.2fK" % Temp_conversionObject.conversion_from_celsius(celsius, "Kelvin"))
                        print("Rankine: %.2f°R" % Temp_conversionObject.conversion_from_celsius(celsius, "Rankine"))
                        print("Delisle: %.2f°De" % Temp_conversionObject.conversion_from_celsius(celsius, "Delisle"))
                        print("Newton: %.2f°N" % Temp_conversionObject.conversion_from_celsius(celsius, "Newton"))
                        print("Réaumur: %.2f°Ré" % Temp_conversionObject.conversion_from_celsius(celsius, "Réaumur"))
                        print("Rømer: %.2f°Rø" % Temp_conversionObject.conversion_from_celsius(celsius, "Rømer"))
                except EOFError as e:
                    print(e)
                    deadend = True
    except EOFError as d:
        print(d)
        deadend = True