from rest_framework import serializers
from .models import Dispositivo, InformacaoCTe

class InformacaoCTeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformacaoCTe
        fields = '__all__'
        extra_kwargs = {'dispositivo': {'required': False}}  # Adicione isso para evitar exigência na requisição

class DispositivoSerializer(serializers.ModelSerializer):
    inf_cte = InformacaoCTeSerializer(many=True)

    class Meta:
        model = Dispositivo
        fields = '__all__'

    def create(self, validated_data):
        inf_cte_data = validated_data.pop('inf_cte', [])  # Use o pop para remover inf_cte do validated_data
        dispositivo = Dispositivo.objects.create(**validated_data)
        for item in inf_cte_data:
            InformacaoCTe.objects.create(dispositivo=dispositivo, **item)
        return dispositivo
