from django.db import models


class Dispositivo(models.Model):
    versao_app = models.CharField(max_length=20)
    imei = models.CharField(max_length=20)
    serial_number = models.CharField(max_length=20)

class InformacaoCTe(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, related_name='inf_cte', on_delete=models.CASCADE)
    ch_md_fe = models.CharField(max_length=12)
    ch_cte = models.CharField(max_length=12)
    dh_chegada = models.DateTimeField()
    dh_reg_sistema = models.DateTimeField()
    cod_ocorrencia = models.CharField(max_length=2)

