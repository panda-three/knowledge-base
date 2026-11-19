from pathlib import Path

from pypdf import PdfReader, PdfWriter
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[2]
QUESTION_PDF = ROOT / "C语言题目汇总.pdf"
ANSWER_PDF = ROOT / "答案.pdf"
TOC_PDF = ROOT / "tmp" / "pdfs" / "目录页.pdf"
OUT_PDF = ROOT / "output" / "pdf" / "C语言题目汇总_含答案_带目录.pdf"


def collect_names() -> list[tuple[str, str]]:
    entries: list[tuple[str, str]] = []
    for dirname in ("真题", "模拟题"):
        folder = ROOT / dirname
        names = sorted(path.stem for path in folder.glob("*.md"))
        entries.extend((dirname, name) for name in names)
    return entries


def draw_toc(entries: list[tuple[str, str]]) -> None:
    registerFont(UnicodeCIDFont("STSong-Light"))
    width, height = A4
    c = canvas.Canvas(str(TOC_PDF), pagesize=A4)

    margin_x = 24 * mm
    y = height - 28 * mm
    c.setFont("STSong-Light", 24)
    c.setFillColor(colors.HexColor("#111827"))
    c.drawString(margin_x, y, "目录")

    y -= 13 * mm
    c.setFont("STSong-Light", 10.5)
    c.setFillColor(colors.HexColor("#6b7280"))
    c.drawString(margin_x, y, "C语言题目汇总 + 答案")

    y -= 13 * mm
    current_section = None
    line_height = 7.2 * mm

    for section, name in entries:
        if y < 24 * mm:
            c.showPage()
            y = height - 25 * mm
            current_section = None

        if section != current_section:
            c.setFont("STSong-Light", 14)
            c.setFillColor(colors.HexColor("#111827"))
            c.drawString(margin_x, y, section)
            y -= 8 * mm
            current_section = section

        c.setFont("STSong-Light", 11)
        c.setFillColor(colors.HexColor("#1f2937"))
        c.drawString(margin_x + 7 * mm, y, name)
        y -= line_height

    c.save()


def merge() -> None:
    entries = collect_names()
    draw_toc(entries)

    writer = PdfWriter()
    for pdf in (TOC_PDF, QUESTION_PDF, ANSWER_PDF):
        reader = PdfReader(str(pdf))
        for page in reader.pages:
            writer.add_page(page)

    OUT_PDF.parent.mkdir(parents=True, exist_ok=True)
    with OUT_PDF.open("wb") as f:
        writer.write(f)

    print(OUT_PDF)
    print(f"entries={len(entries)}")
    print(f"pages={len(PdfReader(str(OUT_PDF)).pages)}")


if __name__ == "__main__":
    merge()
