<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CampusNav</title>
<link href="https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;600;700;900&display=swap" rel="stylesheet">
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Heebo', sans-serif; background: #f8fafc; color: #1e293b; direction: rtl; }

header { 
  background: linear-gradient(135deg, #0f1b35 0%, #1d4ed8 100%);
  padding: 16px; color: white; position: sticky; top: 0; z-index: 100; 
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  display: flex; justify-content: space-between; align-items: center;
}
header div:first-child { flex: 1; text-align: center; }
header h1 { font-size: 1.3rem; font-weight: 700; margin-bottom: 4px; }
header p { font-size: 0.8rem; opacity: 0.85; }

.header-buttons { display: flex; gap: 8px; }
.admin-btn { 
  background: rgba(255,255,255,0.2); color: white; border: 1px solid rgba(255,255,255,0.4);
  padding: 8px 12px; border-radius: 6px; font-size: 0.8rem; cursor: pointer; font-family: 'Heebo';
  transition: all 0.2s;
}
.admin-btn:hover { background: rgba(255,255,255,0.3); }
.admin-btn.logged { background: #059669; }

.admin-indicator { 
  position: fixed; bottom: 20px; right: 20px; background: #059669; color: white;
  padding: 10px 14px; border-radius: 20px; font-size: 0.85rem; font-weight: 600;
  display: none; z-index: 999;
}
.admin-indicator.show { display: block; }

.modal {
  display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.5); z-index: 1000; align-items: center; justify-content: center;
}
.modal.show { display: flex; }

.modal-content {
  background: white; padding: 30px; border-radius: 12px; width: 90%; max-width: 350px;
  box-shadow: 0 10px 40px rgba(0,0,0,0.2);
}
.modal-title { font-size: 1.1rem; font-weight: 700; margin-bottom: 16px; }
.modal-input { 
  width: 100%; padding: 10px 12px; border: 1.5px solid #e2e8f0; 
  border-radius: 8px; font-family: 'Heebo'; font-size: 0.9rem; margin-bottom: 12px;
}
.modal-buttons { display: flex; gap: 8px; }
.modal-btn { 
  flex: 1; padding: 10px; border: none; border-radius: 8px; 
  font-family: 'Heebo'; font-weight: 600; cursor: pointer; font-size: 0.9rem;
}
.modal-btn-submit { background: #0f1b35; color: white; }
.modal-btn-cancel { background: #e2e8f0; color: #475569; }

.intro-banner {
  background: white; padding: 14px 16px; margin-bottom: 12px; border-radius: 10px;
  border-right: 4px solid #1d4ed8; box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}
.intro-banner-text {
  font-size: 0.95rem; line-height: 1.5; color: #1e293b;
}
.intro-banner-text strong { color: #1d4ed8; }

.tabs { 
  display: flex; background: white; border-bottom: 2px solid #e2e8f0; 
  gap: 0; padding: 0 16px; overflow-x: auto;
}
.tab-btn { 
  flex: 1; padding: 14px 12px; border: none; background: transparent; 
  border-bottom: 3px solid transparent; font-family: 'Heebo', sans-serif; 
  font-size: 0.9rem; font-weight: 600; cursor: pointer; color: #475569; 
  transition: all 0.3s; white-space: nowrap;
}
.tab-btn:hover { color: #1d4ed8; }
.tab-btn.active { border-bottom-color: #1d4ed8; color: #1d4ed8; }
.tab-btn.admin-only { background: #fef3c7; color: #92400e; }

.content { padding: 14px; display: none; min-height: 400px; }
.content.active { display: block; }

.search-box { background: white; padding: 14px; border-radius: 10px; margin-bottom: 12px; border: 1px solid #e2e8f0; }
.search-input { width: 100%; padding: 11px 12px; border: 1.5px solid #e2e8f0; border-radius: 8px; font-family: 'Heebo', sans-serif; font-size: 0.95rem; }
.search-input::placeholder { color: #cbd5e1; }
.search-input:focus { outline: none; border-color: #1d4ed8; background: #f0f9ff; }
.search-results { max-height: 180px; overflow-y: auto; display: none; }
.search-results.show { display: block; }
.result-item { padding: 10px 12px; border-bottom: 1px solid #f1f5f9; cursor: pointer; transition: background 0.2s; }
.result-item:hover { background: #f8fafc; }
.result-name { font-weight: 600; font-size: 0.9rem; }
.result-info { font-size: 0.75rem; color: #475569; margin-top: 2px; }

.controls { background: white; padding: 14px; border-radius: 10px; margin-bottom: 12px; border: 1px solid #e2e8f0; }
.control { margin-bottom: 10px; }
.control:last-child { margin-bottom: 0; }
label { font-size: 0.75rem; font-weight: 700; color: #475569; text-transform: uppercase; display: block; margin-bottom: 5px; letter-spacing: 0.3px; }
select { width: 100%; padding: 10px 12px; border: 1.5px solid #e2e8f0; border-radius: 8px; font-family: 'Heebo', sans-serif; font-size: 0.9rem; background: white; }
select:focus { outline: none; border-color: #1d4ed8; }

.btn-group { display: flex; gap: 8px; margin-bottom: 10px; }
.btn { flex: 1; padding: 11px; border: none; border-radius: 8px; font-family: 'Heebo', sans-serif; font-weight: 600; cursor: pointer; font-size: 0.9rem; transition: all 0.2s; }
.btn-swap { background: #f1f5f9; color: #1d4ed8; border: 1.5px solid #e2e8f0; }
.btn-swap:hover { background: #e0f2fe; }
.btn-swap:active { transform: scale(0.97); }
.btn-calc { background: #0f1b35; color: white; flex: 2; }
.btn-calc:hover { background: #1d4ed8; }
.btn-calc:active { transform: scale(0.97); }

.error { background: #fef2f2; border: 1.5px solid #fecdd3; border-radius: 8px; padding: 11px 12px; color: #c41e3a; display: none; margin-bottom: 12px; font-weight: 600; text-align: center; font-size: 0.9rem; }
.error.show { display: block; }

.results { display: none; }
.results.show { display: block; }

.metrics { 
  display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-bottom: 14px;
}
.metric { 
  background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
  padding: 12px; border-radius: 8px; text-align: center; border: 1.5px solid #bfdbfe;
}
.metric-val { font-size: 1.4rem; font-weight: 800; color: #0f1b35; }
.metric-lbl { font-size: 0.75rem; color: #0c4a6e; margin-top: 4px; font-weight: 600; }

.white-card { background: white; padding: 14px; border-radius: 10px; border: 1px solid #e2e8f0; margin-bottom: 12px; }
.card-title { font-weight: 700; margin-bottom: 12px; font-size: 0.95rem; }

.instruction-item { 
  padding: 12px; margin-bottom: 10px; background: #f0f9ff; 
  border-right: 4px solid #1d4ed8; border-radius: 4px; font-size: 0.95rem; line-height: 1.6;
}
.instruction-number { font-weight: 700; color: #1d4ed8; font-size: 1rem; }
.instruction-text { color: #1e293b; margin-top: 4px; }

.route-point { 
  padding: 12px; margin-bottom: 10px; background: white; 
  border-right: 4px solid #1d4ed8; border-radius: 4px; border: 1px solid #e2e8f0;
}
.route-point.start { border-right-color: #059669; background: #f0fdf4; }
.route-point.end { border-right-color: #dc2626; background: #fef2f2; }
.point-icon { font-size: 1.3rem; margin-left: 8px; font-weight: 700; }
.point-name { font-weight: 700; font-size: 0.95rem; }
.point-floor { font-size: 0.8rem; color: #475569; margin-top: 4px; }

.form-group { margin-bottom: 12px; }
.form-group label { display: block; margin-bottom: 6px; font-size: 0.8rem; font-weight: 700; color: #475569; text-transform: uppercase; }
select, textarea, input[type="email"] { width: 100%; padding: 10px 12px; border: 1.5px solid #e2e8f0; border-radius: 8px; font-family: 'Heebo', sans-serif; font-size: 0.9rem; }
select:focus, textarea:focus, input[type="email"]:focus { outline: none; border-color: #1d4ed8; }
textarea { resize: vertical; min-height: 100px; }
.btn-submit { width: 100%; padding: 12px; background: #059669; color: white; border: none; border-radius: 8px; font-family: 'Heebo', sans-serif; font-weight: 700; cursor: pointer; font-size: 0.95rem; }
.btn-submit:hover { background: #047857; }
.btn-submit:active { transform: scale(0.97); }

.success-banner { background: #f0fdf4; border: 1.5px solid #86efac; border-radius: 8px; padding: 12px; color: #166534; text-align: center; display: none; margin-bottom: 12px; font-weight: 600; }
.success-banner.show { display: block; }

.issue-list { display: grid; gap: 10px; }
.issue-card { background: white; padding: 14px; border-radius: 8px; border-right: 4px solid #1d4ed8; border: 1px solid #e2e8f0; }
.issue-type { font-weight: 700; color: #1d4ed8; margin-bottom: 4px; font-size: 0.95rem; }
.issue-location { font-size: 0.85rem; color: #475569; margin-bottom: 6px; }
.issue-desc { font-size: 0.9rem; line-height: 1.5; color: #1e293b; margin-bottom: 8px; background: #f8fafc; padding: 8px; border-radius: 4px; }
.issue-meta { font-size: 0.8rem; color: #94a3b8; display: flex; gap: 12px; flex-wrap: wrap; }

.empty-state { text-align: center; color: #94a3b8; padding: 30px 16px; font-size: 0.9rem; }

footer { text-align: center; padding: 16px; color: #94a3b8; font-size: 0.8rem; }
</style>
</head>
<body>

<header>
  <div>
    <h1>🧭 CampusNav</h1>
    <p>מערכת ניווט חכמה למכללת עזריאלי</p>
  </div>
  <div class="header-buttons">
    <button class="admin-btn" id="adminBtn" onclick="openAdminModal()" title="כניסת מנהל">🔐 ניהול</button>
  </div>
</header>

<div class="admin-indicator" id="adminIndicator">✅ מחובר כמנהל</div>

<div class="modal" id="adminModal">
  <div class="modal-content">
    <div class="modal-title">🔐 כניסת מנהל</div>
    <input type="password" id="adminPassword" class="modal-input" placeholder="הכנס סיסמה..." onkeypress="if(event.key==='Enter') loginAdmin()">
    <div class="modal-buttons">
      <button class="modal-btn modal-btn-submit" onclick="loginAdmin()">כנס</button>
      <button class="modal-btn modal-btn-cancel" onclick="closeAdminModal()">ביטול</button>
    </div>
  </div>
</div>

<div style="padding: 0 16px;">
  <div class="intro-banner">
    <div class="intro-banner-text">
      <strong>ברוכים הבאים!</strong> בחרו נקודת מוצא ויעד כדי לקבל את <strong>המסלול המהיר ביותר</strong> במכללה.
    </div>
  </div>
</div>

<div class="tabs">
  <button class="tab-btn active" onclick="switchTab(0)">🗺️ ניווט</button>
  <button class="tab-btn" onclick="switchTab(1)">📋 המסלול שלי</button>
  <button class="tab-btn" onclick="switchTab(2)">🚨 דיווח בעיה</button>
  <button class="tab-btn admin-only" id="adminTab" onclick="switchTab(3)" style="display: none;">📊 בעיות דווחו</button>
</div>

<!-- TAB 1: NAVIGATION -->
<div class="content active">
  <div class="search-box">
    <input type="text" id="search" class="search-input" placeholder="חפשו כיתה, שירות או מיקום...">
    <div class="search-results" id="results-dropdown"></div>
  </div>

  <div class="controls">
    <div class="control">
      <label>📍 מאיפה אתם יוצאים?</label>
      <select id="from"></select>
    </div>

    <div class="btn-group">
      <button class="btn btn-swap" onclick="swap()" title="החלף מוצא ויעד">⇅ החלף</button>
      <button class="btn btn-calc" onclick="calculate()">🚀 חשב מסלול</button>
    </div>

    <div class="control">
      <label>🎯 לאן תרצו להגיע?</label>
      <select id="to"></select>
    </div>

    <div class="error" id="error"></div>
  </div>

  <div class="results" id="results-tab1">
    <div class="metrics">
      <div class="metric">
        <span class="metric-val" id="time">—</span>
        <span class="metric-lbl">⏱ זמן הליכה</span>
      </div>
      <div class="metric">
        <span class="metric-val" id="dist">—</span>
        <span class="metric-lbl">📏 מרחק</span>
      </div>
      <div class="metric">
        <span class="metric-val" id="stops">—</span>
        <span class="metric-lbl">🚩 עצירות</span>
      </div>
    </div>
  </div>
</div>

<!-- TAB 2: ROUTE INSTRUCTIONS -->
<div class="content">
  <div class="white-card" id="instructions-card">
    <div class="card-title">📋 הוראות הגעה שלכם</div>
    <div id="instructions"></div>
    <div style="text-align: center; color: #94a3b8; padding: 20px; font-size: 0.9rem;">
      👈 חשבו מסלול בטאב "ניווט" כדי לראות הוראות הגעה
    </div>
  </div>

  <div class="white-card">
    <div class="card-title">🗺️ נקודות הדרך</div>
    <div id="route-map"></div>
    <div style="text-align: center; color: #94a3b8; padding: 20px; font-size: 0.9rem;">
      👈 חשבו מסלול בטאב "ניווט"
    </div>
  </div>
</div>

<!-- TAB 3: REPORT ISSUE -->
<div class="content">
  <div class="success-banner" id="success"></div>
  
  <div class="white-card">
    <div class="card-title">🚨 דיווח על בעיה בקמפוס</div>
    <p style="font-size: 0.85rem; color: #475569; margin-bottom: 12px; line-height: 1.5;">
      נתקלתם בכלוך, תקלה, או כל בעיה אחרת במכללה? דווחו לנו ונעדכן את צוות התחזוקה.
    </p>

    <div class="form-group">
      <label>🔍 סוג הבעיה</label>
      <select id="issue-type">
        <option value="">— בחרו סוג בעיה —</option>
        <option value="🧹 כלוך">🧹 כלוך / ניקיון</option>
        <option value="🔧 תקלה">🔧 תקלה טכנית</option>
        <option value="⚠️ בטיחות">⚠️ בטיחות</option>
        <option value="💡 תאורה">💡 תאורה / חשמל</option>
        <option value="🚪 כניסה">🚪 בעיית כניסה / דלת</option>
        <option value="🛗 מעלית">🛗 בעיית מעלית</option>
        <option value="📌 אחר">📌 אחר</option>
      </select>
    </div>

    <div class="form-group">
      <label>📍 היכן בקמפוס?</label>
      <select id="issue-location">
        <option value="">— בחרו מיקום —</option>
        <option value="שער כניסה ראשי">שער כניסה ראשי</option>
        <option value="קפיטריה">קפיטריה</option>
        <option value="ספריה">ספריה</option>
        <option value="שירותים">שירותים</option>
        <option value="מסדרון">מסדרון</option>
        <option value="אזור כיתות">אזור כיתות</option>
        <option value="מעלית">מעלית</option>
        <option value="אחר">מיקום אחר</option>
      </select>
    </div>

    <div class="form-group">
      <label>📝 תיאור הבעיה</label>
      <textarea id="issue-description" placeholder="תארו בקצרה את הבעיה שנתקלתם בה..."></textarea>
    </div>

    <div class="form-group">
      <label>📞 מייל ליצירת קשר (אופציונלי)</label>
      <input type="email" id="issue-email" placeholder="שלכם@gmail.com">
    </div>

    <button class="btn-submit" onclick="submitReport()">📤 שלח דיווח</button>
  </div>
</div>

<!-- TAB 4: ADMIN ISSUES DASHBOARD -->
<div class="content">
  <div class="white-card">
    <div class="card-title">📊 לוח בקרה - כל הדיווחים</div>
    <p style="font-size: 0.85rem; color: #475569; margin-bottom: 12px;">
      כל הדיווחים שנשלחו מהמשתמשים:
    </p>
    
    <div class="issue-list" id="issues-list">
      <div class="empty-state">
        🟢 טוב! אין דיווחים על בעיות כרגע.
      </div>
    </div>
  </div>
</div>

<footer>
  CampusNav • מכללת עזריאלי ירושלים • פרויקט חקר ביצועים
</footer>

<script>
const NODES = {
  "17":{"name":"שער כניסה ראשי","floor":"0","keywords":"כניסה שער ראשי"},
  "9":{"name":"קפיטריה","floor":"0","keywords":"קפה אוכל"},
  "7":{"name":"מרכז שירות","floor":"0","keywords":"שירות סטודנט"},
  "11":{"name":"מחשוב","floor":"0","keywords":"מחשוב IT מעבדה"},
  "8":{"name":"מרכז מודיעין","floor":"0","keywords":"מודיעין ספריה"},
  "6":{"name":"פינת למידה 0","floor":"0","keywords":"למידה"},
  "20":{"name":"שירותים 0","floor":"0","keywords":"שירותים"},
  "28":{"name":"c102","floor":"1","keywords":"כיתה הנדסה"},
  "30":{"name":"c104","floor":"1","keywords":"כיתה"},
  "37":{"name":"c202","floor":"2","keywords":"רובוטיקה"},
  "43":{"name":"c208","floor":"2","keywords":"בינה מלאכותית"},
  "47":{"name":"ספריה","floor":"3","keywords":"ספריה קריאה"},
  "21":{"name":"שירותים 1","floor":"1","keywords":"שירותים"},
  "22":{"name":"שירותים 2","floor":"2","keywords":"שירותים"},
  "23":{"name":"שירותים 3","floor":"3","keywords":"שירותים"}
};

const ADJ_TIME = {"17":[["9",30]],"9":[["17",30],["20",25]],"7":[["6",8],["11",29]],"11":[["7",29]],"8":[["20",17]],"6":[["20",13],["7",8]],"20":[["6",13],["8",17],["21",10]],"21":[["20",10],["22",10],["28",13]],"22":[["21",10],["23",10],["37",13]],"28":[["21",13]],"30":[["21",13]],"37":[["22",13]],"43":[["22",13]],"47":[["23",8]],"23":[["47",8],["22",10]]};
const ADJ_DIST = {"17":[["9",35]],"9":[["17",35],["20",25]],"7":[["6",9],["11",27]],"11":[["7",27]],"8":[["20",8]],"6":[["20",16],["7",9]],"20":[["6",16],["8",8],["21",12]],"21":[["20",12],["22",12],["28",8]],"22":[["21",12],["23",12],["37",8]],"28":[["21",8]],"30":[["21",8]],"37":[["22",8]],"43":[["22",8]],"47":[["23",10]],"23":[["47",10],["22",12]]};

const ADMIN_PASSWORD = "admin123";
let isAdmin = sessionStorage.getItem('isAdmin') === 'true';
let reportedIssues = JSON.parse(localStorage.getItem('campusNavIssues')) || [];

function updateAdminUI() {
  const adminTab = document.getElementById('adminTab');
  const adminBtn = document.getElementById('adminBtn');
  const adminIndicator = document.getElementById('adminIndicator');
  
  if (isAdmin) {
    adminTab.style.display = 'block';
    adminBtn.classList.add('logged');
    adminBtn.textContent = '✅ מחובר';
    adminIndicator.classList.add('show');
  } else {
    adminTab.style.display = 'none';
    adminBtn.classList.remove('logged');
    adminBtn.textContent = '🔐 ניהול';
    adminIndicator.classList.remove('show');
  }
}

function openAdminModal() {
  document.getElementById('adminModal').classList.add('show');
  document.getElementById('adminPassword').focus();
}

function closeAdminModal() {
  document.getElementById('adminModal').classList.remove('show');
  document.getElementById('adminPassword').value = '';
}

function loginAdmin() {
  const password = document.getElementById('adminPassword').value;
  
  if (password === ADMIN_PASSWORD) {
    isAdmin = true;
    sessionStorage.setItem('isAdmin', 'true');
    updateAdminUI();
    closeAdminModal();
  } else {
    alert('❌ סיסמה שגויה');
    document.getElementById('adminPassword').value = '';
    document.getElementById('adminPassword').focus();
  }
}

function switchTab(n) {
  if (n === 3 && !isAdmin) {
    alert('❌ נדרשת כניסה כמנהל');
    openAdminModal();
    return;
  }
  
  document.querySelectorAll('.content').forEach(c => c.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.content')[n].classList.add('active');
  document.querySelectorAll('.tab-btn')[n].classList.add('active');
  
  if (n === 3) displayIssues();
}

function populateSelects() {
  const from = document.getElementById('from');
  const to = document.getElementById('to');
  Object.entries(NODES).forEach(([id, n]) => {
    const o1 = document.createElement('option');
    const o2 = document.createElement('option');
    o1.value = o2.value = id;
    o1.textContent = o2.textContent = n.name;
    from.appendChild(o1);
    to.appendChild(o2);
  });
  from.value = '17'; to.value = '47';
}

document.getElementById('search').addEventListener('input', function(e) {
  const q = e.target.value.toLowerCase();
  const dd = document.getElementById('results-dropdown');
  if (!q) { dd.classList.remove('show'); return; }
  const matches = Object.entries(NODES).filter(([id, n]) => n.name.toLowerCase().includes(q) || n.keywords.toLowerCase().includes(q));
  dd.innerHTML = matches.map(([id, n]) => `<div class="result-item" onclick="setFrom('${id}')"><div class="result-name">${n.name}</div><div class="result-info">קומה ${n.floor}</div></div>`).join('');
  dd.classList.toggle('show', matches.length > 0);
});

function setFrom(id) {
  document.getElementById('from').value = id;
  document.getElementById('search').value = '';
  document.getElementById('results-dropdown').classList.remove('show');
}

function swap() {
  const f = document.getElementById('from');
  const t = document.getElementById('to');
  const tmp = f.value;
  f.value = t.value;
  t.value = tmp;
}

function dijkstra(adj, src, tgt) {
  const ids = Object.keys(NODES);
  const dist = {}, prev = {};
  const unvisited = new Set(ids);
  ids.forEach(n => { dist[n] = Infinity; prev[n] = null; });
  dist[src] = 0;
  while (unvisited.size > 0) {
    let u = null;
    unvisited.forEach(n => { if (u === null || dist[n] < dist[u]) u = n; });
    if (u === tgt || dist[u] === Infinity) break;
    unvisited.delete(u);
    (adj[u] || []).forEach(([nb, w]) => {
      if (!unvisited.has(nb)) return;
      const alt = dist[u] + w;
      if (alt < dist[nb]) { dist[nb] = alt; prev[nb] = u; }
    });
  }
  if (dist[tgt] === Infinity) return null;
  const path = [];
  let c = tgt;
  while (c !== null) { path.unshift(c); c = prev[c]; }
  return path[0] === src ? {path, total: dist[tgt]} : null;
}

function calculate() {
  const src = document.getElementById('from').value;
  const tgt = document.getElementById('to').value;
  const err = document.getElementById('error');
  err.classList.remove('show');

  if (src === tgt) { err.textContent = '📍 אותו מיקום! בחרו יעד שונה'; err.classList.add('show'); return; }

  const res = dijkstra(ADJ_TIME, src, tgt);
  if (!res) { err.textContent = '❌ לא ניתן להגיע ליעד זה'; err.classList.add('show'); return; }

  let tt = 0, td = 0;
  for (let i = 0; i < res.path.length - 1; i++) {
    const a = res.path[i], b = res.path[i + 1];
    const te = (ADJ_TIME[a] || []).find(x => x[0] === b);
    const de = (ADJ_DIST[a] || []).find(x => x[0] === b);
    if (te) tt += te[1];
    if (de) td += de[1];
  }

  const m = Math.floor(tt / 60), s = Math.round(tt % 60);
  document.getElementById('time').textContent = m > 0 ? `${m}:${String(s).padStart(2,'0')}` : `${s}״`;
  document.getElementById('dist').textContent = `${td}מ׳`;
  document.getElementById('stops').textContent = res.path.length - 1;

  const instr = document.getElementById('instructions');
  instr.innerHTML = '';
  let stepNum = 1;
  res.path.forEach((id, i) => {
    const n = NODES[id];
    const next = i < res.path.length - 1 ? NODES[res.path[i + 1]] : null;
    const nextFloor = next ? parseInt(next.floor) : null;
    const currFloor = parseInt(n.floor);
    
    let action = '';
    if (i === 0) action = `🟢 התחילו כאן: <strong>${n.name}</strong>`;
    else if (i === res.path.length - 1) action = `🎯 הגעתם ליעד: <strong>${n.name}</strong>`;
    else if (nextFloor !== null && nextFloor > currFloor) action = `⬆️ עלו קומה לקומה <strong>${nextFloor}</strong> (${n.name})`;
    else if (nextFloor !== null && nextFloor < currFloor) action = `⬇️ רדו קומה לקומה <strong>${nextFloor}</strong> (${n.name})`;
    else action = `➡️ המשיכו ל<strong>${n.name}</strong>`;

    const div = document.createElement('div');
    div.className = 'instruction-item';
    div.innerHTML = `<div class="instruction-number">שלב ${stepNum}</div><div class="instruction-text">${action}</div>`;
    instr.appendChild(div);
    stepNum++;
  });

  const routeMap = document.getElementById('route-map');
  routeMap.innerHTML = '';
  res.path.forEach((id, i) => {
    const n = NODES[id];
    const isStart = i === 0;
    const isEnd = i === res.path.length - 1;
    const next = i < res.path.length - 1 ? NODES[res.path[i + 1]] : null;
    const de = (ADJ_DIST[id] || []).find(x => x[0] === (next ? res.path[i + 1] : null));
    const dist = de ? `${de[1]} מ'` : '';
    
    const div = document.createElement('div');
    div.className = `route-point ${isStart ? 'start' : isEnd ? 'end' : ''}`;
    div.innerHTML = `<span class="point-icon">${isStart ? '🟢' : isEnd ? '🔴' : '🔵'}</span><div><div class="point-name">${n.name}</div><div class="point-floor">קומה ${n.floor} ${dist}</div></div>`;
    routeMap.appendChild(div);
  });

  document.getElementById('results-tab1').classList.add('show');
}

function submitReport() {
  const type = document.getElementById('issue-type').value;
  const loc = document.getElementById('issue-location').value;
  const desc = document.getElementById('issue-description').value;
  const email = document.getElementById('issue-email').value;

  if (!type || !desc.trim()) { alert('⚠️ בחרו סוג בעיה וכתבו תיאור'); return; }

  const issue = {
    id: Date.now(),
    type: type,
    location: loc,
    description: desc,
    email: email,
    timestamp: new Date().toLocaleString('he-IL'),
    status: '⏳ נתקבל'
  };

  reportedIssues.push(issue);
  localStorage.setItem('campusNavIssues', JSON.stringify(reportedIssues));

  const success = document.getElementById('success');
  success.innerHTML = '✅ דיווח נשלח בהצלחה! צוות התחזוקה קיבל את הדיווח שלכם.';
  success.classList.add('show');

  document.getElementById('issue-type').value = '';
  document.getElementById('issue-location').value = '';
  document.getElementById('issue-description').value = '';
  document.getElementById('issue-email').value = '';

  setTimeout(() => success.classList.remove('show'), 4000);
}

function displayIssues() {
  const list = document.getElementById('issues-list');
  
  if (reportedIssues.length === 0) {
    list.innerHTML = '<div class="empty-state">🟢 טוב! אין דיווחים על בעיות כרגע.</div>';
    return;
  }

  list.innerHTML = reportedIssues.slice().reverse().map(issue => `
    <div class="issue-card">
      <div class="issue-type">${issue.type}</div>
      <div class="issue-location">📍 ${issue.location}</div>
      <div class="issue-desc">${issue.description}</div>
      <div class="issue-meta">
        <span>📧 ${issue.email || 'ללא מייל'}</span>
        <span>⏰ ${issue.timestamp}</span>
        <span>${issue.status}</span>
      </div>
    </div>
  `).join('');
}

populateSelects();
updateAdminUI();
</script>
</body>
</html>
