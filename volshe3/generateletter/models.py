from django.db import models


# Create your models here.
class Visaletters(models.Model):


    CIT_CHOICES = (
        ("INDIA", "India"),
        ("USA", "Usa"),
        ("UK", "Uk"),
        ("CHINA", "China"),
        ("JAPAN", "Japan"),
    )
    no_passenger = models.IntegerField(default=1)
    Country = models.CharField(max_length=264, choices=CIT_CHOICES, default="INDIA")
    entry_from = models.CharField(max_length=200)
    departure_to = models.CharField(max_length=200)
    PAS = (("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"))
    Visa_Letter_Number = models.CharField(max_length=264, default="1")
    Date_of_letter = models.CharField(max_length=200, blank=True)
    Routes_and_Places = models.CharField(max_length=500, default="MOSCOW")
    hotels = models.CharField(max_length=264)
    Organization = models.CharField(max_length=200, blank=True)
    multi = (("Paid", "Paid"), ("unpaid", "unpaid"))
    Payment_status = models.CharField(max_length=200, choices=multi, default="unpaid")
    amount = models.PositiveIntegerField()
    firstname_1 = models.CharField(max_length=264)
    lastname_1 = models.CharField(max_length=264)
    Passport_Number_1 = models.CharField(max_length=200, unique=True)
    Date_Of_Birth_1 = models.CharField(max_length=200)
    Sex_1 = models.CharField(max_length=100)
    firstname_2 = models.CharField(max_length=264, blank=True)
    lastname_2 = models.CharField(max_length=264, blank=True)
    Passport_Number_2 = models.CharField(max_length=200, blank=True)
    Date_Of_Birth_2 = models.CharField(max_length=200, blank=True)
    Sex_2 = models.CharField(max_length=100, blank=True)
    firstname_3 = models.CharField(max_length=264, blank=True)
    lastname_3 = models.CharField(max_length=264, blank=True)
    Passport_Number_3 = models.CharField(max_length=200, blank=True)
    Date_Of_Birth_3 = models.CharField(max_length=200, blank=True)
    Sex_3 = models.CharField(max_length=100, blank=True)
    firstname_4 = models.CharField(max_length=264, blank=True)
    lastname_4 = models.CharField(max_length=264, blank=True)
    Passport_Number_4 = models.CharField(max_length=200, blank=True)
    Date_Of_Birth_4 = models.CharField(max_length=200, blank=True)
    Sex_4 = models.CharField(max_length=100, blank=True)
    firstname_5 = models.CharField(max_length=264, blank=True)
    lastname_5 = models.CharField(max_length=264, blank=True)
    Passport_Number_5 = models.CharField(max_length=200, blank=True)
    Date_Of_Birth_5 = models.CharField(max_length=200, blank=True)
    Sex_5 = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.firstname_1
