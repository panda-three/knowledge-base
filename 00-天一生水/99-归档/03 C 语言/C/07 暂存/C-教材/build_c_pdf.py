from __future__ import annotations

import html
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm, mm
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Preformatted,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.platypus.tableofcontents import TableOfContents


ROOT = Path(__file__).resolve().parent
QUESTIONS = ROOT / "C语言题目汇总.md"
ANSWERS = ROOT / "答案.md"
OUT = ROOT / "C语言题目汇总_含答案_打印版.pdf"


registerFont(UnicodeCIDFont("STSong-Light"))


class PrintDoc(BaseDocTemplate):
    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph):
            text = getattr(flowable, "_toc_text", None)
            level = getattr(flowable, "_toc_level", None)
            if text is not None and level is not None:
                self.notify("TOCEntry", (level, text, self.page))


styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="CoverTitle",
        fontName="STSong-Light",
        fontSize=28,
        leading=36,
        alignment=TA_CENTER,
        spaceAfter=18,
    )
)
styles.add(
    ParagraphStyle(
        name="CoverSub",
        fontName="STSong-Light",
        fontSize=13,
        leading=22,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#4b5563"),
    )
)
styles.add(
    ParagraphStyle(
        name="PartTitle",
        fontName="STSong-Light",
        fontSize=19,
        leading=26,
        spaceBefore=8,
        spaceAfter=12,
        textColor=colors.HexColor("#111827"),
    )
)
styles.add(
    ParagraphStyle(
        name="SuiteTitle",
        fontName="STSong-Light",
        fontSize=16,
        leading=23,
        spaceBefore=12,
        spaceAfter=9,
        textColor=colors.HexColor("#111827"),
    )
)
styles.add(
    ParagraphStyle(
        name="QuestionTitle",
        fontName="STSong-Light",
        fontSize=13,
        leading=19,
        spaceBefore=8,
        spaceAfter=6,
        textColor=colors.HexColor("#1f2937"),
    )
)
styles.add(
    ParagraphStyle(
        name="BodyCN",
        fontName="STSong-Light",
        fontSize=10.2,
        leading=15.8,
        spaceAfter=5,
        alignment=TA_LEFT,
    )
)
styles.add(
    ParagraphStyle(
        name="SmallCN",
        fontName="STSong-Light",
        fontSize=9.2,
        leading=13.6,
        spaceAfter=4,
        alignment=TA_LEFT,
    )
)
styles.add(
    ParagraphStyle(
        name="Footer",
        fontName="STSong-Light",
        fontSize=8,
        leading=10,
        alignment=TA_RIGHT,
        textColor=colors.HexColor("#6b7280"),
    )
)


def clean_inline(s: str) -> str:
    s = normalize_text(s)
    s = re.sub(r"`([^`]+)`", r"<font name='Courier'>\1</font>", html.escape(s))
    return s


def normalize_text(s: str) -> str:
    for _ in range(3):
        s = s.replace("\\\\", "\\")
    s = s.replace("\\*", "*").replace("\\_", "_").replace("\\+", "+")
    s = s.replace("\\~", "~").replace("\\.", ".").replace("\\-", "-")
    s = s.replace("\\(", "(").replace("\\)", ")")
    s = s.replace("\\[", "[").replace("\\]", "]")
    s = s.replace("\\<", "<").replace("\\>", ">")
    s = s.replace("\\&lt;", "<").replace("\\&gt;", ">")
    s = s.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
    return s


def para(text: str, style="BodyCN") -> Paragraph:
    return Paragraph(clean_inline(text), styles[style])


def make_heading(text: str, level: int, toc: bool = False) -> Paragraph:
    if level <= 2:
        style = "PartTitle"
    elif level == 3:
        style = "SuiteTitle"
    else:
        style = "QuestionTitle"
    p = para(text, style)
    if toc:
        p._toc_text = text
        p._toc_level = 0
    return p


def is_suite_heading(line: str, in_answer: bool = False) -> bool:
    m = re.match(r"^(#{3})\s+(.+)$", line)
    if not m:
        return False
    title = m.group(2).strip()
    skip = (
        "五、程序阅读题",
        "四、程序阅读题",
        "程序阅读题",
        "反转字符串题目",
        "二、题型说明",
    )
    if any(title.startswith(x) for x in skip):
        return False
    if re.match(r"^\d{1,3}\s", title) or re.match(r"^\d{1,3}\s*题", title) or re.match(r"^\d{1,3}[\\.．]", title):
        return False
    return True


def collect_suite_names(md: str) -> list[str]:
    names = []
    for line in md.splitlines():
        if is_suite_heading(line):
            title = re.sub(r"^###\s+", "", line).strip()
            if title not in names:
                names.append(title)
    return names


def markdown_to_flowables(md: str, suite_names: set[str], answers=False):
    story = []
    in_code = False
    code_lines: list[str] = []
    pending_para: list[str] = []

    def flush_para():
        nonlocal pending_para
        if pending_para:
            text = " ".join(x.strip() for x in pending_para if x.strip())
            if text:
                story.append(para(text))
            pending_para = []

    def flush_code():
        nonlocal code_lines
        code = "\n".join(code_lines).rstrip("\n")
        if code:
            story.append(
                Preformatted(
                    code,
                    ParagraphStyle(
                        "CodeBlock",
                        fontName="STSong-Light",
                        fontSize=7.4,
                        leading=9.2,
                        leftIndent=6,
                        rightIndent=6,
                        borderPadding=6,
                        backColor=colors.HexColor("#f6f7f9"),
                        borderColor=colors.HexColor("#e5e7eb"),
                        borderWidth=0.5,
                        spaceBefore=3,
                        spaceAfter=7,
                    ),
                    maxLineLength=110,
                )
            )
        code_lines = []

    for raw in md.splitlines():
        line = raw.rstrip()
        if line.startswith("```"):
            flush_para()
            if in_code:
                flush_code()
                in_code = False
            else:
                in_code = True
            continue

        if in_code:
            code_lines.append(line)
            continue

        if not line.strip():
            flush_para()
            continue

        if line.strip() == "---":
            flush_para()
            story.append(Spacer(1, 4))
            continue

        hm = re.match(r"^(#{1,6})\s+(.+)$", line)
        if hm:
            flush_para()
            level = len(hm.group(1))
            title = hm.group(2).strip()
            toc = (not answers) and title in suite_names and level == 3
            story.append(make_heading(title, level, toc=toc))
            continue

        if line.startswith("|"):
            flush_para()
            cells = [c.strip() for c in line.strip("|").split("|")]
            if not all(re.fullmatch(r":?-{2,}:?", c or "") for c in cells):
                row = [para(c, "SmallCN") for c in cells]
                story.append(
                    Table(
                        [row],
                        colWidths=None,
                        style=TableStyle(
                            [
                                ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#d1d5db")),
                                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#fbfbfc")),
                                ("LEFTPADDING", (0, 0), (-1, -1), 3),
                                ("RIGHTPADDING", (0, 0), (-1, -1), 3),
                            ]
                        ),
                    )
                )
            continue

        if re.match(r"^(\*\*.+\*\*|[-*]\s+|\d+\.\s+)", line):
            flush_para()
            story.append(para(line))
        else:
            pending_para.append(line)

    flush_para()
    if in_code:
        flush_code()
    return story


def page(canvas, doc):
    canvas.saveState()
    width, height = A4
    canvas.line(18 * mm, 13 * mm, width - 18 * mm, 13 * mm)
    canvas.setFont("STSong-Light", 8)
    canvas.setFillColor(colors.HexColor("#6b7280"))
    canvas.drawRightString(width - 18 * mm, 8 * mm, f"第 {doc.page} 页")
    canvas.restoreState()


def cover_page(canvas, doc):
    canvas.saveState()
    width, height = A4
    canvas.setFillColor(colors.HexColor("#111827"))
    canvas.rect(0, height - 62 * mm, width, 62 * mm, fill=1, stroke=0)
    canvas.setFillColor(colors.white)
    canvas.setFont("STSong-Light", 26)
    canvas.drawCentredString(width / 2, height - 34 * mm, "C语言题目汇总")
    canvas.setFont("STSong-Light", 14)
    canvas.drawCentredString(width / 2, height - 45 * mm, "题目与参考答案打印版")
    canvas.setFillColor(colors.HexColor("#374151"))
    canvas.setFont("STSong-Light", 11)
    canvas.drawCentredString(width / 2, 44 * mm, "根据 C语言题目汇总.md 与 答案.md 整理")
    canvas.drawCentredString(width / 2, 36 * mm, "目录按每套试卷名称编排，便于学生查找和打印")
    canvas.restoreState()


def build():
    q_md = QUESTIONS.read_text(encoding="utf-8")
    a_md = ANSWERS.read_text(encoding="utf-8")
    suite_names = collect_suite_names(q_md)

    story = []

    toc_title = Paragraph(
        "目录",
        ParagraphStyle(
            name="CompactTOCTitle",
            parent=styles["CoverTitle"],
            fontSize=22,
            leading=26,
            spaceAfter=4,
        ),
    )
    story.append(toc_title)
    story.append(Spacer(1, 2))
    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle(
            name="TOCLevel0",
            fontName="STSong-Light",
            fontSize=8.6,
            leading=10.4,
            leftIndent=0,
            firstLineIndent=0,
            rightIndent=0,
            spaceBefore=0,
            spaceAfter=0,
        )
    ]
    story.append(toc)
    story.append(PageBreak())

    story.append(make_heading("题目汇总", 1))
    story.extend(markdown_to_flowables(q_md, set(suite_names), answers=False))
    story.append(PageBreak())
    story.append(make_heading("参考答案", 1))
    story.extend(markdown_to_flowables(a_md, set(), answers=True))

    width, height = A4
    frame = Frame(18 * mm, 16 * mm, width - 36 * mm, height - 35 * mm, id="normal")
    doc = PrintDoc(
        str(OUT),
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=16 * mm,
    )
    doc.addPageTemplates(
        [
            PageTemplate(id="Body", frames=[frame], onPage=page),
        ]
    )
    doc.pageTemplates[0].id = "Body"
    doc.multiBuild(story)


if __name__ == "__main__":
    build()
