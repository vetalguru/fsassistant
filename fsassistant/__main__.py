# Copyright (c) 2025 Vitalii Shkibtan
# Licensed under the MIT License.
# See LICENSE file in the project root for full license text.

from .cli import CliArgumentParser

def main() -> None:
    """
    Main entry point for the File System AI Assistant.
    Parses command line arguments and starts the assistant.
    """

    print("Initializing File System AI Assistant...")
    parser = CliArgumentParser()
    args = parser.parse_args()

    print("Starting Assistant...")
    print(f"Prompt: {args.prompt}")
    print(f"Working Directory: {args.working_directory}")

if __name__ == "__main__":
    main()
