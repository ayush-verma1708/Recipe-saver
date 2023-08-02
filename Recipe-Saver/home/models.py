from django.db import models

# Create your models here.
# gender = [
#     {'male':'male'},
#     {'female':'female'}
# ]    
class Student(models.Model):
    
    name =  models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    image = models.ImageField(null = True , default= None)
    # gender = models.Choices(gender)

    def __str__(self) -> str:
        return self.name