carrito=[]
n_productos=int(input("ingresa el numero de productos carrito:"))
for i in range(n_productos):
    producto=input("ingresa el producto a tu ccarrito:")
    carrito.append(producto)
print("lista creada correctamente")
carrito[0]="barritas"
print(carrito[0])
print(carrito[1])
print(carrito)



