from django.db import models


class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=70)
    society_name = models.CharField(max_length=200, null=True)
    phase = models.CharField(max_length=10,choices=[('one', 'I'), ('two', 'II')])
    wing = models.CharField(max_length=5)
    flat_no = models.IntegerField()
    class Meta:
        db_table = u'Member'
        verbose_name_plural = "Member"
        def __str__(self):
            return self.last_name
