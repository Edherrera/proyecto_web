from django.db import models

# Create your models here.

from apps.acudiente.models import persona

class antecedentes_medicos(models.Model):
    descripcion = models.TextField()

    def __str__(self) -> str:
        return self.descripcion

class Alumna(models.Model):
   
    GENERO = [
        ('F', 'Femenino'),
    ]

    IDENTIFICACION = [
        ('RE', 'Registro Civil'),
        ('TI', 'Targeta Identidad'),
        ('CE', 'Cedula'),
    ]
    
    GRUPO = [
        ('RO', 'O+'),
        ('RA', 'A+'),
        ('RA2', 'A-'),
        ('RB', 'B+'),
        ('RB2', 'B-'),
        ('RAB', 'AB+'),
        ('RAB2', 'AB-'),
        ('RO2', 'O-'),
    ]

    CURSO = [
        ('TR', 'Transicion'),
        ('PR', 'Primero'),
        ('SE', 'Segundo'),
        ('TE', 'Tercero'),
        ('CUA', 'Cuarto A'),
        ('CUB', 'Cuarto B'),
        ('QUA', 'Quinto A'),
        ('QUB', 'Quinto B'),
        ('SEA', 'Sexto A'),
        ('SEB', 'Sexto B'),
        ('SPA', 'Septimo A'),
        ('SPB', 'Septimo B'),
        ('OCA', 'Octavo A'),
        ('OCB', 'Octavo B'),
        ('NOA', 'Noveno A'),
        ('NOB', 'Noveno B'),
        ('NOC', 'Noveno C'),
        ('DEA', 'Decimo A'),
        ('DEB', 'Decimo B'),
        ('DEC', 'Decimo C'),
        ('ONA', 'Once A'),
        ('ONB', 'Once B'),
        ('ONC', 'Oce C'),

    ]

    MATRICULA = [
        ('I', 'Interna'),
        ('E', 'Externa'),
    ]

    codigo = models.CharField(max_length=10,primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    tipo_identificacion = models.CharField(max_length=12, choices=IDENTIFICACION)
    identificacion = models.IntegerField(null=True)
    sexo = models.CharField(max_length=10, choices=GENERO)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    modalidad_matricula = models.CharField(max_length=15, choices=MATRICULA)
    fecha_ingreso = models.DateField()
    grado = models.CharField(max_length=20, choices=CURSO)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    eps = models.CharField(max_length=20)
    arl = models.CharField(max_length=20)
    grupo_rh = models.CharField(max_length=10, choices=GRUPO)
    hobby = models.CharField(max_length=20)
    persona = models.ForeignKey(persona, null = True, blank= True, on_delete = models.CASCADE)
    antecedentes_medicos = models.ManyToManyField(antecedentes_medicos)

    def __str__(self) -> str:
        return self.nombres + '  ' + self.apellidos + ' - ' + str(self.codigo)