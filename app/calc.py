# strike data
strike = 8.7
Actual_price = 0.45
Allocation_ratio = 1
Extra_charge = 0.1
Rate_of_exchange = 1
Type = 'Short'

# stock movement
stockactual = 9.05
stockentry = 9
stockloss = 8.8
stockprofit = 10

class Certificate():
    """Certificate class to store and calculate certificate data"""

    def __init__(self, strike, Actual_price, Allocation_ratio, Extra_charge, Rate_of_exchange, stockactual, stockentry, stockloss, stockprofit, Type):
        "Certitificate Data"
        self.strike = strike
        self.Actual_price = Actual_price
        self.Allocation_ratio = Allocation_ratio
        self.Extra_charge = Extra_charge
        self.Rate_of_exchange = Rate_of_exchange
        self.Type = Type

        """Stock Data"""
        self.stockactual = stockactual
        self.stockentry = stockentry
        self.stockloss = stockloss
        self.stockprofit = stockprofit

    def printerCertificate(self):
        print("\nCertificate Type: ", Type)
        print("Strike price: ", strike)
        print("Actual price: ", Actual_price)
        print("Allocation ratio: ", Allocation_ratio)
        print("Extra charge: ", Extra_charge)
        print("Rate of exchange: ", Rate_of_exchange)
        print("Type: ", Type)

    def printerStock(self):
        print("\nStock actual: ", stockactual)
        print("Stock entry: ", stockentry)
        print("Stock loss: ", stockloss)
        print("Stock profit: ", stockprofit)

    def longcertstockprint(self):
        """Long Certificate"""
        actcert = (((stockactual-strike)*Allocation_ratio)
                   * Rate_of_exchange)+Extra_charge

        entrcert = (((stockentry-strike)*Allocation_ratio)
                    * Rate_of_exchange)+Extra_charge

        losscert = (((stockloss-strike)*Allocation_ratio)
                    * Rate_of_exchange)+Extra_charge

        profcert = (((stockprofit-strike)*Allocation_ratio)
                    * Rate_of_exchange)+Extra_charge

        print("\nCertificate Type: ", Type)
        print(f"Stock: {stockactual} € : , Certificate: {actcert}€")
        print(f"Stock: {stockentry} € : , Certificate: {entrcert}€")
        print(f"Stock: {stockloss} € : , Certificate: {losscert}€")
        print(f"Stock: {stockprofit} € : , Certificate: {profcert}€")

    def shortcertstockprint(self):
        """Short certificate print"""
        actcert = (((strike-stockactual)*Allocation_ratio)*Rate_of_exchange)+Extra_charge
        entrcert = (((strike-stockentry)*Allocation_ratio)*Rate_of_exchange)+Extra_charge
        losscert = (((strike-stockloss)*Allocation_ratio)*Rate_of_exchange)+Extra_charge
        profcert = (((strike-stockprofit)*Allocation_ratio)*Rate_of_exchange)+Extra_charge

        print("\nCertificate Type: ", Type)
        print(f"Stock: {stockactual} € : , Certificate: {actcert}€")
        print(f"Stock: {stockentry} € : , Certificate: {entrcert}€")
        print(f"Stock: {stockloss} € : , Certificate: {losscert}€")
        print(f"Stock: {stockprofit} € : , Certificate: {profcert}€")


l = Certificate(strike, Actual_price, Allocation_ratio, Extra_charge,
                Rate_of_exchange, stockactual, stockentry, stockloss, stockprofit, Type)



if l.Type == 'Long':
    l.longcertstockprint()
else:
    l.shortcertstockprint()