from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models import FileField
from django_resized import ResizedImageField


class News(models.Model):
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    title_en = models.CharField(max_length=255, null=True, blank=True)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_uz = models.CharField(max_length=255, null=True)

    description_en = models.TextField(null=True, blank=True)
    description_ru = models.TextField(null=True, blank=True)
    description_uz = models.TextField(null=True)

    date = models.DateField(null=True)

    views = models.IntegerField(default=0, null=True, blank=True)

    image = ResizedImageField(upload_to='news/images/',
                              validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg', 'webp'])],
                              null=True, blank=True, quality=65, force_format='JPEG')

    image_uz = ResizedImageField(upload_to='news/images/',
                                 validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg', 'webp'])],
                                 null=True, blank=True, quality=65, force_format='JPEG')

    image_ru = ResizedImageField(upload_to='news/images/',
                                 validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg', 'webp'])],
                                 null=True, blank=True, quality=65, force_format='JPEG')

    video_title = models.CharField(max_length=255, null=True, blank=True)
    video = FileField(upload_to='news/videos/',
                      validators=[
                          FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'wmv', 'flv', 'gif'])],
                      null=True, blank=True)

    video_title_uz = models.CharField(max_length=255, null=True, blank=True)
    video_uz = FileField(upload_to='news/videos/',
                         validators=[
                             FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'wmv', 'flv', 'gif'])],
                         null=True, blank=True)

    video_title_ru = models.CharField(max_length=255, null=True, blank=True)
    video_ru = FileField(upload_to='news/videos/',
                         validators=[
                             FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'wmv', 'flv', 'gif'])],
                         null=True, blank=True)

    file_uz_one = models.FileField(upload_to='news/documents/uz',
                                   validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True,
                                   blank=True)
    file_uz_two = models.FileField(upload_to='news/documents/uz',
                                   validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True,
                                   blank=True)
    file_uz_three = models.FileField(upload_to='news/documents/uz',
                                     validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True,
                                     blank=True)
    file_uz_four = models.FileField(upload_to='news/documents/uz',
                                    validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True,
                                    blank=True)
    file_uz_five = models.FileField(upload_to='news/documents/uz',
                                    validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True,
                                    blank=True)
    file_uz_six = models.FileField(upload_to='news/documents/uz',
                                   validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True,
                                   blank=True)
    file_uz_seven = models.FileField(upload_to='news/documents/uz',
                                     validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True,
                                     blank=True)
    file_uz_eight = models.FileField(upload_to='news/documents/uz',
                                     validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True,
                                     blank=True)
    file_uz_nine = models.FileField(upload_to='news/documents/uz',
                                    validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True,
                                    blank=True)
    file_uz_ten = models.FileField(upload_to='news/documents/uz',
                                   validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True,
                                   blank=True)

    file_en_one = models.FileField(upload_to='news/documents/en',
                                   validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True,
                                   blank=True)
    file_en_two = models.FileField(upload_to='news/documents/en',
                                   validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True,
                                   blank=True)
    file_en_three = models.FileField(upload_to='news/documents/en',
                                     validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True,
                                     blank=True)
    file_en_four = models.FileField(upload_to='news/documents/en',
                                    validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True,
                                    blank=True)
    file_en_five = models.FileField(upload_to='news/documents/en',
                                    validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True,
                                    blank=True)
    file_en_six = models.FileField(upload_to='news/documents/en',
                                   validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True,
                                   blank=True)
    file_en_seven = models.FileField(upload_to='news/documents/en',
                                     validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True,
                                     blank=True)
    file_en_eight = models.FileField(upload_to='news/documents/en',
                                     validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True,
                                     blank=True)
    file_en_nine = models.FileField(upload_to='news/documents/en',
                                    validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True,
                                    blank=True)
    file_en_ten = models.FileField(upload_to='news/documents/en',
                                   validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True,
                                   blank=True)

    file_ru_one = models.FileField(upload_to='news/documents/ru',
                                   validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True,
                                   blank=True)
    file_ru_two = models.FileField(upload_to='news/documents/ru',
                                   validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True,
                                   blank=True)
    file_ru_three = models.FileField(upload_to='news/documents/ru',
                                     validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True,
                                     blank=True)
    file_ru_four = models.FileField(upload_to='news/documents/ru',
                                    validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True,
                                    blank=True)
    file_ru_five = models.FileField(upload_to='news/documents/ru',
                                    validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True,
                                    blank=True)
    file_ru_six = models.FileField(upload_to='news/documents/ru',
                                   validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True,
                                   blank=True)
    file_ru_seven = models.FileField(upload_to='news/documents/ru',
                                     validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True,
                                     blank=True)
    file_ru_eight = models.FileField(upload_to='news/documents/ru',
                                     validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True,
                                     blank=True)
    file_ru_nine = models.FileField(upload_to='news/documents/ru',
                                    validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True,
                                    blank=True)
    file_ru_ten = models.FileField(upload_to='news/documents/ru',
                                   validators=[FileExtensionValidator(allowed_extensions=['pdf'])], null=True,
                                   blank=True)
    extra_img_one = ResizedImageField(upload_to='news/extra/images',
                                      validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg'])],
                                      null=True, blank=True, quality=65, force_format='JPEG')
    extra_img_two = ResizedImageField(upload_to='news/extra/images',
                                      validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg'])],
                                      null=True, blank=True, quality=65, force_format='JPEG')
    extra_img_three = ResizedImageField(upload_to='news/extra/images',
                                        validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg'])],
                                        null=True, blank=True, quality=65, force_format='JPEG')

    english = models.BooleanField(blank=True, default=1)

    russian = models.BooleanField(blank=True, default=1)

    uzbek = models.BooleanField(blank=True, default=1)

    def __str__(self):
        return self.title_uz
