"""Minimum total cost to connect cables using a min-heap."""

from heapq import heapify, heappop, heappush
from typing import Iterable, List


def min_connection_cost(cables: Iterable[int]) -> int:
    """
    Return the minimum possible total cost to connect all cables.

    The optimal strategy repeatedly connects the two shortest cables first,
    which is efficiently implemented with a min-heap (similar to Huffman coding).
    """
    heap: List[int] = [length for length in cables if length > 0]
    if len(heap) <= 1:
        return 0

    heapify(heap)
    total_cost = 0

    while len(heap) > 1:
        first = heappop(heap)
        second = heappop(heap)
        cost = first + second
        total_cost += cost
        heappush(heap, cost)

    return total_cost


if __name__ == "__main__":
    sample = [8, 4, 6, 12]
    print(f"Cables: {sample}")
    print(f"Minimum total cost: {min_connection_cost(sample)}")
