# Quick Review Decision Framework
1. See O(n²) on intervals? → Sort first, then one linear pass or heap
2. See unbounded map/cache? → Ask about memory bounds, add TTL or circular buffer
3. See linear scan in a design class? → Binary search if sorted, or restructure storage
4. See full array copy per snapshot/version? → Sparse recording + bisect
5. See sort + full scan for "top k"? → Min-heap of size k, O(n log k)
6. See DFS where BFS would give the shortest? → Switch to BFS (Word Ladder, islands)
7. See sliding window shrinking fully? → "Slide by 1" trick if you want max-window
8. See the sliding window that should be minimised? → Shrink aggressively until invalid
