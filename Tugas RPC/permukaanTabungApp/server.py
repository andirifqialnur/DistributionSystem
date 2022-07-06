from xmlrpc.server import SimpleXMLRPCServer


def permukaanTabung(r, t):
    phi = 3.14
    result = 2 * phi * r * (r + t)
    return result


server = SimpleXMLRPCServer(("localhost", 8000))
print("Server is STARTING . . . ")

server.register_function(permukaanTabung, "permukaanTabung")

server.serve_forever()
