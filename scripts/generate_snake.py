#!/usr/bin/env python3
"""
Simple placeholder SVG generator for a 'github-snake' image.
This is a visual placeholder — you can later replace this script
with a generator that reads your real contributions.
"""

import sys
from math import sin, pi

OUT = sys.argv[1] if len(sys.argv) > 1 else "output/github-snake.svg"

width, height = 800, 140
cells_x, cells_y = 52, 7
cell_w, cell_h = width / cells_x, height / cells_y

svg = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
    '<rect width="100%" height="100%" fill="transparent"/>'
]

# faint grid (optional)
for y in range(cells_y):
    for x in range(cells_x):
        svg.append(f'<rect x="{x*cell_w:.2f}" y="{y*cell_h:.2f}" width="{cell_w-1:.2f}" height="{cell_h-1:.2f}" fill="#0d1117" stroke="#0b0b0b" stroke-width="0.4" />')

# snake path (circles wave)
for i in range(cells_x):
    y_pos = (cells_y/2 + (cells_y/2 - 0.6) * sin(i * 2*pi / 12)) * cell_h + cell_h*0.1
    cx = i*cell_w + cell_w/2
    cy = y_pos
    r = min(cell_w, cell_h) * 0.35
    color = "#0CE6F2" if i % 4 == 0 else "#61dafb"
    svg.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{color}" />')

# head
svg.append(f'<circle cx="{(cells_x-1)*cell_w + cell_w/2:.1f}" cy="{(cells_y/2)*cell_h:.1f}" r="{cell_h*0.5:.1f}" fill="#0CE6F2" />')

svg.append("</svg>")

open(OUT, "w", encoding="utf-8").write("\n".join(svg))
print(f"Written {OUT}")
