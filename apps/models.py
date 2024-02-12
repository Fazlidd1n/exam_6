from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, PositiveIntegerField, ForeignKey, CASCADE, TextField
from django_resized import ResizedImageField


class User(AbstractUser):
    image = ResizedImageField(size=[90, 90], crop=['middle', 'center'], upload_to='user/images',
                              default='user/defoult_user.jpeg')


class Carbonad(Model):
    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        pass

    export_as_csv.short_description = "Export Selected"
    image = ResizedImageField(size=[240, 240], crop=['middle', 'center'], upload_to='product/images',
                              default='product/default.png')
    name = CharField(max_length=255)
    description = TextField(null=True, blank=True)

    def __str__(self):
        return self.name
