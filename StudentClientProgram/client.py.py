class Client:
    def __init__(self, lname, fname, add, city, zipc, phone, email, accnum, numacc, bal):
        self.__lname = lname
        self.__fname = fname
        self.__add = add
        self.__city = zipc
        self.__phone = phone
        self.__email = email
        self.__accnum = accnum
        self.__numacc = numacc
        self.__bal = bal
    def set_lname(self, lname):
        self.__lname = lname
    def set_fname(self, fname):
        self.__fname = fname
    def set_add(self, add):
        self.__add = add
    def set_city(self, city):
        self.__city = city
    def set_zipc(self, zipc):
        self.__zipc = zipc
    def set_phone(self, phone):
        self.__phone = phone
    def set_email(self, email):
        self.__email = email
    def set_accnum(self, accnum):
        self.__accnum = accnum
    def set_numacc(self, numacc):
        self.__numacc = numacc
    def set__bal(self, bal):
        self.__bal = bal
    def get_lname(self):
        return self.__lname
    def get_fname(self):
        return self.__fname
    def get_add(self):
        return self.__add
    def get_city(self):
        return self.__city
    def get_zipc(self):
        return self.__zipc
    def get_phone(self):
        return self.__phone
    def get_email(self):
        return self.__email
    def get_accnum(self):
        return self.__accnum
    def get_numacc(self):
        return self.__numacc
    def get_bal(self):
        return self.__bal
    def __str__(self):
        return "LName: " + self.__lname + \
               "FName: " + self.__fname + \
               "\nADD: " + self.__add + \
               "\nCITY: " + self.__city + \
               "\nzipc: " + self.__zipc + \
               "\nphone: " + self.__phone + \
               "\nemail: " + self.__email + \
               "\naccnum: " + self.__accnum + \
               "\nnumacc: " + self.__numacc + \
               "\nbal: " + self.__bal

    
