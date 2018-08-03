contents of this folder:
19402-Ajoneuvoveron_perusvero_co2_mukaan.pdf: pdf file containing the amount of taxes based on the CO2 emissions
tax.txt: txt file with the contents copied and pasted of said pdf
test_data.csv: data of registered cars from Trafi's website (https://www.trafi.fi/tietopalvelut/tilastot/tieliikenne/ensirekisteroinnit) reduced to contain only every 10th line of the cars registered after 2009
compute_taxes_by_year_and_emission_classes.py: the main program
read_taxes_by_emissions: program that reads 'tax.txt' to a dictionary

This program reads csv files provided by Trafi that include data on cars registered in Finland. It computes the amount of taxes for cars registered in 2010-2016. It is also possible to write, and read the written, csv file in which the program computes taxes from different emission classes from each said year.