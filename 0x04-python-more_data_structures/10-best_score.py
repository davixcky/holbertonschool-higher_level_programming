#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary:
        max_value = max(list(a_dictionary.values()))
        return max_value

    return None
