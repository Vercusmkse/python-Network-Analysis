from typing import List, Tuple


# SVG primitives

def line(x1: int, y1: int, x2: int, y2: int) -> str:
    """Create an SVG line element."""
    return (
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
        f'stroke="black" stroke-width="2" />'
    )


def circle(cx: int, cy: int, r: int) -> str:
    """Create an SVG circle element."""
    return (
        f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="white" '
        f'stroke="black" stroke-width="2" />'
    )


def text(x: int, y: int, content: str, size: int = 14) -> str:
    """Create an SVG text element."""
    return (
        f'<text x="{x}" y="{y}" font-family="Verdana" font-size="{size}" '
        f'fill="black" text-anchor="middle">{content}</text>'
    )


def rect(x: int, y: int, width: int, height: int) -> str:
    """Create an SVG rectangle element."""
    return (
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}" '
        f'fill="white" stroke="black" stroke-width="2" />'
    )


def rotate(el: str, angle: int, cx: int, cy: int) -> str:
    """Rotate an SVG element around a point."""
    return (
        f'<g transform="rotate({angle} {cx} {cy})">{el}</g>'
    )


def translate(el: str, dx: int, dy: int) -> str:
    """Translate an SVG element."""
    return (
        f'<g transform="translate({dx} {dy})">{el}</g>'
    )


def scale(el: str, sx: float, sy: float) -> str:
    """Scale an SVG element."""
    return (
        f'<g transform="scale({sx} {sy})">{el}</g>'
    )


def svg(width: int, height: int, elements: List[str]) -> str:
    """Create an SVG image with the given elements."""
    return (
        f'<svg width="{width}" height="{height}" '
        f'xmlns="http://www.w3.org/2000/svg">{"".join(elements)}</svg>'
    )


# Graph types

def bar_chart(data: List[Tuple[int, int]]) -> str:
    """Create a bar chart SVG from the given data."""
    elements = []
    max_value = max(datum[1] for datum in data)
    bar_width = 50
    bar_height = 200
    for i, (index, value) in enumerate(data):
        x = 25 + i * 75
        y = 250 - value / max_value * bar_height
        elements.extend([
            rect(x, y, bar_width, value / max_value * bar_height),
            text(x + bar_width // 2, y - 10, str(value)),
            text(x + bar_width // 2, 270, str(index)),
        ])
    image_width = 25 + len(data) * 75
    image_height = 300
    return svg(image_width, image_height, elements)
