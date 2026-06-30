from app.discovery_models import OpportunityCandidate


LIKELY = [
    "opportun",
    "tender",
    "procurement",
    "call",
    "expression of interest",
    "eoi",
    "consult",
    "vacanc",
    "fund",
    "grant",
    "rfp",
    "rfq",
]

POSSIBLE = [
    "register",
    "login",
    "sign in",
    "resource",
]


def rank_navigation(
    candidates: list[OpportunityCandidate],
) -> list[OpportunityCandidate]:

    ranked = []

    for c in candidates:

        title = c.title.lower()

        if any(k in title for k in LIKELY):
            ranked.append(c)

    if ranked:
        return ranked

    for c in candidates:

        title = c.title.lower()

        if any(k in title for k in POSSIBLE):
            ranked.append(c)

    return ranked