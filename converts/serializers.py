
from rest_framework import serializers
from converts.models import Convert
# from users import serializers
# from users.serializers import UserSerializer

import string


class ConvertSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Convert
        fields = '__all__'

    def validate(self, datas):
        if len(datas.keys()) == 1:
            raise serializers.ValidationError({"message": "Vous devez entrer une valeur à convertir."})
        if len(datas.keys()) > 2:
            raise serializers.ValidationError({"message": "Vous devez entrer une seule valeur à convertir."})
        return datas

    def validate_value_dec(self, value):
        if not all(c in string.digits for c in value):
            raise serializers.ValidationError({"message": f"{value} n'est pas une valeur décimale!"})
        return value

    def validate_value_bin(self, value):
        if not all(c in ['0', '1'] for c in value):
            raise serializers.ValidationError({"message": f"{value} n'est pas une valeur binaire!"})
        return value

    def validate_value_hex(self, value):
        if not all(c in string.hexdigits for c in value):
            raise serializers.ValidationError({"message": f"{value} n'est pas une valeur hexadécimale!"})
        return value

    def create(self, validated_data):
        convert = Convert(value_dec=validated_data.get('value_dec'),
                          value_bin=validated_data.get('value_bin'),
                          value_hex=validated_data.get('value_hex'))
        data = Convert.convert(convert)
        return Convert.objects.create(value_dec=data.get('dec'),
                                      value_bin=data.get('bin'),
                                      value_hex=data.get('hex'),
                                      base=data.get('base'),
                                      user=validated_data.get('user'))


class ClearSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Convert
        fields = '__all__'
    