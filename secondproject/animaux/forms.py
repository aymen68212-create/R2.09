from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class EspeceForm(ModelForm):
    class Meta:
        model = models.Espece
        fields = ('nom', 'origine', 'est_dangereux')
        labels = {
            'nom': _('Nom'),
            'origine': _('Origine'),
            'est_dangereux': _('Est_dangereux'),
        }

class AnimalForm(ModelForm):
    class Meta:
        model = models.Animal
        fields = ('nom', 'age', 'espece', 'description')
        labels = {
            'nom': _('Nom'),
            'age': _('Age'),
            'espece': _('Espece'),
            'description': _('Description'),
        }