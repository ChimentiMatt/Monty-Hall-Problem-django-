from django.db import models

class OriginalAnswer(models.Model):
    correct = models.IntegerField()
    wrong = models.IntegerField()

    switchedCorrect = models.IntegerField()
    switchedWrong = models.IntegerField()

    def __str__(self):
        return 'results'


# class ChangedAnswer(models.Model):
#     changedCorrect = models.IntegerField()
#     changedWrong = models.IntegerField()

#     def __str__(self):
#         return 'Changed'