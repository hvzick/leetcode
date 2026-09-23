import os
import re
from bisect import bisect_left
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt

try:
    import mplcursors
except Exception:
    mplcursors = None


def get_file_creation_date(filename):
    try:
        # Local filesystem creation time.
        created_ts = os.path.getctime(filename)
        return datetime.fromtimestamp(created_ts)
    except Exception:
        return None


def is_problem_file(filename):
    # Matches names like: 0001E Two Sum.py, 00198M House Robber.py
    return re.match(r"^\d+[EMH] .+\.py$", filename) is not None


def main():
    files = [f for f in os.listdir(".") if f.endswith(".py") and is_problem_file(f)]

    # {year: {iso_week: count}}
    data = defaultdict(lambda: defaultdict(int))

    for file in files:
        date = get_file_creation_date(file)
        if date and date.year > 2023:
            year = date.year
            week_key = date.isocalendar().week
            data[year][week_key] += 1

    plt.figure(figsize=(12, 5))

    # Keep only weeks where at least one file was created (globally).
    all_weeks = sorted({week for year_data in data.values() for week in year_data.keys()})
    if not all_weeks:
        print("No file creation data found after 2023")
        return

    x_vals = list(range(len(all_weeks)))

    current_week = datetime.now().isocalendar().week

    scatter_handles = []
    yearly_series = {}

    # Plot each year on the same week axis. Missing weeks are 0 so lines touch x-axis.
    for year in sorted(data.keys()):
        if year == 2026:
            base_weeks = [week for week in all_weeks if week <= current_week]
        else:
            base_weeks = all_weeks

        # Start plotting from the first week with at least one created file for that year.
        first_non_zero_idx = None
        for idx, week in enumerate(base_weeks):
            if data[year].get(week, 0) > 0:
                first_non_zero_idx = idx
                break

        if first_non_zero_idx is None:
            continue

        plot_weeks = base_weeks[first_non_zero_idx:]

        x_plot = [all_weeks.index(week) for week in plot_weeks]
        y_vals = [data[year].get(week, 0) for week in plot_weeks]

        if year == 2024:
            color = "green"
            marker_size = 22
            zorder = 3
            line_width = 1.2
            alpha = 0.35
        elif year == 2025:
            color = "red"
            marker_size = 24
            zorder = 4
            line_width = 1.2
            alpha = 0.35
        elif year == 2026:
            color = "blue"
            marker_size = 58
            zorder = 5
            line_width = 2.4
            alpha = 1.0
        else:
            color = "gray"
            marker_size = 24
            zorder = 2
            line_width = 0.9
            alpha = 0.35

        plt.plot(x_plot, y_vals, color=color, linewidth=line_width, alpha=alpha, label=str(year), zorder=zorder)
        scatter = plt.scatter(x_plot, y_vals, color=color, s=marker_size, alpha=alpha, zorder=zorder)

        # Vertical guides from x-axis to start/end points for each year.
        plt.vlines(
            [x_plot[0], x_plot[-1]],
            [0, 0],
            [y_vals[0], y_vals[-1]],
            colors=color,
            linestyles="-",
            linewidth=1.0,
            alpha=0.45,
            zorder=max(1, zorder - 1),
        )
        yearly_series[year] = (x_plot, y_vals, color)

        # Store full labels for hover annotations.
        scatter._week_labels = [f"W{week:02d}" for week in plot_weeks]
        scatter._year = year
        scatter._counts = y_vals
        scatter_handles.append(scatter)

    week_labels = [f"W{week:02d}" for week in all_weeks]
    tick_step = 2 if len(all_weeks) <= 30 else 3
    tick_positions = x_vals[::tick_step]
    tick_labels = week_labels[::tick_step]
    plt.xticks(tick_positions, tick_labels, rotation=45, ha="right")

    # Secondary axis for cumulative yearly trend (dashed).
    ax1 = plt.gca()
    ax2 = ax1.twinx()
    for year in sorted(yearly_series.keys()):
        x_plot, y_vals, color = yearly_series[year]
        cumulative = []
        running = 0
        for value in y_vals:
            running += value
            cumulative.append(running)

        ax2.plot(
            x_plot,
            cumulative,
            linestyle="--",
            linewidth=1,
            color=color,
            alpha=0.8,
            label=f"{year} cumulative",
            zorder=1,
        )

    # Vertical marker for current week.
    insert_pos = bisect_left(all_weeks, current_week)
    if insert_pos < len(all_weeks) and all_weeks[insert_pos] == current_week:
        current_x = insert_pos
    elif insert_pos == 0:
        current_x = 0
    elif insert_pos >= len(all_weeks):
        current_x = len(all_weeks) - 1
    else:
        current_x = insert_pos - 0.5

    ax1.axvline(current_x, color="black", linestyle="--", linewidth=1.1, alpha=0.75, label="Current week")
    y_top = ax1.get_ylim()[1]
    ax1.text(current_x + 0.1, y_top * 0.92, "Current week", rotation=90, va="top", ha="left", fontsize=9)

    # Keep full week labels in hover annotations.
    if mplcursors is not None and scatter_handles:
        cursor = mplcursors.cursor(scatter_handles, hover=True)

        @cursor.connect("add")
        def on_add(sel):
            artist = sel.artist
            idx = sel.index
            week_label = artist._week_labels[idx]
            year = artist._year
            count = artist._counts[idx]
            sel.annotation.set_text(f"Year: {year}\nWeek: {week_label}\nFiles created: {count}")

    # Clear baseline and subtle horizontal grid lines only.
    ax1.axhline(0, color="dimgray", linewidth=1.4, zorder=1)
    ax1.grid(axis="y", linestyle="-", linewidth=0.6, alpha=0.25)

    plt.xlabel("Weeks (Only Weeks With File Creation)")
    plt.ylabel("Problems Solved")
    ax2.set_ylabel("Cumulative Problems")
    plt.suptitle("Weekly LeetCode File Creation Activity (2024-2026)")
    ax1.set_title("Weeks with no creations globally are excluded", fontsize=10, pad=8)

    # Merge legends from both axes.
    h1, l1 = ax1.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax1.legend(h1 + h2, l1 + l2, loc="upper left")

    plt.tight_layout()

    plt.savefig("weekly_activity.png", dpi=300, bbox_inches="tight")
    print("Saved as weekly_activity.png")


if __name__ == "__main__":
    main()