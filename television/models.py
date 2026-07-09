from django.db import models

class Actualite(models.Model):
    titre = models.CharField(max_length=200)
    resume = models.TextField()
    date_pub = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='news/', null=True, blank=True)
    en_direct = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Actualite"
        verbose_name_plural = "Actualites"
        ordering = ['-date_pub']

    def __str__(self):
        return self.titre
