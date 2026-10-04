#!/usr/bin/env python3
"""Look up 高中英文參考詞彙表 levels for words or for a whole passage.

Usage:
  python scripts/vocab_level.py abandon reluctant asylum      # look up words
  python scripts/vocab_level.py --text passage.txt            # profile a passage
  echo "Some text ..." | python scripts/vocab_level.py --text -

For a passage it prints the level distribution and lists every word at level 6
or not in the list, so an item writer can check the 考試說明 rule (levels 1-5
are the core; level 6+ only occasionally). Inflections and regular derivatives
(-s, -ed, -ing, -ly, -ness, un-, re-, ...) are mapped back to a base word with
simple heuristics, so treat the result as a guide and confirm doubtful words in
references/vocabulary.md.
"""
import re
import sys
from collections import Counter
from pathlib import Path

VOCAB = Path(__file__).resolve().parent.parent / "references" / "vocabulary.md"
APPENDIX = ("one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen "
            "sixteen seventeen eighteen nineteen twenty thirty forty fifty sixty seventy eighty ninety "
            "hundred thousand million billion first second third fourth fifth sixth seventh eighth ninth "
            "tenth eleventh twelfth twentieth hundredth thousandth millionth billionth monday tuesday "
            "wednesday thursday friday saturday sunday january february march april may june july august "
            "september october november december spring summer autumn fall winter").split()


IRREGULAR = {f: b for b, fs in {
    "be": "am is are was were been being", "have": "has had having", "do": "does did done",
    "go": "went gone goes", "get": "got gotten", "make": "made", "know": "knew known", "take": "took taken",
    "see": "saw seen", "come": "came", "give": "gave given", "find": "found", "think": "thought",
    "tell": "told", "say": "said says", "become": "became", "leave": "left", "feel": "felt",
    "bring": "brought", "begin": "began begun", "keep": "kept", "hold": "held", "write": "wrote written",
    "stand": "stood", "hear": "heard", "mean": "meant", "meet": "met", "run": "ran", "pay": "paid",
    "sit": "sat", "speak": "spoke spoken", "lead": "led", "grow": "grew grown", "lose": "lost",
    "fall": "fell fallen", "send": "sent", "build": "built", "understand": "understood",
    "draw": "drew drawn", "break": "broke broken", "spend": "spent", "rise": "rose risen",
    "drive": "drove driven", "buy": "bought", "wear": "wore worn", "choose": "chose chosen",
    "seek": "sought", "throw": "threw thrown", "catch": "caught", "deal": "dealt", "win": "won",
    "teach": "taught", "eat": "ate eaten", "fight": "fought", "sell": "sold", "forget": "forgot forgotten",
    "fly": "flew flown", "sing": "sang sung", "swim": "swam swum", "drink": "drank drunk",
    "ride": "rode ridden", "shake": "shook shaken", "steal": "stole stolen", "hide": "hid hidden",
    "bite": "bit bitten", "feed": "fed", "sleep": "slept", "lie": "lay lain", "lay": "laid",
    "sink": "sank sunk", "spring": "sprang sprung", "dive": "dove", "flee": "fled", "strike": "struck",
    "swear": "swore sworn", "tear": "tore torn", "wake": "woke woken", "freeze": "froze frozen",
    "forgive": "forgave forgiven", "bear": "bore born borne", "blow": "blew blown", "dig": "dug",
    "hang": "hung", "shine": "shone", "shoot": "shot", "stick": "stuck", "sweep": "swept",
    "swing": "swung", "weep": "wept", "arise": "arose arisen", "bend": "bent", "bind": "bound",
    "bleed": "bled", "breed": "bred", "cling": "clung", "creep": "crept", "lend": "lent", "light": "lit",
    "slide": "slid", "spin": "spun", "sting": "stung", "withdraw": "withdrew withdrawn",
    "overcome": "overcame", "undergo": "underwent undergone", "ring": "rang rung",
    "child": "children", "man": "men", "woman": "women", "person": "people", "foot": "feet",
    "tooth": "teeth", "mouse": "mice", "goose": "geese", "good": "better best", "bad": "worse worst",
    "can": "could", "will": "would", "shall": "should", "may": "might", "not": "n't",
}.items() for f in fs.split()}


def load():
    table = {}
    for line in VOCAB.read_text(encoding="utf-8").splitlines():
        m = re.match(r"- (.+) \((.+)\) \[(\d)\]$", line.strip())
        if not m:
            continue
        head, level = m.group(1), int(m.group(3))
        forms = []
        pron = re.match(r"(\w+) \((.+)\)$", head)               # he (him, his, himself)
        if pron:
            forms = [pron.group(1)] + [f.strip() for f in pron.group(2).split(",")]
        for form in forms or head.split("/"):
            form = form.strip().lower()
            base = re.sub(r"\(.*?\)", "", form)              # agree(ment) -> agree
            full = form.replace("(", "").replace(")", "")    # agree(ment) -> agreement
            for f in {base, full}:
                if f and (f not in table or level < table[f]):
                    table[f] = level
    for w in APPENDIX:
        table.setdefault(w, 0)                               # 0 = 附錄
    for form, base in IRREGULAR.items():
        if base in table and form not in table:
            table[form] = table[base]
    return table


SUFFIXES = [("ies", "y"), ("ied", "y"), ("ier", "y"), ("iest", "y"), ("ily", "y"), ("iness", "y"),
            ("ves", "f"), ("ves", "fe"), ("es", ""), ("s", ""), ("ed", ""), ("ed", "e"), ("ing", ""),
            ("ing", "e"), ("er", ""), ("er", "e"), ("est", ""), ("est", "e"), ("ly", ""), ("ness", ""),
            ("ment", ""), ("less", ""), ("ly", "e"), ("y", ""), ("ize", ""), ("ized", ""), ("ally", ""), ("ically", "ic"), ("ily", "y")]
PREFIXES = ["un", "in", "im", "ir", "il", "non", "re", "dis", "mis", "over", "under"]


def candidates(word):
    yield word
    for suf, rep in SUFFIXES:
        if word.endswith(suf) and len(word) - len(suf) >= 2:
            stem = word[: -len(suf)] + rep
            yield stem
            if len(stem) > 2 and stem[-1] == stem[-2]:       # stopped -> stop
                yield stem[:-1]
    for pre in PREFIXES:
        if word.startswith(pre) and len(word) - len(pre) >= 3:
            yield from candidates(word[len(pre):])


def level_of(word, table):
    w = re.sub(r"['’]s$", "", word.lower()).strip("'’")
    if w in table:
        return table[w], w
    for c in candidates(w):
        if c in table:
            return table[c], c
    return None, None


def main(argv):
    table = load()
    if argv and argv[0] == "--text":
        src = sys.stdin.read() if len(argv) < 2 or argv[1] == "-" else Path(argv[1]).read_text(encoding="utf-8")
        words = re.findall(r"[A-Za-z]+(?:['’-][A-Za-z]+)*", src)
        dist, flagged = Counter(), {}
        for raw in words:
            parts = raw.split("-") if "-" in raw else [raw]
            for p in parts:
                if len(p) <= 2 and p.lower() not in table:   # fragments like "e", "g", "co"
                    continue
                if p[:1].isupper() and p.lower() not in table and level_of(p, table)[0] is None:
                    dist["proper noun?"] += 1
                    continue
                lv, base = level_of(p, table)
                dist[lv if lv is not None else "off-list"] += 1
                if lv is None or lv >= 6:
                    flagged[p.lower()] = "off-list" if lv is None else f"L{lv} ({base})"
        total = sum(dist.values())
        print(f"Tokens: {total}")
        for k in [0, 1, 2, 3, 4, 5, 6, "off-list", "proper noun?"]:
            if dist[k]:
                label = "附錄" if k == 0 else (f"L{k}" if isinstance(k, int) else k)
                print(f"  {label:>12}: {dist[k]:4d} ({dist[k] / total:.1%})")
        if flagged:
            print("Level 6 / off-list words:")
            for w, why in sorted(flagged.items()):
                print(f"  {w}: {why}")
    else:
        for w in argv:
            lv, base = level_of(w, table)
            if lv is None:
                print(f"{w}: not in 參考詞彙表")
            elif base == w.lower():
                print(f"{w}: L{lv}" if lv else f"{w}: 附錄")
            else:
                print(f"{w}: L{lv} (via {base})")


if __name__ == "__main__":
    main(sys.argv[1:] or ["--help"]) if sys.argv[1:] != ["--help"] else print(__doc__)
