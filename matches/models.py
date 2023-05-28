from django.db import models

class Match(models.Model) :

    """ Model Definition for Match """

    type = models.CharField(max_length=140, default="normal") #defalut = normal
    # host_id = 
    host_point = models.PositiveIntegerField()
    # guest_id =
    guest_point = models.PositiveIntegerField()
    # winner_id = 
    # loser_id = 
    start_time : models.DateTimeField()
    end_time : models.DateTimeField()

    def __str__(self):
        return self.name