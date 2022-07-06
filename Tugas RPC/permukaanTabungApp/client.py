from http import server
import xmlrpc.client

server = xmlrpc.client.ServerProxy('http://localhost:8000')

r = input("Masukkan Jari-jari : ")
t = input("Masukkan Tinggi : ")

hasil = server.permukaanTabung(int(r), int(t))

print("Hasilnya = ", hasil)
