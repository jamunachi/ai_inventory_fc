app_name = "ai_inventory_fc"
app_title = "AI Inventory for ERPNext (Frappe Cloud)"
app_publisher = "Your Name"
app_description = "Lightweight AI inventory & sales forecast app compatible with ERPNext and deployable on Frappe Cloud."
app_email = "you@example.com"
app_license = "MIT"
required_apps = ['erpnext']

# Fixtures (roles / workspace)
fixtures = [
  {"doctype": "Workspace", "filters": [ ["name","in",["AI Inventory"]] ] }
]

# Scheduled tasks
scheduler_events = {
  "daily": [
    "ai_inventory_fc.tasks.generate_daily_forecasts"
  ]
}

# Desk pages
website_generators = []

# DocType JavaScript (optional)
doctype_js = {
  "AI Forecast": "public/js/ai_forecast.js"
}

# After install
def after_install():
    import frappe
    frappe.logger().info("AI Inventory FC installed")
