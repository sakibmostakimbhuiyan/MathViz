"""Numerical derivative/integral approximation and visualization.
Numeric functions are pure and tested; plotting is separate.
"""


def numerical_derivative(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)


def numerical_integral(f, a, b, n=1000):
    """Composite trapezoidal rule."""
    if n <= 0:
        raise ValueError("n must be positive.")
    step = (b - a) / n
    total = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        total += f(a + i * step)
    return total * step


def plot_derivative_and_integral(f, x0, a, b, output_path, label="f(x)"):
    import matplotlib.pyplot as plt
    import numpy as np

    xs = np.linspace(a - 1, b + 1, 400)
    ys = [f(x) for x in xs]

    slope = numerical_derivative(f, x0)
    tangent_ys = [f(x0) + slope * (x - x0) for x in xs]

    fill_xs = np.linspace(a, b, 200)
    fill_ys = [f(x) for x in fill_xs]

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(xs, ys, label=label, color="tab:blue")
    ax.plot(xs, tangent_ys, "--", color="tab:red",
            label=f"tangent at x={x0} (slope≈{slope:.3f})")
    ax.fill_between(fill_xs, fill_ys, alpha=0.3, color="tab:green",
                     label=f"∫ from {a} to {b}")
    ax.axvline(x0, color="gray", linewidth=0.5)
    ax.legend()
    ax.set_title("Derivative (tangent line) and integral (shaded area)")
    fig.savefig(output_path, bbox_inches="tight", dpi=120)
    plt.close(fig)

    area = numerical_integral(f, a, b)
    return {"slope_at_x0": slope, "integral_a_to_b": area}


if __name__ == "__main__":
    f = lambda x: x ** 2
    result = plot_derivative_and_integral(f, x0=1.5, a=0, b=2,
                                           output_path="outputs/calculus.png")
    print(result)
