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