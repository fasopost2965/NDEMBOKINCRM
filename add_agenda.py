import re

def main():
    with open("Ndembo Kin Connect v2.dc.html", "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Sidebar
    sidebar_agenda = """
        <div onClick="{{ goAgenda }}" style="display:flex;align-items:center;gap:11px;padding:10px 12px;border-radius:10px;cursor:pointer;font-size:13.5px;font-weight:{{ nv.agenda.w }};color:{{ nv.agenda.c }};background:{{ nv.agenda.b }};" style-hover="background:rgba(255,255,255,.07);">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2.5"></rect><path d="M16 2v4M8 2v4M3 10h18"></path><path d="M8 14h.01M12 14h.01M16 14h.01M8 18h.01M12 18h.01"></path></svg>
          <span style="flex:1;">Agenda</span>
        </div>"""
    content = content.replace('<div onClick="{{ goDocs }}"', sidebar_agenda.strip() + '\n        <div onClick="{{ goDocs }}"')

    # 4. Titles
    content = content.replace('docs: "Devis & Factures",', 'docs: "Devis & Factures", agenda: "Agenda",')
    if 'agenda: "Agenda"' not in content:
        content = re.sub(r'(const titles = \{)', r'\1 agenda: "Agenda",', content)

    # 5. nv Object (add "agenda" to array)
    content = content.replace('"leads","membres"', '"leads","agenda","membres"')

    # 6. Initial state
    agenda_state = """
      agendaVue: "liste",
      agendaEvents: [
        { id: "ev1", titre: "Stage IDA Valencia — Glody", type: "stage", date: "02/07/2026", heure: "08:00", lieu: "Valencia, Espagne", statut: "confirme", projId: "pr1" },
        { id: "ev2", titre: "Tournoi Élite U17 — J1", type: "event", date: "15/07/2026", heure: "09:00", lieu: "Stade Tata Raphaël, Kinshasa", statut: "confirme", projId: "pr3" },
        { id: "ev3", titre: "Tournoi Élite U17 — J2", type: "event", date: "17/07/2026", heure: "10:00", lieu: "Stade Tata Raphaël, Kinshasa", statut: "confirme", projId: "pr3" },
        { id: "ev4", titre: "Tournoi Élite U17 — J3/Final", type: "event", date: "19/07/2026", heure: "15:00", lieu: "Stade Tata Raphaël, Kinshasa", statut: "confirme", projId: "pr3" },
        { id: "ev5", titre: "Camp détection Masina — Éd.3", type: "camp", date: "12/09/2026", heure: "07:30", lieu: "Stade de Masina, Kinshasa", statut: "brouillon", projId: "pr7" },
        { id: "ev6", titre: "Convention détection AS Vita", type: "relation", date: "01/09/2026", heure: "10:00", lieu: "Siège AS Vita Club", statut: "confirme", projId: "pr6" },
        { id: "ev7", titre: "Retour Glody Mbemba — debriefing", type: "autre", date: "28/06/2026", heure: "14:00", lieu: "Agence Ndembo Kin", statut: "confirme", projId: "pr1" },
        { id: "ev8", titre: "Point mensuel — Pathou Kasongo", type: "carriere", date: "07/07/2026", heure: "11:00", lieu: "Agence Ndembo Kin", statut: "confirme", projId: "pr2" }
      ],
      agendaEvSel: null,
      agendaNewOpen: false,
      agendaNew: { titre: "", type: "camp", date: "", heure: "09:00", lieu: "", projId: "" },
"""
    content = content.replace('leadSelId: null,', 'leadSelId: null,\n' + agenda_state)

    # 7. renderVals()
    agenda_render_vals = """
      isAgenda: S.screen === "agenda",
      goAgenda: () => this.go("agenda"),
      agendaVueListe: () => this.setState({ agendaVue: "liste" }),
      agendaVueCal: () => this.setState({ agendaVue: "calendrier" }),
      isAgendaListe: S.agendaVue === "liste",
      isAgendaCal: S.agendaVue === "calendrier",
      agendaVueLB: S.agendaVue === "liste" ? segOn.b : segOff.b,
      agendaVueLC: S.agendaVue === "liste" ? segOn.c : segOff.c,
      agendaVueLS: S.agendaVue === "liste" ? segOn.s : segOff.s,
      agendaVueCB: S.agendaVue === "calendrier" ? segOn.b : segOff.b,
      agendaVueCC: S.agendaVue === "calendrier" ? segOn.c : segOff.c,
      agendaVueCS: S.agendaVue === "calendrier" ? segOn.s : segOff.s,
      agendaNewOpen: S.agendaNewOpen,
      agendaOpenNew: () => this.setState({ agendaNewOpen: true }),
      agendaCloseNew: () => this.setState({ agendaNewOpen: false }),
      agendaNewTitre: (e) => this.setState({ agendaNew: Object.assign({}, S.agendaNew, { titre: e.target.value }) }),
      agendaNewType: (e) => this.setState({ agendaNew: Object.assign({}, S.agendaNew, { type: e.target.value }) }),
      agendaNewDate: (e) => this.setState({ agendaNew: Object.assign({}, S.agendaNew, { date: e.target.value }) }),
      agendaNewHeure: (e) => this.setState({ agendaNew: Object.assign({}, S.agendaNew, { heure: e.target.value }) }),
      agendaNewLieu: (e) => this.setState({ agendaNew: Object.assign({}, S.agendaNew, { lieu: e.target.value }) }),
      agendaNewVal: S.agendaNew,
      agendaSaveNew: () => {
        const n = S.agendaNew;
        if (!n.titre.trim()) { this.notify("Donnez un titre à l'événement"); return; }
        if (!n.date) { this.notify("Choisissez une date"); return; }
        const ev = { id: "ev" + Date.now(), titre: n.titre.trim(), type: n.type, date: n.date, heure: n.heure, lieu: n.lieu, statut: "confirme", projId: n.projId };
        this.setState({ agendaEvents: S.agendaEvents.concat([ev]), agendaNewOpen: false, agendaNew: { titre: "", type: "camp", date: "", heure: "09:00", lieu: "", projId: "" } });
        this.notify("Événement ajouté à l'agenda");
      },
      agendaEvSel: (() => {
        const ev = S.agendaEvents.find((e) => e.id === S.agendaEvSel);
        if (!ev) return null;
        const typeColors = { stage: "#0E97C4", event: "#D9A400", camp: "#1F8A5B", carriere: "#9B59B6", relation: "#E8262C", transfert: "#E87D26", autre: "#7A8E96" };
        const c = typeColors[ev.type] || "#7A8E96";
        const proj = S.projets.find((p) => p.id === ev.projId);
        return { ...ev, c, projTitre: proj ? proj.titre : null, statutL: ev.statut === "confirme" ? "Confirmé" : "Brouillon", statutC: ev.statut === "confirme" ? "#1F8A5B" : "#D9A400", close: () => this.setState({ agendaEvSel: null }), supprimer: () => { this.setState({ agendaEvents: S.agendaEvents.filter((x) => x.id !== ev.id), agendaEvSel: null }); this.notify("Événement supprimé"); } };
      })(),
      agendaEvSelOpen: !!S.agendaEvSel,
      agendaEvents: S.agendaEvents.slice().sort((a, b) => {
        const toMs = (d) => { const p = d.split("/"); return new Date(+p[2], +p[1] - 1, +p[0]).getTime(); };
        return toMs(a.date) - toMs(b.date);
      }).map((ev) => {
        const typeColors = { stage: "#0E97C4", event: "#D9A400", camp: "#1F8A5B", carriere: "#9B59B6", relation: "#E8262C", transfert: "#E87D26", autre: "#7A8E96" };
        const c = typeColors[ev.type] || "#7A8E96";
        const typeLabels = { stage: "Stage", event: "Événement", camp: "Camp", carriere: "Carrière", relation: "Relation", transfert: "Transfert", autre: "Autre" };
        const tl = typeLabels[ev.type] || ev.type;
        return { id: ev.id, titre: ev.titre, type: ev.type, typeL: tl, date: ev.date, heure: ev.heure, lieu: ev.lieu, c, statutL: ev.statut === "confirme" ? "Confirmé" : "Brouillon", statutC: ev.statut === "confirme" ? "#1F8A5B" : "#D9A400", open: () => this.setState({ agendaEvSel: ev.id }) };
      }),
      agendaTypeOpts: [
        { key: "camp", label: "Camp de détection" },
        { key: "stage", label: "Stage international" },
        { key: "event", label: "Événement / Tournoi" },
        { key: "carriere", label: "Suivi carrière" },
        { key: "relation", label: "Rencontre partenaire" },
        { key: "transfert", label: "Transfert" },
        { key: "autre", label: "Autre" }
      ],
      agendaSpotOpts: S.sportifs.map((s) => ({ key: s.id, nom: s.nom })),
      agendaProjOpts: S.projets.filter((p) => p.statut !== "annule").map((p) => ({ key: p.id, nom: p.titre })),
"""
    content = content.replace('partOptsRaw:', agenda_render_vals + '      partOptsRaw:')

    # 8. HTML Template
    agenda_html = """
<sc-if value="{{ isAgenda }}" hint-placeholder-val="{{ false }}">
  <div data-screen-label="Agenda">
    <!-- En-tête -->
    <div style="display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-bottom:18px;">
      <div>
        <div style="font-size:clamp(19px,3vw,23px);font-weight:800;letter-spacing:-.015em;">Agenda</div>
        <div style="font-size:13px;color:#5E7077;margin-top:3px;">Événements et jalons de l'agence</div>
      </div>
      <div style="display:flex;gap:8px;flex-wrap:wrap;">
        <!-- Toggle vue liste / calendrier -->
        <div style="display:inline-flex;border:1px solid #D3DEE2;border-radius:10px;overflow:hidden;">
          <button onClick="{{ agendaVueListe }}" style="border:none;padding:8px 14px;font-size:12px;font-weight:600;cursor:pointer;background:{{ agendaVueLB }};color:{{ agendaVueLC }};box-shadow:{{ agendaVueLS }};">Liste</button>
          <button onClick="{{ agendaVueCal }}" style="border:none;padding:8px 14px;font-size:12px;font-weight:600;cursor:pointer;background:{{ agendaVueCB }};color:{{ agendaVueCC }};box-shadow:{{ agendaVueCS }};">Calendrier</button>
        </div>
        <button onClick="{{ agendaOpenNew }}" style="border:none;border-radius:10px;background:#173A47;color:#FFFFFF;padding:9px 16px;font-size:13px;font-weight:700;cursor:pointer;display:inline-flex;align-items:center;gap:8px;" style-hover="background:#0F2E39;">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M12 5.5v13M5.5 12h13"></path></svg>
          Ajouter un événement
        </button>
      </div>
    </div>

    <!-- Vue Liste -->
    <sc-if value="{{ isAgendaListe }}" hint-placeholder-val="{{ true }}">
      <div style="display:flex;flex-direction:column;gap:8px;">
        <sc-for list="{{ agendaEvents }}" as="ev" hint-placeholder-count="6">
          <div onClick="{{ ev.open }}" style="background:{{ thCard }};border:1px solid {{ thCardBd }};border-radius:14px;padding:14px 16px;display:flex;align-items:center;gap:14px;cursor:pointer;transition:box-shadow .12s;" style-hover="box-shadow:0 4px 16px rgba(19,39,48,.08);">
            <!-- Type color bar -->
            <div style="width:4px;height:44px;border-radius:4px;background:{{ ev.c }};flex-shrink:0;"></div>
            <!-- Info principale -->
            <div style="flex:1;min-width:0;">
              <div style="font-size:14px;font-weight:700;color:{{ thText }};white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">{{ ev.titre }}</div>
              <div style="font-size:12px;color:{{ thSub }};margin-top:3px;display:flex;align-items:center;gap:10px;flex-wrap:wrap;">
                <span>{{ ev.date }} · {{ ev.heure }}</span>
                <sc-if value="{{ ev.lieu }}" hint-placeholder-val="{{ '' }}">
                  <span>· {{ ev.lieu }}</span>
                </sc-if>
              </div>
            </div>
            <!-- Badge type -->
            <span style="font-size:11px;font-weight:700;color:{{ ev.c }};background:{{ ev.c }}18;padding:3px 9px;border-radius:99px;white-space:nowrap;flex-shrink:0;">{{ ev.typeL }}</span>
            <!-- Badge statut -->
            <span style="font-size:11px;font-weight:700;color:{{ ev.statutC }};background:{{ ev.statutC }}18;padding:3px 9px;border-radius:99px;white-space:nowrap;flex-shrink:0;">{{ ev.statutL }}</span>
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#C9D6DA" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;"><path d="m9 18 6-6-6-6"></path></svg>
          </div>
        </sc-for>
      </div>
    </sc-if>

    <!-- Vue Calendrier (grille mois courant statique) -->
    <sc-if value="{{ isAgendaCal }}" hint-placeholder-val="{{ false }}">
      <div style="background:{{ thCard }};border:1px solid {{ thCardBd }};border-radius:16px;padding:20px;">
        <div style="font-size:15px;font-weight:800;color:{{ thText }};margin-bottom:16px;text-align:center;">Juillet 2026</div>
        <div style="display:grid;grid-template-columns:repeat(7,1fr);gap:6px;margin-bottom:8px;">
          <div style="text-align:center;font-size:11px;font-weight:700;color:#7A8E96;">L</div>
          <div style="text-align:center;font-size:11px;font-weight:700;color:#7A8E96;">M</div>
          <div style="text-align:center;font-size:11px;font-weight:700;color:#7A8E96;">M</div>
          <div style="text-align:center;font-size:11px;font-weight:700;color:#7A8E96;">J</div>
          <div style="text-align:center;font-size:11px;font-weight:700;color:#7A8E96;">V</div>
          <div style="text-align:center;font-size:11px;font-weight:700;color:#7A8E96;">S</div>
          <div style="text-align:center;font-size:11px;font-weight:700;color:#7A8E96;">D</div>
        </div>
        <!-- Juillet 2026 commence mercredi — 2 cases vides avant le 1er -->
        <div style="display:grid;grid-template-columns:repeat(7,1fr);gap:6px;">
          <div></div><div></div>
          <div style="border-radius:8px;padding:7px 4px;text-align:center;font-size:13px;font-weight:600;background:{{ thCardBd }};color:{{ thText }};">1</div>
          <div style="border-radius:8px;padding:7px 4px;text-align:center;font-size:13px;font-weight:600;color:{{ thText }};">2</div>
          <div style="border-radius:8px;padding:7px 4px;text-align:center;font-size:13px;font-weight:600;background:#0E97C418;color:#0E97C4;position:relative;">3</div>
          <div style="border-radius:8px;padding:7px 4px;text-align:center;font-size:13px;font-weight:600;color:{{ thText }};">4</div>
          <div style="border-radius:8px;padding:7px 4px;text-align:center;font-size:13px;font-weight:600;color:{{ thText }};">5</div>
          <div style="border-radius:8px;padding:7px 4px;text-align:center;font-size:13px;font-weight:600;color:{{ thText }};">6</div>
          <div style="border-radius:8px;padding:7px 4px;text-align:center;font-size:13px;font-weight:600;color:{{ thSub }};">7</div>
          <div style="border-radius:8px;padding:7px 4px;text-align:center;font-size:13px;font-weight:600;background:#0E97C418;color:#0E97C4;">8</div>
          <div style="border-radius:8px;padding:7px 4px;text-align:center;font-size:13px;font-weight:600;color:{{ thText }};">9</div>
          <div style="border-radius:8px;padding:7px 4px;text-align:center;font-size:13px;font-weight:600;color:{{ thText }};">10</div>
          <div style="border-radius:8px;padding:7px 4px;text-align:center;font-size:13px;font-weight:600;color:{{ thText }};">11</div>
          <div style="border-radius:8px;padding:7px 4px;text-align:center;font-size:13px;font-weight:600;color:{{ thText }};">12</div>
          <div style="border-radius:8px;padding:7px 4px;text-align:center;font-size:13px;font-weight:600;color:{{ thSub }};">13</div>
          <div style="border-radius:8px;padding:7px 4px;text-align:center;font-size:13px;font-weight:600;color:{{ thSub }};">14</div>
          <div style="border-radius:8px;padding:7px 4px;text-align:center;font-size:13px;font-weight:600;background:#D9A40018;color:#D9A400;">15</div>
          <div style="border-radius:8px;padding:7px 4px;text-align:center;font-size:13px;font-weight:600;color:{{ thText }};">16</div>
          <div style="border-radius:8px;padding:7px 4px;text-align:center;font-size:13px;font-weight:600;background:#D9A40018;color:#D9A400;">17</div>
          <div style="border-radius:8px;padding:7px 4px;text-align:center;font-size:13px;font-weight:600;color:{{ thText }};">18</div>
          <div style="border-radius:8px;padding:7px 4px;text-align:center;font-size:13px;font-weight:600;background:#D9A40018;color:#D9A400;">19</div>
          <div style="border-radius:8px;padding:7px 4px;text-align:center;font-size:13px;font-weight:600;color:{{ thSub }};">20</div>
          <div style="border-radius:8px;padding:7px 4px;text-align:center;font-size:13px;font-weight:600;color:{{ thSub }};">21</div>
          <div style="border-radius:8px;padding:7px 4px;text-align:center;font-size:13px;font-weight:600;color:{{ thText }};">22</div>
          <div style="border-radius:8px;padding:7px 4px;text-align:center;font-size:13px;font-weight:600;color:{{ thText }};">23</div>
          <div style="border-radius:8px;padding:7px 4px;text-align:center;font-size:13px;font-weight:600;color:{{ thText }};">24</div>
          <div style="border-radius:8px;padding:7px 4px;text-align:center;font-size:13px;font-weight:600;color:{{ thText }};">25</div>
          <div style="border-radius:8px;padding:7px 4px;text-align:center;font-size:13px;font-weight:600;color:{{ thSub }};">26</div>
          <div style="border-radius:8px;padding:7px 4px;text-align:center;font-size:13px;font-weight:600;color:{{ thSub }};">27</div>
          <div style="border-radius:8px;padding:7px 4px;text-align:center;font-size:13px;font-weight:600;background:#1F8A5B18;color:#1F8A5B;">28</div>
          <div style="border-radius:8px;padding:7px 4px;text-align:center;font-size:13px;font-weight:600;color:{{ thText }};">29</div>
          <div style="border-radius:8px;padding:7px 4px;text-align:center;font-size:13px;font-weight:600;color:{{ thText }};">30</div>
          <div style="border-radius:8px;padding:7px 4px;text-align:center;font-size:13px;font-weight:600;color:{{ thText }};">31</div>
        </div>
        <!-- Légende -->
        <div style="margin-top:16px;display:flex;gap:14px;flex-wrap:wrap;">
          <div style="display:flex;align-items:center;gap:6px;font-size:12px;color:#7A8E96;"><span style="width:10px;height:10px;border-radius:50%;background:#0E97C4;display:inline-block;"></span>Stage/Carrière</div>
          <div style="display:flex;align-items:center;gap:6px;font-size:12px;color:#7A8E96;"><span style="width:10px;height:10px;border-radius:50%;background:#D9A400;display:inline-block;"></span>Événement/Tournoi</div>
          <div style="display:flex;align-items:center;gap:6px;font-size:12px;color:#7A8E96;"><span style="width:10px;height:10px;border-radius:50%;background:#1F8A5B;display:inline-block;"></span>Camp détection</div>
        </div>
      </div>
    </sc-if>

    <!-- Panel détail événement -->
    <sc-if value="{{ agendaEvSelOpen }}" hint-placeholder-val="{{ false }}">
      <div onClick="{{ agendaEvSel.close }}" style="position:fixed;inset:0;z-index:49;background:rgba(0,0,0,.3);"></div>
      <div style="position:fixed;right:0;top:0;bottom:0;z-index:50;width:min(420px,100vw);background:{{ thCard }};box-shadow:-4px 0 32px rgba(0,0,0,.14);display:flex;flex-direction:column;animation:slideIn .18s ease;">
        <div style="display:flex;align-items:center;justify-content:space-between;padding:18px 20px;border-bottom:1px solid {{ thCardBd }};">
          <div style="font-size:15px;font-weight:800;color:{{ thText }};">Détail événement</div>
          <button onClick="{{ agendaEvSel.close }}" style="border:none;background:none;cursor:pointer;color:{{ thSub }};display:grid;place-items:center;width:32px;height:32px;border-radius:8px;" style-hover="background:{{ thCardBd }};">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M6 6l12 12M18 6 6 18"></path></svg>
          </button>
        </div>
        <div style="flex:1;overflow-y:auto;padding:20px;">
          <div style="width:100%;height:5px;border-radius:4px;background:{{ agendaEvSel.c }};margin-bottom:20px;"></div>
          <div style="font-size:18px;font-weight:800;color:{{ thText }};margin-bottom:8px;">{{ agendaEvSel.titre }}</div>
          <div style="display:flex;gap:8px;margin-bottom:16px;flex-wrap:wrap;">
            <span style="font-size:12px;font-weight:700;color:{{ agendaEvSel.c }};background:{{ agendaEvSel.c }}18;padding:4px 10px;border-radius:99px;">{{ agendaEvSel.typeL }}</span>
            <span style="font-size:12px;font-weight:700;color:{{ agendaEvSel.statutC }};background:{{ agendaEvSel.statutC }}18;padding:4px 10px;border-radius:99px;">{{ agendaEvSel.statutL }}</span>
          </div>
          <div style="display:flex;flex-direction:column;gap:12px;">
            <div style="display:flex;gap:12px;align-items:flex-start;">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#7A8E96" stroke-width="1.8" stroke-linecap="round" style="flex-shrink:0;margin-top:2px;"><rect x="3" y="4" width="18" height="18" rx="2.5"></rect><path d="M16 2v4M8 2v4M3 10h18"></path></svg>
              <div style="font-size:13px;color:{{ thText }};">{{ agendaEvSel.date }} à {{ agendaEvSel.heure }}</div>
            </div>
            <sc-if value="{{ agendaEvSel.lieu }}" hint-placeholder-val="{{ '' }}">
              <div style="display:flex;gap:12px;align-items:flex-start;">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#7A8E96" stroke-width="1.8" stroke-linecap="round" style="flex-shrink:0;margin-top:2px;"><path d="M12 2C8.134 2 5 5.134 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.866-3.134-7-7-7z"></path><circle cx="12" cy="9" r="2.5"></circle></svg>
                <div style="font-size:13px;color:{{ thText }};">{{ agendaEvSel.lieu }}</div>
              </div>
            </sc-if>
            <sc-if value="{{ agendaEvSel.projTitre }}" hint-placeholder-val="{{ '' }}">
              <div style="display:flex;gap:12px;align-items:flex-start;">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#7A8E96" stroke-width="1.8" stroke-linecap="round" style="flex-shrink:0;margin-top:2px;"><rect x="3.5" y="4" width="4.8" height="16" rx="1.2"></rect><rect x="9.8" y="4" width="4.8" height="11" rx="1.2"></rect><rect x="16.1" y="4" width="4.8" height="7" rx="1.2"></rect></svg>
                <div style="font-size:13px;color:{{ thText }};">Projet : {{ agendaEvSel.projTitre }}</div>
              </div>
            </sc-if>
          </div>
        </div>
        <div style="padding:16px 20px;border-top:1px solid {{ thCardBd }};">
          <button onClick="{{ agendaEvSel.supprimer }}" style="width:100%;border:1px solid #E8262C;background:transparent;color:#E8262C;border-radius:10px;padding:11px;font-size:13px;font-weight:700;cursor:pointer;" style-hover="background:#E8262C18;">Supprimer l'événement</button>
        </div>
      </div>
    </sc-if>

    <!-- Modal nouvel événement -->
    <sc-if value="{{ agendaNewOpen }}" hint-placeholder-val="{{ false }}">
      <div onClick="{{ agendaCloseNew }}" style="position:fixed;inset:0;z-index:49;background:rgba(0,0,0,.3);"></div>
      <div style="position:fixed;inset:0;z-index:50;display:flex;align-items:center;justify-content:center;padding:20px;">
        <div style="background:{{ thCard }};border-radius:18px;width:100%;max-width:480px;box-shadow:0 24px 60px rgba(0,0,0,.2);animation:fadeUp .18s ease;">
          <div style="display:flex;align-items:center;justify-content:space-between;padding:18px 20px;border-bottom:1px solid {{ thCardBd }};">
            <div style="font-size:15px;font-weight:800;color:{{ thText }};">Ajouter un événement</div>
            <button onClick="{{ agendaCloseNew }}" style="border:none;background:none;cursor:pointer;color:{{ thSub }};display:grid;place-items:center;width:32px;height:32px;border-radius:8px;" style-hover="background:{{ thCardBd }};">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M6 6l12 12M18 6 6 18"></path></svg>
            </button>
          </div>
          <div style="padding:20px;display:flex;flex-direction:column;gap:14px;">
            <div>
              <label style="font-size:11px;font-weight:700;color:{{ thSub }};letter-spacing:.06em;text-transform:uppercase;display:block;margin-bottom:6px;">Titre *</label>
              <input value="{{ agendaNewVal.titre }}" onChange="{{ agendaNewTitre }}" placeholder="ex: Camp détection Masina" style="width:100%;padding:10px 12px;border:1px solid {{ thInputBd }};border-radius:10px;font-size:13px;background:{{ thInput }};color:{{ thText }};outline:none;" />
            </div>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
              <div>
                <label style="font-size:11px;font-weight:700;color:{{ thSub }};letter-spacing:.06em;text-transform:uppercase;display:block;margin-bottom:6px;">Date *</label>
                <input type="date" value="{{ agendaNewVal.date }}" onChange="{{ agendaNewDate }}" style="width:100%;padding:10px 12px;border:1px solid {{ thInputBd }};border-radius:10px;font-size:13px;background:{{ thInput }};color:{{ thText }};outline:none;" />
              </div>
              <div>
                <label style="font-size:11px;font-weight:700;color:{{ thSub }};letter-spacing:.06em;text-transform:uppercase;display:block;margin-bottom:6px;">Heure</label>
                <input type="time" value="{{ agendaNewVal.heure }}" onChange="{{ agendaNewHeure }}" style="width:100%;padding:10px 12px;border:1px solid {{ thInputBd }};border-radius:10px;font-size:13px;background:{{ thInput }};color:{{ thText }};outline:none;" />
              </div>
            </div>
            <div>
              <label style="font-size:11px;font-weight:700;color:{{ thSub }};letter-spacing:.06em;text-transform:uppercase;display:block;margin-bottom:6px;">Type</label>
              <select value="{{ agendaNewVal.type }}" onChange="{{ agendaNewType }}" style="width:100%;padding:10px 12px;border:1px solid {{ thInputBd }};border-radius:10px;font-size:13px;background:{{ thInput }};color:{{ thText }};outline:none;">
                <sc-for list="{{ agendaTypeOpts }}" as="t" hint-placeholder-count="5">
                  <option value="{{ t.key }}">{{ t.label }}</option>
                </sc-for>
              </select>
            </div>
            <div>
              <label style="font-size:11px;font-weight:700;color:{{ thSub }};letter-spacing:.06em;text-transform:uppercase;display:block;margin-bottom:6px;">Lieu</label>
              <input value="{{ agendaNewVal.lieu }}" onChange="{{ agendaNewLieu }}" placeholder="ex: Stade de Masina" style="width:100%;padding:10px 12px;border:1px solid {{ thInputBd }};border-radius:10px;font-size:13px;background:{{ thInput }};color:{{ thText }};outline:none;" />
            </div>
          </div>
          <div style="padding:16px 20px;border-top:1px solid {{ thCardBd }};display:flex;gap:10px;">
            <button onClick="{{ agendaCloseNew }}" style="flex:1;border:1px solid {{ thBtnSecBd }};background:{{ thBtnSec }};color:{{ thBtnSecC }};border-radius:10px;padding:11px;font-size:13px;font-weight:600;cursor:pointer;">Annuler</button>
            <button onClick="{{ agendaSaveNew }}" style="flex:2;border:none;background:#173A47;color:#FFFFFF;border-radius:10px;padding:11px;font-size:13px;font-weight:700;cursor:pointer;" style-hover="background:#0F2E39;">Enregistrer</button>
          </div>
        </div>
      </div>
    </sc-if>
  </div>
</sc-if>
"""
    content = content.replace('    </div>\n  </div>\n  <sc-if value="{{ isMobile }}"', agenda_html + '\n    </div>\n  </div>\n  <sc-if value="{{ isMobile }}"')

    with open("Ndembo Kin Connect v2.dc.html", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    main()
