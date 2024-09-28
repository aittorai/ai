#!/usr/bin/env python

# Copyright (c) 2022 App Development Team

import logging
import os

from aittor.app.run_app import run_app

logging.getLogger("xformers").addFilter(lambda record: "A matching Triton is not available" not in record.getMessage())


def main():
    # Change working directory to the repo root
    os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    run_app()


if __name__ == "__main__":
    main()
