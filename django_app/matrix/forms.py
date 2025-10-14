from django.forms import ModelForm
from . import models

from django import forms

from django.core.exceptions import ValidationError



class Table21(forms.Form):
    row1_column1 = forms.FloatField(initial=0, required=True)
    row2_column1 = forms.FloatField(initial=0, required=True)

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data, "cleaned_data", self.fields)
        if len(cleaned_data.values()) < len(self.fields):
             print("!")
             raise ValidationError("Fields should not be empty")

    def save(self):
        return models.Table21.objects.create(
             **self.cleaned_data
        )


class Table22(forms.Form):
    row1_column1 = forms.FloatField(initial=0, required=True)
    row1_column2 = forms.FloatField(initial=0, required=True)
    row2_column1 = forms.FloatField(initial=0, required=True)
    row2_column2 = forms.FloatField(initial=0, required=True)


    def save(self):
        return models.Table22.objects.create(
             **self.cleaned_data
        )



class Table23(forms.Form):
    row1_column1 = forms.FloatField( initial=0, required=True)
    row1_column2 = forms.FloatField( initial=0, required=True)
    row1_column3 = forms.FloatField( initial=0, required=True)
    row2_column1 = forms.FloatField( initial=0, required=True)
    row2_column2 = forms.FloatField( initial=0, required=True)
    row2_column3 = forms.FloatField( initial=0, required=True)

    
    def save(self):
        return models.Table23.objects.create(
             **self.cleaned_data
        )


class Table24(forms.Form):
    row1_column1 = forms.FloatField( initial=0, required=True)
    row1_column2 = forms.FloatField( initial=0, required=True)
    row1_column3 = forms.FloatField( initial=0, required=True)
    row1_column4 = forms.FloatField( initial=0, required=True)

    row2_column1 = forms.FloatField( initial=0, required=True)
    row2_column2 = forms.FloatField( initial=0, required=True)
    row2_column3 = forms.FloatField( initial=0, required=True)
    row2_column4 = forms.FloatField( initial=0, required=True)


    
    def save(self):
        return models.Table24.objects.create(
             **self.cleaned_data
        )


class Table25(forms.Form):
    row1_column1 = forms.FloatField( initial=0, required=True)
    row1_column2 = forms.FloatField( initial=0, required=True)
    row1_column3 = forms.FloatField( initial=0, required=True)
    row1_column4 = forms.FloatField( initial=0, required=True)
    row1_column5 = forms.FloatField( initial=0, required=True)


    row2_column1 = forms.FloatField( initial=0, required=True)
    row2_column2 = forms.FloatField( initial=0, required=True)
    row2_column3 = forms.FloatField( initial=0, required=True)
    row2_column4 = forms.FloatField( initial=0, required=True)
    row1_column5 = forms.FloatField( initial=0, required=True)


    
    def save(self):
        return models.Table25.objects.create(
             **self.cleaned_data
        )


class Table31(forms.Form):
    row1_column1 = forms.FloatField( initial=0, required=True)
    row2_column1 = forms.FloatField( initial=0, required=True)
    row3_column1 = forms.FloatField( initial=0, required=True)

    
    def save(self):
        return models.Table31.objects.create(
             **self.cleaned_data
        )


class Table32(forms.Form):
    row1_column1 = forms.FloatField( initial=0, required=True)
    row1_column2 = forms.FloatField( initial=0, required=True)
    row2_column1 = forms.FloatField( initial=0, required=True)
    row2_column2 = forms.FloatField( initial=0, required=True)
    row3_column1 = forms.FloatField( initial=0, required=True)
    row3_column2 = forms.FloatField( initial=0, required=True)

    
    def save(self):
        return models.Table32.objects.create(
             **self.cleaned_data
        )


class Table33(forms.Form):
    row1_column1 = forms.FloatField( initial=0, required=True)
    row1_column2 = forms.FloatField( initial=0, required=True)
    row1_column3 = forms.FloatField( initial=0, required=True)
    row2_column1 = forms.FloatField( initial=0, required=True)
    row2_column2 = forms.FloatField( initial=0, required=True)
    row2_column3 = forms.FloatField( initial=0, required=True)
    row3_column1 = forms.FloatField( initial=0, required=True)
    row3_column2 = forms.FloatField( initial=0, required=True)
    row3_column3 = forms.FloatField( initial=0, required=True)

    
    def save(self):
        return models.Table33.objects.create(
             **self.cleaned_data
        )


class Table34(forms.Form):
    row1_column1 = forms.FloatField( initial=0, required=True)
    row1_column2 = forms.FloatField( initial=0, required=True)
    row1_column3 = forms.FloatField( initial=0, required=True)
    row1_column4 = forms.FloatField( initial=0, required=True)

    row2_column1 = forms.FloatField( initial=0, required=True)
    row2_column2 = forms.FloatField( initial=0, required=True)
    row2_column3 = forms.FloatField( initial=0, required=True)
    row2_column4 = forms.FloatField( initial=0, required=True)

    row3_column1 = forms.FloatField( initial=0, required=True)
    row3_column2 = forms.FloatField( initial=0, required=True)
    row3_column3 = forms.FloatField( initial=0, required=True)
    row3_column4 = forms.FloatField( initial=0, required=True)


    def save(self):
        return models.Table34.objects.create(
             **self.cleaned_data
        )


class Table35(forms.Form):
    row1_column1 = forms.FloatField( initial=0, required=True)
    row1_column2 = forms.FloatField( initial=0, required=True)
    row1_column3 = forms.FloatField( initial=0, required=True)
    row1_column4 = forms.FloatField( initial=0, required=True)
    row1_column5 = forms.FloatField( initial=0, required=True)

    row2_column1 = forms.FloatField( initial=0, required=True)
    row2_column2 = forms.FloatField( initial=0, required=True)
    row2_column3 = forms.FloatField( initial=0, required=True)
    row2_column4 = forms.FloatField( initial=0, required=True)
    row2_column5 = forms.FloatField( initial=0, required=True)

    row3_column1 = forms.FloatField( initial=0, required=True)
    row3_column2 = forms.FloatField( initial=0, required=True)
    row3_column3 = forms.FloatField( initial=0, required=True)
    row3_column4 = forms.FloatField( initial=0, required=True)
    row3_column5 = forms.FloatField( initial=0, required=True)

    
    def save(self):
        return models.Table35.objects.create(
             **self.cleaned_data
        )


class Table41(forms.Form):
    row1_column1 = forms.FloatField( initial=0, required=True)
    row2_column1 = forms.FloatField( initial=0, required=True)
    row3_column1 = forms.FloatField( initial=0, required=True)
    row4_column1 = forms.FloatField( initial=0, required=True)

    
    def save(self):
        return models.Table41.objects.create(
             **self.cleaned_data
        )


class Table42(forms.Form):
    row1_column1 = forms.FloatField( initial=0, required=True)
    row1_column2 = forms.FloatField( initial=0, required=True)
    row2_column1 = forms.FloatField( initial=0, required=True)
    row2_column2 = forms.FloatField( initial=0, required=True)
    row3_column1 = forms.FloatField( initial=0, required=True)
    row3_column2 = forms.FloatField( initial=0, required=True)
    row4_column1 = forms.FloatField( initial=0, required=True)
    row4_column2 = forms.FloatField( initial=0, required=True)

    
    def save(self):
        return models.Table42.objects.create(
             **self.cleaned_data
        )


class Table43(forms.Form):
    row1_column1 = forms.FloatField( initial=0, required=True)
    row1_column2 = forms.FloatField( initial=0, required=True)
    row1_column3 = forms.FloatField( initial=0, required=True)
    row2_column1 = forms.FloatField( initial=0, required=True)
    row2_column2 = forms.FloatField( initial=0, required=True)
    row2_column3 = forms.FloatField( initial=0, required=True)
    row3_column1 = forms.FloatField( initial=0, required=True)
    row3_column2 = forms.FloatField( initial=0, required=True)
    row3_column3 = forms.FloatField( initial=0, required=True)
    row4_column1 = forms.FloatField( initial=0, required=True)
    row4_column2 = forms.FloatField( initial=0, required=True)
    row4_column3 = forms.FloatField( initial=0, required=True)

    
    def save(self):
        return models.Table43.objects.create(
             **self.cleaned_data
        )


class Table44(forms.Form):
    row1_column1 = forms.FloatField( initial=0, required=True)
    row1_column2 = forms.FloatField( initial=0, required=True)
    row1_column3 = forms.FloatField( initial=0, required=True)
    row1_column4 = forms.FloatField( initial=0, required=True)

    row2_column1 = forms.FloatField( initial=0, required=True)
    row2_column2 = forms.FloatField( initial=0, required=True)
    row2_column3 = forms.FloatField( initial=0, required=True)
    row2_column4 = forms.FloatField( initial=0, required=True)

    row3_column1 = forms.FloatField( initial=0, required=True)
    row3_column2 = forms.FloatField( initial=0, required=True)
    row3_column3 = forms.FloatField( initial=0, required=True)
    row3_column4 = forms.FloatField( initial=0, required=True)

    row4_column1 = forms.FloatField( initial=0, required=True)
    row4_column2 = forms.FloatField( initial=0, required=True)
    row4_column3 = forms.FloatField( initial=0, required=True)
    row4_column4 = forms.FloatField( initial=0, required=True)

    
    def save(self):
        return models.Table44.objects.create(
             **self.cleaned_data
        )


class Table45(forms.Form):
    row1_column1 = forms.FloatField( initial=0, required=True)
    row1_column2 = forms.FloatField( initial=0, required=True)
    row1_column3 = forms.FloatField( initial=0, required=True)
    row1_column4 = forms.FloatField( initial=0, required=True)
    row1_column5 = forms.FloatField( initial=0, required=True)

    row2_column1 = forms.FloatField( initial=0, required=True)
    row2_column2 = forms.FloatField( initial=0, required=True)
    row2_column3 = forms.FloatField( initial=0, required=True)
    row2_column4 = forms.FloatField( initial=0, required=True)
    row2_column5 = forms.FloatField( initial=0, required=True)

    row3_column1 = forms.FloatField( initial=0, required=True)
    row3_column2 = forms.FloatField( initial=0, required=True)
    row3_column3 = forms.FloatField( initial=0, required=True)
    row3_column4 = forms.FloatField( initial=0, required=True)
    row3_column5 = forms.FloatField( initial=0, required=True)
    
    row4_column1 = forms.FloatField( initial=0, required=True)
    row4_column2 = forms.FloatField( initial=0, required=True)
    row4_column3 = forms.FloatField( initial=0, required=True)
    row4_column4 = forms.FloatField( initial=0, required=True)
    row4_column5 = forms.FloatField( initial=0, required=True)

    
    def save(self):
        return models.Table45.objects.create(
             **self.cleaned_data
        )


class Table51(forms.Form):
    row1_column1 = forms.FloatField( initial=0, required=True)
    row2_column1 = forms.FloatField( initial=0, required=True)
    row3_column1 = forms.FloatField( initial=0, required=True)
    row4_column1 = forms.FloatField( initial=0, required=True)
    row5_column1 = forms.FloatField( initial=0, required=True)

    
    def save(self):
        return models.Table51.objects.create(
             **self.cleaned_data
        )


class Table52(forms.Form):
    row1_column1 = forms.FloatField( initial=0, required=True)
    row1_column2 = forms.FloatField( initial=0, required=True)
    row2_column1 = forms.FloatField( initial=0, required=True)
    row2_column2 = forms.FloatField( initial=0, required=True)
    row3_column1 = forms.FloatField( initial=0, required=True)
    row3_column2 = forms.FloatField( initial=0, required=True)
    row4_column1 = forms.FloatField( initial=0, required=True)
    row4_column2 = forms.FloatField( initial=0, required=True)
    row5_column1 = forms.FloatField( initial=0, required=True)
    row5_column2 = forms.FloatField( initial=0, required=True)

    
    def save(self):
        return models.Table52.objects.create(
             **self.cleaned_data
        )



class Table53(forms.Form):
    row1_column1 = forms.FloatField( initial=0, required=True)
    row1_column2 = forms.FloatField( initial=0, required=True)
    row1_column3 = forms.FloatField( initial=0, required=True)
    row2_column1 = forms.FloatField( initial=0, required=True)
    row2_column2 = forms.FloatField( initial=0, required=True)
    row2_column3 = forms.FloatField( initial=0, required=True)
    row3_column1 = forms.FloatField( initial=0, required=True)
    row3_column2 = forms.FloatField( initial=0, required=True)
    row3_column3 = forms.FloatField( initial=0, required=True)
    row4_column1 = forms.FloatField( initial=0, required=True)
    row4_column2 = forms.FloatField( initial=0, required=True)
    row4_column3 = forms.FloatField( initial=0, required=True)
    row5_column1 = forms.FloatField( initial=0, required=True)
    row5_column2 = forms.FloatField( initial=0, required=True)
    row5_column3 = forms.FloatField( initial=0, required=True)
    

    def save(self):
        return models.Table53.objects.create(
             **self.cleaned_data
        )


class Table54(forms.Form):
    row1_column1 = forms.FloatField( initial=0, required=True)
    row1_column2 = forms.FloatField( initial=0, required=True)
    row1_column3 = forms.FloatField( initial=0, required=True)
    row1_column4 = forms.FloatField( initial=0, required=True)

    row2_column1 = forms.FloatField( initial=0, required=True)
    row2_column2 = forms.FloatField( initial=0, required=True)
    row2_column3 = forms.FloatField( initial=0, required=True)
    row2_column4 = forms.FloatField( initial=0, required=True)

    row3_column1 = forms.FloatField( initial=0, required=True)
    row3_column2 = forms.FloatField( initial=0, required=True)
    row3_column3 = forms.FloatField( initial=0, required=True)
    row3_column4 = forms.FloatField( initial=0, required=True)

    row4_column1 = forms.FloatField( initial=0, required=True)
    row4_column2 = forms.FloatField( initial=0, required=True)
    row4_column3 = forms.FloatField( initial=0, required=True)
    row4_column4 = forms.FloatField( initial=0, required=True)

    row5_column1 = forms.FloatField( initial=0, required=True)
    row5_column2 = forms.FloatField( initial=0, required=True)
    row5_column3 = forms.FloatField( initial=0, required=True)
    row5_column4 = forms.FloatField( initial=0, required=True)
    

    def save(self):
        return models.Table54.objects.create(
             **self.cleaned_data
        )


class Table55(forms.Form):
    row1_column1 = forms.FloatField( initial=0, required=True)
    row1_column2 = forms.FloatField( initial=0, required=True)
    row1_column3 = forms.FloatField( initial=0, required=True)
    row1_column4 = forms.FloatField( initial=0, required=True)
    row1_column5 = forms.FloatField( initial=0, required=True)

    row2_column1 = forms.FloatField( initial=0, required=True)
    row2_column2 = forms.FloatField( initial=0, required=True)
    row2_column3 = forms.FloatField( initial=0, required=True)
    row2_column4 = forms.FloatField( initial=0, required=True)
    row2_column5 = forms.FloatField( initial=0, required=True)

    row3_column1 = forms.FloatField( initial=0, required=True)
    row3_column2 = forms.FloatField( initial=0, required=True)
    row3_column3 = forms.FloatField( initial=0, required=True)
    row3_column4 = forms.FloatField( initial=0, required=True)
    row3_column5 = forms.FloatField( initial=0, required=True)
    
    row4_column1 = forms.FloatField( initial=0, required=True)
    row4_column2 = forms.FloatField( initial=0, required=True)
    row4_column3 = forms.FloatField( initial=0, required=True)
    row4_column4 = forms.FloatField( initial=0, required=True)
    row4_column5 = forms.FloatField( initial=0, required=True)

    row5_column1 = forms.FloatField( initial=0, required=True)
    row5_column2 = forms.FloatField( initial=0, required=True)
    row5_column3 = forms.FloatField( initial=0, required=True)
    row5_column4 = forms.FloatField( initial=0, required=True)
    row5_column5 = forms.FloatField( initial=0, required=True)

    
    def save(self):
        return models.Table55.objects.create(
             **self.cleaned_data
        )