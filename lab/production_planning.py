# /// script
# dependencies = ["numpy", "scipy", "sympy", "matplotlib"]
# ///
"""Verify the worked example and regenerate its figures: uv run lab/production_planning.py."""
# // math-verified: optimum=(40,20), contribution=2600; resource use=(100,80); corner contributions=(0,2000,2600,2000); extra-capacity optimum=(44,18), contribution=2660, gain=60.
from pathlib import Path
import json
import numpy as np
import sympy as sp
from scipy.optimize import linprog
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, StrMethodFormatter

root = Path(__file__).resolve().parents[1]
a = np.array([[2, 1], [1, 2]], dtype=float)
b = np.array([100, 80], dtype=float)
profit = np.array([40, 50], dtype=float)
x, y = sp.symbols('x y')
intersection = sp.solve([2*x+y-100, x+2*y-80], [x, y])
vertices = np.array([[0, 0], [50, 0], [40, 20], [0, 40]])
assert np.all(a @ vertices.T <= b[:, None])
values = vertices @ profit
result = linprog(-profit, A_ub=a, b_ub=b, bounds=(0, None), method='highs')
assert result.success and np.allclose(result.x, [40, 20])
assert np.array_equal(values, [0, 2000, 2600, 2000])
assert intersection == {x: 40, y: 20}
usage = a @ result.x
assert np.allclose(usage, [100, 80])
assert np.isclose(result.x.sum(), 60)
assert np.isclose(-result.fun - max(values[1], values[3]), 600)
extra = linprog(-profit, A_ub=a, b_ub=[106, 80], bounds=(0, None), method='highs')
assert extra.success and np.allclose(extra.x, [44, 18])
assert np.isclose(-extra.fun, float(40 * 44 + 50 * 18))
assert np.allclose(a @ extra.x, [106, 80])
assert np.isclose(-extra.fun + result.fun, 60)
print(json.dumps({'intersection': [int(intersection[x]), int(intersection[y])], 'corner_profits': values.tolist(), 'resource_use': usage.tolist(), 'units': int(result.x.sum()), 'improvement': 600, 'extra_machining_profit': round(-extra.fun, 2)}, indent=2))

ink, accent, paper = '#43413E', '#F53630', '#f5f4f1'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12, 'text.color': ink, 'axes.labelcolor': ink, 'axes.edgecolor': ink, 'xtick.color': ink, 'ytick.color': ink, 'svg.fonttype': 'none'})
xx = np.linspace(0, 60, 601)
for optimum in [False, True]:
    fig, ax = plt.subplots(figsize=(8.6, 5.4), layout='constrained')
    fig.patch.set_facecolor(paper)
    ax.set_facecolor(paper)
    ax.fill(vertices[:, 0], vertices[:, 1], facecolor=accent, alpha=.12, zorder=1)
    ax.plot(xx, b[0] - a[0, 0]*xx, color=ink, linewidth=1.8, label='Machining: 2x + y = 100')
    ax.plot(xx, (b[1] - a[1, 0]*xx)/a[1, 1], color=ink, linewidth=1.8, linestyle='--', label='Assembly: x + 2y = 80')
    ax.scatter(vertices[:, 0], vertices[:, 1], color=ink, s=32, zorder=4)
    ax.text(13, 14, 'FEASIBLE\nPRODUCTION', fontsize=11, weight='bold', linespacing=1.5)
    if optimum:
        ax.plot(xx, (2600-profit[0]*xx)/profit[1], color=accent, linewidth=2.2, label='Contribution: 40x + 50y = 2,600')
        ax.scatter([40], [20], s=90, color=accent, zorder=5)
        ax.annotate('OPTIMUM (40, 20)\n$2,600 / week', xy=(40, 20), xytext=(43, 30), fontsize=11, color=accent, weight='bold', arrowprops={'arrowstyle': '-', 'color': accent}, ha='left')
    else:
        ax.annotate('(40, 20)', xy=(40, 20), xytext=(43, 24), fontsize=11)
    ax.set(xlim=(0, 60), ylim=(0, 60), xlabel='Standard lamps / week (x)', ylabel='Studio lamps / week (y)')
    ax.xaxis.set_major_locator(MultipleLocator(10))
    ax.yaxis.set_major_locator(MultipleLocator(10))
    ax.xaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))
    ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))
    ax.spines[['top', 'right']].set_visible(False)
    ax.grid(color=ink, alpha=.10, linewidth=.6)
    ax.set_axisbelow(True)
    ax.legend(loc='upper right', frameon=False, fontsize=9)
    filename = 'optimal-mix' if optimum else 'feasible-region'
    fig.savefig(root / 'images' / 'production-planning' / f'{filename}.png', dpi=180)
    plt.close(fig)
