class StringManipulator:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input("Enter a string: ")

    def printString(self):
        print(self.text.upper())

string_obj = StringManipulator()
string_obj.getString()
string_obj.printString()
