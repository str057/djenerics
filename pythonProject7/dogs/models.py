from django.db import models

class Breed(models.Model):
    name = models.CharField(
        max_length=100,
        дverbose_name="Название породы",
        help_text="введите Название породы",
    )
    description = models.TextField(
        дverbose_name="Описание породы",
        help_text="введите описание породы",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Порода"
        verbose_name_plural = "Породы"

    def __str__(self):
        return self.name

class Dog(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="кличка", help_text="введите кличку собаки"
    )
    breed = models.ForeignKey(
        Breed,
        on_delete=models.SET_NULL,
        verbose_name="кличка",
        help_text="введите породу собаки",
        blank=True,
        null=True,
        related_name="dogs",
    )
    photo = models.CharField(
        upload_to="dogs/photo",
        blank=True,
        null=True,
        verbose_name="фото",
        help_text="Загрузите фото собаки",
    )
    date_born = models.DateField(
        blank=True,
        null=True,
        verbose_name="дата рождения",
        help_text="укжите дату рождения",
    )
    # имя, порода, фото, дата, рождения.

    class Meta:
        verbose_name = "собака"
        verbose_name_plural = "собака"
        ordering = ["bread", "name"]

    def __str__(self):
        return self.name


