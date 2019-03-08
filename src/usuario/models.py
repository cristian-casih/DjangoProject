from django.db import models

# Create your models here.
from stream_django.activity import Activity

from stream_django.feed_manager import feed_manager

feed_manager.get_user_feed(user_id)
timeline = feed_manager.get_news_feeds(user_id)['timeline']
timeline_aggregated = feed_manager.get_news_feeds(user_id)['timeline_aggregated']
notification_feed = feed_manager.get_notification_feed (user_id)
feed_manager.follow_user (request.user.id, target_user)

class Like(models.Model, Activity):
    ...

class Tweet(models.Model, Activity):
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    @property
    def activity_actor_attr(self):
        return self.author