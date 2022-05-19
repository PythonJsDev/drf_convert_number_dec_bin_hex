from django.db import models
# from djangoHexadecimal.fields import HexadecimalField
from typing import Dict


class Convert(models.Model):
    value_dec = models.CharField(max_length=25, blank=True, null=True)
    value_bin = models.CharField(max_length=25, blank=True, null=True)
    value_hex = models.CharField(max_length=25, blank=True, null=True)
    base = models.CharField(max_length=3, blank=True, null=True)

    user = models.ForeignKey("users.User", related_name="converts", on_delete=models.CASCADE)

    # class Bases(models.TextChoices):
    #     BINAIRE = 'Bin', 'Binaire'
    #     DECIMAL = 'Dec', 'Decimal'
    #     HEXADECIMAL = 'Hex', 'Business'

    # base = models.CharField(max_length=3, choices=Bases.choices)

    def convert(self) -> Dict:
        data = {}
        if self.value_bin:
            data['base'] = 'bin'
            data['bin'] = self.value_bin
            data['dec'] = str(int(self.value_bin, 2))
            data['hex'] = str(hex(int(self.value_bin, 2))[2::].upper())
            return data
        if self.value_dec:
            data['base'] = 'dec'
            data['dec'] = self.value_dec
            data['bin'] = str(bin(int(self.value_dec, 10))[2::])
            data['hex'] = str(hex(int(self.value_dec, 10))[2::].upper())
            return data
        if self.value_hex:
            data['base'] = 'hex'
            data['hex'] = self.value_hex
            data['bin'] = str(bin(int(self.value_hex, 16))[2::])
            data['dec'] = str(int(self.value_hex, 16))
            return data
