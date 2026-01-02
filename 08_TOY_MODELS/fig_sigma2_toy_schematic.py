import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge, Circle, FancyArrowPatch, Rectangle

# ------------------------------------------------------------
# Conceptual schematic for Σ₂ toy:
# (a) double-well potential in x
# (b) phase circle with gate near phi = pi
# (c) admissibility logic: cross + linger
# ------------------------------------------------------------

def V(x):
    return 0.25 * (x**2 - 1)**2

def main():
    fig, axs = plt.subplots(1, 3, figsize=(12, 3.6))

    # -------------------------
    # (a) Double-well potential
    # -------------------------
    ax = axs[0]
    x = np.linspace(-2.0, 2.0, 600)
    y = V(x)
    ax.plot(x, y, linewidth=2)
    ax.set_title("(a) First-order dynamics")
    ax.set_xlabel("$x$")
    ax.set_ylabel("$V(x)$")
    ax.set_xlim(-2, 2)
    ax.set_ylim(0, y.max() * 1.05)

    # Mark wells and saddle
    ax.axvline(0.0, linestyle="--", linewidth=1)
    ax.text(0.02, 0.95, "saddle", transform=ax.transAxes, va="top")
    ax.text(0.15, 0.12, "left well", transform=ax.transAxes)
    ax.text(0.62, 0.12, "right well", transform=ax.transAxes)

    # Two conceptual crossings (arrows) — one "non-admissible" (gray), one "admissible" (black)
    # (These are illustrative only; not data-driven.)
    y_arrow = 0.65 * y.max()
    ax.add_patch(FancyArrowPatch(
        (-1.0, y_arrow), (1.0, y_arrow),
        arrowstyle="->", mutation_scale=12, linewidth=2, alpha=0.35
    ))
    ax.text(0.03, 0.80, "stochastic crossings\noccur", transform=ax.transAxes, alpha=0.7)

    ax.add_patch(FancyArrowPatch(
        (-1.0, y_arrow * 0.78), (1.0, y_arrow * 0.78),
        arrowstyle="->", mutation_scale=12, linewidth=2
    ))
    ax.text(0.03, 0.62, "some become\nadmissible", transform=ax.transAxes)

    # -------------------------
    # (b) Phase gate on S^1  (IMPROVED + collision-fixed)
    # -------------------------
    ax = axs[1]
    # Put title a bit higher so it doesn't collide with the top tick label
    ax.set_title("(b) Phase gate", pad=16)
    ax.set_aspect("equal")
    ax.axis("off")

    R = 1.0

    # Outer circle
    ax.add_patch(Circle((0, 0), R, fill=False, linewidth=2))

    # Gate wedge near phi = pi (left side)
    gate_center = np.pi
    gate_half_width = 0.25  # radians
    theta1 = np.degrees(gate_center - gate_half_width)
    theta2 = np.degrees(gate_center + gate_half_width)
    ax.add_patch(Wedge((0, 0), R, theta1, theta2, width=0.25, alpha=0.25))

    # Cardinal ticks + labels: 0, pi/2, pi, 3pi/2
    # Move labels slightly inward to avoid title/caption collisions.
    ticks = [
        (0.0, r"$0$"),
        (0.5*np.pi, r"$\pi/2$"),
        (np.pi, r"$\pi$"),
        (1.5*np.pi, r"$3\pi/2$"),
    ]
    for ang, lab in ticks:
        x0, y0 = R*np.cos(ang), R*np.sin(ang)
        x1, y1 = 1.07*R*np.cos(ang), 1.07*R*np.sin(ang)
        ax.plot([x0, x1], [y0, y1], linewidth=2)

        # label radius (inward vs previous)
        rl = 1.16 * R
        xt, yt = rl*np.cos(ang), rl*np.sin(ang)

        # Nudge the top and bottom labels slightly to avoid collisions
        if np.isclose(ang, 0.5*np.pi):
            yt -= 0.06   # move pi/2 label slightly down
        if np.isclose(ang, 1.5*np.pi):
            yt += 0.06   # move 3pi/2 label slightly up

        ax.text(xt, yt, lab, ha="center", va="center")

    # Label the gate with an annotation arrow (placed above-left)
    gx, gy = 0.92*R*np.cos(gate_center), 0.92*R*np.sin(gate_center)
    ax.annotate(
        "gate",
        xy=(gx, gy),
        xytext=(-0.10, 1.28),
        textcoords="data",
        ha="center",
        arrowprops=dict(arrowstyle="->", linewidth=2),
    )

    # Direction of rotation (omega): small tangent arrow near top-right
    ang = 0.35*np.pi
    p = np.array([R*np.cos(ang), R*np.sin(ang)])
    tdir = np.array([-np.sin(ang), np.cos(ang)])  # ccw tangent
    q = p + 0.25*tdir
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="->", mutation_scale=12, linewidth=2))
    ax.text(q[0] + 0.10, q[1] + 0.05, r"$\omega$", ha="left", va="center")

    # Conceptual phase samples (NOT data): proto scattered vs true clustered near gate
    rng = np.random.default_rng(0)

    # Proto: scattered points
    proto_pts = rng.uniform(0, 2*np.pi, size=10)
    ax.scatter(0.97*R*np.cos(proto_pts), 0.97*R*np.sin(proto_pts), s=25, alpha=0.35)

    # True: clustered points near gate_center
    true_pts = gate_center + rng.normal(scale=0.18, size=10)
    ax.scatter(0.97*R*np.cos(true_pts), 0.97*R*np.sin(true_pts), s=25, alpha=0.9)

    # Move captions well below the circle to avoid the bottom tick label region
    ax.text(-1.05, -1.42, "true: stabilized", ha="left")
    ax.text(1.05, -1.42, "proto: diffuse", ha="right")

    # Small legend line further down
    ax.text(0.0, -1.62, r"$\phi \in S^1$ with narrow viable window", ha="center")
    # -------------------------
    # (c) Admissibility logic
    # -------------------------
    ax = axs[2]
    ax.set_title("(c) Admissibility criterion")
    ax.axis("off")

    # Layout: three rows of "events" with simple boxes + labels
    # Row positions
    y0 = 0.78
    dy = 0.27

    def draw_case(y, label_left, label_right, ok):
        # Left small box: "cross?"
        ax.add_patch(Rectangle((0.05, y - 0.06), 0.18, 0.12, fill=False, linewidth=2))
        ax.text(0.14, y, label_left, ha="center", va="center")

        # Arrow to right box
        ax.add_patch(FancyArrowPatch(
            (0.23, y), (0.42, y),
            arrowstyle="->", mutation_scale=12, linewidth=2
        ))

        # Right box: "in gate + linger?"
        ax.add_patch(Rectangle((0.42, y - 0.06), 0.38, 0.12, fill=False, linewidth=2))
        ax.text(0.61, y, label_right, ha="center", va="center")

        # Result marker
        ax.text(0.86, y, "✓" if ok else "✗", fontsize=18, va="center")

    draw_case(y0, "cross", "outside gate", ok=False)
    draw_case(y0 - dy, "cross", "in gate\n(no linger)", ok=False)
    draw_case(y0 - 2*dy, "cross", "in gate\n+ linger", ok=True)

    ax.text(0.05, 0.02,
            "Admissible = crossing occurs while in gate\n"
            "and phase remains in gate for a minimum duration.",
            transform=ax.transAxes)

    plt.tight_layout()

    # Save outputs
    out_pdf = "08_TOY_MODELS/fig_sigma2_toy_schematic.pdf"
    out_png = "08_TOY_MODELS/fig_sigma2_toy_schematic.png"
    fig.savefig(out_pdf, bbox_inches="tight")
    fig.savefig(out_png, dpi=200, bbox_inches="tight")
    print(f"Wrote: {out_pdf}")
    print(f"Wrote: {out_png}")

    plt.show()


if __name__ == "__main__":
    main()