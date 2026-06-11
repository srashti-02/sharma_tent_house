import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent / "src")
)

from services.availability_service import dates_overlap


def test_overlap_true():
    assert dates_overlap(
        "2026-06-10",
        "2026-06-18",
        "2026-06-12",
        "2026-06-16"
    )


def test_overlap_false():
    assert not dates_overlap(
        "2026-06-01",
        "2026-06-05",
        "2026-06-10",
        "2026-06-15"
    )