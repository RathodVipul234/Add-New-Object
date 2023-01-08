from .widgets import RelatedFieldWidgetWrapper1
from django import forms
from .models import *
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper, FilteredSelectMultiple
from django.forms.widgets import Select
from django.contrib.admin import site as admin_site


class manytomany3manytomanyform(forms.ModelForm):
    class Meta:
        model = manytomany3manytomany 
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(manytomany3manytomanyform, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['required'] = False

class manytomany3foreignkeyform(forms.ModelForm):
    class Meta:
        model = manytomany3foreignkey
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(manytomany3foreignkeyform, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['required'] = False


class Manytomany3ModelForm(forms.ModelForm):
    class Meta:
        model = manytomany3
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(Manytomany3ModelForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['manytomany_link'].widget = RelatedFieldWidgetWrapper1(
                                                widget = FilteredSelectMultiple(('manytomany_link'),False),
                                                rel = manytomany3._meta.get_field('manytomany_link').remote_field,
                                                admin_site = admin_site,
                                                form_obj = manytomany3manytomanyform
                                                )
        self.fields['foreignkey_link'].widget = RelatedFieldWidgetWrapper1(
                                                widget = Select(attrs={'class': 'select'}),
                                                rel = manytomany3._meta.get_field('foreignkey_link').remote_field,
                                                admin_site = admin_site,
                                                form_obj=manytomany3foreignkeyform
                                                )
        self.fields['manytomany_link'].queryset = manytomany3manytomany.objects.all()
        self.fields['foreignkey_link'].queryset = manytomany3foreignkey.objects.all()
