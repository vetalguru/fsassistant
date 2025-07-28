# Copyright (c) 2025 Vitalii Shkibtan
# Licensed under the MIT License.
# See LICENSE file in the project root for full license text.

import pytest
from fsassistant.cli import CliArgumentParser


def test_valid_arguments():
    parser = CliArgumentParser()
    args = parser.parse_args([
        "--prompt", "Sort files by date",
        "--working_directory", "/tmp/testdir"
    ])
    assert args.prompt == "Sort files by date"
    assert args.working_directory == "/tmp/testdir"


def test_missing_prompt():
    parser = CliArgumentParser()
    with pytest.raises(SystemExit) as excinfo:
        parser.parse_args([
            "--working_directory", "/tmp/testdir"
        ])
    assert excinfo.value.code == 2


def test_missing_working_directory():
    parser = CliArgumentParser()
    with pytest.raises(SystemExit) as excinfo:
        parser.parse_args([
            "--prompt", "Find duplicates"
        ])
    assert excinfo.value.code == 2


def test_no_arguments():
    parser = CliArgumentParser()
    with pytest.raises(SystemExit) as excinfo:
        parser.parse_args([])
    assert excinfo.value.code == 2
