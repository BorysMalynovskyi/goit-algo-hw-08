"""Merge k sorted lists into one sorted list using a min-heap."""

import heapq
from typing import List, Sequence


def merge_k_lists(lists: Sequence[Sequence[int]]) -> List[int]:
    """Merge multiple sorted lists into a single sorted list in O(n log k)."""
    merged: List[int] = []
    heap: list[tuple[int, int, int]] = []

    for list_index, sequence in enumerate(lists):
        if sequence:
            heapq.heappush(heap, (sequence[0], list_index, 0))

    while heap:
        value, list_index, element_index = heapq.heappop(heap)
        merged.append(value)

        next_index = element_index + 1
        if next_index < len(lists[list_index]):
            next_value = lists[list_index][next_index]
            heapq.heappush(heap, (next_value, list_index, next_index))

    return merged


if __name__ == "__main__":
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Sorted list:", merged_list)
