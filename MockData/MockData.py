import copy
import json
import random
import sys
from faker import Faker
fake = Faker()
from faker.providers import BaseProvider

class MyProvider(BaseProvider):
    def employeeid(self):
        return str(random.randrange(1000000, 9999999))
    def workertype(self):
        return random.choice('ABCDE')
    def pronoun(self):
        pnouns = ['He/Him/His', 'She/Her/Hers', 'They/Them']
        return random.choice(pnouns)
    def workerstatus(self):
        wstatus = ['Employed', 'Terminated', 'Leave']
        return random.choice(wstatus)
    def provisioninggroup(self):
        return random.choice('ABCDE')
    def employeetype(self):
        return random.choice('ABCDE')
    def timetype(self):
        return random.choice('ABCDE')
    def username(self, fname, lname, eid):
        return f'''{fname[0].lower()}{lname.lower()}{eid}'''
    def hiredate(self):
        return fake.iso8601(tzinfo=None, end_datetime=None)
    def terminationdate(self, wstatus):
        if wstatus == 'Terminated':
            return fake.iso8601(tzinfo=None, end_datetime=None)
        else:
            return None
    def preferrednamedisplay(self, fname, lname):
        return f'''{fname[0]}{lname}'''
    def jobcode(self):
        return random.choice('12345')
    def jobtitle(self):
        return random.choice('ABCDE')
    def positiongroup(self):
        return random.choice('ABCDE')
    def positionid(self):
        return random.choice('12345')
    def costcenterid(self):
        return random.choice('12345')
    def costcentername(self):
        return random.choice('ABCDE')
    def buildingcode(self):
        return '1'
    def buildingname(self):
        return random.choice('ABCDE')
    def mailstop(self):
        mstop = ['Front Desk', 'Office', 'Secretary']
        return random.choice(mstop)
    def union(self):
        ulist = ['None', 'PWU 199']
        return random.choice(ulist)
    def departmentid(self):
        return random.choice('12345')
    def departmentname(self):
        return random.choice('ABCDE')
    def costcenterid(self):
        return random.choice('12345')
    def departmentid(self):
        return random.choice('12345')
    def departmentname(self):
        return random.choice('ABCDE')
    def divisionid(self):
        return random.choice('12345')
    def divisionname(self):
        return random.choice('ABCDE')
    def sectionid(self):
        return random.choice('12345')
    def sectionname(self):
        return random.choice('ABCDE')
    def electedofficialid(self):
        return random.choice('12345')
    def electedofficialname(self):
        return random.choice('ABCDE')
    def officeid(self):
        return random.choice('12345')
    def officename(self):
        return random.choice('ABCDE')
    def unitid(self):
        return random.choice('12345')
    def unitname(self):
        return random.choice('ABCDE')
    def email(self, fname, lname, eid):
        return f'''{fname[0].lower()}{lname.lower()}@multco.us'''
    def primaryworkphone(self):
        return f'''503.823.4000'''
    def primaryworkphonedevicetype(self):
        return 'Phone'
    def primaryworkphoneextension(self):
        return str(random.randrange(1, 1000))
    def faxphone(self, phone):
        return f'''503.823.4001'''
    def faxphonedevicetype(self):
        return 'Fax'
    def faxextension(self, pext):
        return pext
    def mobilephone(self):
        return f'''503.{random.randrange(100, 999)}.{random.randrange(1000, 9999)}'''
    def mobilephonedevicetype(self):
        return 'Mobile'
    def mobilephoneextension(self):
        return None
    def pagerphone(self):
        return None
    def pagerphonedevicetype(self):
        return None
    def pagerphoneextension(self):
        return None
    def manageremployeeid(self):
        return str(random.randrange(1000000, 9999999))
    def managerorganizationid(self):
        return random.choice('12345')
    def managerorganizationname(self):
        return random.choice('ABCDE')


def main():
    print("Welcome to Mock Data ")

    if len(sys.argv) == 3:
        inname = sys.argv[1]
        jname = 'WorkerList'

        nobjects = int(sys.argv[2])
    else:
        print('\nUsage: python MockData.py templateFile numWorkers')
        print('Example: python MockData.py Worker.json 10')

        return -1

    with open(inname, newline='') as infile:
        jtemp = json.load(infile)

        print(jtemp)

        fake.add_provider(MyProvider)

        jlist = []

        for i in range(nobjects):
            ctemp = copy.deepcopy(jtemp)
            fname = fake.first_name()
            mname = fake.first_name()
            lname = fake.last_name()
            eid = fake.employeeid()
            ctemp['employeeID'] = eid
            ctemp['workerType'] = fake.workertype()
            ctemp['pronoun'] = fake.pronoun()
            ctemp['workerStatus'] = fake.workerstatus()
            ctemp['provisioningGroup'] = fake.provisioninggroup()
            ctemp['employeeType'] = fake.employeetype()
            ctemp['timeType'] = fake.timetype()
            ctemp['username'] = fake.username(fname, lname, eid)
            ctemp['hireDate'] = fake.hiredate()
            ctemp['originalHireDate'] = ctemp['hireDate']
            ctemp['terminationDate'] = fake.terminationdate(ctemp['workerStatus'])
            ctemp['legalFirstName'] = fname
            ctemp['legalMiddleName'] = mname
            ctemp['legalLastName'] = lname
            ctemp['preferredFirstName'] = fname
            ctemp['preferredMiddleName'] = mname
            ctemp['preferredLastName'] = lname
            ctemp['preferredNameDisplay'] = fake.preferrednamedisplay(fname, lname)
            ctemp['jobCode'] = fake.jobcode()
            ctemp['jobTitle'] = fake.jobtitle()
            ctemp['positionGroup'] = fake.positiongroup()
            ctemp['positionID'] = fake.positionid()
            ctemp['costCenterID'] = fake.costcenterid()
            ctemp['costCenterName'] = fake.costcentername()
            ctemp['buildingCode'] = fake.buildingcode()
            ctemp['buildingName'] = fake.buildingname()
            ctemp['mailStop'] = fake.mailstop()
            ctemp['union'] = fake.union()
            ctemp['departmentID'] = fake.departmentid()
            ctemp['departmentName'] = fake.departmentname()
            ctemp['divisionID'] = fake.divisionid()
            ctemp['divisionName'] = fake.divisionname()
            ctemp['sectionID'] = fake.sectionid()
            ctemp['sectionName'] = fake.sectionname()
            ctemp['electedOfficialID'] = fake.electedofficialid()
            ctemp['electedOfficialName'] = fake.electedofficialname()
            ctemp['officeID'] = fake.officeid()
            ctemp['officeName'] = fake.officename()
            ctemp['unitID'] = fake.unitid()
            ctemp['unitName'] = fake.unitname()
            ctemp['email'] = fake.email(fname, lname, eid)
            ctemp['primaryWorkPhone'] = fake.primaryworkphone()
            ctemp['primaryWorkPhoneDeviceType'] = fake.primaryworkphonedevicetype()
            ctemp['primaryWorkPhoneExtension'] = fake.primaryworkphoneextension()
            ctemp['faxPhone'] = fake.faxphone(ctemp['primaryWorkPhone'])
            ctemp['faxPhoneDeviceType'] = fake.faxphonedevicetype()
            ctemp['faxExtension'] = fake.faxextension(ctemp['primaryWorkPhoneExtension'])
            ctemp['mobilePhone'] = fake.mobilephone()
            ctemp['mobilePhoneDeviceType'] = fake.mobilephonedevicetype()
            ctemp['mobilePhoneExtension'] = fake.mobilephoneextension()
            ctemp['pagerPhone'] = fake.pagerphone()
            ctemp['pagerPhoneDeviceType'] = fake.pagerphonedevicetype()
            ctemp['pagerPhoneExtension'] = fake.pagerphoneextension()
            ctemp['managerEmployeeID'] = fake.manageremployeeid()
            ctemp['managerOrganizationID'] = fake.managerorganizationid()
            ctemp['managerOrganizationName'] = fake.managerorganizationname()
#            print(ctemp)
            jlist.append(ctemp)
#            print(fake.name())

        print(jlist)
        with open(f'''{jname}.json''', 'w') as outfile:
            json.dump(jlist, outfile, indent=2)

    return 0


if __name__ == '__main__':
    main()
