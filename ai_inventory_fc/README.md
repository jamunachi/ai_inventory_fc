# AI Inventory for ERPNext (Frappe Cloud)

A minimal, Frappe-app-compatible reimplementation of AI inventory forecasting that works on ERPNext and installs cleanly on Frappe Cloud.

## Features
- DocTypes: AI Forecast, AI Forecast Result, AI Forecast Sync Log.
- Lightweight moving-average forecast (no heavy ML deps).
- Background job to generate forecasts from Stock Ledger / Sales Invoice Items.
- ERPNext dependency declared in `app.json` (`required_apps`: ['erpnext']).

## Install (bench / Frappe Cloud)
```bash
# bench
bench get-app https://your.repo/ai_inventory_fc.git
bench --site your.site install-app ai_inventory_fc
```

On Frappe Cloud: create a new site/app from this repo; ensures Python 3.10+ and ERPNext v15.
