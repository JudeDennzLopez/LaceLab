from shared import *

# ===== THIS PAGE: Home =====
def v_home():
    d = S["d"]
    chips = "".join(f'<button class="chip {"on" if c==S["cat"] else ""}" data-act="cat" data-v="{c}" data-go="catalog">{c}</button>' for c in CATS)
    rev = [("Bea Nicole S.", "UST Artlets Council", "The satin finish is so soft around the neck, walang kati even on 8am–7pm days."),
           ("Kenji M.", "DevCon Summit Manila", "Ordered 350 pcs for our convention. Shipped in 4 days and the breakaway upgrade was a hit.")]
    revh = "".join(f'<div class="card" style="padding:24px"><div style="color:var(--coral)">★★★★★</div><p style="font-style:italic">“{t}”</p><b>{n}</b> <span class="mut">{o}</span></div>' for n, o, t in rev)
    return f'''<section class="hero"><div><span class="tag">⚡ 1-Day Rush Available</span>{greet()}<h1>Design your custom lace in minutes.</h1>
    <p>No minimum order. Ultra HD sublimation print from ₱120 each. Try the live preview — it's the real thing.</p>
    <div style="margin-top:24px;display:flex;gap:12px"><button class="btn coral" data-act="go" data-v="studio">Start customizing</button><button class="btn" style="background:rgba(255,255,255,.15)" data-act="go" data-v="catalog">Browse ready laces</button></div></div>
    <div class="stage" style="height:380px">{lace(COLORS[d["col"]], "#fff", d["text"], d["w"], d["tex"], d["font"], d["brk"], "none", False, "hero")}</div></section>
    <section class="sec"><div class="row" style="margin-bottom:16px"><h2>Trending ready-to-wear</h2><button class="btn ghost" data-act="go" data-v="catalog">See all</button></div>
    <div style="margin-bottom:20px">{chips}</div><div class="grid">{"".join(card(p) for p in PRODUCTS[6:10])}</div></section>
    <section class="sec card" style="padding:32px;display:flex;justify-content:space-between;align-items:center;background:var(--soft)"><div><span class="tag" style="background:var(--ind)">BULK SAVINGS · UP TO 40% OFF</span><h2>Ordering for an org or batch?</h2><p class="mut">Rates from 20+ pcs with free digital proofing and layout help.</p></div><button class="btn ind" data-act="batch">Inquire batch rates</button></section>
    <section class="sec"><h2 style="margin-bottom:16px">Trusted by 15,000+ Pinoy students &amp; orgs</h2><div style="display:grid;grid-template-columns:1fr 1fr;gap:24px">{revh}</div></section>'''


def _cat(el, v, e):
    S["cat"] = v
    if el.dataset.go: save_state(); goto(el.dataset.go); return False
def _batch(el, v, e):
    modal('<h2>Batch inquiry sent 📨</h2><p class="mut">Our team will send a free digital proof and a wholesale tier list within a day.</p><button class="btn ind" data-act="close">Great</button>'); return False
ACTIONS.update(cat=_cat, batch=_batch)
start("home", v_home)

