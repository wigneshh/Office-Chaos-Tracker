from django.db import models

class Employee(models.Model):
    name=models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    chaos_level = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Interaction(models.Model):
     employee1 = models.ForeignKey(Employee, related_name='interactions1', on_delete=models.CASCADE)
     employee2 = models.ForeignKey(Employee, related_name='interactions2', on_delete=models.CASCADE)
     description = models.TextField()
     chaos_points = models.IntegerField()

     def __str__(self):
        return f"{self.employee1.name} ↔ {self.employee2.name}"