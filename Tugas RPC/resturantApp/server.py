# Server Side
from xmlrpc.server import SimpleXMLRPCServer

# Operation Side (Restaurant Prgramming)


def pesanan(food, drink, foodQTY, drinkQTY):
    '''
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
    '''

    foodData = [[1, "Ayam Bakar", 25000], [2, "Ikan Bakar", 20000], [
        3, "Udang Bakar", 27000], [4, "Nasi Goreng", 22000], [5, "Burger", 15000]]
    drinkData = [[1, "Jus Alpukat", 15000], [2, "Teh Manis", 7000], [
        3, "ExtraJoss + Susu", 10000], [4, "Jus Buah Naga", 20000], [5, "Kopi Hitam", 17000]]

    record_data = [foodData[0], drinkData[0], foodData[2], drinkData[2]]

    food = int(record_data[0])
    drink = int(record_data[1])
    foodQTY = int(record_data[2])
    drinkQTY = int(record_data[3])

    foodResult = food * foodQTY
    drinkResult = drink * drinkQTY

    result = (
        f"Jadi total yang harus anda bayar adalah {foodResult + drinkResult}")

    # result = foodResult + drinkResult
    return result


# RPC Initialize SIde
server = SimpleXMLRPCServer(('localhost', 8000))
server.register_function(pesanan, "pesanan")

print("SERVER IS STARTING RIGHT NOW  . . . ")

server.serve_forever()
