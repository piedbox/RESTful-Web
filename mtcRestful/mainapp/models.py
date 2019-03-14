from django.db import models



class Toy(models.Model):
    """Basic model of toys."""

    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150, blank=False, default='')
    description = models.CharField(max_length=250, blank=True, default='')
    toy_category = models.CharField(max_length=200, blank=False, default='')
    base_material = models.CharField(max_length=40, blank=True, default='')
    was_included_in_home = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', related_name='toys',
                              on_delete=models.CASCADE)

    class Meta:
        # Sorted by name field
        ordering = ('name',)
