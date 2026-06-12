import re
import os

def main():
    with open("Ndembo Kin Connect.dc.html", "r", encoding="utf-8") as f:
        content = f.read()

    # --- 1. Modify this.state ---
    state_inject = """
      screen: "login",
      loginEmail: "", loginPassword: "", loginError: "", showPwd: false,
      darkMode: false,
      leads: [
        { id: "l1", nom: "Thierry Luba", age: 16, poste: "Attaquant", club: "Saint-Esprit FC", tel: "+243 90 123 4567", message: "Mon fils joue en U17, je cherche un accompagnement pour une détection Europe.", date: "09/06/2026", statut: "nouveau" },
        { id: "l2", nom: "Famille Nkosi", age: 18, poste: "Milieu", club: "Non affilié", tel: "+243 81 987 6543", message: "Intéressé par la carte VIP et un suivi personnalisé.", date: "07/06/2026", statut: "contacté" },
        { id: "l3", nom: "Rebecca Ntumba", age: 15, poste: "Gardienne", club: "Académie Amani", tel: "+243 99 456 7890", message: "Entraîneur recommande une détection pour sélection nationale.", date: "05/06/2026", statut: "qualifié" }
      ],
      leadSelId: null,
"""
    content = re.sub(r'(this\.state\s*=\s*\{)', r'\1\n' + state_inject, content, count=1)

    # --- 2. Add this.LEADS ---
    leads_const = """
    this.LEADS = {
      nouveau: { l: "Nouveau", c: "#0B7FA6", bg: "#DFF3FA" },
      contacté: { l: "Contacté", c: "#9A6E00", bg: "#FFF1C9" },
      qualifié: { l: "Qualifié", c: "#1F8A5B", bg: "#E1F3E9" },
      converti: { l: "Converti", c: "#44707F", bg: "#E5EBEE" },
      fermé: { l: "Fermé", c: "#C9252B", bg: "#FBE5E5" }
    };
"""
    # Find a good place to inject constants (e.g. after this.STATUTS)
    content = re.sub(r'(this\.STATUTS\s*=\s*\{.*?\};)', r'\1\n' + leads_const, content, flags=re.DOTALL)

    # --- 3. Add printDoc method ---
    print_doc_method = """
  printDoc(d) {
    const t = this.docTotaux(d);
    const w = window.open("", "_blank");
    w.document.write(`<!DOCTYPE html><html><head><meta charset="utf-8"><title>${d.num}</title>
    <style>body{font-family:system-ui,sans-serif;margin:0;padding:32px;color:#16282F;}h1{font-size:18px;font-weight:800;color:#132730;}table{width:100%;border-collapse:collapse;margin:24px 0;}th{text-align:left;font-size:11px;font-weight:700;text-transform:uppercase;color:#7A8E96;padding:8px 12px;border-bottom:2px solid #E0E8EA;}td{padding:10px 12px;border-bottom:1px solid #EEF3F4;font-size:13px;}@media print{button{display:none;}}</style></head>
    <body>
    <div style="display:flex;justify-content:space-between;margin-bottom:32px;">
      <div><h1>NDEMBO KIN CONNECT SARL</h1><div style="font-size:12px;color:#7A8E96;">12, av. de la Libération — Gombe, Kinshasa</div></div>
      <div style="text-align:right;"><div style="font-size:22px;font-weight:800;">${d.type==="devis"?"DEVIS":"FACTURE"}</div><div style="font-size:14px;color:#44707F;">${d.num}</div><div style="font-size:12px;color:#7A8E96;">Date : ${d.date}</div></div>
    </div>
    <div style="padding:14px;background:#F5F8F9;border-radius:8px;margin-bottom:24px;"><div style="font-size:11px;font-weight:700;text-transform:uppercase;color:#7A8E96;">CLIENT</div><div style="font-size:15px;font-weight:700;">${d.clientNom}</div></div>
    <table><thead><tr><th>Description</th><th>Qté</th><th>Prix unit.</th><th>Total</th></tr></thead>
    <tbody>${d.lignes.map(l=>`<tr><td>${l.label}</td><td>${l.qte}</td><td>${l.prix} $</td><td>${l.qte*l.prix} $</td></tr>`).join("")}</tbody></table>
    <div style="text-align:right;"><div style="font-size:13px;">Sous-total : <strong>${t.st} $</strong></div>${d.tva?`<div style="color:#7A8E96;font-size:13px;">TVA (25%) : ${t.tv} $</div>`:""}<div style="font-size:17px;font-weight:800;margin-top:8px;">Total : ${t.tot} $</div></div>
    <div style="margin-top:40px;font-size:11px;color:#7A8E96;border-top:1px solid #E0E8EA;padding-top:16px;">Orange Money · M-Pesa · Airtel Money · Virement Rawbank · Espèces</div>
    <button onclick="window.print();window.close();" style="margin-top:16px;padding:10px 20px;background:#132730;color:#FFF;border:none;border-radius:8px;font-size:13px;cursor:pointer;font-weight:700;">Imprimer / PDF</button>
    </body></html>`);
    w.document.close();
  }
"""
    content = re.sub(r'(renderVals\(\)\s*\{)', print_doc_method + r'\n  \1', content, count=1)

    # Replace print logic inside renderVals with printDoc(d)
    # wizPdf
    content = content.replace('wizPdf: () => alert("Génération PDF... (démo)"),', 'wizPdf: () => this.printDoc(this.vmDocRow(S.docs.find(d=>d.id===S.wiz.ref))),')
    # prev.print
    content = content.replace('print: () => alert("Impression... (démo)"),', 'print: () => this.printDoc(this.vmDocRow(S.docs.find(d=>d.id===S.docPrev))),')
    
    # Reports exports
    export_pdf_logic = """exportPdf: () => {
      const w = window.open("", "_blank");
      w.document.write(`<!DOCTYPE html><html><head><meta charset="utf-8"><title>Rapport</title></head><body><h1>Rapport exporté</h1><button onclick="window.print();window.close();">Imprimer / PDF</button></body></html>`);
      w.document.close();
    },"""
    content = re.sub(r'exportPdf:\s*\(\)\s*=>\s*alert\("Export PDF\.\.\. \(démo\)"\),', export_pdf_logic, content)
    
    export_csv_logic = """exportCsv: () => {
      const csv = "data:text/csv;charset=utf-8,KPI,Valeur\\nTotal,100\\n";
      const a = document.createElement("a"); a.href = encodeURI(csv); a.download = "rapport.csv"; document.body.appendChild(a); a.click(); document.body.removeChild(a);
    },"""
    content = re.sub(r'exportCsv:\s*\(\)\s*=>\s*alert\("Export CSV\.\.\. \(démo\)"\),', export_csv_logic, content)

    # --- 4. Dark Mode Colors ---
    # We define `th` object inside renderVals
    th_logic = """
    const dm = S.darkMode;
    const th = {
      bg: dm ? "#0F1C22" : "#EEF3F4",
      sidebar: dm ? "#08131A" : "#132730",
      card: dm ? "#162330" : "#FFFFFF",
      cardBd: dm ? "#243A44" : "#E1E9EB",
      input: dm ? "#1E2F38" : "#FFFFFF",
      inputBd: dm ? "#2A4550" : "#D3DEE2",
      text: dm ? "#E7F1F4" : "#16282F",
      sub: dm ? "#5E8A96" : "#7A8E96",
      header: dm ? "#0F1C22" : "rgba(238,243,244,.93)",
      headerBd: dm ? "#243A44" : "#E0E8EA",
      btnSec: dm ? "#162330" : "#FFFFFF",
      btnSecBd: dm ? "#243A44" : "#D3DEE2",
      btnSecC: dm ? "#E7F1F4" : "#173A47"
    };
"""
    content = re.sub(r'(const\s+S\s*=\s*this\.state;)', r'\1\n' + th_logic, content)

    # Now we need to flatten the `th` variables for DCLogic (because it prefers flat objects or simple nested)
    # Actually, the user says "renderVals() retourne un objet PLAT uniquement — si {{ th.bg }} ne fonctionne pas, aplatir en thBg, thCard, etc."
    # Let's flatten them inside the return object of renderVals:
    flatten_th = """
      thBg: th.bg,
      thSidebar: th.sidebar,
      thCard: th.card,
      thCardBd: th.cardBd,
      thInput: th.input,
      thInputBd: th.inputBd,
      thText: th.text,
      thSub: th.sub,
      thHeader: th.header,
      thHeaderBd: th.headerBd,
      thBtnSec: th.btnSec,
      thBtnSecBd: th.btnSecBd,
      thBtnSecC: th.btnSecC,
"""
    content = re.sub(r'(return\s*\{)', r'\1\n' + flatten_th, content)

    # Replace colors in HTML with {{ thBg }}, {{ thCard }}, etc.
    content = content.replace('color:#16282F', 'color:{{ thText }}')
    content = content.replace('background:#EEF3F4', 'background:{{ thBg }}')
    content = content.replace('background:#132730', 'background:{{ thSidebar }}')
    content = content.replace('background:#FFFFFF', 'background:{{ thCard }}')
    content = content.replace('border:1px solid #E1E9EB', 'border:1px solid {{ thCardBd }}')
    content = content.replace('border:1px solid #E0E8EA', 'border:1px solid {{ thHeaderBd }}')
    content = content.replace('background:rgba(238,243,244,.93)', 'background:{{ thHeader }}')
    
    # We must be careful not to break badges. "Les couleurs de statut (badges, chips colorés) ne changent PAS en dark mode."
    # E.g. background:#FFFFFF in inputs and cards:
    content = content.replace('background:#F2F6F7', 'background:{{ thCard }}')
    content = content.replace('color:#7A8E96', 'color:{{ thSub }}')

    # Add dark mode toggle to settings screen (under Apparence)
    settings_appear = """
            <div style="background:{{ thCard }};border:1px solid {{ thCardBd }};border-radius:14px;padding:16px 18px;">
              <div style="font-size:14.5px;font-weight:700;">Apparence</div>
              <div style="display:flex;align-items:center;gap:10px;margin-top:13px;">
                <div onClick="{{ toggleDark }}" style="width:40px;height:22px;border-radius:99px;position:relative;cursor:pointer;transition:background .2s;background:{{ darkBg }};">
                  <span style="position:absolute;top:3px;width:16px;height:16px;border-radius:50%;background:#FFFFFF;transition:left .2s;left:{{ darkLeft }};"></span>
                </div>
                <span style="font-size:13px;font-weight:600;">Mode sombre</span>
              </div>
            </div>
"""
    # Insert before "Facturation" section
    content = content.replace('<div style="font-size:14.5px;font-weight:700;">Facturation</div>', settings_appear + '\n              <div style="font-size:14.5px;font-weight:700;">Facturation</div>')

    # Inject toggle methods
    toggle_methods = """
      toggleDark: () => this.setState({ darkMode: !S.darkMode }),
      darkBg: dm ? "#0E97C4" : "#C7D4D9",
      darkLeft: dm ? "21px" : "3px",
"""
    content = re.sub(r'(toggleTvaDefaut:\s*\(\)\s*=>\s*this\.setState\(\{.*?\}\),)', r'\1\n' + toggle_methods, content)

    # --- 5. Add Leads screen (F4) ---
    # Add to navMap
    content = content.replace('docs: "docs",', 'docs: "docs", leads: "leads",')
    content = content.replace('docs: "Devis & Factures",', 'docs: "Devis & Factures", leads: "Leads",')
    
    # Add to titles
    content = content.replace('docs: "Devis & Factures",', 'docs: "Devis & Factures", leads: "Leads",')

    # Add to forEach of nv
    content = content.replace('["dash","projets","sportifs","partenaires","docs","membres","precontrat","rapports","parametres"].forEach', '["dash","projets","sportifs","partenaires","docs","leads","membres","precontrat","rapports","parametres"].forEach')

    # Add sidebar item HTML
    sidebar_leads = """
        <div onClick="{{ goLeads }}" style="display:flex;align-items:center;gap:11px;padding:10px 12px;border-radius:10px;cursor:pointer;font-size:13.5px;font-weight:{{ nv.leads.w }};color:{{ nv.leads.c }};background:{{ nv.leads.b }};" style-hover="background:rgba(255,255,255,.07);">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 13V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h9"></path><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path><path d="M16 19h6M19 16v6"></path></svg>
          <span style="flex:1;">Leads</span>
          <sc-if value="{{ hasNewLeads }}" hint-placeholder-val="{{ true }}">
            <span style="width:8px;height:8px;border-radius:50%;background:#E8262C;"></span>
          </sc-if>
        </div>
"""
    content = content.replace('<div onClick="{{ goDocs }}"', sidebar_leads + '\n        <div onClick="{{ goDocs }}"')

    # Leads logic in renderVals
    leads_logic = """
      goLeads: () => this.setState({ screen: "leads" }),
      isLeads: S.screen === "leads",
      hasNewLeads: S.leads.some(l => l.statut === "nouveau"),
      leadsKpis: [
        { label: "Total leads", val: S.leads.length },
        { label: "Nouveaux", val: S.leads.filter(l => l.statut === "nouveau").length },
        { label: "Qualifiés", val: S.leads.filter(l => l.statut === "qualifié").length }
      ],
      leadsList: S.leads.map(l => {
        const st = this.LEADS[l.statut];
        return {
          ...l,
          stLabel: st.l, stC: st.c, stBg: st.bg,
          open: () => this.setState({ leadSelId: l.id })
        };
      }),
      selLead: S.leadSelId ? (()=>{
        const l = S.leads.find(x => x.id === S.leadSelId);
        const st = this.LEADS[l.statut];
        return {
          ...l, stLabel: st.l, stC: st.c, stBg: st.bg,
          close: () => this.setState({ leadSelId: null }),
          setStatut: (newSt) => {
            const nl = [...S.leads];
            const idx = nl.findIndex(x => x.id === S.leadSelId);
            nl[idx].statut = newSt;
            this.setState({ leads: nl });
          },
          creerSportif: () => {
            const ns = [...S.sportifs, {
              id: "s" + Date.now(), nom: l.nom, age: l.age, tel: l.tel,
              club: l.club, date: "Aujourd'hui", docs: [], projets: [], notes: [], sub: l.poste
            }];
            const nl = [...S.leads];
            const idx = nl.findIndex(x => x.id === S.leadSelId);
            nl[idx].statut = "converti";
            this.setState({ sportifs: ns, leads: nl, leadSelId: null, screen: "sportifs" });
          }
        };
      })() : null,
      leadStatutOpts: Object.keys(this.LEADS).map(k => ({ k, l: this.LEADS[k].l })),
"""
    content = re.sub(r'(goDocs:\s*\(\)\s*=>\s*this\.setState\(\{ screen:\s*"docs"\s*\}\),)', leads_logic + r'\1', content)

    # Leads HTML Screen
    leads_html = """
      <sc-if value="{{ isLeads }}" hint-placeholder-val="{{ false }}">
        <div data-screen-label="Leads">
          <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(168px,1fr));gap:11px;margin-top:16px;">
            <sc-for list="{{ leadsKpis }}" as="k" hint-placeholder-count="3">
              <div style="background:{{ thCard }};border:1px solid {{ thCardBd }};border-radius:14px;padding:15px 16px;">
                <div style="font-size:11px;font-weight:700;color:{{ thSub }};letter-spacing:.06em;text-transform:uppercase;">{{ k.label }}</div>
                <div style="font-size:26px;font-weight:800;letter-spacing:-.02em;margin-top:6px;font-variant-numeric:tabular-nums;">{{ k.val }}</div>
              </div>
            </sc-for>
          </div>
          <div style="background:{{ thCard }};border:1px solid {{ thCardBd }};border-radius:14px;padding:6px 18px;margin-top:14px;">
            <sc-for list="{{ leadsList }}" as="l" hint-placeholder-count="3">
              <div onClick="{{ l.open }}" style="display:flex;align-items:center;gap:12px;padding:12px 0;border-top:1px solid {{ thCardBd }};cursor:pointer;flex-wrap:wrap;">
                <span style="flex:1;min-width:170px;">
                  <span style="display:block;font-size:13.5px;font-weight:600;">{{ l.nom }} ({{ l.age }} ans)</span>
                  <span style="display:block;font-size:11.5px;color:{{ thSub }};">{{ l.poste }} · {{ l.club }}</span>
                </span>
                <span style="font-size:11.5px;color:{{ thSub }};white-space:nowrap;">{{ l.date }}</span>
                <span style="padding:3px 10px;border-radius:999px;font-size:11px;font-weight:700;white-space:nowrap;background:{{ l.stBg }};color:{{ l.stC }};">{{ l.stLabel }}</span>
              </div>
            </sc-for>
          </div>
          <sc-if value="{{ selLead }}" hint-placeholder-val="{{ false }}">
            <div onClick="{{ selLead.close }}" style="position:fixed;inset:0;z-index:60;background:rgba(10,22,27,.45);"></div>
            <div style="position:fixed;top:0;right:0;bottom:0;width:min(430px,100vw);z-index:61;background:{{ thCard }};box-shadow:-14px 0 44px rgba(10,22,27,.2);display:flex;flex-direction:column;">
              <div style="padding:18px 20px 0;display:flex;align-items:flex-start;justify-content:space-between;gap:10px;">
                <span style="display:inline-block;padding:3px 10px;border-radius:999px;font-size:11px;font-weight:700;background:{{ selLead.stBg }};color:{{ selLead.stC }};">{{ selLead.stLabel }}</span>
                <button onClick="{{ selLead.close }}" style="border:none;background:#ECF1F2;border-radius:9px;width:30px;height:30px;cursor:pointer;display:grid;place-items:center;color:#5E7077;">X</button>
              </div>
              <div style="padding:10px 20px 0;font-size:17px;font-weight:800;line-height:1.35;">{{ selLead.nom }}</div>
              <div style="padding:12px 20px 0;font-size:13px;color:{{ thSub }};">{{ selLead.poste }} · {{ selLead.club }} · {{ selLead.age }} ans</div>
              <div style="padding:12px 20px 0;font-size:13px;color:{{ thSub }};">{{ selLead.tel }}</div>
              <div style="flex:1;padding:20px;">
                <div style="font-size:11px;font-weight:700;color:{{ thSub }};letter-spacing:.08em;">MESSAGE</div>
                <div style="margin-top:7px;padding:12px 14px;border-radius:11px;background:#F7FAFA;font-size:12.5px;color:#33474F;">{{ selLead.message }}</div>
                <div style="margin-top:20px;">
                  <div style="font-size:11px;font-weight:700;color:{{ thSub }};letter-spacing:.08em;margin-bottom:8px;">CHANGER STATUT</div>
                  <div style="display:flex;gap:8px;flex-wrap:wrap;">
                    <sc-for list="{{ leadStatutOpts }}" as="so" hint-placeholder-count="5">
                      <button onClick="{{ () => selLead.setStatut(so.k) }}" style="border:1px solid {{ thCardBd }};border-radius:999px;background:{{ thCard }};color:{{ thText }};padding:6px 12px;font-size:11.5px;cursor:pointer;">{{ so.l }}</button>
                    </sc-for>
                  </div>
                </div>
                <button onClick="{{ selLead.creerSportif }}" style="margin-top:24px;border:none;border-radius:10px;background:#173A47;color:#FFFFFF;padding:11px 14px;font-size:13px;font-weight:700;cursor:pointer;width:100%;">Créer fiche sportif</button>
              </div>
            </div>
          </sc-if>
        </div>
      </sc-if>
"""
    content = content.replace('<sc-if value="{{ isDocs }}"', leads_html + '\n      <sc-if value="{{ isDocs }}"')

    # --- 6. Add F1 (Login screen) ---
    login_html = """
  <sc-if value="{{ isLogin }}" hint-placeholder-val="{{ true }}">
    <div style="min-height:100vh;display:flex;align-items:center;justify-content:center;background:#EEF3F4;padding:20px;">
      <div style="background:#FFFFFF;width:100%;max-width:400px;border-radius:20px;padding:32px;box-shadow:0 10px 25px rgba(0,0,0,0.05);text-align:center;">
        <img src="assets/logo-lockup.png" alt="Ndembo Kin" style="width:120px;height:auto;margin:0 auto 24px;display:block;" />
        <h2 style="font-size:20px;font-weight:800;color:#132730;margin:0 0 8px;">Bienvenue</h2>
        <p style="font-size:13px;color:#7A8E96;margin:0 0 24px;">Connectez-vous pour accéder au CRM</p>
        
        <input value="{{ loginEmail }}" onChange="{{ onLoginEmail }}" placeholder="Adresse email" style="width:100%;padding:12px 14px;border:1px solid #D3DEE2;border-radius:12px;font-size:14px;margin-bottom:12px;outline:none;" />
        
        <div style="position:relative;margin-bottom:24px;">
          <input type="{{ showPwd ? 'text' : 'password' }}" value="{{ loginPassword }}" onChange="{{ onLoginPwd }}" placeholder="Mot de passe" style="width:100%;padding:12px 40px 12px 14px;border:1px solid #D3DEE2;border-radius:12px;font-size:14px;outline:none;" />
          <button onClick="{{ togglePwd }}" style="position:absolute;right:12px;top:50%;transform:translateY(-50%);border:none;background:transparent;cursor:pointer;color:#7A8E96;font-size:12px;font-weight:600;">Afficher</button>
        </div>
        
        <sc-if value="{{ loginError }}" hint-placeholder-val="{{ false }}">
          <div style="color:#E8262C;font-size:12px;font-weight:600;margin-bottom:16px;">{{ loginError }}</div>
        </sc-if>
        
        <button onClick="{{ doLogin }}" style="width:100%;padding:14px;border:none;border-radius:12px;background:#132730;color:#FFFFFF;font-size:14px;font-weight:700;cursor:pointer;box-shadow:0 4px 10px rgba(19,39,48,0.2);">Se connecter</button>
        
        <p style="font-size:11px;color:#9AAAB1;margin:24px 0 0;">3 comptes démo disponibles</p>
      </div>
    </div>
  </sc-if>
  <sc-if value="{{ notLogin }}" hint-placeholder-val="{{ false }}">
"""
    # Find start of main app UI
    main_ui_start = '<div style="font-family:\'Archivo\',system-ui,sans-serif;'
    content = content.replace(main_ui_start, login_html + main_ui_start)

    # Close notLogin at the end of the template
    content = content.replace('</x-dc>', '  </sc-if>\n</x-dc>')

    login_logic = """
      isLogin: S.screen === "login",
      notLogin: S.screen !== "login",
      onLoginEmail: (e) => this.setState({ loginEmail: e.target.value }),
      onLoginPwd: (e) => this.setState({ loginPassword: e.target.value }),
      togglePwd: () => this.setState({ showPwd: !S.showPwd }),
      doLogin: () => {
        const mail = S.loginEmail.toLowerCase().trim();
        const pwd = S.loginPassword;
        if (mail === "admin@ndembokin.com" && pwd === "admin123") {
          this.setState({ screen: "dash", role: "admin", loginError: "" });
        } else if (mail === "partenaire@cdleganes.es" && pwd === "part123") {
          this.setState({ screen: "espacePartenaire", role: "partenaire", loginError: "" });
        } else if (mail === "sportif@ndembokin.com" && pwd === "sport123") {
          this.setState({ screen: "espaceSportif", role: "sportif", loginError: "" });
        } else {
          this.setState({ loginError: "Email ou mot de passe incorrect." });
        }
      },
"""
    content = re.sub(r'(renderVals\(\)\s*\{\s*const S = this\.state;\n\s*const dm = S\.darkMode;\n\s*const th = \{.*?\};\n\s*return \{)', r'\1\n' + login_logic, content, flags=re.DOTALL)

    # Add @media print to helmet
    media_print = """
<style>
@media print { body { background: #FFFFFF !important; } .no-print { display: none !important; } }
</style>
"""
    content = content.replace('</helmet>', media_print + '</helmet>')

    with open("Ndembo Kin Connect v2.dc.html", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    main()
