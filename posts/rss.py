from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Post


class LatestPostsFeed(Feed):
    title = 'Multi Author Blog RSS'
    link = '/rss/'
    description = 'Latest published posts from Multi Author Blog.'

    def items(self):
        return Post.objects.filter(is_published=True).order_by('-created_at')[:20]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return reverse('post_detail', args=[item.id])

    def item_pubdate(self, item):
        return item.created_at

    def item_author_name(self, item):
        return item.author.get_full_name() or item.author.username
