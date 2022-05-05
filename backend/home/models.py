from pyexpat import model
from django.db import models

langs = [
    ('python', 'Python'),
    ('java', 'Java'),
    ('c++', 'C++')
]
# Create your models here.
class CodeFile(models.Model):

    class Language(models.TextChoices):
        python = 'python', 'Python'
        java = 'java', 'Java'
        cpp = 'c++', 'C++'
    
    language = models.CharField(max_length=10, choices=Language.choices, default=Language.python)
    title = models.CharField(max_length=250, default=language)
    code = models.TextField()
    inp = models.TextField(null=True)
    output = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title