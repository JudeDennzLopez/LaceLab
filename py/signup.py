from shared import *

# ===== THIS PAGE: Sign up =====
def v_auth(mode):
    su = mode == "signup"
    fld = lambda i, l, t="text", v="", ph="": f'<label for="{i}">{l}</label><input id="{i}" class="txt" type="{t}" value="{esc(v)}" placeholder="{ph}">'
    err = f'<div role="alert" style="color:#ba1a1a;font-weight:600;margin-top:10px">{esc(S["err"])}</div>' if S["err"] else ""
    name = fld("au-name", "Full name", "text", S["nm"], "Maria Santos") if su else ""
    pw2 = fld("au-pw2", "Confirm password", "password") if su else ""
    other = ('Already have an account? <button class="price" style="font-size:15px" data-act="go" data-v="login">Log in</button>' if su
             else 'New to LaceLab? <button class="price" style="font-size:15px" data-act="go" data-v="signup">Create an account</button>')
    return f'''<div class="auth"><div class="art"><div><span class="tag">{"Join 15,000+ students &amp; orgs" if su else "Welcome back"}</span><h1 style="font-size:40px;line-height:46px">{"Save your designs. Earn points." if su else "Your laces are waiting."}</h1></div>
    {lace("#ff6b6b", "#fff", "LACELAB • " + ("NEW MEMBER" if su else "WELCOME BACK"), 25, "satin", "athletic", True, "none", False, "au")}</div>
    <div class="card fm"><h2>{"Create your account" if su else "Log in"}</h2><p class="mut" style="margin:0 0 8px">{"It takes under a minute." if su else "Log in to check out and track your points."}</p>
    {name}{fld("au-email", "Email", "email", S["email"], "you@school.edu.ph")}{fld("au-pw", "Password", "password", "", "At least 6 characters")}{pw2}{err}
    <button class="btn coral" style="justify-content:center;margin-top:18px" data-act="auth" data-v="{mode}">{"Sign up" if su else "Log in"}</button>
    <p class="mut" style="text-align:center;margin:14px 0 0">{other}</p>
    <p class="mut" style="text-align:center;font-size:12px;margin:8px 0 0">Demo only: accounts are saved in this browser, not on a server.</p></div></div>'''
def v_login(): return v_auth("login")
def v_signup(): return v_auth("signup")


def _key(e):
    if e.key == "Enter" and (e.target.id or "").startswith("au-") and not do_auth(S["view"]): render()
doc.addEventListener("keydown", create_proxy(_key))
start("signup", v_signup)

