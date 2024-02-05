import tkinter as tk
from tkinter import scrolledtext
from googletrans import Translator

class TranslationApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x800")
        self.root.title("Multi-lang translator")

        # Input Text
        self.label_input = tk.Label(root, text="Enter Text in English:")
        self.label_input.pack()
        self.input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=15)
        self.input_text.pack()

        # Translation Results
        self.label_results = tk.Label(root, text="Translations:")
        self.label_results.pack()

        # Translated Text Elements
        self.translated_texts = {}
        languages = ["fr", "de", "es", "pt"]

        for language in languages:
            self.translated_texts[language.lower()] = tk.StringVar()  # Use lowercase language code
            label = tk.Label(root, text=f"{language}:")
            label.pack()
            text_element = tk.Entry(root, textvariable=self.translated_texts[language.lower()], state='readonly', width=80)
            text_element.pack()

        # Translate Button
        self.translate_button = tk.Button(root, text="Translate", command=self.translate_text)
        self.translate_button.pack()

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
            self.translated_texts[language].set(translation)  # Use lowercase language code

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslationApp(root)
    root.mainloop()
