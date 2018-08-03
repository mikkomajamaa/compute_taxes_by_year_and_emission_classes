######################################################################
# Mikko Majamaa 3rd of August 2018
#
# Read the txt file made by copying the content of the pdf file from
# Trafis website which contains the amount of taxes based on CO2
# emissions starting of 1st of January 2017.
#
# source of the pdf:
# https://www.trafi.fi/filebank/a/1451562298/0c255e16194750e2e32e41437f7012f9/19402-Ajoneuvoveron_perusvero_co2_mukaan.pdf

def read_taxes_by_emissions_file():
    file_name = "tax.txt"
    file_var = open(file_name, "r")
    content = file_var.read()
    tax_dict = {}
    key = ""
    value = ""
    i = 0
    j = 0
    taxes = content.replace("\n", " ")
    taxes = taxes.replace(",", ".")
    taxes = taxes.replace(" ", ",")
    taxes = taxes.replace("-", "")
    taxes = taxes.split(",")
    for i in range(0, round((len(taxes))/2)):
        key = int(taxes[j].strip("'"))
        value = float(taxes[j+1].strip("'"))
        tax_dict[key] = value
        j += 2
    return tax_dict
######################################################################
# eof
