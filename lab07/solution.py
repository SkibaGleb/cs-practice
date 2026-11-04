import numpy as np


def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    if width <= 0:
        return []
    if len(values) % width != 0:
        return []
    arr = np.asarray(values, dtype=float).reshape(-1, width)
    return arr.tolist()


def block(matrix: list[list[float]],
          rows: list[int],
          columns: list[int]) -> list[list[float]]:
    if not matrix or not rows or not columns:
        return []
    arr = np.asarray(matrix, dtype=float)
    sub = arr[np.ix_(rows, columns)]
    return sub.tolist()


def column_means(matrix: list[list[float]]) -> list[float]:
    if not matrix:
        return []
    arr = np.asarray(matrix, dtype=float)
    means = arr.mean(axis=0)
    return np.round(means, 6).tolist()


def column_range(matrix: list[list[float]], column: int) -> float:
    if not matrix:
        return 0.0
    arr = np.asarray(matrix, dtype=float)
    col = arr[:, column]
    return float(np.round(col.max() - col.min(), 6))