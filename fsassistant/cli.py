# Copyright (c) 2025 Vitalii Shkibtan
# Licensed under the MIT License.
# See LICENSE file in the project root for full license text.

import argparse


class CliArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog="fsassistant", description="File System AI Assistant"
        )
        self._add_arguments()

    def _add_arguments(self) -> None:
        self.parser.add_argument(
            "--prompt",
            type=str,
            help="File System AI Assistant prompt",
            required=True,
        )

        self.parser.add_argument(
            "--working_directory",
            type=str,
            help="Working directory for the File System AI Assistant",
            required=True,
        )

    def parse_args(self, args=None):
        return self.parser.parse_args(args)
