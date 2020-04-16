from django import forms

from core.models import ServiciosCliente


class ServicioClienteForm(forms.ModelForm):
    ESTADOS = (
        ('PENDIENTE', 'PENDIENTE'),
        ('EN PROGRESO', 'EN PROGRESO'),
        ('FINALIZADO', 'FINALIZADO'),
    )
    estado = forms.ChoiceField(choices=ESTADOS)

    class Meta:
        model = ServiciosCliente
        fields = '__all__'
