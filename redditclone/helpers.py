def flag_user_thread_votes(threads, request):
    for thread in threads:
        if thread.upvoters.filter(user=request.user).exists():
            thread.has_upvoted = True
        elif thread.downvoters.filter(user=request.user).exists():
            thread.has_downvoted = True
