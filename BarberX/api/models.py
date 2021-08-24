from django.db import models

# Create your models here.
class Cliente(models.Model):

    class Meta:

        db_table = 'cliente'

    name = models.CharField(max_length=100, blank=False)
    surname = models.CharField(max_length=100, blank=False)
    endereco = models.CharField(max_length=100, blank=False)
    endereco_lat = models.DecimalField(max_digits=10, decimal_places=8)
    endereco_lng = models.DecimalField(max_digits=10, decimal_places=8)
    phone = models.CharField(max_length=15, blank=False)
    avatar = models.URLField()
    email = models.EmailField(blank=False)
    password = models.CharField(max_length=100, blank=False)
    cpf = models.CharField(max_length=15, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
            return  self.name

class Barbearia(models.Model):

    class Meta:

        db_table = 'barbearia'

    name = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=15, blank=False)
    endereco = models.CharField(max_length=100, blank=False)
    endereco_lat = models.DecimalField(max_digits=10, decimal_places=8)
    endereco_lng = models.DecimalField(max_digits=10, decimal_places=8)
    avatar = models.URLField()
    bio = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    password = models.CharField(max_length=100, blank=False)
    document = models.CharField(max_length=50, blank=False)
    date_closed = models.DateField(auto_now=False, null=True)
    open_hour = models.TimeField(auto_now=False, null=True)
    closed_hour = models.TimeField(auto_now=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
            return  self.name

class Servico(models.Model):

    class Meta:

        db_table = 'servico'

    name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=100, blank=False)
    avatar = models.URLField()
    price = models.FloatField(blank=False)
    barbearia = models.ForeignKey(Barbearia, on_delete=models.PROTECT, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
            return  self.name

class Ordem_Servico(models.Model):

    class Meta:

        db_table = 'ordem_servico'

    barbearia = models.ForeignKey(Barbearia, on_delete=models.PROTECT, blank=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, blank=False)
    servico = models.ForeignKey(Servico, on_delete=models.PROTECT, blank=False)
    # comentario = QuillField()
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True)
    avaliacao = models.FloatField()

    def __str__(self):
            return  str(self.servico)


class Agenda(models.Model):

    class Meta:

        db_table = 'agenda'

    data = models.DateTimeField(auto_now=False, auto_now_add=False, blank=False)
    barbearia = models.ForeignKey(Barbearia, on_delete=models.PROTECT, blank=False)
    servico = models.ForeignKey(Servico, on_delete=models.PROTECT, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.data)