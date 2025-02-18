'''You are given a non-negative floating point number rounded to two decimal places celsius, that denotes the temperature in Celsius.

You should convert Celsius into Kelvin and Fahrenheit and return it as an array ans = [kelvin, fahrenheit].

Return the array ans. Answers within 10-5 of the actual answer will be accepted.

Note that:

Kelvin = Celsius + 273.15
Fahrenheit = Celsius * 1.80 + 32.00'''

class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        ans = []
        kelvin = celsius + 273.15               # convert celcius to kelvin
        fahrenheit = celsius * 1.80 + 32.00     # convert celcius to fahrenheit
        ans.append(kelvin)
        ans.append(fahrenheit)
        return ans

mySol = Solution()
celsius = 122.11
print(mySol.convertTemperature(celsius))
