"""This is a wrapper around the main app entrypoint, to allow for CLI args to be parsed before running the app."""


def run_app() -> None:
    # Before doing _anything_, parse CLI args!
    from aittor.frontend.cli.arg_parser import AppConfigArgs

    AppConfigArgs.parse_args()

    from aittor.app.api_app import app_api

    app_api()
