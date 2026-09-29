import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from graph_algorithms import bfs_steps, dfs_steps  # noqa: E402

GRAPH = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C", "E"],
    "E": ["D"],
}


class GraphAlgorithmTests(unittest.TestCase):
    def test_bfs_order(self):
        self.assertEqual(bfs_steps(GRAPH, "A"), ["A", "B", "C", "D", "E"])

    def test_dfs_order(self):
        self.assertEqual(dfs_steps(GRAPH, "A"), ["A", "B", "D", "C", "E"])

    def test_bfs_visits_all_reachable_nodes(self):
        self.assertEqual(set(bfs_steps(GRAPH, "A")), set(GRAPH.keys()))

    def test_single_node_graph(self):
        self.assertEqual(bfs_steps({"X": []}, "X"), ["X"])
        self.assertEqual(dfs_steps({"X": []}, "X"), ["X"])


if __name__ == "__main__":
    unittest.main()
