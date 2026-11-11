# CMPS 2200 Recitation 08 Answers

**Name:**Lily Goldman


Place all written answers from `recitation-10.md` here for easier grading.



- **2) (2 pts)** What is the work of `reachable`, assuming $n$ nodes and $m$ edges?

  Each node is added to the frontier and popped at most once, which is $O(n)$. When a node is popped, we loop over its neighbors. Over all nodes, this checks each edge twice (once from each end), which is $O(m)$. So the work is $O(n + m)$.

- **4) (1 pt)** What is the worst case number of times we need to call `reachable` to determine if a graph is connected?

  **Once.** Call `reachable` from any node. The graph is connected if and only if the result contains all $n$ nodes.

- **5) (2 pts)** What is the work of `connected`, assuming $n$ nodes and $m$ edges?

  It is one call to `reachable`, which is $O(n + m)$, plus an $O(1)$ size comparison. So the work is $O(n + m)$.

- **7) (1 pt)** What if we switched the graph representation to an adjacency matrix? Would the work of `reachable` change? If so, what would it be? If not, why not?

  **Yes.** With an adjacency matrix, finding a node's neighbors means scanning its entire row of $n$ entries, even if it has only a few neighbors. Each of the $n$ nodes costs $O(n)$, so the work becomes $O(n^2)$.