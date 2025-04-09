import os
import subprocess
import platform
import urllib.request

def install_pandoc():
    system = platform.system().lower()
    
    if system == "windows":
        print("Windows işletim sistemi tespit edildi, Pandoc kurulumu başlatılıyor...")
        url = "https://github.com/jgm/pandoc/releases/download/2.19/pandoc-2.19-windows-x86_64.msi"
        filename = "pandoc-installer.msi"
        urllib.request.urlretrieve(url, filename)
        subprocess.run(["msiexec", "/i", filename, "/quiet"], check=True)
        print("Pandoc başarıyla kuruldu.")


build_system = [".vscode", "chapters", "images", "out", "scripts",]
files_to_create = [
    (".vscode/tasks.json", '''{
        "version": "2.0.0",
        "tasks": [
            {
                "label": "Derlemece",
                "type": "shell",
                "command": "scripts/compile.bat",
                "group": {
                    "kind": "build",
                    "isDefault": true
                },
                "presentation": {
                    "reveal": "always",
                    "panel": "dedicated"
                }
            }
        ]
    }'''),
    ("chapters/ch01.md", "# Test Text"),
    ("scripts/compile.bat", '''powershell -Command "Get-Content chapters/*.md -Encoding UTF8 | Out-File out/kitap.md -Encoding UTF8; pandoc kapak.md out/kitap.md -o out/kitap.pdf --pdf-engine=xelatex --template=default --highlight-style=tango -V titlepage -V papersize=a5"'''),
    ("kapak.md", "\\vspace*{5cm} \\begin{center} {\Huge \\textbf{Python Taktikleri}} \\\\ \\vspace{1cm} {\Large Bir Öğrencinin Notları} \\\\ \\vspace{2cm} {\large Berat Dizdar} \\\\ \\vspace{1cm} 2024 \\\\ \end{center} \\thispagestyle{empty} \\tableofcontents \\newpage")
]

[os.mkdir(x) for x in build_system if not os.path.exists(x)]
[open(f, 'w', encoding="utf-8").write(content) for f, content in files_to_create if not os.path.exists(f)]

install_pandoc()
