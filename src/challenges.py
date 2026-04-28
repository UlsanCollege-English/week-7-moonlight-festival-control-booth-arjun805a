"""
Week 7: Moonlight Festival Control Booth

Use Python's heapq module to solve priority queue problems.
"""

from __future__ import annotations

import heapq


def order_festival_alerts(alerts: list[tuple[int, str]]) -> list[str]:
    """
    Return alert titles in the order they should be handled.

    Each alert is a tuple:
        (priority, title)

    Smaller priority numbers should be handled first.
    """
    heap = []

    for priority, title in alerts:
        heapq.heappush(heap, (priority, title))

    result = []

    while heap:
        _, title = heapq.heappop(heap)
        result.append(title)

    return result


def order_festival_alerts_stable(alerts: list[tuple[int, str]]) -> list[str]:
    """
    Return alert titles in the order they should be handled.

    If two alerts have the same priority, keep the original input order.
    """
    heap = []

    for index, (priority, title) in enumerate(alerts):
        heapq.heappush(heap, (priority, index, title))

    result = []

    while heap:
        _, _, title = heapq.heappop(heap)
        result.append(title)

    return result


def top_k_festival_alerts(alerts: list[tuple[int, str]], k: int) -> list[str]:
    """
    Return the titles of the k most urgent alerts.

    If k <= 0, return an empty list.
    If k is larger than the number of alerts, return as many as possible.
    """
    if k <= 0:
        return []

    heap = []

    # IMPORTANT: use index to keep stable order
    for index, (priority, title) in enumerate(alerts):
        heapq.heappush(heap, (priority, index, title))

    result = []

    for _ in range(min(k, len(heap))):
        _, _, title = heapq.heappop(heap)
        result.append(title)

    return result


def peek_next_festival_alert(alerts: list[tuple[int, str]]) -> str | None:
    """
    Return the title of the next alert to handle without permanently
    changing the original input.

    If alerts is empty, return None.
    """
    if not alerts:
        return None

    heap = alerts.copy()
    heapq.heapify(heap)

    return heap[0][1]