from pathlib import Path


def read_input_file(filename: str) -> list[str]:
    return get_file_contents(filename).splitlines()


def get_file_contents(filename: str) -> str:
    return (Path(__file__).parent.parent.parent / f"inputs/{filename}").read_text()
