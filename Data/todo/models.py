from django.db import models


#
# TYPE = (
#     ('Travel', 'Travel'),
#     ('Meeting', 'Meeting'),
#     ('Phone', 'Phone'),
#     ('Study', 'Study'),
#     ('Appointment', 'Appointment'),
#     ('Rest', 'Rest'),
#     ('Other', 'Other')
# )


class Type(models.Model):
    name = models.CharField(primary_key=True, max_length=20)

    def __str__(self):
        return f'{self.name}'


class Schedule(models.Model):
    name = models.CharField(max_length=40)
    time = models.TimeField()
    complete = models.BooleanField(default=False)
    # type = models.CharField(max_length=40, choices=TYPE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} {self.name} {self.time} {self.complete} {self.type}'

    class Meta:
        verbose_name_plural = 'Schedule'

