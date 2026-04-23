"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    return[round(score) for score in student_scores]

    pass


def count_failed_students(student_scores):
    return sum(1 for score in student_scores if score <= 40)


def above_threshold(student_scores, threshold):
    return [score for score in student_scores if score >= threshold]


def letter_grades(highest):
    step = (highest - 40) // 4
    return [41 + step * i for i in range(4)]


def student_ranking(student_scores, student_names):
    return [
        f"{rank}. {name}: {score}"
        for rank, (name, score) in enumerate(zip(student_names, student_scores), start=1)
    ]


def perfect_score(student_info):
    for name, score in student_info:
        if score == 100:
            return [name, score]
    return []