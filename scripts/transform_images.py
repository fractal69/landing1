from pathlib import Path
from PIL import Image, ImageOps
from pillow_heif import register_heif_opener
from tqdm import tqdm
import os

# Permite abrir archivos HEIC del iPhone
register_heif_opener()

# ==========================
# CONFIGURACIÓN
# ==========================

INPUT_DIR = Path("assets")
OUTPUT_DIR = Path("web")
THUMB_DIR = Path("thumbs")

MAX_SIZE = 1600          # lado mayor
THUMB_SIZE = 400

WEBP_QUALITY = 82
WEBP_METHOD = 6          # 0 rápido - 6 mejor compresión

SUPPORTED = {
    ".jpg",
    ".jpeg",
    ".png",
    ".heic",
    ".heif",
    ".webp"
}

OUTPUT_DIR.mkdir(exist_ok=True)
THUMB_DIR.mkdir(exist_ok=True)

# ==========================

def human(size):
    """Convierte bytes a KB/MB"""
    units = ["B", "KB", "MB", "GB"]

    i = 0
    while size >= 1024 and i < len(units)-1:
        size /= 1024
        i += 1

    return f"{size:.1f} {units[i]}"


def optimize_image(path):

    img = Image.open(path)

    # Corrige orientación del iPhone
    img = ImageOps.exif_transpose(img)

    # Elimina canal alfa si existe
    if img.mode not in ("RGB",):
        img = img.convert("RGB")

    # -----------------------------
    # Imagen principal
    # -----------------------------

    web = img.copy()

    web.thumbnail(
        (MAX_SIZE, MAX_SIZE),
        Image.Resampling.LANCZOS
    )

    outfile = OUTPUT_DIR / (path.stem.lower() + ".webp")

    web.save(
        outfile,
        "WEBP",
        quality=WEBP_QUALITY,
        method=WEBP_METHOD
    )

    # -----------------------------
    # Thumbnail
    # -----------------------------

    thumb = img.copy()

    thumb.thumbnail(
        (THUMB_SIZE, THUMB_SIZE),
        Image.Resampling.LANCZOS
    )

    thumbfile = THUMB_DIR / (path.stem.lower() + ".webp")

    thumb.save(
        thumbfile,
        "WEBP",
        quality=75,
        method=WEBP_METHOD
    )

    return (
        os.path.getsize(path),
        os.path.getsize(outfile)
    )


def main():

    files = [
        f for f in INPUT_DIR.iterdir()
        if f.suffix.lower() in SUPPORTED
    ]

    if not files:
        print("No se encontraron imágenes.")
        return

    total_original = 0
    total_new = 0

    print(f"Procesando {len(files)} imágenes...\n")

    for f in tqdm(files):

        old, new = optimize_image(f)

        total_original += old
        total_new += new

    ahorro = 100 * (1 - total_new / total_original)

    print("\n==============================")
    print("Proceso finalizado")
    print("==============================")
    print(f"Original : {human(total_original)}")
    print(f"Optimizado: {human(total_new)}")
    print(f"Ahorro   : {ahorro:.1f}%")
    print("==============================")


if __name__ == "__main__":
    main()