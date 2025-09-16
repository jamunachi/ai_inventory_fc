import frappe
from ai_inventory_fc.ai_inventory.forecast import generate_forecast

def on_update(doc, method=None):
    if doc.item_code:
        qty = generate_forecast(doc.company, doc.item_code, doc.horizon_days or 14)
        frappe.msgprint(f"Predicted {qty:.2f} units for {doc.item_code}")
