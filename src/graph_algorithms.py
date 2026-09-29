"""Step-by-step BFS/DFS traversal, with an optional matplotlib snapshot
of each step. The traversal logic (bfs_steps/dfs_steps) has no plotting
dependency and is fully unit tested.
"""
from collections import deque


def bfs_steps(graph, start):
    """Return the order nodes are VISITED (dequeued) in BFS from start."""
    visited = {start}
    order = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in sorted(graph.get(node, [])):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order


def dfs_steps(graph, start):
    """Return the order nodes are visited in DFS (iterative, pre-order)."""
    visited = set()
    order = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        for neighbor in sorted(graph.get(node, []), reverse=True):
            if neighbor not in visited:
                stack.append(neighbor)
    return order


def plot_traversal(graph, order, output_path, title):
    import matplotlib.pyplot as plt
    import math

    nodes = list(graph.keys())
    n = len(nodes)
    angle_step = 2 * math.pi / n
    pos = {node: (math.cos(i * angle_step), math.sin(i * angle_step))
           for i, node in enumerate(nodes)}

    fig, ax = plt.subplots(figsize=(6, 6))
    drawn_edges = set()
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            edge = tuple(sorted((node, neighbor)))
            if edge in drawn_edges:
                continue
            drawn_edges.add(edge)
            x1, y1 = pos[node]
            x2, y2 = pos[neighbor]
            ax.plot([x1, x2], [y1, y2], color="lightgray", zorder=1)

    for i, node in enumerate(order):
        x, y = pos[node]
        ax.scatter(x, y, s=800, color="tab:blue", zorder=2)
        ax.text(x, y, node, ha="center", va="center", color="white", zorder=3)
        ax.text(x, y - 0.15, f"#{i+1}", ha="center", va="center",
                color="black", fontsize=8, zorder=3)

    remaining = set(graph) - set(order)
    for node in remaining:
        x, y = pos[node]
        ax.scatter(x, y, s=800, color="lightgray", zorder=2)
        ax.text(x, y, node, ha="center", va="center", zorder=3)

    ax.set_title(f"{title}: visit order {order}")
    ax.set_aspect("equal")
    ax.axis("off")
    fig.savefig(output_path, bbox_inches="tight", dpi=120)
    plt.close(fig)


if __name__ == "__main__":
    sample_graph = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "D"],
        "D": ["B", "C", "E"],
        "E": ["D"],
    }
    bfs_order = bfs_steps(sample_graph, "A")
    dfs_order = dfs_steps(sample_graph, "A")
    print("BFS order:", bfs_order)
    print("DFS order:", dfs_order)
    plot_traversal(sample_graph, bfs_order, "outputs/bfs.png", "BFS")
    plot_traversal(sample_graph, dfs_order, "outputs/dfs.png", "DFS")
