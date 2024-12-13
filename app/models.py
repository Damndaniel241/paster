from django.db import models
import uuid
import random

# Create your models here.

def generate_unique_id(length=8):
    """
    Generate a unique ID of a specified length.

    Args:
        length (int): The length of the ID. Defaults to 8.

    Returns:
        str: A unique ID.
    """
    unique_id = uuid.uuid4().hex
    unique_id_with_upper = ''.join(
    char.upper() if random.choice([True, False]) else char
    for char in unique_id)
    
    return unique_id_with_upper[:length]


class Link(models.Model):
    title = models.CharField(max_length=30,null=True,blank=True)
    url_id = models.CharField(max_length=8, default=generate_unique_id, editable=False, unique=True)
    content = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return self.title
