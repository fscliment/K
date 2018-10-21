from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from datetime import date

# Defina sus constantes en esta sección
# EXPERIENCE_CHOICES serán las únicas dos opciones que se podrán seleccionar al momento de crear un objeto de la clase
# Experiencia. La Base de Datos almacenará solamente el carácter (1 byte), en lugar de almacenar toda la cadena de
# caracteres, Django se encargará de hacer la vinculación clave-valor según el caracter almacenado en la BD para ese objeto.
EXPERIENCE_CHOICES = (
    ('1', 'Habilidad'),
    ('2', 'Experiencia'),
)

# Creando los modelos de la base de datos
class Perfil(models.Model):
    autor = models.CharField('Autor', max_length = 64, blank=False, null=False)
    nombre = models.CharField('Nombre', max_length = 64, blank=False, null=False)
    direccion = models.CharField('Dirección', max_length=128, blank=False, null=False)
    telefono = models.CharField('Teléfono', max_length=32, blank=False, null=False)
    email = models.CharField('Correo Electrónico', max_length=64, blank=False, null=False)
    webpage = models.CharField('Página Web', max_length=64)
    puesto = models.CharField('Puesto de Trabajo', max_length=64, blank=False, null=False)
    imagen = models.ImageField('Imagen', upload_to="perfil_imagenes", blank=False, null=False)
    cv = models.FileField('Resumen', upload_to="perfil_cv", blank=True, null=True, max_length=32768)
    fecha_nacimiento = models.DateField('Fecha de nacimiento', blank=False, null=False)

    def __str__(self):
        return self.nombre

    # Función para limitar la clase a que sólo pueda existir una única instancia de esa clase.
    def clean(self):
        modelo = self.__class__
        if (modelo.objects.count() > 0 and
                self.id != modelo.objects.get().id):
            raise ValidationError("Sólo puedes crear 1 Instancia de %s " % modelo.__name__)

    # Función para calcular la edad en años dada una fecha de nacimiento.
    def edad(self):
        diff = (date.today() - self.fecha_nacimiento).days
        edad = str(int(diff / 365)) # Edad en años
        return edad

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfil'

class Proyecto(models.Model):
    titulo = models.CharField('Título', max_length = 64, blank=False, null=False)
    descripcion = models.TextField('Descripción', max_length=256, blank=False, null=False)
    tags = models.CharField('Etiquetas', max_length=64, blank=True, null=True, help_text="Separe las etiquetas con una coma: tag1,tag2,tag3...")
    url = models.URLField('URL', max_length=128)
    imagen = models.ImageField(upload_to="proyectos_imagenes")
    empresa = models.CharField('Título', max_length = 64, blank=False, null=False)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

class Referencia(models.Model):
    nombre = models.CharField('Nombre', max_length = 64, blank=False, null=False)
    puesto = models.CharField('Puesto de Trabajo', max_length=64, blank=False, null=False)
    empresa = models.CharField('Empresa', max_length=64, blank=False, null=False)
    comentario = models.TextField('Comentario', max_length=512, blank=False, null=False)
    imagen = models.ImageField(upload_to="referencias_imagenes")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Referencia'
        verbose_name_plural = 'Referencias'

class Experiencia(models.Model):
    nombre = models.CharField('Nombre', max_length = 64, blank=False, null=False)
    porcentaje = models.IntegerField('Porcentaje', blank=False, null=False,
                              validators = [MinValueValidator(0), MaxValueValidator(100)])
    # El tipo de Experiencia se divide en: Habilidad y Conocimiento.
    # Los que son del tipo Habilidad se muestran en los gráficos circulares.
    # Los que son del tipo Conocimiento se muestran en los gráficos lineales.
    # '1' = Habilidad, '2' = Conocimiento
    tipo = models.CharField('Tipo', choices=EXPERIENCE_CHOICES, default='1', max_length = 1, blank=False, null=False)


    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Experiencia'
        verbose_name_plural = 'Experiencias'

class Reconocimiento(models.Model):
    titulo = models.CharField('Título', max_length = 64, blank=False, null=False)
    descripcion = models.TextField('Descripción', max_length = 512, blank=False, null=False)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Reconocimiento'
        verbose_name_plural = 'Reconocimientos'