#   Purpose and version of program
__purpose__ = "This program converts to multiple different temperature scales using an input from any of the temperature scales."
__version__ = "Program Version: 1.2"

#   License and Author
__author__ = "Faycal Kilali"
__copyright__ = "Copyright (C) 2021 Faycal Kilali"
__license__ = "GNU GENERAL PUBLIC LICENSE"
__license_version__ = "3.0"

#   Display purpose and version, license and version of license.
print(__purpose__, "\n", __version__)
print(__copyright__, "\n", __license__, __license_version__, "\n")

# Importing exit implementation
from exit_with_q_module import quit_program

def DisplayError(ErrorNumber):
    if ErrorNumber == 0:
        print("Please follow the directions in the program")
    elif ErrorNumber == 1:
        print(
            "Your input temperature is below the absolute zero of %s by the Law of Thermodynamics, try plugging in a realistic temperature."
            % choice
        )
    else:
        pass

class Temp_conversion:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_kelvin(self, choice):
        switcher_to_kelvin = {
            "Celsius": self.temperature + 273.15,
            "Fahrenheit": (self.temperature + 459.67) * 5 / 9,
            "Kelvin": self.temperature,
            "Rankine": self.temperature * 5 / 9,
            "Delisle": 373.15 - self.temperature * 2 / 3,
            "Newton": self.temperature * 100 / 33 + 273.15,
            "Reaumur": self.temperature * 5 / 4 + 273.15,
            "Romer": (self.temperature - 7.5) * 40 / 21 + 273.15,
        }
        return switcher_to_kelvin.get(choice, "Invalid temperature scale")

    def from_kelvin(self, kelvin, convert):
        switcher_from_kelvin = {
            "Celsius": kelvin - 273.15,
            "Fahrenheit": kelvin * 9 / 5 - 459.67,
            "Rankine": kelvin * 9 / 5,
            "Delisle": (373.15 - kelvin) * 3 / 2,
            "Newton": (kelvin - 273.15) * 33 / 100,
            "Reaumur": (kelvin - 273.15) * 4 / 5,
            "Romer": (kelvin - 273.15) * 21 / 40 + 7.5,
        }
        return switcher_from_kelvin.get(convert, "Invalid temperature input")


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
    user_input = input(
        "Input the unit of measure you would like to convert from.\n0 for Celsius, 1 for Fahrenheit, 2 for Kelvin, 3 for Rankine, 4 for Delisle, 5 for Newton, 6 for Reaumur, 7 for Romer: "
    )
    if user_input == "q":
        quit_program()
    try:
        float(user_input)
    except ValueError:
        DisplayError(0)
        continue
    if len(user_input) == 0:
        DisplayError(0)
        continue
    else:
        user_input_float = float(user_input)
        if user_input_float not in range(0, 8):
            DisplayError(0)
            continue
        else:
            switcher = {
                0: "Celsius",
                1: "Fahrenheit",
                2: "Kelvin",
                3: "Rankine",
                4: "Delisle",
                5: "Newton",
                6: "Reamur",
                7: "Romer",
            }
            choice = switcher.get(user_input_float)
            user_input_pt2 = input(
                "Plug in the %s temperature to convert it: " % choice
            )
            if user_input_pt2 == "q":
                quit_program()
            try:
                float(user_input_pt2)
            except ValueError:
                DisplayError(0)
                continue
            user_input_pt2_float = float(user_input_pt2)
            if choice == "Celsius" and user_input_pt2_float < abs_celsius:
                DisplayError(1)
                continue
            elif choice == "Fahrenheit" and user_input_pt2_float < abs_fahrenheit:
                DisplayError(1)
                continue
            elif choice == "Kelvin" and user_input_pt2_float < abs_kelvin:
                DisplayError(1)
                continue
            elif choice == "Rankine" and user_input_pt2_float < abs_rankine:
                DisplayError(1)
                continue
            elif choice == "Delisle" and user_input_pt2_float > abs_delisle:
                DisplayError(1)
                continue
            elif choice == "Newton" and user_input_pt2_float < abs_newton:
                DisplayError(1)
                continue
            elif choice == "Reaumur" and user_input_pt2_float < abs_Reaumur:
                DisplayError(1)
                continue
            elif choice == "Romer" and user_input_pt2_float < abs_Romer:
                DisplayError(1)
                continue
            else:
                Temp_conversionObject = (
                    Temp_conversion()
                )  # Assigns the object to Temp_conversionObject
                Temp_conversionObject.temperature = user_input_pt2_float  # Assigns the float value of user_input_pt2_float as an attribute to the object's temperature property
                if (
                    __name__ == "__main__"
                ):  # Checks if the name of the input key is from this module
                    kelvin = Temp_conversionObject.to_kelvin(choice)
                    print("Kelvin: %.3fK" % kelvin)
                    print(
                        "Celsius: %.3fC"
                        % Temp_conversionObject.from_kelvin(kelvin, "Celsius")
                    )
                    print(
                        "Fahrenheit: %.3fF"
                        % Temp_conversionObject.from_kelvin(kelvin, "Fahrenheit")
                    )
                    print(
                        "Rankine: %.3fR"
                        % Temp_conversionObject.from_kelvin(kelvin, "Rankine")
                    )
                    print(
                        "Delisle: %.3fDe"
                        % Temp_conversionObject.from_kelvin(kelvin, "Delisle")
                    )
                    print(
                        "Newton: %.3fN"
                        % Temp_conversionObject.from_kelvin(kelvin, "Newton")
                    )
                    print(
                        "Reaumur: %.3fRe"
                        % Temp_conversionObject.from_kelvin(kelvin, "Reaumur")
                    )
                    print(
                        "Romer: %.3fRo"
                        % Temp_conversionObject.from_kelvin(kelvin, "Romer")
                    )
                else:
                    deadend = True
                    continue
