from pathlib import Path

ruta = "."

for i in Path(ruta).iterdir():
    print(str(i).replace(ruta.replace("/", "\\") + "\\", ""))
