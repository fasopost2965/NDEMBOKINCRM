import re

def main():
    filename = "Ndembo Kin Connect v2.dc.html"
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # The block looks like this:
    # thBg: th.bg,
    # thSidebar: th.sidebar,
    # thCard: th.card,
    # thCardBd: th.cardBd,
    # thInput: th.input,
    # thInputBd: th.inputBd,
    # thText: th.text,
    # thSub: th.sub,
    # thHeader: th.header,
    # thHeaderBd: th.headerBd,
    # thBtnSec: th.btnSec,
    # thBtnSecBd: th.btnSecBd,
    # thBtnSecC: th.btnSecC,

    block_regex = re.compile(r'\n\s*thBg: th\.bg,\s*\n\s*thSidebar: th\.sidebar,\s*\n\s*thCard: th\.card,\s*\n\s*thCardBd: th\.cardBd,\s*\n\s*thInput: th\.input,\s*\n\s*thInputBd: th\.inputBd,\s*\n\s*thText: th\.text,\s*\n\s*thSub: th\.sub,\s*\n\s*thHeader: th\.header,\s*\n\s*thHeaderBd: th\.headerBd,\s*\n\s*thBtnSec: th\.btnSec,\s*\n\s*thBtnSecBd: th\.btnSecBd,\s*\n\s*thBtnSecC: th\.btnSecC,', re.MULTILINE)
    
    matches = list(block_regex.finditer(content))
    if len(matches) > 1:
        # Keep the last match, remove the others
        last_match = matches[-1]
        
        # Build new content
        new_content = ""
        last_end = 0
        for i, match in enumerate(matches):
            if i == len(matches) - 1:
                # Keep it
                new_content += content[last_end:match.end()]
                last_end = match.end()
            else:
                # Skip it
                new_content += content[last_end:match.start()]
                last_end = match.end()
                
        new_content += content[last_end:]
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Removed {len(matches) - 1} bad blocks.")
    else:
        print("Could not find multiple blocks.")

if __name__ == "__main__":
    main()
