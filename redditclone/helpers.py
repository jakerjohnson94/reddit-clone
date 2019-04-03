def get_vote_score(votes):
    score = 0
    for vote in votes:
        if vote.vote_type == 1:
            score += 1
        elif vote.vote_type == 2:
            score -= 1
    return score
