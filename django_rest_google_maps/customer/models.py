from django.db import models


class Genders(models.IntegerChoices):
    FEMALE = (1, "Female")
    MALE = (2, "Male")
    NA = (3, "NA")


class Occupation(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class State(models.Model):
    initials = models.CharField(max_length=2)

    class Meta:
        ordering = ["initials"]

    def __str__(self):
        return self.initials


class City(models.Model):
    state = models.ForeignKey(State, models.DO_NOTHING, related_name="state")
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    longitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)

    class Meta:
        ordering = ["state", "name"]

    def __str__(self):
        return f"{self.name} - {self.state.initials}"


class Company(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    gender = models.PositiveSmallIntegerField(choices=Genders.choices, default=Genders.FEMALE)
    company = models.ForeignKey(Company, models.DO_NOTHING, related_name="company")
    occupation = models.ForeignKey(Occupation, models.DO_NOTHING, related_name="occupation", null=True, blank=True)
    city = models.ForeignKey(City, models.DO_NOTHING, related_name="city", null=True, blank=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.id} - {self.first_name} from {self.city}"
