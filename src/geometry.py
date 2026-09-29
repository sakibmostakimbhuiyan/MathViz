"""Geometry theorem visualizations: Pythagorean theorem and the inscribed
angle theorem (circle theorem). Pure-logic functions are separated from
plotting so they can be unit tested without matplotlib.
"""
import math


def pythagorean_areas(a, b):
    """Given leg lengths a, b of a right triangle, return (a^2, b^2, c^2, c)."""
    if a <= 0 or b <= 0:
        raise ValueError("Side lengths must be positive.")
    c = math.hypot(a, b)
    return {"a_sq": a ** 2, "b_sq": b ** 2, "c_sq": c ** 2, "c": c}


def inscribed_angle_ratio(central_angle_deg):
    """Inscribed angle theorem: inscribed angle = half the central angle
    subtending the same arc. Returns the inscribed angle in degrees."""
    if not (0 <= central_angle_deg <= 360):
        raise ValueError("Central angle must be between 0 and 360 degrees.")
    return central_angle_deg / 2


def plot_pythagorean(a, b, output_path):
    import matplotlib.pyplot as plt
    from matplotlib.patches import Polygon

    result = pythagorean_areas(a, b)
    fig, ax = plt.subplots(figsize=(6, 6))

    # Right triangle with legs along the axes
    triangle = [(0, 0), (a, 0), (0, b)]
    ax.add_patch(Polygon(triangle, fill=False, edgecolor="black", linewidth=2))

    # Square on side a (along x-axis, below)
    ax.add_patch(Polygon([(0, 0), (a, 0), (a, -a), (0, -a)],
                          facecolor="#8ecae6", edgecolor="black", alpha=0.6))
    ax.text(a / 2, -a / 2, f"a²={result['a_sq']:.1f}", ha="center", va="center")

    # Square on side b (along y-axis, left)
    ax.add_patch(Polygon([(0, 0), (0, b), (-b, b), (-b, 0)],
                          facecolor="#ffb703", edgecolor="black", alpha=0.6))
    ax.text(-b / 2, b / 2, f"b²={result['b_sq']:.1f}", ha="center", va="center")

    # Square on hypotenuse: hypotenuse runs from p1=(a,0) to p2=(0,b)
    p1, p2 = (a, 0), (0, b)
    dx, dy = p2[0] - p1[0], p2[1] - p1[1]
    length = math.hypot(dx, dy)  # == c
    nx, ny = dy / length, -dx / length  # outward normal (away from origin)
    p3 = (p1[0] + nx * length, p1[1] + ny * length)
    p4 = (p2[0] + nx * length, p2[1] + ny * length)
    ax.add_patch(Polygon([p1, p2, p4, p3], facecolor="#fb8500",
                          edgecolor="black", alpha=0.6))
    ax.text((p1[0] + p4[0]) / 2, (p1[1] + p4[1]) / 2,
            f"c²={result['c_sq']:.1f}", ha="center", va="center")

    ax.set_title(f"Pythagorean theorem: a²+b²=c²  ({result['a_sq']:.0f}+{result['b_sq']:.0f}={result['c_sq']:.0f})")
    ax.set_aspect("equal")
    ax.autoscale()
    ax.axis("off")
    fig.savefig(output_path, bbox_inches="tight", dpi=120)
    plt.close(fig)
    return result


def plot_inscribed_angle(central_angle_deg, output_path):
    import matplotlib.pyplot as plt

    inscribed = inscribed_angle_ratio(central_angle_deg)
    fig, ax = plt.subplots(figsize=(6, 6))
    circle = plt.Circle((0, 0), 1, fill=False, edgecolor="black")
    ax.add_patch(circle)

    start_deg = 90 - central_angle_deg / 2
    end_deg = 90 + central_angle_deg / 2
    p_start = (math.cos(math.radians(start_deg)), math.sin(math.radians(start_deg)))
    p_end = (math.cos(math.radians(end_deg)), math.sin(math.radians(end_deg)))
    p_apex = (math.cos(math.radians(270)), math.sin(math.radians(270)))

    ax.plot(*zip((0, 0), p_start), color="tab:blue")
    ax.plot(*zip((0, 0), p_end), color="tab:blue")
    ax.plot(*zip(p_apex, p_start), color="tab:red")
    ax.plot(*zip(p_apex, p_end), color="tab:red")

    ax.set_title(f"Central {central_angle_deg}° → inscribed {inscribed}° (same arc)")
    ax.set_aspect("equal")
    ax.axis("off")
    fig.savefig(output_path, bbox_inches="tight", dpi=120)
    plt.close(fig)
    return inscribed


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Geometry theorem visualizer.")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p1 = sub.add_parser("pythagorean")
    p1.add_argument("a", type=float)
    p1.add_argument("b", type=float)
    p1.add_argument("--out", default="outputs/pythagorean.png")

    p2 = sub.add_parser("inscribed-angle")
    p2.add_argument("central_angle", type=float)
    p2.add_argument("--out", default="outputs/inscribed_angle.png")

    args = parser.parse_args()
    if args.cmd == "pythagorean":
        result = plot_pythagorean(args.a, args.b, args.out)
        print(f"Saved {args.out}. c = {result['c']:.3f}")
    else:
        inscribed = plot_inscribed_angle(args.central_angle, args.out)
        print(f"Saved {args.out}. Inscribed angle = {inscribed}°")
