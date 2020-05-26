from typing import List


def latest(scores: List) -> List:
    """
    Return the last added score from a list of scores
    """
    # Check the argument type
    if not isinstance(scores, List):
        raise TypeError("Argument 'scores' must be of type list.")

    return scores[-1]


def personal_best(scores: List) -> List:
    """
    Return the highest score from a list of scores
    """
    # Check the argument type
    if not isinstance(scores, List):
        raise TypeError("Argument 'scores' must be of type list.")

    return max(scores)


def personal_top_three(scores: List) -> List:
    """
    Return the three highest scores from a list of scores
    """
    # Check the argument type
    if not isinstance(scores, List):
        raise TypeError("Argument 'scores' must be of type list.")

    result = []

    while scores:
        if len(result) == 3:
            break
        _max = max(scores)
        result.append(_max)
        scores.remove(_max)

    return result
