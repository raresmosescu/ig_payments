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
    # successful_promos = models.IntegerField(default=0) # number of finished promos without bad experiences ( a refund isn't necessarily a bad experience )
    # unsuccessful_promos = models.IntegerField(default=0) # number of promos that ended with a bad action (refund, escalation, etc.)
    # category_tags = models.CharField(max_length=140)
    # followers = models.IntegerField()
    # post_frequency = models.CharField(max_length=15)
    bundle_discount = models.FloatField(default=0)

class Post(models.Model):
    page_id = models.ForeignKey(Page, db_column="page_id", on_delete=models.CASCADE)
    placement = models.CharField(max_length=15)
    goal = models.CharField(max_length=15)
    price = models.FloatField() 

class Package(models.Model):
    page_id = models.ForeignKey(Page, db_column="page_id", on_delete=models.CASCADE)
    option_name = models.CharField(max_length=15, null=True, blank=True)
    package_type = models.CharField(max_length=15) # growth or sales
    price_total = models.FloatField(null=True, blank=True)
    price_discounted = models.FloatField(null=True, blank=True)
    price_final = models.FloatField(null=True, blank=True)

# many 2 many
class PostPackage(models.Model):
    post_id = models.ForeignKey(Page, db_column="post_id", on_delete=models.CASCADE)
    posts_amount = models.IntegerField()
    package_id = models.ForeignKey(Package, db_column="package_id", on_delete=models.CASCADE)

class BulkDiscount(models.Model):
    page_id = models.ForeignKey(Page, db_column="page_id", on_delete=models.CASCADE)
    discount = models.FloatField()
    amount = models.IntegerField()
    discounted_post_goal = models.CharField(max_length=15)
    discounted_post_placement = models.CharField(max_length=15)

class Promo(models.Model):
    page_id = models.ForeignKey(Page, db_column="page_id", on_delete=models.CASCADE)
    client_id = models.ForeignKey(User, db_column="client_id", on_delete=models.CASCADE)
    option_id = models.ForeignKey(Package, db_column="option_id", on_delete=models.CASCADE)
    content_url = models.URLField()
    caption_url = models.URLField()
    submitted_at = models.DateTimeField()
    scheduled_for = models.DateTimeField()