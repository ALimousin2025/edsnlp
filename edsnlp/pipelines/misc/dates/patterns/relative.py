from edsnlp.utils.regex import make_pattern

from . import directions, numbers, units


def make_specific_pattern(forward: bool = True):

    if forward:
        p = directions.preceding_direction_pattern
        p += r"\s+"
        p += numbers.number_pattern
        p += r"\s+"
        p += units.unit_pattern
    else:
        p = numbers.number_pattern
        p += r"\s+"
        p += units.unit_pattern
        p += r"\s+"
        p += directions.following_direction_pattern

    return p


relative_patterns = [
    make_specific_pattern(forward=True),
    make_specific_pattern(forward=False),
]

specific = {
    "minus1": (r"hier", dict(direction="ago", day=1)),
    "minus2": (r"avant[-\s]hier", dict(direction="ago", day=2)),
    "plus1": (r"demain", dict(direction="in", day=1)),
    "plus2": (r"après[-\s]demain", dict(direction="in", day=2)),
}

specific_pattern = make_pattern(
    [f"(?P<specific_{k}>{p})" for k, (p, _) in specific.items()],
)

specific_dict = {k: v for k, (_, v) in specific.items()}

relative_patterns.append(specific_pattern)
