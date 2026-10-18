"""Multibuy recovery extractor (2026-10-17).

Texts are the real RapidOCR reads of Kim Phat flyer-125 cell
renders (work/kim-phat/prevalence.json). The payload price is the
collapsed bundle total; the extractor must return the printed
per-unit price, the count and the total — or nothing.
"""

from grocery_meta_search.pipeline.multibuy import extract_multibuy

VERMICELLE = (
    "3POUR 5$ ainRi Rww LMA MAMA dreh VollkoroReisnudels 200G "
    "VERMICELLE DE RIZ BRUN MAMA 200G 1,99/CH BROWN RICE VERMICELLI REG.2,59"
)
SHIMEJI = "2POUR 199 CHAMPIGNONS SHIMEJI BLANCS PRODUIT DE CHINE 1,29/CH WHITE SHIMEJI MUSHROOMS REG.1,49/CH"
DURIAN = "2POUR 6 99 +TPS SOUFFLES AU DURIAN KIMPHAT-4X40G 3,99/CH+TPS REG.4,99/CH+TPS"
EPICES = "2POUR 3$ EPICES POUR CREVETTES ET FRUITS DE MER 1,69/CH REG.2,29/CH"
PAIN_VAPEUR = "2POUR 599 PAIN VAPEUR AU PORC ET LEGUMES KIMPHAT-1UN. REG.3,29/CH"
MURES = "3POUR 29 98 MORES PRODUIT DU MEXIQUE 227G-1,29/CH BLACKBERRIES REG.2,49/CH"


def test_badge_with_printed_unit() -> None:
    assert extract_multibuy(VERMICELLE, 5.0) == (1.99, 3, 5.0)
    assert extract_multibuy(SHIMEJI, 1.99) == (1.29, 2, 1.99)
    assert extract_multibuy(DURIAN, 6.99) == (3.99, 2, 6.99)
    assert extract_multibuy(EPICES, 3.0) == (1.69, 2, 3.0)


def test_badge_without_unit_falls_back_to_total_over_count() -> None:
    # Only the REG. unit prints; the badge total (599 = 5.99) equals
    # the payload, so the unit price is total / count.
    assert extract_multibuy(PAIN_VAPEUR, 5.99) == (3.0, 2, 5.99)


def test_garbled_badge_total_still_recovers_via_unit() -> None:
    # '3 POUR 2.98' read as '3POUR 29 98': the parsed total (29.98)
    # is wrong, but the unit print + bundle inequalities identify
    # the offer and the payload supplies the total.
    assert extract_multibuy(MURES, 2.98) == (1.29, 3, 2.98)


def test_name_pour_is_not_a_badge() -> None:
    assert extract_multibuy("PREPARATION POUR BOISSON AU CHOCOLAT 900G", 9.99) is None
    assert extract_multibuy("TRIPES DE BEUF POUR FONDUE CHINOISE 5,99/LB", 5.99) is None
    assert extract_multibuy("ENVELOPPES POUR WONTONS 400G", 2.29) is None


def test_bundle_inequalities_reject_plain_prices() -> None:
    # A badge-shaped read whose numbers cannot be a bundle of the
    # payload (unit not below payload, or payload not below
    # count * unit) is not recovered.
    assert extract_multibuy("2POUR 3$ EPICES 4,50/CH", 3.0) is None
    assert extract_multibuy("2POUR 3$ EPICES 1,20/CH", 3.0) is None


def test_no_payload_no_recovery() -> None:
    assert extract_multibuy(VERMICELLE, None) is None


METRO_PATES = "pâtes Selection 500 g, choix varié Selection pasta 2/4$ ou 299 l'unité"


def test_slash_badge_with_unite_unit() -> None:
    # Metro house style: '2/4$' badge, unit printed as '2,99 l'unité'
    # (OCR drops the decimal comma here: '299 l'unité' carries no
    # decimal part, so the total/count fallback applies).
    assert extract_multibuy(METRO_PATES, 4.0) == (2.0, 2, 4.0)


def test_slash_badge_decimal_unite() -> None:
    text = "pâtes Selection 500 g Selection pasta 2/4$ ou 2,99 l'unité"
    assert extract_multibuy(text, 4.0) == (2.99, 2, 4.0)


def test_slash_form_needs_dollar_sign() -> None:
    # A size fraction is not a badge.
    assert extract_multibuy("FILET 1/2 KG 3,50/CH", 3.5) is None
