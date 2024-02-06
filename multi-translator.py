import tkinter as tk
from tkinter import scrolledtext
from googletrans import Translator
import datetime

class TranslationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Translator")

        # self.root.configure(bg="black")

        # Input Text
        self.label_input = tk.Label(root, text="Enter Text:")
        self.label_input.grid(row=0, column=1, columnspan=4)
        self.input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10, bg="light yellow")
        self.input_text.grid(row=1, column=1, columnspan=4)

        # Translation Results
        self.label_results = tk.Label(root, text="Translations:")
        self.label_results.grid(row=2, column=2, columnspan=2)

        # Translated Text Elements
        self.translated_texts = {}
        self.translated_text_widgets = {}
        languages = ["fr", "de", "es", "pt"]

        row_number = 3
        col_number = 0
        for language in languages:
            language_lower = language.lower()
            self.translated_texts[language_lower] = tk.StringVar()  # Use lowercase language code
            label = tk.Label(root, text=f"{language}:")
            label.grid(row=row_number, column=col_number, sticky='w', padx=5)

            text_element = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10, bg="light cyan")
            text_element.grid(row=row_number, column=col_number + 1, padx=5, pady=5)

            # Store the Text widget in a dictionary
            self.translated_text_widgets[language_lower] = text_element

            row_number += 1

            # Reset row_number and increment col_number to start a new row
            if row_number > 4:
                row_number = 3
                col_number += 3

        # Translate Button
        self.translate_button = tk.Button(root, text="Translate", command=self.translate_text, bg="light blue")
        self.translate_button.grid(row=6, column=2, columnspan=2, pady=10)

    def translate_text(self):
        input_text = self.input_text.get("1.0", tk.END).strip()
        selected_languages = ["fr", "de", "es", "pt"]

        if input_text:
            translations = self._get_translations(input_text, selected_languages)
            self._display_results(translations)
        else:
            for language in self.translated_texts:
                self.translated_texts[language].set("")

    def _get_translations(self, text, target_languages):
        translator = Translator()
        translations = {}
        for language in target_languages:
            translation = translator.translate(text, dest=language)
            translations[language] = translation.text
        return translations

    def _display_results(self, translations):
        for language, translation in translations.items():
            language_lower = language.lower()
            self.translated_texts[language_lower].set(translation)  # Use lowercase language code

            # Retrieve the corresponding Text widget and update its content
            text_element = self.translated_text_widgets[language_lower]
            text_element.config(state='normal')
            text_element.delete("1.0", tk.END)
            text_element.insert(tk.END, translation)
            text_element.config(state='disabled')

if __name__ == "__main__":
    today = datetime.date.today()
    thresholddate = datetime.date(2024, 4, 1)
    if today < thresholddate:
        root = tk.Tk()
        root.geometry("1000x600")
        app = TranslationApp(root)
        root.mainloop()
