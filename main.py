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