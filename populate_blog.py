import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()

#FAKE POP SCRIPT
import random
from blog.models import Post, Comment
from django.contrib.auth.models import User
from faker import Faker
from django.utils import timezone
import random

fakegen = Faker()

def populate(N=5):

    for entry in range(N):

        # get the topic for the entry
        fake_author = User.objects.get(username='chesterfield')

        fake_title = fakegen.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
        fake_text = fakegen.text(max_nb_chars=200, ext_word_list=None)
        fake_created_date = timezone.now()


        post = Post.objects.get_or_create(author=fake_author, title=fake_title, text=fake_text,
                                            created_date=fake_created_date, published_date=fake_created_date)[0]

        count_comments = random.randint(1,6)

        for comment in range(count_comments):
            fake_post = post
            fake_author = fakegen.first_name()
            fake_comment_text = fakegen.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
            fake_comment_created_date = timezone.now()
            fake_comment_approved_comment = True

            comment = Comment.objects.get_or_create(post=fake_post, author=fake_author, text=fake_comment_text,
                                                created_date=fake_comment_created_date,
                                                approved_comment=fake_comment_approved_comment)[0]


if __name__ == '__main__':
    print("populate script")
    populate(20)
    print("complete")
