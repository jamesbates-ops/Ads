// Builds the Casedrops briefing pack (.docx) from brief.json, mirroring the edit pack page.
// Run: npm install docx@9.8.1 && node build_brief.js out.docx
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, BorderStyle,
  ShadingType, AlignmentType, HeadingLevel, ExternalHyperlink, InternalHyperlink, Bookmark,
  LevelFormat, Footer, PageNumber, PositionalTab, PositionalTabAlignment, PositionalTabRelativeTo,
  PositionalTabLeader, VerticalAlign, TableLayoutType,
} = require("docx");

const data = JSON.parse(fs.readFileSync(path.join(__dirname, "brief.json"), "utf8"));
const out = process.argv[2] || path.join(__dirname, data.docname);

const INK = "1C1A21", MUTED = "645E6D", LINE = "E0DCE6", HEAD = "F5F4F7";
const CLARET = "8A1F3D", CLARET_TINT = "F7E8ED", STRAW = "7A5C06";
const FONT = "Arial", MONO = "Consolas";
const W = 9638; // A4 width minus 2 cm margins, in DXA

const t = (text, o = {}) => new TextRun({ text, font: FONT, ...o });
const mono = (text, o = {}) => new TextRun({ text, font: MONO, size: 16, ...o });
const p = (children, o = {}) => new Paragraph({ children: [].concat(children), spacing: { after: 120 }, ...o });
const link = (text, url, o = {}) =>
  new ExternalHyperlink({ link: url, children: [mono(text, { color: INK, underline: {}, ...o })] });
const jump = (text, anchor) =>
  new InternalHyperlink({ anchor, children: [t(text, { bold: true, color: INK, underline: {} })] });
const kicker = (text, color = MUTED) => t(text.toUpperCase(), { size: 14, color, characterSpacing: 20 });
const inZip = (...dirs) => {
  const runs = [t("In the zip:  ", { size: 16, color: MUTED })];
  dirs.forEach((d, i) => {
    if (i) runs.push(t("  and  ", { size: 16, color: MUTED }));
    runs.push(mono(d, { bold: true }));
  });
  return p(runs, { spacing: { before: 40, after: 160 } });
};
const h1 = (text, anchor) => new Paragraph({
  heading: HeadingLevel.HEADING_1,
  children: [anchor ? new Bookmark({ id: anchor, children: [t(text)] }) : t(text)],
});

const cellBorder = { style: BorderStyle.SINGLE, size: 4, color: LINE };
const borders = { top: cellBorder, bottom: cellBorder, left: cellBorder, right: cellBorder };
const noBorder = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const noBorders = { top: noBorder, bottom: noBorder, left: noBorder, right: noBorder };

function cell(children, width, o = {}) {
  return new TableCell({
    width: { size: width, type: WidthType.DXA },
    borders: o.borders || borders,
    shading: o.fill ? { fill: o.fill, type: ShadingType.CLEAR, color: "auto" } : undefined,
    margins: { top: 80, bottom: 80, left: 110, right: 110 },
    verticalAlign: o.valign || VerticalAlign.TOP,
    children: [].concat(children).map(c => (c instanceof Paragraph ? c : new Paragraph({ children: [].concat(c) }))),
  });
}
function table(widths, header, rows, o = {}) {
  const sum = widths.reduce((a, b) => a + b, 0);
  if (sum !== W) throw new Error(`table widths ${sum} != ${W}`);
  const head = header && new TableRow({
    tableHeader: true,
    children: header.map((h, i) => cell(new Paragraph({ children: [kicker(h, o.headColors?.[i] || MUTED)] }), widths[i], { fill: HEAD })),
  });
  const body = rows.map(r => new TableRow({ cantSplit: true, children: r.map((c, i) => cell(c, widths[i], o)) }));
  return new Table({
    width: { size: W, type: WidthType.DXA }, columnWidths: widths, layout: TableLayoutType.FIXED,
    rows: head ? [head, ...body] : body,
  });
}
const gap = () => new Paragraph({ children: [], spacing: { after: 60 } });

// ---------- content ----------
const kids = [];

kids.push(p(kicker("Edit pack · Briefing · 9:16 UGC · voiceover over B-roll"), { spacing: { after: 80 } }));
kids.push(new Paragraph({ heading: HeadingLevel.TITLE, children: [t("Casedrops Edit Pack")] }));
kids.push(p(t("One hook clip with a hook line over it, then seven B-roll clips in order under the body lines. The ad comes in two versions, red wine and white wine. The cut, timing and voiceover are identical in both, so one edit serves both versions.", { color: MUTED, size: 22 }), { spacing: { after: 200 } }));

const facts = [["Picture", "Hook 4s + B-roll 7 × 5s"], ["Voiceover", "Romy, ElevenLabs"], ["Audio on clips", "None, all silent"], ["Clips finished", "25 Sep 2026"]];
kids.push(table([2410, 2409, 2410, 2409], null, [facts.map(([k, v]) => [
  new Paragraph({ children: [kicker(k)], spacing: { after: 20 } }),
  new Paragraph({ children: [t(v, { bold: true })] }),
])], { borders: noBorders }));
kids.push(new Paragraph({ children: [], spacing: { after: 120 }, border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: INK, space: 6 } } }));

// Download everything
kids.push(h1("Download everything", "zip"));
kids.push(p(t("One zip with all 26 files. Its folders follow this brief section by section, and every file name in this brief is the file’s name in the zip. Click a file name to open that single file online.")));
kids.push(p([t("Download: ", { bold: true }), link(data.zip.name, data.zip.url, { size: 18, bold: true }), t("  (82 MB)", { color: MUTED })], { spacing: { after: 160 } }));
const ind = (s) => new Paragraph({ indent: { left: 240 }, children: [mono(s, { size: 17 })] });
const D = data.dirs;
kids.push(table([4100, 4338, 1200], ["In the zip", "What it is", "Files"], [
  [new Paragraph({ children: [mono(data.root + "/", { size: 17, bold: true })] }), t("Top folder", { color: MUTED }), t("")],
  [ind(data.docname), t("This brief"), t("1", { color: MUTED })],
  [ind("file_index.csv"), t("Every file with its section, version, the line it plays under, its duration and its source file"), t("1", { color: MUTED })],
  [ind(D.hook + "/"), jump("Hook clips", "hooks"), t("4", { color: MUTED })],
  [ind(D.red + "/"), new Paragraph({ children: [jump("Body B-roll", "broll"), t(", red wine")] }), t("7", { color: MUTED })],
  [ind(D.white + "/"), new Paragraph({ children: [jump("Body B-roll", "broll"), t(", white wine")] }), t("7", { color: MUTED })],
  [ind(D.vo + "/"), jump("Voiceover", "vo"), t("8", { color: MUTED })],
]));

// How the cut runs
kids.push(h1("How the cut runs", "cut"));
kids.push(p(t("The picture runs 39s. The voiceover runs 33–36s depending on which hook you use, so there is room to trim the B-roll tails.")));
let at = 4;
const cutRows = [[t("Hook clip", { bold: true }), t("0–4s"), t("4s"), t("H1, H2 or H3")]];
for (const b of data.broll) {
  cutRows.push([t(b.code, { bold: true }), t(`${at}–${at + 5}s`), t("5s"), t(b.under)]);
  at += 5;
}
kids.push(table([2000, 2300, 1300, 4038], ["Clip", "Time in the cut", "Length", "Plays under"], cutRows));
kids.push(gap());
kids.push(p([t("Red version: ", { bold: true, color: CLARET }), t("a red hook bottle (1, 3 or 4), then the red wine B-roll.")], { spacing: { before: 120, after: 60 } }));
kids.push(p([t("White version: ", { bold: true, color: STRAW }), t("Bottle 2 (white), then the white wine B-roll.")]));

// Hook clips
kids.push(h1("Hook clips", "hooks"));
kids.push(p(t("Pick one clip and lay H1, H2 or H3 over it. Each clip shows her holding the bottle to camera in both hands. Every clip is 4s, 9:16 and silent.")));
kids.push(inZip(D.hook + "/"));
kids.push(table([2700, 1500, 1900, 3538], ["Bottle", "Wine", "Use in", "File"], data.hooks.map(h => {
  const red = h.ver === "red";
  return [
    t(h.name, { bold: true }),
    t(red ? "Red wine" : "White wine", { color: red ? CLARET : STRAW, bold: true }),
    t(red ? "Red version" : "White version"),
    link(h.zip, h.url),
  ];
})));
kids.push(gap());
kids.push(new Paragraph({
  children: [t("H1 names a price ($80, down to $20). ", { bold: true }), t("Only put H1 over the bottle that price is actually true for.")],
  shading: { fill: CLARET_TINT, type: ShadingType.CLEAR, color: "auto" },
  border: { left: { style: BorderStyle.SINGLE, size: 24, color: CLARET, space: 8 } },
  indent: { left: 160 }, spacing: { before: 120, after: 120 },
}));

// Body B-roll
kids.push(h1("Body B-roll", "broll"));
kids.push(p(t("Play these in order. Each clip starts on the frame the one before it ends on, so BR1 to BR7 run as one continuous take. The red and white versions match frame for frame.")));
kids.push(inZip(D.red + "/", D.white + "/"));
kids.push(table([700, 3700, 1000, 4238], ["Clip", "Action", "Under", "Files: red wine / white wine"], data.broll.map(b => [
  t(b.code, { bold: true }),
  t(b.act),
  t(b.under, { color: MUTED }),
  [
    new Paragraph({ children: [t("Red    ", { size: 15, bold: true, color: CLARET }), link(b.red.zip, b.red.url)], spacing: { after: 40 } }),
    new Paragraph({ children: [t("White  ", { size: 15, bold: true, color: STRAW }), link(b.white.zip, b.white.url)] }),
  ],
])));
kids.push(p(t("Every clip is 5.04s at 24fps (121 frames). The red files are 1080×1912 and the white files are 1082×1916, so scale the white ones to fit and the cut points line up.", { color: MUTED, size: 18 }), { spacing: { before: 120, after: 120 } }));

// Voiceover
kids.push(h1("Voiceover", "vo"));
kids.push(p(t("Both versions use the same lines, read by Romy (ElevenLabs). Every line is its own file, and the durations are the length of each file.")));
kids.push(inZip(D.vo + "/"));
kids.push(table([650, 4538, 950, 3500], ["Line", "What she says", "Length", "File"], data.vo.map(v => [
  t(v.code, { bold: true }),
  t(`“${v.text}”`),
  t(`${v.dur}s`, { color: MUTED }),
  link(v.zip, v.url),
])));

// Before release
kids.push(h1("Before release", "checks"));
const checks = [
  "H1 says $80 down to $20, which is 75% off, but H2 says 70% off. If both refer to the same bottle, make the numbers agree.",
  "The prices, free delivery, trade prices and the full refund all need to be true and backed up for the market the ad runs in.",
  "The presenter is AI-generated and speaks as a customer. Label the ad as paid, and add the AI or actor disclosure your markets and platforms require.",
];
for (const c of checks) kids.push(new Paragraph({ numbering: { reference: "checks", level: 0 }, spacing: { after: 100 }, children: [t(c)] }));

kids.push(new Paragraph({
  spacing: { before: 360 }, border: { top: { style: BorderStyle.SINGLE, size: 4, color: LINE, space: 8 } },
  children: [t("Full record with prompts and IDs: ", { size: 17, color: MUTED }), mono("plan/casedrops-ugc-plan.md", { size: 15, color: MUTED }), t(" and ", { size: 17, color: MUTED }), mono("plan/bottle-hold-shots.md", { size: 15, color: MUTED }), t(" in the Ads repo.", { size: 17, color: MUTED })],
}));

// ---------- document ----------
const doc = new Document({
  creator: "Casedrops", title: "Casedrops Edit Pack: briefing", description: "Briefing pack for the Casedrops 9:16 UGC ad edit",
  styles: {
    default: { document: { run: { font: FONT, size: 20, color: INK } } },
    paragraphStyles: [
      { id: "Title", name: "Title", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { font: FONT, size: 52, bold: true, color: INK }, paragraph: { spacing: { after: 120 } } },
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { font: FONT, size: 30, bold: true, color: INK }, paragraph: { spacing: { before: 400, after: 100 }, keepNext: true, outlineLevel: 0 } },
    ],
  },
  numbering: { config: [{ reference: "checks", levels: [{ level: 0, format: LevelFormat.BULLET, text: "☐", alignment: AlignmentType.LEFT,
    style: { paragraph: { indent: { left: 400, hanging: 320 } }, run: { font: "Segoe UI Symbol", color: MUTED } } }] }] },
  sections: [{
    properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 1134, bottom: 1134, left: 1134, right: 1134 } } },
    footers: { default: new Footer({ children: [new Paragraph({ run: { font: FONT, size: 15, color: MUTED }, children: [
      t("Casedrops Edit Pack · briefing", { size: 15, color: MUTED }),
      new TextRun({ children: [new PositionalTab({ alignment: PositionalTabAlignment.RIGHT, relativeTo: PositionalTabRelativeTo.MARGIN, leader: PositionalTabLeader.NONE })] }),
      t("Page ", { size: 15, color: MUTED }), new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 15, color: MUTED }),
      t(" of ", { size: 15, color: MUTED }), new TextRun({ children: [PageNumber.TOTAL_PAGES], font: FONT, size: 15, color: MUTED }),
    ] })] }) },
    children: kids,
  }],
});

Packer.toBuffer(doc).then(buf => { fs.writeFileSync(out, buf); console.log("wrote", out, buf.length); });
