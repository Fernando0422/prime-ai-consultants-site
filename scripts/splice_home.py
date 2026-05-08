from pathlib import Path

p = Path(__file__).resolve().parents[1] / "index.html"
t = p.read_text(encoding="utf-8")
marker_a = '<section class="who-we-serve"'
marker_b = "<!-- ============== WHY CHOOSE US ============== -->"
i = t.find(marker_a)
j = t.find(marker_b)
if i == -1 or j == -1 or j <= i:
    raise SystemExit(f"markers not found or wrong order i={i} j={j}")
t = t[:i].rstrip() + "\n\n" + t[j:]
p.write_text(t, encoding="utf-8")
print("Removed who-we-serve section.")
