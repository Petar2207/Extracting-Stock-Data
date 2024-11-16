import yfinance as yf
import pandas as pd

pd.set_option('display.max_columns', None)
y = 1
while y == 1:
    x = input("Write ticker symbol: ")
    apple = yf.Ticker(x)
    apple_info = apple.info
    y = 0
    if not apple_info or 'shortName' not in apple_info:
        print("Ticker not found.")
        try:
            y = int(input("If you want to try again, press 1 (or any other key to exit): "))
            if y != 1:
                print("Exiting...")
                exit()
        except:
            exit()
lista = list()
k = 1
for i in apple_info.keys():
    lista.append(f"{k}. {i}")
    k += 1
print("Below is brief history")
print(apple.history(period="max").head())
print("Available information options:")
for item in lista:
    print(item)
q=input("If you want to search by number pres 1\nIf you want search by key pres 2 ")
try:
    q=int(q)
except:
    print("invalid input")
    exit()
if q==1:
    z = input("Choose number! What information do you want to know? ")

    while not z.isdigit() or int(z) < 1 or int(z) > len(lista):
        z = input(f"Invalid number, please try again (between 1 and {len(lista)}): ")

    z = int(z) - 1
    chosen_key = lista[z].split(". ")[1]

    chosen_value = apple_info.get(chosen_key, "No information available for this key.")
    print(f"Information for {chosen_key}: {chosen_value}")
elif q==2:
    z=input("write which information do you want")
    try:
        print(apple_info[z])
    except:
        print("there is no key",z)
else:
    print("invalid input")
    exit()






