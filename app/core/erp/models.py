from django.db import models
from datetime import datetime

# Create your models here.
class Client(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombres')
    surnames = models.CharField(max_length=150, verbose_name='Apellidos')
    age = models.PositiveIntegerField(verbose_name='Edad')
    sex = models.CharField(max_length=50, verbose_name='Sexo')
    birthdate = models.DateField(verbose_name='Fecha de nacimiento')
    telephone = models.CharField(max_length=10, verbose_name='Teléfono')
    email = models.EmailField(max_length=150, verbose_name='Correo electrónico')
    address = models.CharField(max_length=200, verbose_name='Dirección')
    history_medical_number = models.CharField(max_length=10, verbose_name='Número de historia clinica')
    last_eye_exam = models.DateField(verbose_name='Ultimo examen de la vista')
    frame_only = models.BooleanField(default=False, verbose_name='Compra solo armazón')
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    def __str__(self):
        return self.names + ' ' + self.surnames

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'cliente'
        ordering = ['id']


class EyesGraduation(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Cliente')

    eye_choice = [('derecho', 'Derecho'), ('izquierdo', 'Izquierdo'), ('ambos', 'Ambos')]

    select_eye = models.CharField(max_length=50, choices=eye_choice, verbose_name='Ojo a graduar')

    sph = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Esfera')
    cyl = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Cilindro')
    axis = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Eje')
    ao = models.DecimalField(max_digits=5, decimal_places=2,  null=True, blank = True, verbose_name='Altura de oblea')
    add = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Adición')
    prism = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Prisma')
    base = models.CharField(max_length=50, null=True, blank=True, verbose_name='Base')
    observation = models.TextField(max_length=200, verbose_name='Observación')

    def __str__(self):
        return self.client.names + ' ' + self.client.surnames

    class Meta:
        verbose_name = 'Graduación de ojos'
        verbose_name_plural = 'Graduaciones de ojos'
        db_table = 'graduacion_ojos'
        ordering = ['id']



class Departament(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    description = models.CharField(max_length=100, verbose_name='Descripción')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        db_table = 'departamento'
        ordering = ['id']

class Jobs(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    description = models.CharField(max_length=100, verbose_name='Descripción')
    departament = models.ForeignKey(Departament, on_delete=models.CASCADE, verbose_name='Departamento')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Puesto'
        verbose_name_plural = 'Puestos'
        db_table = 'puesto'
        ordering = ['id']



class Employee(models.Model):
    names = models.CharField(max_length=50, verbose_name='Nombres')
    lastname = models.CharField(max_length=50, verbose_name='Apellidos')
    password = models.CharField(max_length=10, verbose_name='Contraseña')
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE, verbose_name='Puesto')
    sex = models.CharField(max_length=50, verbose_name='Sexo')
    email = models.EmailField(max_length=50, verbose_name='Correo electrónico')
    phone = models.CharField(max_length=50, verbose_name='Teléfono')
    address = models.CharField(max_length=50, verbose_name='Dirección')
    age = models.PositiveIntegerField(verbose_name='Edad')
    salary = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Salario')
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True, verbose_name='Avatar')
    cvitae = models.FileField(upload_to='cvitae/%Y/%m/%d', null=True, blank=True, verbose_name='Currículum')
    state = models.BooleanField(default=True, verbose_name='Estado')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    def __str__(self):
        return self.names


    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['id']



class HeadOffice(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre', unique=True)
    address = models.CharField(max_length=100, verbose_name='Dirección')
    telephone = models.CharField(max_length=10, verbose_name='Teléfono')
    email = models.EmailField(max_length=50, verbose_name='Correo electrónico')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    ceo = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='CEO')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Sucursal Matriz'
        verbose_name_plural = 'Sucursales Matrices'
        db_table = 'sucursal_matriz'
        ordering = ['id']

class BranchOffice(models.Model):
    name = models.CharField(max_length=50, blank=False, verbose_name='Nombre', unique=True)
    address = models.CharField(max_length=100, blank=False, verbose_name='Dirección')
    telephone = models.CharField(max_length=10, blank=False, verbose_name='Teléfono')
    email = models.EmailField(max_length=50, verbose_name='Correo electrónico')
    city = models.CharField(max_length=50, verbose_name='Ciudad')
    state = models.CharField(max_length=50, verbose_name='Estado')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    head_office = models.ForeignKey(HeadOffice, on_delete=models.CASCADE, verbose_name='Sucursal matriz')
    branch_manager = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Gerente de sucursal')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Sucursal'
        verbose_name_plural = 'Sucursales'
        db_table = 'sucursal'
        ordering = ['id']



class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre', unique=True)
    description = models.CharField(max_length=100, verbose_name='Descripción')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        db_table = 'categoria'
        ordering = ['id']

class DepartamentProduct(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre', unique=True)
    description = models.CharField(max_length=100, verbose_name='Descripción')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Departamento de producto'
        verbose_name_plural = 'Departamentos de productos'
        db_table = 'departamento_producto'
        ordering = ['id']


class Product(models.Model):
    key = models.CharField(max_length=50, verbose_name='Clave', unique=True)
    name = models.CharField(max_length=50, verbose_name='Nombre', unique=True)
    description = models.CharField(max_length=100, verbose_name='Descripción')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoría')
    departament = models.ForeignKey(DepartamentProduct, on_delete=models.CASCADE, verbose_name='Departamento')
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio')
    price_purchase = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio de compra')
    stock = models.IntegerField(default=0, verbose_name='Existencia')
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True, verbose_name='Imagen')
    state = models.BooleanField(default=True, verbose_name='Estado')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    taxes = models.DecimalField(default=0.00, max_digits=2, decimal_places=2, verbose_name='Impuestos')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'producto'
        ordering = ['id']


class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Cliente')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Empleado')
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de venta')
    branch_office = models.ForeignKey(BranchOffice, on_delete=models.CASCADE, verbose_name='Sucursal')
    payment_method = models.CharField(max_length=50, verbose_name='Método de pago')
    amount_paid = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Monto pagado')
    credit = models.BooleanField(default=False, verbose_name='Crédito')
    credit_amount = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Monto de crédito')
    credit_limit = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Límite de crédito')
    credit_days = models.IntegerField(default=0, verbose_name='Días de crédito')
    due_date = models.DateField(null=True, blank=True, verbose_name='Fecha de vencimiento')
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Total')
    state = models.BooleanField(default=True, verbose_name='Estado')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    def __str__(self):
        return self.client.names + ' ' + self.employee.names

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        db_table = 'venta'
        ordering = ['id']


class DetailSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, verbose_name='Venta')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Producto')
    qty = models.IntegerField(default=0, verbose_name='Cantidad')
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Subtotal')
    discount = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Descuento')

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Detalle de venta'
        verbose_name_plural = 'Detalles de venta'
        db_table = 'detalle_venta'
        ordering = ['id']



class Quote(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Cliente')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Empleado')
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de cotización')  # Sin paréntesis
    branch_office = models.ForeignKey(BranchOffice, on_delete=models.CASCADE, verbose_name='Sucursal')
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Total')
    state = models.BooleanField(default=True, verbose_name='Estado')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    def __str__(self):
        return self.client.names + ' ' + self.employee.names

    class Meta:
        verbose_name = 'Cotización'
        verbose_name_plural = 'Cotizaciones'
        db_table = 'cotizacion'
        ordering = ['id']


class DetailQuote(models.Model):
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE, verbose_name='Cotización')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Producto')
    qty = models.IntegerField(default=0, verbose_name='Cantidad')
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Subtotal')
    discount = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Descuento')

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Detalle de cotización'
        verbose_name_plural = 'Detalles de cotización'
        db_table = 'detalle_cotizacion'
        ordering = ['id']




""""
Faltan modelos de inventario y traspasos



class CentralWarehouse(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    address = models.CharField(max_length=100, verbose_name='Dirección')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    manager = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Gerente de almacén')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Almacén central'
        verbose_name_plural = 'Almacenes centrales'
        db_table = 'almacen_central'
        ordering = ['id']


"""
