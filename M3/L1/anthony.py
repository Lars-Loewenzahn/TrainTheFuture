import sys
import json
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QListWidget, QPushButton, QTextEdit, QLineEdit,
    QMessageBox, QLabel, QFileDialog
)


class SmartNotesApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Smart Notes")
        self.resize(800, 600)

        self.notes_data = {}  # {filepath: {"content": str, "tags": []}}
        self.current_note_path = None

        self.init_ui()

    def init_ui(self):
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)

        # Left: text editor
        self.text_editor = QTextEdit()
        main_layout.addWidget(self.text_editor)

        # Right: layout for notes & tags
        right_layout = QVBoxLayout()

        # --- Notes list ---
        notes_label = QLabel("List of notes")
        self.notes_list = QListWidget()
        self.notes_list.itemClicked.connect(self.load_selected_note)

        note_buttons = QHBoxLayout()
        self.create_btn = QPushButton("Create note")
        self.save_btn = QPushButton("Save")
        self.delete_btn = QPushButton("Delete")

        self.create_btn.clicked.connect(self.create_note)
        self.save_btn.clicked.connect(self.save_note)
        self.delete_btn.clicked.connect(self.delete_note)

        note_buttons.addWidget(self.create_btn)
        note_buttons.addWidget(self.delete_btn)


        # --- Tags ---
        tags_label = QLabel("Tags")
        self.tags_list = QListWidget()
        self.tag_input = QLineEdit()
        self.tag_input.setPlaceholderText("Enter tag...")

        tag_buttons = QHBoxLayout()
        self.add_tag_btn = QPushButton("Add")
        self.remove_tag_btn = QPushButton("Remove")
        self.search_tag_btn = QPushButton("Search")

        self.add_tag_btn.clicked.connect(self.add_tag)
        self.remove_tag_btn.clicked.connect(self.remove_tag)
        self.search_tag_btn.clicked.connect(self.search_by_tag)

        tag_buttons.addWidget(self.add_tag_btn)
        tag_buttons.addWidget(self.remove_tag_btn)
        tag_buttons.addWidget(self.search_tag_btn)

        # --- Assemble UI ---
        right_layout.addWidget(notes_label)
        right_layout.addWidget(self.notes_list)
        right_layout.addLayout(note_buttons)
        right_layout.addWidget(self.save_btn)

        right_layout.addWidget(tags_label)
        right_layout.addWidget(self.tags_list)
        right_layout.addWidget(self.tag_input)
        right_layout.addLayout(tag_buttons)

        main_layout.addLayout(right_layout)

    def create_note(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Create Note", "", "JSON Files (*.json)")
        if file_path:
            if not file_path.endswith(".json"):
                file_path += ".json"
            default_data = {
                "content": "",
                "tags": []
            }
            with open(file_path, "w") as f:
                json.dump(default_data, f, indent=4)
            self.notes_data[file_path] = default_data
            self.notes_list.addItem(file_path)
            self.notes_list.setCurrentRow(self.notes_list.count() - 1)
            self.load_selected_note()

    def open_note(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Note", "", "JSON Files (*.json)")
        if file_path:
            try:
                with open(file_path, "r") as f:
                    data = json.load(f)
                self.notes_data[file_path] = data
                self.notes_list.addItem(file_path)
                self.notes_list.setCurrentRow(self.notes_list.count() - 1)
                self.load_selected_note()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not open file:\n{e}")

    def load_selected_note(self):
        item = self.notes_list.currentItem()
        if item:
            path = item.text()
            self.current_note_path = path
            note = self.notes_data.get(path, {})
            self.text_editor.setText(note.get("content", ""))
            self.tags_list.clear()
            self.tags_list.addItems(note.get("tags", []))

    def save_note(self):
        if self.current_note_path:
            content = self.text_editor.toPlainText()
            tags = [self.tags_list.item(i).text() for i in range(self.tags_list.count())]
            self.notes_data[self.current_note_path] = {"content": content, "tags": tags}
            try:
                with open(self.current_note_path, "w") as f:
                    json.dump(self.notes_data[self.current_note_path], f, indent=4)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not save file:\n{e}")

    def delete_note(self):
        if self.current_note_path:
            confirm = QMessageBox.question(self, "Delete", f"Delete file?\n{self.current_note_path}")
            if confirm == QMessageBox.Yes:
                try:
                    os.remove(self.current_note_path)
                    self.notes_data.pop(self.current_note_path, None)
                    for i in range(self.notes_list.count()):
                        if self.notes_list.item(i).text() == self.current_note_path:
                            self.notes_list.takeItem(i)
                            break
                    self.current_note_path = None
                    self.text_editor.clear()
                    self.tags_list.clear()
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Could not delete file:\n{e}")

    def add_tag(self):
        tag = self.tag_input.text().strip()
        if tag and self.current_note_path:
            tags = [self.tags_list.item(i).text() for i in range(self.tags_list.count())]
            if tag not in tags:
                self.tags_list.addItem(tag)
                self.tag_input.clear()

    def remove_tag(self):
        selected = self.tags_list.currentItem()
        if selected:
            self.tags_list.takeItem(self.tags_list.row(selected))

    def search_by_tag(self):
        tag = self.tag_input.text().strip()
        if tag:
            matched_files = []
            for path, data in self.notes_data.items():
                if tag in data.get("tags", []):
                    matched_files.append(path)
            self.notes_list.clear()
            self.notes_list.addItems(matched_files)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SmartNotesApp()
    window.show()
    sys.exit(app.exec_())

