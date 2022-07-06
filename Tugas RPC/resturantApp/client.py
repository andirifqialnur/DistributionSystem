# Client Side
from xmlrpc import server
import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://localhost:8000")

print('''
        food 1 = Ayam Bakar (25000)
        food 2 = Ikan Bakar (20000)
        food 3 = Udang Bakar (27000)
        food 4 = Nasi Goreng (22000)
        food 5 = Burger (15000)

        drink 1 = Jus Alpukat (15000)
        drink 2 = Teh Manis (7000)
        drink 3 = ExtraJoss + Susu (10000)
        drink 4 = Jus Buah Naga (20000)
        drink 5 = Kopi Hitam (17000)
    ''')

food_Input = input(
    "Silahkan pilih menu masakan anda dengan mengetikkan nomornya : ")
food_qty = input("Berapa Kuantitas yang anda inginkan : ")
drink_Input = input(
    "Silahkan pilih nminuman anda dengan mengetikkan nomornya : ")
drink_qty = input("Berapa Kuantitas yang anda inginkan : ")


result = server.pesanan(int(food_Input), int(food_qty),
                        int(drink_Input), int(drink_qty),)

print(result)
