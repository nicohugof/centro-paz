import json
import sqlite3
import hashlib
import re
from pathlib import Path
from PIL import Image
import pytest

ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = ROOT / "docs" / "INTEGRITY_MANIFEST_PR15.json"


def sha256_file(filepath: Path) -> str:
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()


def test_integrity_manifest_and_clinical_assets():
    """Valida criptográficamente el manifiesto de integridad de los 28 contenidos y recursos."""
    assert MANIFEST_PATH.exists(), f"El manifiesto {MANIFEST_PATH} no existe."
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))

    # 1. Base de datos
    db_rel = manifest["database"]["path"]
    db_file = ROOT / db_rel
    assert db_file.exists(), f"Base de datos {db_file} no encontrada."
    assert sha256_file(db_file) == manifest["database"]["sha256"]

    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute("SELECT count(*) FROM editorial_items WHERE status != 'CLINICAL_QA'")
    assert c.fetchone()[0] == 0, "Se detectaron ítems fuera del estado CLINICAL_QA"

    c.execute("SELECT count(*) FROM editorial_items WHERE approved_by IS NOT NULL OR published_at IS NOT NULL")
    assert c.fetchone()[0] == 0, "Se detectaron aprobaciones o publicaciones clínicas no autorizadas"

    # 2. Los 28 activos gráficos PNG
    assets = manifest["assets"]
    assert len(assets) == 28, f"Se esperaban 28 activos, encontrados {len(assets)}"

    for asset in assets:
        img_file = ROOT / asset["file_path"]
        assert img_file.exists(), f"Activo PNG no encontrado: {img_file}"
        assert sha256_file(img_file) == asset["sha256"], f"Hash SHA-256 discordante para {img_file}"
        with Image.open(img_file) as im:
            assert im.format == "PNG"
            assert list(im.size) == asset["dimensions"]
            assert im.mode == asset["mode"]

    # 3. Verificación de cero inline event handlers en HTML y dashboard.py
    pattern = re.compile(r"\bon(click|input|load|submit|change|keyup|keydown)=", re.IGNORECASE)

    html_text = (ROOT / "tools" / "cpaz_media_os_dashboard.html").read_text(encoding="utf-8")
    assert len(pattern.findall(html_text)) == 0, "Se detectaron inline event handlers en tools HTML"

    py_text = (ROOT / "media_os" / "dashboard.py").read_text(encoding="utf-8")
    assert len(pattern.findall(py_text)) == 0, "Se detectaron inline event handlers en dashboard.py"
