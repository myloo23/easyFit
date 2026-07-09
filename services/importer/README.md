# easyFit Importer

Local Apple Health export inventory importer.

This milestone streams `export.xml` and produces a privacy-safe aggregate inventory. It does
not persist raw health records to SQLite.

Minimum Python version: 3.12. The implementation uses the Python standard library for
production parsing and keeps development tooling limited to pytest, ruff, and mypy.

## CLI

```bash
python -m easyfit_importer inventory --input personal-health-data/export.zip
python -m easyfit_importer inventory --input personal-health-data/apple_health_export/
```

Optionally write safe JSON to an ignored private path:

```bash
python -m easyfit_importer inventory \
  --input personal-health-data/export.zip \
  --output personal-health-data/inventory-summary.json
```
