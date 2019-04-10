from selenium import webdriver
from django.utils import timezone
from .settings import MEDIA_ROOT
import os
import urllib


def flag_user_thread_votes(thread, request):
        if thread.upvoters.filter(user=request.user).exists():
            thread.has_upvoted = True
        elif thread.downvoters.filter(user=request.user).exists():
            thread.has_downvoted = True


def set_post_score(post):
    try:
        post.score = len(post.upvoters.all()) - len(post.downvoters.all())
        post.save()
        return post
    except Exception as e:
        print("Failed to set score")


def flag_own_post(post, user):
    post.is_own_post = post.sender.user == user


def get_url_link_thumbnail(post, url):
    driver = webdriver.PhantomJS()
    driver.set_window_size(100, 100)  # set the window size that you need
    driver.get(url)
    url_name = urllib.parse.quote_plus(url + str(timezone.now()))
    if not os.path.exists(MEDIA_ROOT):
        os.makedirs(MEDIA_ROOT)
    img_path = f"{MEDIA_ROOT}/{url_name}.png"
    driver.save_screenshot(img_path)
    return f"{url_name}.png"
