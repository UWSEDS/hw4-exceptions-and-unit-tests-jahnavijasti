import unittest
import os
import urllib.request

from Hw4_get_del_data import get_data
from Hw4_get_del_data import del_data


class Test_Hw4_get_del_data(unittest.TestCase):

    def testGetData_FileExists_Success(self):
        # Arrange Unit Test
        url = "https://data.seattle.gov/resource/4xy5-26gy.csv"

        filename = os.path.basename(url)
        # urllib.urlopen(url)
        if not os.path.exists(filename):
            request = urllib.request.Request(url)
            with urllib.request.urlopen(request) as response:
                csv = response.read()

            with open(os.path.join("/Users/tondapu/analysis", filename), 'wb') as file:
                file.write(csv)

        expectedResult = "file exists"

        # Act
        valueToValidate = get_data(url)

        # Assert
        self.assertEqual(valueToValidate, expectedResult, "testGetData_FileExists_Success Test Failed!")

    def testGetData_FileNotExists_Success(self):
        # Arrange Unit Test
        url = "https://data.seattle.gov/resource/4xy5-26gy.csv"

        filename = os.path.basename(url)
        if os.path.isfile(filename):
            os.remove(filename)

        expectedResult = "downloading"

        # Act
        valueToValidate = get_data(url)

        # Assert
        self.assertEqual(valueToValidate, expectedResult, "testGetData_FileNotExists_Success Test Failed!")

    def testGetData_InvalidURL(self):
        # Arrange Unit Test
        invalid_url = "https://data.seattle.gov/resource/4xy5-26gy.csv1"

        filename = os.path.basename("https://data.seattle.gov/resource/4xy5-26gy.csv")
        if os.path.isfile(filename):
            os.remove(filename)

        expectedResult = 404

        # Act
        valueToValidate = get_data(invalid_url)

        # Assert
        self.assertEqual(valueToValidate, expectedResult, "testGetData_InvalidURL Test Failed!")

    def testDelData_Success(self):
        # Arrange Unit Test
        url = "https://data.seattle.gov/resource/4xy5-26gy.csv"

        filename = os.path.basename(url)
        # urllib.urlopen(url)
        if not os.path.exists(filename):
            request = urllib.request.Request(url)
            with urllib.request.urlopen(request) as response:
                csv = response.read()

            with open(os.path.join("/Users/tondapu/analysis", filename), 'wb') as file:
                file.write(csv)

        expectedResult = "deleted file"

        # Act
        valueToValidate = del_data(url)

        # Assert
        self.assertEqual(valueToValidate, expectedResult, "testDelData_Success Test Failed!")

    def testDelData_FileNotExists_Success(self):
        # Arrange Unit Test
        url = "https://data.seattle.gov/resource/4xy5-26gy.csv"

        filename = os.path.basename(url)
        if os.path.isfile(filename):
            os.remove(filename)

        expectedResult = "no file to delete"

        # Act
        valueToValidate = del_data(url)

        # Assert
        self.assertEqual(valueToValidate, expectedResult, "testGetData_FileNotExists_Success Test Failed!")

