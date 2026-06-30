from __future__ import annotations

import hashlib
import xml.etree.ElementTree as et
import zipfile
from pathlib import Path
from typing import List


WORD_NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def read_docx_paragraphs(path: Path) -> List[str]:
    """Extract non-empty paragraphs from a .docx file in ordinal order."""
    paragraphs: List[str] = []
    with zipfile.ZipFile(path, "r") as archive:
        xml_bytes = archive.read("word/document.xml")
    root = et.fromstring(xml_bytes)
    for paragraph in root.findall(".//w:p", WORD_NS):
        chunks: List[str] = []
        for node in paragraph.findall(".//w:t", WORD_NS):
            if node.text:
                chunks.append(node.text)
        text = "".join(chunks).strip()
        if text:
            paragraphs.append(text)
    return paragraphs


def stable_text_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

