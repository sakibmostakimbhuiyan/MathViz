# 📐 MathViz: Algorithmic & Mathematical Visualizer

> A small Python toolkit that turns geometry theorems, graph-traversal algorithms, and calculus concepts into visual, testable code — three focused modules instead of one do-everything tool.

![Status](https://img.shields.io/badge/status-working%20prototype-brightgreen)
![Python](https://img.shields.io/badge/python-3.8+-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## 🎯 Motivation

Some ideas in math and CS click faster when you can see them. MathViz generates static images (PNG) for three areas: geometric theorems, classic graph-search algorithms, and single-variable calculus.

## ⚙️ Modules

| Module | What it shows | Depends on |
|---|---|---|
| `src/geometry.py` | Pythagorean theorem (squares on each side) and the inscribed angle theorem | matplotlib |
| `src/graph_algorithms.py` | BFS and DFS traversal order on a graph, node-by-node | matplotlib |
| `src/calculus.py` | A function's tangent line (derivative) and shaded area (integral) at a point/interval | matplotlib, numpy |

Every module separates **pure logic** (traversal order, derivative/integral approximation, side-length math — no plotting) from the **plotting function**, so the logic is unit tested without needing to render images.

## ⚠️ Honesty Notes

- The derivative and integral are **numerical approximations** (finite differences, trapezoidal rule), not symbolic calculus. They will be slightly off for functions with sharp curvature, by design of the method.
- The BFS/DFS graph layout places nodes evenly on a circle for a clear picture; it is not a general-purpose graph-layout algorithm.
- These are visualization scripts, not a published Python package (no `pip install mathviz` yet).

## 🚀 Usage

```bash
git clone https://github.com/sakibmostakimbhuiyan/MathViz.git
cd MathViz
pip install matplotlib numpy

python3 src/geometry.py pythagorean 3 4 --out outputs/pythagorean.png
python3 src/geometry.py inscribed-angle 80 --out outputs/inscribed_angle.png
python3 src/graph_algorithms.py   # generates outputs/bfs.png and outputs/dfs.png
python3 src/calculus.py           # generates outputs/calculus.png

python3 -m unittest discover -s tests
```

## 🗂️ Project Structure

```
src/        geometry.py, graph_algorithms.py, calculus.py
tests/      unit tests for the non-plotting logic (12 tests, all passing)
outputs/    generated images land here (not committed, see .gitignore)
```

## 🗺️ Roadmap

- [x] Geometry, graph traversal, and calculus modules with tested logic
- [ ] Animate BFS/DFS step-by-step instead of a single final image
- [ ] Add more theorems (Thales, triangle inequality)
- [ ] Package as an installable library

## 📄 License

MIT License. See [LICENSE](LICENSE).

## 👤 Author

**Sakib Mostakim Bhuiyan** · [GitHub](https://github.com/sakibmostakimbhuiyan)
