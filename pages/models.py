from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Page(models.Model):
    owner_id = models.ForeignKey(User, db_column="owner_id", on_delete=models.CASCADE)
    username = models.CharField(max_length=30, unique=True)
    audience_insights_url = models.URLField(null=True, blank=True)
    last_insights_update = models.DateField(null=True, blank=True)
    trust_score = models.FloatField(null=True, blank=True) # number of finished promos / number of escalations or other bad experiences (refunds aren't always bad)
    is_verified = models.BooleanField(default=False, blank=True)

class Promotion(models.Model):
    client_id = models.ForeignKey(User, db_column="client_id", on_delete=models.CASCADE)
    content_url = models.URLField()
    caption_url = models.URLField()
    creation_datetime = models.DateTimeField()
    datetime = models.DateTimeField()

# many to many between Promotion and Page
class Calendar(models.Model):
    page_id = models.ForeignKey(Page, db_column="page_id", on_delete=models.CASCADE)
    promotion_id = models.ForeignKey(Promotion, db_column="promotion_id", on_delete=models.CASCADE)
