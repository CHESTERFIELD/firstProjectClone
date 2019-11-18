from .models import Post, Comment
from operator import itemgetter
import collections

def get_most_post():
    my_dict = dict()

    for post in Post.objects.all():
        c = Comment.objects.filter(post__id=post.id).count()
        other = {post: c}
        my_dict.update(other)

    my_dict_sorted = sorted(my_dict.items(), key=itemgetter(1), reverse=True)[:5]

    return my_dict_sorted
