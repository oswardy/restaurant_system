import csv
import pyfiglet
from fpdf import FPDF

filename = 'data.csv'
filename_obj = None
ascii_banner = pyfiglet.figlet_format("Oswardy")
print(ascii_banner)


class PDF(FPDF):
    #Header class
    def header(self):
        self.set_font('Arial', 'B', 15)        
        self.cell(0, 10, "Oswardy Restaurant's Receipt", 1, 0, 'C')
        self.ln(20)

    #Footer class
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, '©Copyright by Oswardy', 1, 0, 'C')

def read_sales(data_file):
    # Read data
    with open(data_file, 'r') as f:
        reader = csv.DictReader(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        burger = 0
        fries = 0
        lamb = 0
        nachos = 0
        tigers = 0
        pizza = 0
        for row in reader:
            burger += int(row['Burger'])
            fries += int(row['Fries'])
            lamb += int(row['Lamb'])
            nachos += int(row['Nachos'])
            tigers += int(row['Tigers'])
            pizza += int(row['Pizza'])
        print("Quantity of Burger: " + str(burger)+ " Total(RM) " + str(doublec_burger*burger))
        print("Quantity of Fries:  " + str(fries) + " Total(RM) " + str(french_fries*fries))
        print("Quantity of Lamb:   " + str(lamb) +  " Total(RM) " + str(lamb_chop*lamb))
        print("Quantity of Nachos: " + str(nachos)+ " Total(RM) " + str(cheesy_nachos*nachos))
        print("Quantity of Tigers: " + str(tigers) +" Total(RM) " + str(doublec_burger*tigers))
        print("Quantity of Pizza:  " + str(pizza) + " Total(RM) " + str(beef_pizza*pizza))
        print("                       -----------")
        print("Total sales = \t\t       "+ str((doublec_burger*burger)+(french_fries*fries)+(lamb_chop*lamb)+(cheesy_nachos*nachos)+(doublec_burger*tigers)+(beef_pizza*pizza)))
        print("                       -----------")


def receipt(data_file):
    # Read data
    with open(data_file, 'r') as f:
        reader = csv.DictReader(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        burger = 0
        fries = 0
        lamb = 0
        nachos = 0
        tigers = 0
        pizza = 0
        for row in reader:
            burger += int(row['Burger'])
            fries += int(row['Fries'])
            lamb += int(row['Lamb'])
            nachos += int(row['Nachos'])
            tigers += int(row['Tigers'])
            pizza += int(row['Pizza'])
            print("========================\n  Transaction Id: " + row['Transaction Id'] + "\n========================")
            print("Quantity of Burger: " + str(burger))
            print("Quantity of Fries: " + str(fries))
            print("Quantity of Lamb: " + str(lamb))
            print("Quantity of Nachos: " + str(nachos))
            print("Quantity of Tigers: " + str(tigers))
            print("Quantity of Pizza: " + str(pizza))



#   ok

doublec_burger = 16.00
french_fries = 5.00
lamb_chop = 19.00
cheesy_nachos = 9.00
tiger_beer = 50.00
beef_pizza = 18.00

T_N = 1


def inputNumber(message):
    while True:
        try:
            user_input = int(input(message))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return user_input


def printmenu():
    print("""
+-------------------------------------------+
|                    Menu                   |
+---------------------------------+---------+
| A\tDouble Cheese Burger        | RM""" + str(doublec_burger) + """|
+---------------------------------+---------+
| B\tCheesy French Fries         | RM""" + str(french_fries) + """ |
+---------------------------------+---------+
| C\tLamb Chop with French Fries | RM""" + str(lamb_chop) + """|
+---------------------------------+---------+
| D\tCheesy Nachos               | RM""" + str(cheesy_nachos) + """ |
+---------------------------------+---------+
| E\tOne Bucket of Tiger Beer    | RM""" + str(tiger_beer) + """|
+---------------------------------+---------+
| F\tBeef Bacon Pizza            | RM""" + str(beef_pizza) + """|
+---------------------------------+---------+
""")
    print("=================================================================")
    print("| Select a letter(ex. A or a) to order or 'done'to finish order |")
    print("=================================================================")
    qty_burger = 0
    qty_french_fries = 0
    qty_lamb_chop = 0
    qty_cheesy_nachos = 0
    qty_tiger_beer = 0
    qty_beef_pizza = 0

    total = 0.0
    global T_N
    DONE = True
    while (DONE):
        print("-----------------")
        print("Transaction No: ", T_N)
        Item = input("| Selection: ")
        if Item == "A" or Item == "a":
            qty_burger += inputNumber("| How many would you like? Quantity: ")
            total = total + (doublec_burger * float(qty_burger))
            print("| You have ordered " + str(qty_burger) + " double cheese burger!")
            print("| Total:", total)
        elif Item == "B" or Item == "b":
            qty_french_fries += inputNumber("| How many would you like?Quantity: ")
            total = total + (french_fries * float(qty_french_fries))
            print("| You have ordered " + str(qty_french_fries) + " french fries!")
            print("| Total:", total)
        elif Item == "C" or Item == "c":
            qty_lamb_chop += inputNumber("| How many would you like?Quantity: ")
            total = total + (lamb_chop * float(qty_lamb_chop))
            print("| You have ordered " + str(qty_lamb_chop) + " set of lamb chop!")
            print("| Total:", total)
        elif Item == "D" or Item == "d":
            qty_cheesy_nachos += inputNumber("| How many would you like?Quantity: ")
            total = total + (cheesy_nachos * float(qty_cheesy_nachos))
            print("| You have ordered " + str(qty_cheesy_nachos) + " cheesy nachos!")
            print("| Total:", total)
        elif Item == "E" or Item == "e":
            qty_tiger_beer = inputNumber("| How many would you like?Quantity: ")
            total = total + (tiger_beer * float(qty_tiger_beer))
            print("| You have ordered " + str(qty_tiger_beer) + " buckets of tiger beer!")
            print("| Total:", total)
        elif Item == "F" or Item == "f":
            qty_beef_pizza += inputNumber("| How many would you like?Quantity: ")
            total = total + (beef_pizza * float(qty_beef_pizza))
            print("| You have ordered " + str(qty_beef_pizza) + " beef bacon pizza!")
            print("| Total:", total)
        elif Item == "DONE" or Item == "done":
            print("")
            print("| Total:           ", total)
            print(f"| GST:            + {total * 0.06:3.2f}")
            print("|                  -------")
            print("| Final total(RM): ", total + total * 0.06)
            print("|                  -------")
            print("")
            print("Thank you very much!")
            print("Please come again!")
            DONE = False
            writer.writerow({
                'Transaction Id': T_N,
                'Burger': qty_burger,
                'Fries': qty_french_fries,
                'Lamb': qty_lamb_chop,
                'Nachos': qty_cheesy_nachos,
                'Tigers': qty_tiger_beer,
                'Pizza': qty_beef_pizza
            })
            T_N += 1
        else:
            print("| Please select again,this is letter is not in the menu")


def setup_data_file():
    global writer
    global filename_obj
    filename_obj = open(filename, mode='w')
    fields = ['Transaction Id', 'Burger', 'Fries', 'Lamb', 'Nachos', 'Tigers', 'Pizza']
    writer = csv.DictWriter(filename_obj, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, fieldnames=fields)
    writer.writeheader()

def generatereceipt(data_file):
  num = inputNumber("Please enter the transation no: ")
  with open(data_file, 'r') as f:
        reader  = csv.DictReader(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        burger = 10
        fries = 0
        lamb = 0
        nachos = 0
        tigers = 0
        pizza = 0
        for i, row in enumerate(reader,1) :
          if num == i:
            print("Receipt of transaction No "+ str(i)+ " have been created") 
            pdf = PDF()
            pdf.alias_nb_pages()
            pdf.add_page()
            pdf.set_font('Times', 'B', 12)
            pdf.cell(0, 10, 'Transaction number: ' + str(num), 0, 1)
            pdf.set_font('Times', '', 12)
            pdf.cell(0, 10, 'Burgers sold today: ' + str(row['Burger']), 0, 0)
            pdf.cell(-50, 10, 'Total sales: RM' + str(int(row['Burger'])*doublec_burger),0, 1, 'C')
            pdf.cell(0, 10, 'Fries : ' + str(row['Fries']), 0, 0)
            pdf.cell(-50, 10, 'Total sales: RM' + str(int(row['Fries'])*french_fries),0, 1, 'C')
            pdf.cell(0, 10, 'Lambs : ' + str(row['Lamb']), 0, 0)
            pdf.cell(-50, 10, 'Total sales: RM' + str(int(row['Lamb'])*lamb_chop),0, 1, 'C')
            pdf.cell(0, 10, 'Nachos : ' + str(row['Nachos']), 0, 0)
            pdf.cell(-50, 10, 'Total sales: RM' + str(int(row['Nachos'])*cheesy_nachos),0, 1, 'C')
            pdf.cell(0, 10, 'Bucket Tigers beers : ' + str(row['Tigers']), 0, 0)
            pdf.cell(-50, 10, 'Total sales: RM' + str(int(row['Tigers'])*tiger_beer),0, 1, 'C')
            pdf.cell(0, 10, 'Beef Pizza : ' + str(row['Pizza']), 0, 0)
            pdf.cell(-50, 10, 'Total sales: RM' + str(int(row['Pizza'])*beef_pizza),0, 1, 'C')
            pdf.output('sales.pdf', 'F')
            break

        else:
          print("Transaction No Not found")





# main function
def main():
    setup_data_file()
    repeat = True
    while (repeat):
        filename_obj.flush()
        user_input = inputNumber("1. Order\n2. Food sales\n3. Generate Receipt\n4. Exit\nNumber:")
        if user_input == 1:
            printmenu()
        elif user_input == 2:
            read_sales(filename)
        elif user_input == 3:
            generatereceipt(filename)
        else:
            repeat = False
    filename_obj.close()


if __name__ == "__main__":
    main()
