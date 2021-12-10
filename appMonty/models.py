from django.db import models

class OriginalAnswer(models.Model):
    correct = models.IntegerField()
    wrong = models.IntegerField()

    changedCorrect = models.IntegerField()
    changedWrong = models.IntegerField()

    def __str__(self):
        return 'Answers'


# class ChangedAnswer(models.Model):
#     changedCorrect = models.IntegerField()
#     changedWrong = models.IntegerField()

#     def __str__(self):
#         return 'Changed'