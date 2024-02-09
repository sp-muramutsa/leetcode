class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        def convert(number):
            string_to_integer = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

            integer = 0
            for char in number:
                if char in string_to_integer:
                    integer = integer * 10 + string_to_integer[char]
            
            return integer
        
        
        number1 = convert(num1)
        number2 = convert(num2)

        product = str(number1 * number2)

        return product

        


        
        
