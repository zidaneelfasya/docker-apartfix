# apart/models.py

from django.db import models

class TeamMember(models.Model):
    nama = models.CharField(max_length=100)
    NIM = models.CharField(max_length=15)
    kelas = models.CharField(max_length=10)
    role = models.CharField(max_length=50)
    image = models.ImageField(upload_to='team_images/', blank=True, null=True)

    def __str__(self):
        return self.nama
