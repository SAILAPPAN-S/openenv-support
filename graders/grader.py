def grade_easy(ticket):
    if ticket.category == "billing":
        return 1.0
    elif ticket.category:
        return 0.5
    return 0.0


def grade_medium(ticket):
    score = 0.0

    if ticket.category == "billing":
        score += 0.5

    if ticket.priority:
        score += 0.5

    return score


def grade_hard(ticket):
    score = 0.0

    if ticket.category:
        score += 0.3

    if ticket.priority:
        score += 0.3

    if ticket.resolved:
        score += 0.4

    return min(score, 1.0)