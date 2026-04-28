# Week 7 Homework: Moonlight Festival Control Booth

**Due:** Sun 2026-04-19 23:59
**Topic:** Heaps + Priority Queues (`heapq`)
**Standards:** S11 primary, with S1 and S3 support

---

## Story

You are helping run the control booth for the Moonlight Festival.

During the festival, the control booth receives many alerts and requests, such as:

* "Main Stage microphone failed"
* "North Gate security call"
* "Performer arrived at backstage"
* "Rain warning near food court"

Each alert has a **priority number**:

* `1` = most urgent
* `2` = urgent
* `3` = normal
* larger numbers = less urgent

The booth should not always respond in arrival order.
It should respond in **priority order**.

Your job is to use Python’s `heapq` module to help organize these festival alerts.

---

## Learning goals

By completing this homework, you should be able to:

* use `heapq` correctly
* solve a priority-queue problem with a real story
* handle tie cases clearly
* write tests that prove your code works
* explain time and space complexity carefully

---

## Files you must complete

```text
src/challenges.py
tests/test_challenges.py
README.md
```

---

## Function 1: `order_festival_alerts`

Write a function:

```python
order_festival_alerts(alerts: list[tuple[int, str]]) -> list[str]
```

Each alert is a tuple like:

```python
(priority, title)
```

Return a list of alert titles in the order they should be handled.

### Example

```python
alerts = [
    (2, "Food court power issue"),
    (1, "Main Stage microphone failed"),
    (3, "Lost umbrella report"),
]
```

Expected result:

```python
["Main Stage microphone failed", "Food court power issue", "Lost umbrella report"]
```

### Rules

* Use `heapq`
* Smaller priority number goes first
* Do not just sort the full list and stop there

---

## Function 2: `order_festival_alerts_stable`

Write a function:

```python
order_festival_alerts_stable(alerts: list[tuple[int, str]]) -> list[str]
```

If two alerts have the same priority, the one that appeared **earlier in the input list** should be handled first.

### Example

```python
alerts = [
    (1, "Security check at North Gate"),
    (1, "Lighting issue at East Stage"),
    (2, "Performer arrived backstage"),
]
```

Expected result:

```python
["Security check at North Gate", "Lighting issue at East Stage", "Performer arrived backstage"]
```

### Hint

You will probably need to store **extra information** in the heap.

---

## Function 3: `top_k_festival_alerts`

Write a function:

```python
top_k_festival_alerts(alerts: list[tuple[int, str]], k: int) -> list[str]
```

Return the titles of the **k most urgent alerts**, from most urgent to less urgent.

### Example

```python
alerts = [
    (3, "Merch tent low stock"),
    (1, "Storm warning"),
    (2, "Ticket scanner issue"),
    (1, "Stage power failure"),
]
```

If `k = 3`, the expected result is:

```python
["Storm warning", "Stage power failure", "Ticket scanner issue"]
```

### Rules

* Use `heapq`
* Handle `k` carefully

---

## Stretch: `peek_next_festival_alert`

Write a function:

```python
peek_next_festival_alert(alerts: list[tuple[int, str]]) -> str | None
```

Return the title of the next alert that should be handled **without permanently changing the original input**.

If there are no alerts, return `None`.

---

## What your tests must prove

### For `order_festival_alerts`

* normal case
* empty input
* one alert

### For `order_festival_alerts_stable`

* different priorities
* same-priority tie case
* all alerts same priority

### For `top_k_festival_alerts`

* `k = 0`
* `k > len(alerts)`
* duplicate priorities
* empty input

### For the stretch

* empty input
* normal case

---

## Requirements

* Python 3.11+
* stdlib only
* public functions should use type hints
* write clear docstrings
* keep code readable

---

## Complexity expectations

In your README, explain:

* time complexity
* space complexity
* why a heap is a good fit here

Do not just write something vague like “fast” or “good performance.”

---

## Submission checklist

* [ ] `src/challenges.py` is complete
* [ ] `tests/test_challenges.py` is complete
* [ ] `README.md` is complete
* [ ] `pytest -q` passes
* [ ] edge cases are tested
* [ ] work is pushed to the correct GitHub Classroom repo
