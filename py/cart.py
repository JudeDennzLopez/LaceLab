from shared import *

# ===== THIS PAGE: Cart =====
def v_cart():
    if not S["cart"]:
        return '<div class="card" style="padding:64px;text-align:center"><h2>Your cart is empty</h2><p class="mut">Design something loud.</p><button class="btn ind" data-act="go" data-v="studio">Open the studio</button></div>'
    sub = subtotal(); pr = PROMOS.get(S["promo"], 0); dsc = sub * pr
    ship = 0 if sub - dsc >= 500 else 50; tot = sub - dsc + ship
    left = max(0, 500 - (sub - dsc))
    items = ""
    for n, i in enumerate(S["cart"]):
        art = lace(i["a"], i["z"], i["t"], i["w"], i["tex"], i["font"], i.get("brk", False), "none", False, "i%d" % n)
        items += f'''<div class="card item"><div class="stage">{art}</div><div><b>{esc(i["name"])}</b><div class="mut">{esc(i["desc"])}</div><div class="qty" style="margin-top:8px"><button data-act="cq" data-i="{n}" data-v="-1">−</button><b>{i["qty"]}</b><button data-act="cq" data-i="{n}" data-v="1">+</button></div></div>
        <div style="text-align:right"><div class="price">{peso(i["price"] * i["qty"])}</div><button class="mut" data-act="rm" data-i="{n}">Remove</button></div></div>'''
    pays = "".join(f'<label class="pay"><input type="radio" name="pay" value="{p}" {"checked" if p==S["pay"] else ""}> <b>{p}</b></label>' for p in ["GCash", "Maya", "Cash on Delivery", "Credit / Debit"])
    ok = f'<div class="mut" style="color:var(--ind);margin-top:6px">✓ {S["promo"]} applied (−{int(pr*100)}%)</div>' if pr else ('<div class="mut" style="color:var(--coral);margin-top:6px">Code not recognised. Try STUDENT10.</div>' if S["promo"] else "")
    return f'''<div class="row" style="margin-bottom:16px"><h1 style="font-size:40px">Your cart</h1><button class="btn ghost" data-act="clear">Clear all</button></div>
    <div class="cart"><div><div class="card" style="padding:16px 20px;margin-bottom:16px"><div class="row"><b>Free nationwide shipping over ₱500</b><span class="mut">{"You unlocked it 🎉" if not left else "Add %s more" % peso(left)}</span></div><div class="bar2" style="margin-top:10px"><i style="width:{min(100, (sub-dsc)/5):.0f}%"></i></div></div>{items}
    <div class="card" style="padding:20px"><h3 style="margin-bottom:10px">Payment method</h3>{pays}</div></div>
    <div class="card sum"><h3>Order summary</h3><div style="display:flex;gap:8px;margin-top:14px"><input id="promo" class="txt" style="border-radius:99px" placeholder="Voucher code" value="{esc(S["promo"])}"><button class="btn ghost" data-act="promo">Apply</button></div>{ok}
    <div class="row"><span>Items subtotal</span><span>{peso(sub)}</span></div>{f'<div class="row" style="color:var(--ind)"><span>Discount</span><span>−{peso(dsc)}</span></div>' if dsc else ""}
    <div class="row"><span>Shipping</span><span>{"Free" if not ship else peso(ship)}</span></div><hr style="border:0;border-top:1px solid var(--line)">
    <div class="row"><b>Total</b><span class="price" style="font-size:28px">{peso(tot)}</span></div><button class="btn coral" style="width:100%;justify-content:center;margin-top:12px" data-act="pay">Proceed to checkout</button></div></div>'''


def _cq(el, v, e): i = S["cart"][int(el.dataset.i)]; i["qty"] = max(1, i["qty"] + int(v))
def _rm(el, v, e): S["cart"].pop(int(el.dataset.i))
def _clear(el, v, e): S["cart"].clear()
def _promo(el, v, e): S["promo"] = doc.getElementById("promo").value.strip().upper()
def _pay(el, v, e):
    if not S["user"]:
        S["nxt"] = "cart.html"; S["err"] = "Please log in or sign up to check out."; save_state(); goto("login"); return False
    modal(f'<h2>Order placed 🎉</h2><p class="mut">{cart_count()} item(s) via {S["pay"]}. This is a demo — no payment was taken.</p><button class="btn coral" data-act="done">Back to home</button>'); return False
def _done(el, v, e): S["cart"].clear(); S["promo"] = ""; save_state(); goto("home"); return False
def _inp(e):
    if e.target.name == "pay": S["pay"] = e.target.value; save_state()
ACTIONS.update(cq=_cq, rm=_rm, clear=_clear, promo=_promo, pay=_pay, done=_done); INPUTS.append(_inp)
start("cart", v_cart)

