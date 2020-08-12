import fire
import operator
import csv
import sys


class Iprice:
    """this class Provides a simple interface to print string in different format and print it to CSV file.
     as a command line program."""

    def __init__(self, textInput):
        self.textInput = textInput
    textInput = property(operator.attrgetter('_textInput'))

    @textInput.setter
    def textInput(self, text):
        if not text:
            raise Exception("textInput cannot be empty")
        self._textInput = text

    def capitalize(self):
        return self.textInput.upper()

    def customFormat(self):
        rawString = self.textInput.lower()
        customFormat = ''
        for num in range(0, len(rawString)):
            if (num % 2):
                customFormat += rawString[num].upper()
            else:
                customFormat += rawString[num]
        return customFormat

    def csvBuilder(self):
        row = self.textInput.lower()
        try:
            file = open('output.csv', 'w')
            with file:
                writer = csv.writer(file)
                writer.writerow(row)
            print("CSV created!")
        except:
            print("Something went wrong when writing to the file")


def main(textInput):
    iprce_instance = Iprice(textInput)
    print(iprce_instance.capitalize())
    print(iprce_instance.customFormat())
    iprce_instance.csvBuilder()


if __name__ == '__main__':
    fire.Fire(main)
