import unittest

class Employee:

# Employee Object Counstructor function for employee class
    def __init__(self, StaffId, LastName, FirstName, RegHours, HourlyRate, OTMultiple, TaxCredit, StandardBand):
        # Set the values for each variable in class
        self.StaffId = StaffId
        self.LastName = LastName
        self.FirstName = FirstName
        self.RegHours = int(RegHours)
        self.HourlyRate = int(HourlyRate)
        self.OTMultiple = float(OTMultiple)
        self.TaxCredit = int(TaxCredit)
        self.StandardBand = int(StandardBand)
        

    def computePayment(self, hours, date):
        OTRate = float(self.HourlyRate * self.OTMultiple)
        OT = 0
        if(hours > self.RegHours):
            OT = hours - self.RegHours

        RegularPay = (hours - OT) * self.HourlyRate
        OTPay = OT * OTRate
        GrossPay = RegularPay + OTPay

        HigherPay = 0
        if(GrossPay > RegularPay):
            HigherPay = GrossPay - self.StandardBand
            

        StdTax = self.StandardBand * 0.20

        HighTax = 0
        if(GrossPay > self.StandardBand):
            HighTax = (GrossPay - self.StandardBand) * 0.40

        TotalTax = StdTax + HighTax

        NetDeduction = TotalTax - self.TaxCredit
        NetPay = GrossPay - NetDeduction

        return {
            'name': self.FirstName+' ' + self.LastName,
            'Date': date,
            'Regular Hours Worked': self.RegHours,
            'Overtime Hours Worked': OT,
            'Regular Rate': self.HourlyRate,
            'Overtime Rate': OTRate,
            'Regular Pay': RegularPay,
            'Overtime Pay': OTPay,
            'Gross Pay': GrossPay,
            'Standard Rate Pay': self.StandardBand,
            'Higher Rate Pay': round(HigherPay, 2),
            'Standard Tax': round(StdTax, 2),
            'Higher Tax': round(HighTax, 2),
            'Total Tax': TotalTax,
            'Tax Credit': self.TaxCredit,
            'Net Deductions': round(NetDeduction, 2),
            'Net Pay': round(NetPay, 2)
        }

def computeAllPayment(empFileName, HoursFileName):
    finalResult = []
    with open(empFileName, 'r') as fobj:
        for line in fobj:
            data = line.split()
            emp = Employee(data[0], data[1], data[2], data[3],
                           data[4], data[5], data[6], data[7])
            with open(HoursFileName, 'r') as hobj:
                for hline in hobj:
                    hrs = hline.split()
                    if(hrs[0] == emp.StaffId):
                        pay = emp.computePayment(int(hrs[2]), hrs[1])
                        finalResult.append(pay)
    print(finalResult)
    def main():
    computeAllPayment(r"C:\Users\AKHIL\Documents\AP pythonCA1\data\Employees.txt", r"C:\Users\AKHIL\Documents\AP pythonCA1\data\Hours.txt")


class EmployeeTest(unittest.TestCase): #creating a Employeetest class for unit test
    
    #Creating three functions named testNetLessEqualGross,testNetLessEqualGrossa,testNetLessEqualGrossb for testing the net pay is less than equal to gross pay  
    def testNetLessEqualGross(self):
        e = Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 70, 700) 
        pi = e.computePayment(1,'31/10/2021')
        self.assertLessEqual(pi['Net Pay'], pi['Gross Pay'])
    def testNetLessEqualGrossa(self):
        e1 = Employee(12346, 'Deo', 'John', 39, 12, 2.6, 50, 825) 
        pi1= e1.computePayment(40,'12/11/2021')
        self.assertLessEqual(pi1['Net Pay'], pi1['Gross Pay'])
    def testNetLessEqualGrossb(self):
        e2 = Employee(12347, 'Shane', 'John', 39, 12, 0.5, 60, 955) 
        pi2= e2.computePayment(68,'12/11/2021')
        self.assertLessEqual(pi2['Net Pay'], pi2['Gross Pay'])
         
        #Creating three functions named testOverTimeNotNeg,testOverTimeNotNega and testOverTimeNotNegb for testing Overtime pay is not negative
    def testOverTimeNotNeg(self):
        e = Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 70, 700)
        pi = e.computePayment(36, '31/10/2021')
        self.assertGreater(pi['Overtime Pay'], 1)
    def testOverTimeNotNega(self):
        e1 = Employee(12346, 'Deo', 'John', 39, 12, 2.6, 50, 825) 
        pi1= e1.computePayment(23,'12/11/2021')
        self.assertGreater(pi1['Overtime Pay'], 1)
    def testOverTimeNotNegb(self):
        e2 = Employee(12347, 'Shane', 'John', 39, 12, 0.5, 60, 955) 
        pi2= e2.computePayment(48,'12/11/2021')
        self.assertGreater(pi2['Overtime Pay'],1)
        
        #Create three functions named testRegHourExceed,testRegHourExceeda,testRegHourExceedb for testing Regular Hours Worked cannot exceed hours worked
    def testRegHourExceed(self):
        e = Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 70, 700)
        pi = e.computePayment(30, '31/10/2021')
        self.assertLessEqual(pi['Regular Hours Worked'], 30)
    def testRegHourExceeda(self):
        e1 = Employee(12346, 'Deo', 'John', 39, 12, 2.6, 50, 825) 
        pi1= e1.computePayment(23,'12/11/2021')
        self.assertLessEqual(pi1['Regular Hours Worked'], 23)
    def testRegHourExceedb(self):
        e2 = Employee(12347, 'Shane', 'John', 39, 12, 0.5, 60, 955) 
        pi2= e2.computePayment(48,'12/11/2021')
        self.assertLessEqual(pi2['Regular Hours Worked'], 48)
         

        
        #Create three  functions named testHighTaxNotNeg,testHighTaxNotNega,testHighTaxNotNegb for testing Higher Tax cannot be negative.
    def testHighTaxNotNeg(self):
        e = Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 70, 700)
        pi = e.computePayment(300, '31/10/2021')
        self.assertGreater(pi['Higher Tax'],1) 
    def testHighTaxNotNega(self):
        e1 = Employee(12346, 'Deo', 'John', 39, 12, 2.6, 50, 825) 
        pi1= e1.computePayment(23,'12/11/2021')
        self.assertGreater(pi1['Higher Tax'],1)
    def testHighTaxNotNegb(self):
        e2 = Employee(12347, 'Shane', 'John', 39, 12, 0.5, 60, 955) 
        pi2= e2.computePayment(48,'12/11/2021')
        self.assertGreater(pi2['Higher Tax'],1) 
        
        #Create function testNetPayNotNeg for tetsing Net Pay is not negative
    def testNetPayNotNeg(self):
        e = Employee(12345, 'Green', 'Joe', 37, 16, 1.5, 70, 700)
        pi = e.computePayment(0, '31/10/2021')
        self.assertGreater(pi['Net Pay'],1)
    def testNetPayNotNega(self):
        e1 = Employee(12346, 'Deo', 'John', 39, 12, 2.6, 50, 825) 
        pi1= e1.computePayment(23,'12/11/2021')
        self.assertGreater(pi1['Net Pay'],1)
    def testNetPayNotNegb(self):
        e2 = Employee(12347, 'Shane', 'John', 39, 12, 0.5, 60, 955) 
        pi2= e2.computePayment(48,'12/11/2021')
        self.assertGreater(pi2['Net Pay'],1)
         #Running the tests below line

if __name__ == "__main__":
    main()
    unittest.main()
