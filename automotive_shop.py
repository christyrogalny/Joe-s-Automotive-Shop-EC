class Customer:
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone


    def set_name(self, name):
        self.__name = name 

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone


    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    def print_person(self):
        print('Name: ', self.__name)


class Car(Customer):
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year


    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year


    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    #def print_person(self):
        #print('Name: ', self.__name)


tax_rate = 0.06
class ServiceQuote(Customer):
    def __init__(self, pcharge, lcharge):
        self.__pcharge = pcharge
        self.__lcharge = lcharge

    def set_pcharge(self, pcharge):
        self.__parts_charges = pcharge

    def set_lchage(self, lcharge):
        self.__labor_charges = lcharge


    def get_parts_charges(self):
        return self.__parts_charges

    def get_labor_charges(self):
        return self.__labor_charge 
