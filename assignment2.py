#Marcos Paiva 6247860 - code for age calculation, anniversary listing, and string checks connection

import socket
import re

class Assignment2:
    def __init__(self, year):
        self.year = year

    def tellAge(self, currentYear):
        # Calculate and print age based on the supplied currentYear
        age = currentYear - self.year
        print(f"Your age is {age}")

    def listAnniversaries(self):
        currentYear = 2023
        anniversaries = []
        # Calculate and return a list of 10-year anniversaries
        for i in range(10, currentYear - self.year + 1, 10):
            anniversaries.append(i)
        return anniversaries

    def modifyYear(self, n):
        year_str = str(self.year)
        # First part: "n" times the first two characters in the text representation of the year
        part1 = year_str[:2] * n

        # Second part: Odd-positioned characters of text representation of year multiplied by "n"
        odd_chars = [c for i, c in enumerate(year_str) if i % 2 == 1]
        part2 = ''.join(str(int(c) * n) for c in odd_chars)

        # Return the modified year as a concatenated string
        return part1 + part2

    @staticmethod
    def checkGoodString(string: str) -> bool:
        # Check if the string meets specific criteria and return True or False
        if len(string) < 9:
            return False
        if not string[0].islower():
            return False
        if len(re.findall(r'\d', string)) != 1:
            return False
        return True

    @staticmethod
    def connectTcp(host, port):
        try:
            # Create a TCP socket, attempt to connect, and close the connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            s.close()
            return True
        except:
            return False

# Example usage with comments:
a = Assignment2(2000)
a.tellAge(2023)  # This should print 'Your age is 23'
ret = a.listAnniversaries()
print(ret)  # This should print '[10, 20]'

retval = Assignment2.connectTcp("www.google.com", 80)
if retval:
    print("Connection established correctly")
else:
    print("Some error")

ret = Assignment2.checkGoodString("f1obar0more")
print(ret)

ret = Assignment2.checkGoodString("foobar0more")
print(ret)

a = Assignment2(1782)
ret = a.modifyYear(3)
print(ret)

a = Assignment2(1991)
a.tellAge(2023)  # This should print 'Your age is 32'
ret = a.listAnniversaries()
print(ret)  # This should print '[10, 20, 30]'
