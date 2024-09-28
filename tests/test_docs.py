from aittor.app.services.config.config_default import AIAppConfig
from scripts.update_config_docstring import generate_config_docstrings


def test_app_config_docstrings_are_current():
    # If this test fails, run `python scripts/update_config_docstring.py`. See the comments in that script for
    # an explanation of why this is necessary.
    #
    # A make target is provided to run the script: `make update-config-docstring`.

    assert AIAppConfig.__doc__ is not None

    generated_docstring = generate_config_docstrings()

    formatted_dunder_docstring = f'    """{AIAppConfig.__doc__.strip()}\n    """'

    assert generated_docstring == formatted_dunder_docstring
