from pathlib import Path

from playwright.sync_api import sync_playwright

_playwright = None
_contexts = {}

PROFILE_ROOT = (
    Path(__file__).resolve().parent.parent
    / "profiles"
)

PROFILE_ROOT.mkdir(exist_ok=True)


def get_page(portal: str):

    global _playwright

    if _playwright is None:
        _playwright = sync_playwright().start()

    if portal not in _contexts:

        profile = PROFILE_ROOT / portal
        profile.mkdir(exist_ok=True)

        context = _playwright.chromium.launch_persistent_context(
            user_data_dir=str(profile),
            headless=True,
        )

        _contexts[portal] = context

    context = _contexts[portal]

    if context.pages:
        return context.pages[0]

    return context.new_page()