from django.db import models

class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField() 
    tel = models.PositiveIntegerField()  # number
    webSite = models.URLField() 
    trackingLink = models.URLField() 
    method = models.CharField(max_length=255, choices=[('paypal', 'PayPal'), ('bank_transfer', 'Bank Transfer'), ('payonner', 'Payonner')])  # list paypal, bank transfer, payonner
    rate = models.CharField(max_length=255, choices=[('5', '5'), ('10', '10'), ('15', '15')])  # list 5, 10, 15
    commPref = models.CharField(max_length=255, choices=[('email', 'Email'), ('phone', 'Phone'), ('meet', 'Meet')])  # list email, phone, meet
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])  # list male, female
    location = models.CharField(max_length=255, choices=[('Tunis', 'Tunis'), ('Sousse', 'Sousse'), ('Ariana', 'Ariana'), ('Sfax', 'Sfax'), ('Mahdia', 'Mahdia'), ('Jandouba', 'Jandouba'), ('Kef', 'Kef'), ('Touzer', 'Touzer'), ('Jerjis', 'Jerjis'), ('Ben_Arous', 'Ben Arous')])  # list of locations
    field = models.CharField(max_length=255, choices=[('health', 'Health'), ('it', 'IT'), ('marketing', 'Marketing'), ('foods', 'Foods'), ('clothes', 'Clothes')])  # list health, it, marketing, foods, clothes
    age = models.PositiveIntegerField() 
    experience = models.PositiveIntegerField()
    imagePath = models.URLField(default='https://source.unsplash.com/featured/?person')

    def __str__(self):
        return f'{self.firstName} {self.lastName}'
