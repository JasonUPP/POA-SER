from django import forms
from django.forms import ModelForm
from apps.anteproyecto.models import *

class ApForm(forms.ModelForm):
    class Meta:
        model = AnteProyecto
        fields = {'nombre', 'user', 'totalA', 'imagen', 'estado'}
        widgets = {
        'nombre': forms.TextInput(attrs={'class':'form-control'}),
        'user': forms.Select(attrs={'class':'form-control'}),
        'totalA':forms.NumberInput(attrs={'class':'form-control'}),
        'estado': forms.Select(attrs={'class':'form-control'}),
        }


class FilaForm(forms.ModelForm):
    class Meta:
        model = Fila
        fields = ('anteProyecto', 'capitulo', 'concepto', 'partidagenerica', 'partidaespecifica','enero', 'febrero', 'marzo',
        'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre', 'totalF')

        widgets = {
        'anteProyecto': forms.Select(attrs={'class':'form-control'}),
        'capitulo': forms.Select(attrs={'class':'form-control'}),
        'concepto': forms.Select(attrs={'class':'form-control'}),
        'partidagenerica': forms.Select(attrs={'class':'form-control'}),
        'partidaespecifica': forms.Select(attrs={'class':'form-control'}),
        'enero':forms.NumberInput(),
        'febrero':forms.NumberInput(),
        'marzo':forms.NumberInput(),
        'abril':forms.NumberInput(),
        'mayo':forms.NumberInput(),
        'junio':forms.NumberInput(),
        'julio':forms.NumberInput(),
        'agosto':forms.NumberInput(),
        'septiembre':forms.NumberInput(),
        'octubre':forms.NumberInput(),
        'noviembre':forms.NumberInput(),
        'diciembre':forms.NumberInput(),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['concepto'].queryset = Concepto.objects.none()
        self.fields['partidagenerica'].queryset = PartidaGenerica.objects.none()
        self.fields['partidaespecifica'].queryset = PartidaEspecifica.objects.none()

        if 'concepto' in self.data:
            try:
                capitulo_id = int(self.data.get('capitulo'))
                self.fields['concepto'].queryset = Concepto.objects.filter(capitulo_id=capitulo_id).order_by('id')
            except (ValueError, TypeError):
                pass #entrada inválida del cliente; ignorar y retroceder a un Queryset de concepto vacío
        elif self.instance.pk:
            self.fields['concepto'].queryset = self.instance.capitulo.concepto_set.order_by('id')

        if 'partidagenerica' in self.data:
            try:
                concepto_id = int(self.data.get('concepto'))
                self.fields['partidagenerica'].queryset = PartidaGenerica.objects.filter(concepto_id=concepto_id).order_by('id')
            except (ValueError, TypeError):
                pass #entrada inválida del cliente; ignorar y retroceder a un Queryset de pg vacío
        elif self.instance.pk:
            self.fields['partidagenerica'].queryset = self.instance.concepto.partidagenerica_set.order_by('id')

        if 'partidaespecifica' in self.data:
            try:
                partidaGenerica_id = int(self.data.get('partidagenerica'))
                self.fields['partidaespecifica'].queryset = PartidaEspecifica.objects.filter(partidaGenerica_id=partidaGenerica_id).order_by('id')
            except (ValueError, TypeError):
                pass #entrada inválida del cliente; ignorar y retroceder a un Queryset de pe vacío
        elif self.instance.pk:
            self.fields['partidaespecifica'].queryset = self.instance.partidagenerica.partidaespecifica_set.order_by('id')

class CapituloForm(forms.ModelForm):
    class Meta:
        model = Capitulo
        fields = {'numero'}
        widgets = {
        'numero':forms.NumberInput(attrs={'class':'form-control'}),
        }

class ConceptoForm(forms.ModelForm):
    class Meta:
        model = Concepto
        fields = {'numero','capitulo'}
        widgets = {
        'numero':forms.NumberInput(attrs={'class':'form-control'}),
        'capitulo': forms.Select(attrs={'class':'form-control'}),
        }

class PGForm(forms.ModelForm):
    class Meta:
        model = PartidaGenerica
        fields = {'numero','concepto'}
        widgets = {
        'numero':forms.NumberInput(attrs={'class':'form-control'}),
        'concepto': forms.Select(attrs={'class':'form-control'}),
        }

class PEForm(forms.ModelForm):
    class Meta:
        model = PartidaEspecifica
        fields = {'numero','nombre','descripcion','partidaGenerica'}
        widgets = {
        'numero':forms.NumberInput(attrs={'class':'form-control'}),
        'nombre': forms.TextInput(attrs={'class':'form-control'}),
        'descripcion': forms.TextInput(attrs={'class':'form-control'}),
        'partidaGenerica': forms.Select(attrs={'class':'form-control'}),
        }
