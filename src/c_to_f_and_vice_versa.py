class Celsius:
    
    def __init__(self, temperature = 0):
        self.temperature = temperature
    
    def conversion_to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

def errormessage_function():
    print("Please follow the directions in the program")
    
deadend = False
while deadend == False:
    try:
        user_input = input("To convert from Celsius to Fahrenheit input in 0, for the other way around input in 1: ")
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
            if user_input_int > 1 or user_input_int < 0:
                errormessage_function()
                continue
            else:
                if user_input_int == 1:
                    choice = "Fahrenheit"
                elif user_input_int == 0:
                    choice = "Celsius"
                user_input_pt2 = input("Plug in the %s temperature to convert it: " % choice)
                try:
                    float(user_input_pt2)
                except ValueError:
                    errormessage_function()
                    continue

                user_input_pt2_int = int(user_input_pt2)
            CelsiusObject = Celsius()
            CelsiusObject.temperature = user_input_pt2_int
            print("Celsius: %.2f" % CelsiusObject.temperature)
            print("Fahrenheit: %.2f" % CelsiusObject.conversion_to_fahrenheit())

    except EOFError as e:
        print(e)
        deadend = True
