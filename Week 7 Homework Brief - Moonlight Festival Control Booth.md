# Week 7 Homework: Moonlight Festival Control Booth

## Summary

This project uses Python’s `heapq` module to manage festival alerts using a priority queue. Each alert has a priority where smaller numbers mean higher urgency. The program processes alerts in the correct order, handles ties properly, and supports retrieving the top K alerts and peeking the next alert.

---

## Approach

### order_festival_alerts

- Created a min-heap using `heapq`
- Inserted all `(priority, title)` pairs into the heap
- Used `heappop()` to extract alerts in correct priority order
- Stored titles in result list

---

### order_festival_alerts_stable

- Added index to maintain order: `(priority, index, title)`
- Heap compares priority first, then index
- This ensures stable ordering when priorities are equal

---

### top_k_festival_alerts

- Used heap to store alerts
- Extracted only first `k` elements
- Handled edge cases:
  - If `k <= 0`, return empty list
  - If `k > len(alerts)`, return all alerts

---

### peek_next_festival_alert

- Copied the list to avoid modifying original input
- Converted copy into heap using `heapify()`
- Returned the smallest element (`heap[0]`)
- Returned `None` if input is empty

---

## Code Implementation

```python
from __future__ import annotations
import heapq


def order_festival_alerts(alerts: list[tuple[int, str]]) -> list[str]:
    heap = []

    for priority, title in alerts:
        heapq.heappush(heap, (priority, title))

    result = []

    while heap:
        _, title = heapq.heappop(heap)
        result.append(title)

    return result


def order_festival_alerts_stable(alerts: list[tuple[int, str]]) -> list[str]:
    heap = []

    for index, (priority, title) in enumerate(alerts):
        heapq.heappush(heap, (priority, index, title))

    result = []

    while heap:
        _, _, title = heapq.heappop(heap)
        result.append(title)

    return result


def top_k_festival_alerts(alerts: list[tuple[int, str]], k: int) -> list[str]:
    if k <= 0:
        return []

    heap = []

    for priority, title in alerts:
        heapq.heappush(heap, (priority, title))

    result = []

    for _ in range(min(k, len(heap))):
        _, title = heapq.heappop(heap)
        result.append(title)

    return result


def peek_next_festival_alert(alerts: list[tuple[int, str]]) -> str | None:
    if not alerts:
        return None

    heap = alerts.copy()
    heapq.heapify(heap)

    return heap[0][1]