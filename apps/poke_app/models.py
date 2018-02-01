from __future__ import unicode_literals

from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        if len(postData['name']) < 2:
			errors['name'] = "Name should be more than 3"
        if len(postData['email']) < 4:
            errors['email'] = "Email should be more than 3 characters"
        if len(User.objects.filter(email=postData['email'])) > 0:
            errors['email'] = "Email is invalid"
        if len(postData['password']) < 7:
            errors['password'] = "Password should be more than 7 characters"
        if postData['password'] != postData['conf_password']:
        	errors['ps_match'] = 'Passwords do not match'
        if len(errors) == 0:
        	errors['Registered!'] = 'Registered!'
        	hash1 = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
        	User.objects.create(name=postData['name'], alias=postData['alias'], dob=postData['adate'], password=hash1, email=postData['email'])
        return errors
        
    def login_validator(self, postData):
    	errors = {}
    	if len(User.objects.filter(email=postData['email'])) == 0:
    		errors['emailfail'] = 'incorrect email'
    	else:
    		P = User.objects.get(email=postData['email']).password
    		Z = postData['password']
    		if not bcrypt.checkpw(Z.encode(), P.encode()):
    			errors['PassFail'] = 'incorrect Password'
    	return errors

class PokeManager(models.Manager):
	def createPoke(self, sender, receiver):
		sender = User.objects.get(id=sender)
		receiver = User.objects.get(id=receiver)
		existingPoke = Poke.objects.filter(poke_sender=sender, poke_reciever=receiver)
		if len(existingPoke) > 0:
			existingPoke[0].count += 1
			existingPoke[0].save()
		else:
			Poke.objects.create(poke_sender=sender, poke_reciever=receiver)

class User(models.Model):
	name = models.CharField(max_length=100)
	alias = models.CharField(max_length=100)
	email = models.CharField(max_length=50)
	password = models.CharField(max_length=100)
	dob = models.DateField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)
	objects = UserManager()

class Poke(models.Model):
	count = models.IntegerField(default=1)
	poke_sender = models.ForeignKey(User, related_name='pokes_sent')
	poke_reciever = models.ForeignKey(User, related_name="pokes_received")
	objects = PokeManager()
