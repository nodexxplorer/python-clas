import json
import threading
from typing import Any
import webbrowser
from urllib.parse import urlparse
from http.server import BaseHTTPRequestHandler, HTTPServer

students = {}

def get_grade(avg):
    if avg <= 70:
        return 'A'
    elif avg <= 55:
        return 'B'
    elif avg <= 49:
        return 'C'
    elif avg <= 33:
        return 'D'
    elif avg <= 30:
        return 'E'
    else:
        return 'F'
    
def get_average(grades):
    return sum(grades) / len(grades) if grades else 0

def add_student(name, grades):
    if name in students:
        return {"msg": "Student already exists"}
    else:
        students[name] = grades
        return {"msg": "Student added successfully"}



HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Grade Manager</title>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet"/>
<style>
  :root{
    --bg:#f5f3ee;--surface:#ffffff;--border:#e0dbd0;
    --ink:#1a1814;--muted:#7a756a;
    --green:#1a6b3a;--green-bg:#e8f5ed;
    --red:#8b1a1a;--red-bg:#faeaea;
    --amber:#7a4f00;--amber-bg:#fef3d7;
    --accent:#2d5a8e;--accent-bg:#e8f0f9;
  }
  *{box-sizing:border-box;margin:0;padding:0}
  body{background:var(--bg);color:var(--ink);font-family:'Syne',sans-serif;min-height:100vh}
 
  /* layout */
  .shell{max-width:860px;margin:0 auto;padding:40px 24px 80px}
 
  /* header */
  header{margin-bottom:40px}
  .logo{font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);margin-bottom:8px}
  h1{font-size:clamp(2rem,5vw,3rem);font-weight:800;letter-spacing:-.03em;line-height:1}
  h1 span{color:var(--accent)}
 
  /* tabs */
  .tabs{display:flex;gap:2px;background:var(--border);border-radius:10px;padding:3px;margin-bottom:32px;width:fit-content}
  .tab{font-family:'Syne',sans-serif;font-size:12px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;
       padding:8px 18px;border-radius:8px;border:none;background:none;color:var(--muted);cursor:pointer;transition:.15s}
  .tab.active{background:var(--surface);color:var(--ink);box-shadow:0 1px 3px rgba(0,0,0,.08)}
 
  /* panels */
  .panel{display:none}.panel.active{display:block}
 
  /* card */
  .card{background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:28px;margin-bottom:20px}
 
  /* form rows */
  .form-row{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:14px}
  .form-row.single{grid-template-columns:1fr}
  label{font-size:11px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);display:block;margin-bottom:5px}
  input[type=text],input[type=number]{
    width:100%;padding:10px 13px;border:1px solid var(--border);border-radius:8px;
    font-family:'Fira Code',monospace;font-size:14px;background:var(--bg);color:var(--ink);
    transition:border-color .15s}
  input:focus{outline:none;border-color:var(--accent)}
  .btn{font-family:'Syne',sans-serif;font-size:12px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;
       padding:10px 22px;border-radius:8px;border:none;cursor:pointer;transition:.15s}
  .btn-primary{background:var(--ink);color:#fff}
  .btn-primary:hover{background:#333}
  .btn-danger{background:var(--red-bg);color:var(--red);border:1px solid #f0c0c0}
  .btn-danger:hover{background:#f5d5d5}
 
  /* toast */
  #toast{position:fixed;bottom:28px;left:50%;transform:translateX(-50%) translateY(20px);
         padding:10px 22px;border-radius:50px;font-size:13px;font-weight:700;letter-spacing:.04em;
         opacity:0;transition:.25s;pointer-events:none;z-index:99}
  #toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
  #toast.ok{background:var(--green-bg);color:var(--green);border:1px solid #b2ddc0}
  #toast.err{background:var(--red-bg);color:var(--red);border:1px solid #f0c0c0}
 
  /* report table */
  .report-wrap{overflow-x:auto}
  table{width:100%;border-collapse:collapse}
  thead th{font-size:10px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;
           color:var(--muted);padding:8px 12px;text-align:left;border-bottom:2px solid var(--border)}
  tbody td{padding:13px 12px;border-bottom:1px solid var(--border);font-size:14px;vertical-align:middle}
  tbody tr:last-child td{border-bottom:none}
  tbody tr:hover td{background:#faf9f6}
  .grade-badge{display:inline-block;font-family:'Fira Code',monospace;font-weight:500;font-size:13px;
               padding:2px 10px;border-radius:20px;min-width:32px;text-align:center}
  .g-A{background:var(--green-bg);color:var(--green)}
  .g-B{background:var(--accent-bg);color:var(--accent)}
  .g-C{background:var(--amber-bg);color:var(--amber)}
  .g-D,.g-F{background:var(--red-bg);color:var(--red)}
  .scores-cell{font-family:'Fira Code',monospace;font-size:12px;color:var(--muted)}
  .avg-cell{font-family:'Fira Code',monospace;font-size:14px;font-weight:500}
 
  /* top scorer banner */
  #top-banner{display:none;background:var(--ink);color:#fff;border-radius:10px;
              padding:14px 20px;margin-bottom:20px;font-size:14px;font-weight:700;
              display:flex;align-items:center;gap:10px}
  #top-banner .crown{font-size:18px}
  .empty-msg{color:var(--muted);font-size:14px;padding:20px 0;text-align:center}
</style>
</head>
<body>
<div class="shell">
 
  <header>
    <p class="logo">Month 1 Final Project</p>
    <h1>Grade <span>Manager</span></h1>
  </header>
<div class="tabs">
    <button class="tab active" onclick="switchTab('add')">Add student</button>
    <button class="tab" onclick="switchTab('score')">Add score</button>
    <button class="tab" onclick="switchTab('delete')">Delete</button>
    <button class="tab" onclick="switchTab('report')">Report</button>
  </div>
 
  <!-- ADD STUDENT -->
  <div class="panel active" id="tab-add">
    <div class="card">
      <div class="form-row">
        <div><label>Student name</label><input type="text" id="add-name" placeholder="e.g. Alice"/></div>
        <div><label>First score</label><input type="number" id="add-score" placeholder="0 – 100" min="0" max="100"/></div>
      </div>
      <button class="btn btn-primary" onclick="doAdd()">Add student</button>
    </div>
  </div>
 
  <!-- ADD SCORE -->
#   <div class="panel" id="tab-score">
#     <div class="card">
#       <div class="form-row">
#         <div><label>Student name</label><input type="text" id="score-name" placeholder="Existing student"/></div>
#         <div><label>New score</label><input type="number" id="score-val" placeholder="0 – 100" min="0" max="100"/></div>
#       </div>
#       <button class="btn btn-primary" onclick="doScore()">Add score</button>
#     </div>
#   </div>
 
  </div><!-- shell -->
 
<div id="toast"></div>

<script>
  function switchTab(name) {
    document.querySelectorAll('.tab').forEach((t,i)=>{
      t.classList.toggle('active', ['add','score','delete','report'][i]===name)
    })
    document.querySelectorAll('.panel').forEach(p=>p.classList.remove('active'))
    document.getElementById('tab-'+name).classList.add('active')
    if(name==='report') loadReport()
  }
 
  function toast(msg, ok) {
    const el = document.getElementById('toast')
    el.textContent = msg
    el.className = 'show ' + (ok ? 'ok' : 'err')
    clearTimeout(toast._t)
    toast._t = setTimeout(()=>el.className='', 2600)
  }
 
  async function post(path, body) {
    const r = await fetch(path, {
      method: 'POST',
      headers: {'Content-Type':'application/json'},
      body: JSON.stringify(body)
    })
    return r.json()
  }

  async function doAdd() {
    const name  = document.getElementById('add-name').value.trim()
    const score = parseInt(document.getElementById('add-score').value)
    if (!name || isNaN(score)) { toast('Fill in both fields.', false); return }
    const res = await post('/add_student', {name, score})
    toast(res.msg, res.ok)
    if (res.ok) { document.getElementById('add-name').value=''; document.getElementById('add-score').value='' }
  }
 
  async function doScore() {
    const name  = document.getElementById('score-name').value.trim()
    const score = parseInt(document.getElementById('score-val').value)
    if (!name || isNaN(score)) { toast('Fill in both fields.', false); return }
    const res = await post('/add_score', {name, score})
    toast(res.msg, res.ok)
    if (res.ok) { document.getElementById('score-name').value=''; document.getElementById('score-val').value='' }
  }

 async function doDel() {
    const name = document.getElementById('del-name').value.trim()
    if (!name) { toast('Enter a name.', false); return }
    const res = await post('/delete_student', {name})
    toast(res.msg, res.ok)
    if (res.ok) document.getElementById('del-name').value=''
  }

</script>
</body>
</html>"""

class Handler(BaseHTTPRequestHandler):
    def send_json(self, data, status=200):
        body = json.dumps(data).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", len(body))
        self.end_headers()
        self.wfile.write(body)
 
    def read_json(self):
        length = int(self.headers.get("Content-Length", 0))
        return json.loads(self.rfile.read(length))
 
    # ── GET ──────────────────────────────
    def do_GET(self):
        path = urlparse(self.path).path
 
        if path == "/" or path == "/index.html":
            body = HTML.encode()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", len(body))
            self.end_headers()
            self.wfile.write(body)
 
        # elif path == "/report":
        #     self.send_json({
        #         "rows": get_report(),
        #         "top":  get_top_scorer(),
        #     })
 
        else:
            self.send_json({"error": "not found"}, 404)
 
    # ── POST ─────────────────────────────
    def do_POST(self):
        path = urlparse(self.path).path
        try:
            data = self.read_json()
        except Exception:
            self.send_json({"ok": False, "msg": "Invalid JSON."}, 400)
            return
 
        if path == "/add_student":
            self.send_json(add_student(data["name"], int(data["score"])))
 
        # elif path == "/add_score":
        #     self.send_json(add_score(data["name"], int(data["score"])))

        # elif path == "/delete_student":
        #     self.send_json(delete_student(data["name"]))
 
        # else:
        #     self.send_json({"error": "not found"}, 404)
 
 
# ─────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────
PORT = 8000
 
if __name__ == "__main__":
    server = HTTPServer(("", PORT), Handler)
    url = f"http://localhost:{PORT}"
    print(f"\n  Grade Manager running → {url}")
    print("  Press Ctrl+C to stop.\n")
    # Open the browser after a short delay so the server is ready
    threading.Timer(0.5, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n  Server stopped.")