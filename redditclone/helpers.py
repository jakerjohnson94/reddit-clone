from selenium import webdriver
from datetime import datetime
from .settings import MEDIA_ROOT


def flag_user_thread_votes(threads, request):
    for thread in threads:
        if thread.upvoters.filter(user=request.user).exists():
            thread.has_upvoted = True
        elif thread.downvoters.filter(user=request.user).exists():
            thread.has_downvoted = True


def set_post_score(post):
    try:
        post.score = len(post.upvoters.all()) - len(post.downvoters.all())
        post.save()
        return post.score
    except Exception as e:
        print("Failed to set score")


def flag_own_post(post, user):
    post.is_own_post = post.sender.user == user


def get_url_link_thumbnail(url):
    driver = webdriver.PhantomJS()
    driver.set_window_size(700, 560)  # set the window size that you need
    driver.get(url)
    driver.save_screenshot(f"{MEDIA_ROOT}/{datetime.now()}-{url}")
