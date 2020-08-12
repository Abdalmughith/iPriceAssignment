
import iPrice

class IpriceTest():
    """Tests for Iprice class"""
    iPriceInstance = iPrice.Iprice("hello world")
    def test_capitalize(self):
        assert self.iPriceInstance.capitalize() == "HELLO WORLD", "Should be HELLO WORLD"
        print("test_capitalize pass!")


    def test_customFormat(self):
        assert self.iPriceInstance.customFormat() == "hElLo wOrLd", "Should be hElLo wOrLd"
        print("test_customFormat pass!")


    def test_csvBuilder(self):
        self.iPriceInstance.csvBuilder()
        try:
            file = open('output.csv', 'r')
            with file:
                row = file.readline().strip()
                assert row == "h,e,l,l,o, ,w,o,r,l,d", "Should be h,e,l,l,o, ,w,o,r,l,d"
                print("test_csvBuilder pass!")
        except:
            print("Something went wrong when reading file or file does not has correct content!")



if __name__ == '__main__':
    ipriceTestInstance = IpriceTest()
    ipriceTestInstance.test_capitalize()
    ipriceTestInstance.test_customFormat()
    ipriceTestInstance.test_csvBuilder()
