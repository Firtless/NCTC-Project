# NCTC
# Object-Oriented Architecture for Notes

import os
from pathlib import Path
from typing import List, Optional
from datetime import datetime


class NoteManager:

    def __init__(self, storage_path: str = "notes.txt"):
        self.storage_path: Path = Path(storage_path)
        self.session_notes: List[str] = [
            "NCTC Note taking, type to your heart content "]

    def add_note(self, note_text: str):
        cleaned_text = note_text.strip()
        if cleaned_text:
            self.session_notes.append(cleaned_text)

    def save_disk(self):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        try:
            with open(self.storage_path, "a", encoding="utf-8") as file:
                file.write(f"\nSession ended: {timestamp}\n")
                file.write("=" * 35 + "\n")
                for note in self.session_notes[1:]:
                    file.write(f"{note}\n")
            return True
        except IOError as err:
            print(f"ERROR couldn't save: {err}")
            return False

    def read_notes(self):
        if not self.storage_path.exists():
            return "No previos Note history found"

        try:
            return self.storage_path.read_text(encoding="utf-8")
        except IOError as err:
            return f"Error couldn't read file: {err}"


def notepad_cli():
    manager = NoteManager(storage_path="demo_file.txt")
    print(f"\n<<< {manager.session_notes[0]} >>>")

    while True:
        usr_input = input("Note > ").strip()

        if usr_input.lower() == "quit":
            break

        manager.add_note(usr_input)

    if manager.save_disk():
        print("\n--- Content of Saved Notes ---")
        print(manager.read_notes())
        os.system('open "demo_file.txt"')


if __name__ == "__main__":
    notepad_cli()
