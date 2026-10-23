from shared import *

# ===== THIS PAGE: Catalog =====
def filtered():
    L = [p for p in PRODUCTS if (S["cat"] == "All" or p["c"] == S["cat"]) and S["q"].lower() in (p["n"] + p["c"] + p["t"]).lower()]
    key = {"best": lambda p: -p["rv"], "low": lambda p: p["p"], "high": lambda p: -p["p"], "rate": lambda p: -p["r"]}[S["sort"]]
    return sorted(L, key=key)

def v_catalog():
    L = filtered()
    chips = "".join(f'<button class="chip {"on" if c==S["cat"] else ""}" data-act="cat" data-v="{c}">{c}</button>' for c in CATS)
    opts = "".join(f'<option value="{k}" {"selected" if k==S["sort"] else ""}>{v}</option>' for k, v in [("best", "Best selling"), ("low", "Price: low to high"), ("high", "Price: high to low"), ("rate", "Top rated")])
    body = "".join(card(p) for p in L) or '<p class="mut">No laces match that search. Try “anime” or “corporate”.</p>'
    return f'''<div class="row" style="margin-bottom:20px"><div><h1 style="font-size:40px">Explore ready laces</h1><span class="mut">Showing {len(L)} designs</span></div>
    <div style="display:flex;gap:12px"><input id="q" class="txt" style="width:320px;border-radius:99px" placeholder="Search school, theme, or finish…" value="{esc(S["q"])}"><select id="sort" class="txt" style="width:190px;border-radius:99px">{opts}</select></div></div>
    <div style="margin-bottom:24px">{chips}</div><div class="grid">{body}</div>'''


def _cat(el, v, e): S["cat"] = v
def _inp(e):
    t = e.target
    if t.id == "q": S["q"] = t.value; render("q")
    elif t.id == "sort": S["sort"] = t.value; render()
ACTIONS.update(cat=_cat); INPUTS.append(_inp)
start("catalog", v_catalog)

