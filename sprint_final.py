
# CREAMOS LAS CLASES DEL MODELO

class Proveedor:
    def __init__(self, id, nombre,tipoProducto):
        self.id = id
        self.nombre = nombre
        self.tipoProducto = tipoProducto
        self.listaBodegas = []
        self.listaProductos = []
    
    def inscripcionBodega(self,bodega):
        self.listaBodegas.append(bodega)

    def crearProductos(self):
        sku = 1#input('Ingresar código : ')
        nombre_producto =  'polera'#input('Ingresar producto : ')
        categoria = 'polera'#input('Ingresar categoría : ')
        valor_neto = 'polera'#input('Ingresar valor neto : ')
        proveedor ='polera' #input('Ingresar proveedor : ')
        stock = 'polera'#input('Ingresar stock : ')
        lista = []
        for datos in [sku, nombre_producto, categoria, valor_neto, proveedor, stock]:
            lista.append(datos)
        self.listaProductos.append(lista) 
        print(self.listaProductos)

    def modificarProducto(self):
        sku = input('Modificar código : ')
        if (sku in self.listaProductos):
            nombre_producto = input('Modificar producto : ')
            categoria = input('Modificar categoría : ')
            valor_neto = input('Modificar valor neto : ')
            proveedor = input('Modificar proveedor : ')
            stock = input('Modificar stock : ')
            lista = []
            for datos in [sku, nombre_producto, categoria, valor_neto, proveedor, stock]:
                lista.append(datos)
            self.listaProductos.append(datos) 
            print(self.listaProductos)
        else:
            print('El producto no existe...')


class Bodega:
    def __init__(self,id,nombre,cantidad_total):
        self.id = id
        self.nombre = nombre
        self.cantidad_total = cantidad_total
        self.listaProveedores =[] #list(proveedores)
        #self.proveedores.append(proveedores)
        self.productosBodega = []
        #self.productos.append(productos)
        self.transferencia = []

    def agregar_proveedor(self,*proveedor:Proveedor):
        for agregar in proveedor:
            self.listaProveedores.append(agregar)
        print(self.listaProveedores)
        return self.listaProveedores

    def eliminar_proveedor(self,*proveedor:Proveedor):
        for eliminar in proveedor:
            self.listaProveedores.remove(eliminar)
        print(self.listaProveedores)
        return self.listaProveedores
        

    def transferir_productos(self,proveedor:Proveedor):
        if not len(proveedor.listaProductos) <= 0 :
            for datos in proveedor.listaProductos:
                self.productosBodega.append(datos)
                
        else:
            print('El proveedor no tiene productos...')
        print(self.productosBodega)

    def cantidad_total_productos_transferidos(self,proveedor:Proveedor):
        print(f'La cantidad de producto transferido: {len(proveedor.listaProductos)}')

    def mostrar_productos_tranferidos(self,proveedor:Proveedor):
        for i in proveedor.listaProductos:
            print(f'´productos ---> {i}')
    
    def mostrar_total_productoBodega(self):
        return f'Cantidad total de productos en bodega : {len(self.productosBodega)}'

class Usuario:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def mostrarProveedores(self,bodega:Bodega):
        for proveedor in bodega.listaProveedores:
            print(proveedor)

class Operario(Usuario):
    def mostrarProveedores(self,bodega:Bodega):
        super().mostrarProveedores(bodega)


class Administradores(Usuario):
    def __init__(self,id, nombre,bodega:Bodega):
        super().__init__(id, nombre)
        self.bodega = bodega

    def mostrarProveedores(self,bodega:Bodega):
        super().mostrarProveedores(bodega)
    
    def verstock(self,bodega:Bodega):
        return f'Cantidad total de productos en bodega : {len(bodega.productosBodega)}'


# PROBAR PRODUCTOS
proveedor1 = Proveedor(111,'unimarc','lacteos')
proveedor2 = Proveedor(111,'santaisabel','lacteos')
print('*'*60)
#CREAR PRODUCTOS DESDE PROVEEDOR
proveedor1.crearProductos()
proveedor1.crearProductos()
proveedor1.crearProductos()
proveedor2.crearProductos()
print('*'*60)
# INSTANCIO UNA BODEGA
bodega1 = Bodega('aa','Bodega1',2000,)
# INSTANCIO UN OPERARIO
operario1= Usuario(11111,'Marcos')
# INSTANCIO UN ADMINISTRADOR
administrador1 = Administradores(333333,'Neifer',bodega1)
# INSTANCIO UN USUARIO
Usuario1 = Usuario(22222,'Ronald')
# METODOS DE BODEGA
bodega1.transferir_productos(proveedor1)
print('*'*60)
bodega1.cantidad_total_productos_transferidos(proveedor1)
print('*'*60)
bodega1.mostrar_productos_tranferidos(proveedor1)
print('*'*60)
bodega1.transferir_productos(proveedor2)
print('*'*60)
bodega1.cantidad_total_productos_transferidos(proveedor2)
print('*'*60)
bodega1.mostrar_productos_tranferidos(proveedor2)
print('*'*60)
print(bodega1.mostrar_total_productoBodega())
print('*'*60)
print(bodega1.agregar_proveedor(proveedor1.nombre, proveedor2.nombre))
print('*'*60)
# METODOS DE USUARIO
Usuario1.mostrarProveedores(bodega1)
print('*'*60)
operario1.mostrarProveedores(bodega1)
print('*'*60)
# METODO DE ADMINISTRADOR
administrador1.mostrarProveedores(bodega1)
print('*'*60)
print(administrador1.verstock(bodega1))
print('*'*60)






