import io
import os
import unittest

os.environ.setdefault("TELEGRAM_BOT_TOKEN", "123:test")
os.environ.setdefault("OPENAI_API_KEY", "sk-test")
os.environ.setdefault("DATABASE_URL", "postgresql://test:test@localhost/test")

from docx import Document

from bot import extract_text


class ExtractTextTest(unittest.TestCase):
    def test_txt(self):
        self.assertEqual(extract_text("notes.txt", "Привет".encode()), "Привет")

    def test_docx(self):
        stream = io.BytesIO()
        document = Document()
        document.add_paragraph("Учебный материал")
        document.save(stream)
        self.assertIn("Учебный материал", extract_text("notes.docx", stream.getvalue()))

    def test_rejects_unknown_format(self):
        with self.assertRaises(ValueError):
            extract_text("notes.csv", b"a,b")


if __name__ == "__main__":
    unittest.main()
