from django.db import models


class ScoreboardTags(models.Model):
    tag = models.CharField(max_length = 30)
    style = models.CharField(max_length = 30)

    def __str__(self):
        return (self.tag)


class Scoreboard(models.Model):
    machine_id = models.IntegerField()
    display = models.BooleanField()
    tag_id = models.ForeignKey(ScoreboardTags, on_delete = models.CASCADE)
    running = models.BooleanField()
    percentage = models.IntegerField()
    update_at = models.DateTimeField(auto_now = True)
