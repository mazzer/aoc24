from pathlib import Path


def read_input_file(filename: str):
    return (
        (Path(__file__).parent.parent.parent / f"inputs/{filename}")
        .read_text()
        .splitlines()
    )
