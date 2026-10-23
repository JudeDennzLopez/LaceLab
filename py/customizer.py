from shared import *

# ===== THIS PAGE: Customizer =====
def v_studio():
    d = S["d"]; u = unit(d); q = d["qty"]; dc = disc(q); tot = u * q * (1 - dc)
    def tiles(items, key, fmt):
        return "".join(f'<button class="tile {"on" if d[key]==k else ""}" data-act="set" data-k="{key}" data-v="{k}">{fmt(k, v)}</button>' for k, v in items.items())
    def add(n): return "Included" if n == 0 else f"+₱{n}"
    sw = "".join(f'<button class="sw {"on" if d["col"]==n else ""}" style="background:{c}" aria-label="{n}" data-act="set" data-k="col" data-v="{n}"></button>' for n, c in COLORS.items())
    hold = "".join(f'<button class="tile {"on" if d["hold"]==k else ""}" data-act="set" data-k="hold" data-v="{k}"><b>{v[0]}</b><span class="mut">{"+₱%d" % v[1] if v[1] else "₱0"}</span></button>' for k, v in HOLD.items())
    return f'''<div class="studio"><div class="stage"><span class="tag" style="position:absolute;top:16px;left:16px;background:var(--tan)">Unit {peso(u)} · est. 2–3 days</span>{lace(COLORS[d["col"]], "#fff", d["text"], d["w"], d["tex"], d["font"], d["brk"], d["hold"], True, "st")}</div>
    <div class="opts"><div><h1 style="font-size:36px;line-height:44px">Studio customizer</h1><span class="mut">The preview updates as you click.</span></div>
    <div><h3>1. Strap width</h3><div class="tiles">{tiles(WIDTHS, "w", lambda k, v: f'<b>{v[0]}</b><span class="mut">{v[1]}</span><br><span class="price" style="font-size:16px">₱{v[2]}</span>')}</div></div>
    <div><h3>2. Fabric texture</h3><div class="tiles">{tiles(TEX, "tex", lambda k, v: f'<b>{v[0]}</b><span class="mut">{v[1]}</span><br><span class="mut">{add(v[2])}</span>')}</div></div>
    <div><h3>3. Base palette — <span class="mut">{d["col"]}</span></h3>{sw}</div>
    <div><h3>4. Your text</h3><input id="txt" class="txt" maxlength="32" value="{esc(d["text"])}" placeholder="School, company or handle"><div class="tiles" style="margin-top:10px">{tiles(FONTS, "font", lambda k, v: f'<b>{v[0]}</b>')}</div></div>
    <div><h3>5. Hook &amp; hardware</h3><div class="tiles">{tiles(CLIPS, "clip", lambda k, v: f'<b>{v[0]}</b><span class="mut">{v[1]}</span>')}
    <button class="tile {"on" if d["brk"] else ""}" data-act="tog" data-k="brk"><b>Breakaway clasp</b><span class="mut">+₱15</span></button>
    <button class="tile {"on" if d["det"] else ""}" data-act="tog" data-k="det"><b>Detachable loop</b><span class="mut">+₱20</span></button></div></div>
    <div><h3>6. Badge holder</h3><div class="tiles">{hold}</div></div>
    <div class="row card" style="padding:14px 18px"><div><b>Quantity</b><div class="mut">5+ save 15% · 20+ save 30%{f' · <b style="color:var(--coral)">{int(dc*100)}% off applied</b>' if dc else ''}</div></div><div class="qty"><button data-act="qty" data-v="-1">−</button><b>{q}</b><button data-act="qty" data-v="1">+</button></div></div>
    <div class="card dock"><div><span class="mut">Total estimated</span><div class="price" style="font-size:28px">{peso(tot)}</div></div><button class="btn coral" data-act="addc">Add to cart</button></div></div></div>'''


def _set(el, v, e):
    k = el.dataset.k; d = S["d"]; d[k] = int(v) if k == "w" else v
    if k == "clip": d["brk"] = False
def _tog(el, v, e):
    k = el.dataset.k; d = S["d"]; d[k] = not d[k]
    if k == "brk" and d[k]: d["clip"] = "trigger"
def _qty(el, v, e): S["d"]["qty"] = max(1, min(500, S["d"]["qty"] + int(v)))
def _addc(el, v, e): add_custom(); return False
def _inp(e):
    if e.target.id == "txt": S["d"]["text"] = e.target.value.upper(); render("txt")
ACTIONS.update(set=_set, tog=_tog, qty=_qty, addc=_addc); INPUTS.append(_inp)
start("studio", v_studio)

