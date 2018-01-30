from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.utils.feedgenerator import Rss201rev2Feed
from django.conf import settings

from posts.models import Post

class OfficialFeed(Rss201rev2Feed):
    def add_root_elements(self, handler):
        Rss201rev2Feed.add_root_elements(self, handler)
        handler.startElement(u'image', {})
        handler.addQuickElement(u"url", settings.SITE["logo_url"])
        handler.addQuickElement(u"title", settings.SITE["title"])
        handler.addQuickElement(u"link", settings.SITE["url"])
        handler.endElement(u"image")

    def add_item_elements(self, handler, item):
        super(OfficialFeed, self).add_item_elements(handler, item)

class RSS(Feed):
    feed_type = OfficialFeed
    title = settings.SITE["title"]
    description = settings.SITE["description"]
    link = "/rss/" # apparantly very important; I don't know why

    def items(self):
        return Post.objects.all().filter(draft=0)

    def item_title(self, item):
        return item.title

    def item_author_name(self, item):
        return item.user.get_full_name()
