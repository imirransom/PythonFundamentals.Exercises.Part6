
def convert_to_celsius(fahrenheit_temp: float) -> float:
    """
    Given a float representing a temperature in fahrenheit, return the corresponding value in celsius.

    :param fahrenheit_temp: A float representing a temperature in fahrenheit
    :return: A float representing the corresponding value of the fahrenheit_temp parameter in celsius
    """
    return round((fahrenheit_temp - 32) / 1.8, 2)


def convert_to_fahrenheit(celsius_temp: float) -> int:
    """
    Given a float representing a temperature in celsius, return the corresponding value in fahrenheit.

    :param celsius_temp: A float representing a temperature in celsius
    :return:  A float representing the corresponding value of the celsius_temp parameter in fahrenheit
    """
    # °F = (°C × (9/5)) + 32
    return int((celsius_temp * 1.8) + 32)

def convert_celsius_to_kelvin(celsius_temp: float) -> int:

    return int(celsius_temp + 273.15)



def convert_fahrenheit_to_kelvin_(fahrenheit_temp: float) -> int:

    return int(((fahrenheit_temp - 32) * 1.8) + 273.15)




def convert_kelvin_to_celsius(kelvin_temp: float) -> float:

    return kelvin_temp - 273.15



def convert_kelvin_to_fahrenheit(kelvin_temp: float) -> float:

    return ((kelvin_temp - 273.15) * 1.8) + 32