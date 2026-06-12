def main():
    filename = "Ndembo Kin Connect v2.dc.html"
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    th_logic = """
    const dm = S.darkMode;
    const th = {
      bg: dm ? "#0A161B" : "#EEF3F4",
      sidebar: dm ? "#050A0C" : "#132730",
      card: dm ? "#11222A" : "#FFFFFF",
      cardBd: dm ? "#1D3642" : "#E1E9EB",
      input: dm ? "#0A161B" : "#FFFFFF",
      inputBd: dm ? "#1D3642" : "#D3DEE2",
      text: dm ? "#E7F1F4" : "#16282F",
      sub: dm ? "#7A99A5" : "#7A8E96",
      header: dm ? "rgba(10,22,27,.93)" : "rgba(238,243,244,.93)",
      headerBd: dm ? "#1D3642" : "#E0E8EA",
      btnSec: dm ? "#1D3642" : "#FFFFFF",
      btnSecBd: dm ? "#2C4C5B" : "#D3DEE2",
      btnSecC: dm ? "#FFFFFF" : "#173A47"
    };
"""
    
    target_line = "const S = this.state, ps = this.STATUTS, ts = this.TYPES, cs = this.CARTES, dst = this.DOCST;"
    
    if target_line in content:
        content = content.replace(target_line, target_line + "\n" + th_logic)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print("Successfully injected th_logic.")
    else:
        print("Target line not found.")

if __name__ == "__main__":
    main()
