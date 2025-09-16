import frappe
from .ai_inventory.forecast import generate_forecasts_for_all_companies

def generate_daily_forecasts():
    generate_forecasts_for_all_companies()
