######################################################################
#Mikko Majamaa 3rd of August 2018

import read_taxes_by_emissions

class Car:
    year_registered = ""
    emissions = ""
    tax = 0
    
def menu():
    print("Anna haluamasi toiminnon numero seuraavasta valikosta:")
    print("1) Lue ajoneuvotiedot")
    print("2) Laske ja tulosta verot")
    print("3) Kirjoita CSV-tiedosto")
    print("4) Tulosta CSV-tiedoston data näytölle")
    print("0) Lopeta")
    choice = input("Valintasi: ")
    return choice

def read_file(tax_keys_values):
    list_var = []
    try:
        file_name = input("Anna luettavan tiedoston nimi: ")
        file_var = open(file_name, "r", encoding="utf-8")
        line =  file_var.readline()
        for i in range(0,7):
            list_var.append([]) #make a new list inside the list_var for each year 
        for line in file_var:
            if (line[0:2] == "M1"): #passanger car
                car = Car()
                columns = line.split(";")
                if (columns[1] != ""):
                    car.year_registered = int(columns[1][0:4])  #column with index one contains the year car was registered
                else:
                    car.year_registered = 0
                if (columns[33] != ""):
                    car.emissions = int(columns[33]) #column with index 33 contains the car's CO2 emissions
                else:
                    car.emissions = 0;
                if (car.emissions >= 400):
                    car.emissions = 400
                car.tax = tax_keys_values.get(car.emissions)
                for i in range(0,len(list_var)): #arrange the cars by year inside the list_var's lists
                    if (car.year_registered == 2010+i): 
                        list_var[i].append(car)
            if line == "":
                break
        print("Tiedosto '" + file_name + "' luettu.")
        return list_var
    except FileNotFoundError:
        print("Tiedostoa '" + file_name + "' ei löytynyt.")
        return list_var

def compute_and_print_taxes(cars):
    if (len(cars) != 0):
        year = 2010
        print("Verokertymät vuosittain 2010-luvulla ovat seuraavat:")
        for i in range(0,len(cars)):
            taxes = sum(parsi_cars(cars[i]))
            print(year,"{0:.0f} euroa.".format(taxes))        
            year += 1
    else:
        print("Tiedostoa ei olla vielä luettu.")

def write_csv(cars):
    if (len(cars) != 0):
        file_name = input("Anna kirjoitettavan tiedoston nimi: ")
        file_var = open(file_name, "w")
        file_var.write(";50;100;150;200;250;300;350;400;1000;\n")
        for i in range(0,len(cars)):
            list_var = [round(x) for x in parsi_cars(cars[i])]
            print(2010+i,*list_var, sep=';', end=';\n', file=file_var)
        file_var.close()
        print("CSV-tiedosto kirjoitettu.")
        return file_name
    else:
        print("Tiedostoa ei olla vielä luettu.")


def parsi_cars(cars): #arrange the yearly taxes by emissions classes
    yearly_taxes = []
    for i in range(0,9):
        yearly_taxes.append(0)
    for n in range(0,9):
        for i in cars:
            if i.emissions > n*50-1 and i.emissions < (n+1)*50:
                yearly_taxes[n] += i.tax
    return yearly_taxes

def print_csv(file_name):
    try:
        file_var = open(file_name, "r")
        print("CSV-tiedoston data on seuraava:")
        while True:
            line = file_var.readline()[:-1]
            if (line == ""):
                break
            print(line)
        file_var.close()
    except FileNotFoundError:
        print("Tiedostoa '" + file_name + "' ei löytynyt.")

def main():
    car_list = []
    tax_keys_values = {}
    file_name = None;
    while True:
        choice = menu()
        if (choice == "0"):
            break
        elif (choice == "1"):
            if not tax_keys_values: #read the txt file with amount of taxes for certain amount of CO2 emissions to a dict if the dict is empty
                tax_keys_values = read_taxes_by_emissions.read_taxes_by_emissions_file()
            car_list = read_file(tax_keys_values)
        elif (choice == "2"):
            compute_and_print_taxes(car_list)
        elif (choice == "3"):
            file_name = write_csv(car_list)
        elif (choice == "4"):
            if (file_name != None):
                print_csv(file_name)
            else:
                print("CSV-tiedostoa ei olla vielä kirjoitettu.")
        else:
            print("Tuntematon valinta")
        
main()
print("Kiitos ohjelman käytöstä.")

######################################################################
# eof
