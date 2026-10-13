#!/bin/bash
# Resume of the circulaires.club Phase 3b batch (user-approved group 3 work).
# Launched 2026-10-13 ~18:00 UTC after the first batch died ~15:02 UTC when its
# worker session ended (~2h of silence; machine restarted 16:53 UTC).
# costco was probed standalone before this (1 edition, 85 items, ~80s) and is
# excluded below. Idempotent: upsert skips existing editions.
set -u
cd /home/hatch/workspace/grocery-meta-search
PYTHONPATH=src .venv/bin/python -m grocery_meta_search.pipeline.fetch \
  --db data/grocery.db \
  --slugs euro-marche,fruiterie-valmont,frutta-si,intermarche-palumbo,l-intermarche,la-moisson,marche-axep,marche-bonanza,marche-esposito,marche-fu-tai,marche-newon,marche-sheng-tai,marches-tau,marches-tradition,mm-food-market,monde-au-naturel,odessa-poissonnier,shop-sante,t-t
echo "exit=$?"
