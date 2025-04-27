import numpy as np

def precision_at_k(actual, predicted, k=5):
    """Precision at top K"""
    actual_set = set(actual)
    pred_set = set(predicted[:k])
    if len(pred_set) == 0:
        return 0
    return len(actual_set & pred_set) / len(pred_set)

def recall_at_k(actual, predicted, k=5):
    """Recall at top K"""
    actual_set = set(actual)
    pred_set = set(predicted[:k])
    if len(actual_set) == 0:
        return 0
    return len(actual_set & pred_set) / len(actual_set)
