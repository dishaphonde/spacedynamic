import os

css_file = r"c:\Users\phond\Music\spacedynamics\css\style.css"

with open(css_file, "r", encoding="utf-8") as f:
    content = f.read()

# Replace root variables
new_root = """
:root{
  --color-primary: #1a5d3a;
  --color-primary-light: #237348;
  --color-accent: #2f9e5c;
  --color-accent-hover: #268049;
  --color-bg: #ffffff;
  --color-bg-alt: #f7f9f7;
  --color-heading: #1a1a1a;
  --color-text: #5c5c5c;
  --color-border: #e5e5e8;

  --navy: var(--color-primary);
  --navy-deep: var(--color-primary-light);
  --navy-soft: var(--color-primary-light);
  --gold: var(--color-accent);
  --gold-light: var(--color-accent-hover);
  --white: var(--color-bg);
  --gray-bg: var(--color-bg-alt);
  --gray-line: var(--color-border);
  --slate: var(--color-text);
  --ink: var(--color-heading);

  --font-display: 'Inter', sans-serif;
  --font-body: 'Inter', sans-serif;

  --radius-sm: 6px;
  --radius-md: 8px;
  --radius-lg: 12px;

  --shadow-soft: 0 4px 12px rgba(0,0,0,0.03);
  --shadow-strong: 0 8px 24px rgba(0,0,0,0.06);

  --container: 1240px;
  --nav-h: 90px;
}
"""

import re
content = re.sub(r':root\s*\{[\s\S]*?\n\}', new_root.strip(), content, count=1)

# Replace hardcoded RGBA values for old navy/gold
content = content.replace("rgba(11,31,58", "rgba(26,93,58")
content = content.replace("rgba(7,21,39", "rgba(26,93,58")
content = content.replace("rgba(200,169,81", "rgba(47,158,92")

with open(css_file, "w", encoding="utf-8") as f:
    f.write(content)

print("style.css updated successfully.")
