"""Page-harvest tests: extraction policy + config (no network, no OCR)."""

from grocery_meta_search.pipeline.harvest import (
    harvest_from_lines,
    load_harvest_configs,
)


def test_single_size_fills() -> None:
    lines = ["riz Vite & Bon", "Ben's Original", "132 g, choix varié", "reg. 1,99"]
    assert harvest_from_lines(lines, True, True) == {"size": "132 g"}


def test_two_distinct_sizes_stay_empty() -> None:
    lines = ["SAUCES BBQ", "350 ml", "ou format 750 ml en spécial"]
    # two weight/volume rivals: ambiguous, no fill
    assert "size" not in harvest_from_lines(lines, True, False)


def test_count_plus_weight_resolves_to_weight() -> None:
    lines = ["CREVETTES 60-70 UNITÉS", "907 g"]
    assert harvest_from_lines(lines, True, False) == {"size": "907 g"}


def test_same_size_twice_is_one_distinct_value() -> None:
    lines = ["NUTELLA 725 g", "tartinade", "725g"]
    assert harvest_from_lines(lines, True, False) == {"size": "725 g"}


def test_unit_capture_and_conflicts() -> None:
    assert harvest_from_lines(["2,95 $/KG", "BOEUF HACHÉ"], False, True) == {
        "unit": "kg"
    }
    assert harvest_from_lines(["CH/EA", "POMMES"], False, True) == {"unit": "each"}
    # two different units printed: ambiguous, no fill
    assert harvest_from_lines(["$/lb", "ou $/kg"], False, True) == {}
    # a package size is not a price unit
    assert harvest_from_lines(["132 g, choix varié"], False, True) == {}


def test_fields_switches_respected() -> None:
    lines = ["132 g", "$/lb"]
    assert harvest_from_lines(lines, True, False) == {"size": "132 g"}
    assert harvest_from_lines(lines, False, True) == {"unit": "lb"}
    assert harvest_from_lines(lines, False, False) == {}


def test_descending_range_garble_rejected() -> None:
    # OCR stitched two format ranges into a descending one (metro cheese).
    lines = ["fromage Cracker Barrel", "250-220g", "choix varié"]
    assert "size" not in harvest_from_lines(lines, True, False)
    # Ascending ranges are real and fill normally.
    lines = ["YOGOURT PLANT BASED", "500 - 650 G"]
    assert harvest_from_lines(lines, True, False) == {"size": "500 - 650 G"}


def test_grocery_litre_cap() -> None:
    # Round-2 review: OCR stitches stored celery as "66L"; grocery
    # packages top out at the 18.9 L water-jug format.
    assert "size" not in harvest_from_lines(["CELERIS", "66L"], True, False)
    assert harvest_from_lines(["EAU", "18.9 L"], True, False) == {"size": "18.9 L"}


def test_protein_callout_not_harvested() -> None:
    # Round-2 review: protein badges filled as sizes (IGA skewers).
    lines = ["BROCHETTES DE POULET", "23G DE PROTÉINES PAR PORTION"]
    assert "size" not in harvest_from_lines(lines, True, False)


def test_config_shape() -> None:
    configs = load_harvest_configs()
    assert "marches-tau" in configs and "super-c" in configs
    assert "akhavan" not in configs  # structured source, no harvest needed
    assert configs["bulk-barn"]["fields"] == ["unit"]


def test_harvest_per_unit_denominator() -> None:
    """Unit-price references in small print are not the package:
    they must not block the real size through ambiguity, nor pose
    as the price unit of a pack item (giant-tiger, round-2 review)."""
    # Jam: real size range + a per-unit reference range.
    got = harvest_from_lines(
        ["Confiture Triple Fruits", "375-500 ml", "0,79-1,06/100 ml"],
        want_size=True, want_unit=True,
    )
    assert got.get("size") == "375-500 ml"
    # 12-pack: the '0,50/100 g' reference is not the pack's unit.
    got = harvest_from_lines(
        ["Barres 12 x 100 g", "5,96", "0,50/100 g"],
        want_size=True, want_unit=True,
    )
    assert "unit" not in got
    # Weighed goods: no package size anywhere, so the denominator
    # IS the price basis and the unit survives.
    got = harvest_from_lines(
        ["Poitrine de dinde", "2,99/100 g"],
        want_size=True, want_unit=True,
    )
    assert got.get("unit") == "100g"
    assert "size" not in got
