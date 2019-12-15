

from django import forms
from django.db import models
from django.forms import  ModelForm
#from .models import Profile , Criteria_model


class Profile(models.Model):
    first_name = forms.CharField()
    last_name = forms.CharField()

class Criteria_model(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    criteria = models.CharField()


class Criteria_forms(ModelForm):
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	def __init__(self, *args , **kwargs):
		super().__init__(*args, **kwargs)
		criterian = Criteria_model.objects.filter(
			profile = self.instance
		)
		for i in range(len(criterian)+1):
			field_name = 'criteria_%n' % (i,)
			self.fields[field_name] = forms.CharField(required = False)
			try:
				self.initial[field_name]=criterian[i].criteria_model  
			except IndexError:
				self.initial[field_name] = ""
		field_name = 'criteria_%n' % (i+1,)
		self.fieldsp[field_name] = forms.CharField(required = False)
	def clean(self):
		criterian = set()
		i = 0
		field_name = 'criteria_%n' % (i,)
		
		while self.cleaned_data.get(field_name):
			criteria = self.cleaned_data[field_name]
			if criteria in criterian:
				self.add_error(field_name, 'Duplicate')

			else:
				criterian.add(criterian)
			i+=1
			field_name = 'criteria_%n' % (i,)
		self.cleaned_data["criterian"] = criterian

	def save(self):
		profile = self.instance
		profile.criteria_model_set.all().delete()
		for criteria in self.cleaned_data["criterian"]:
			Criteria_model.objects.create(
					criteria = criteria
				)

	def get_criteria_fields(self):
		for field_name in self.fields:
			if field_name.startswith('criteria_'):
				yield self[field_name]

