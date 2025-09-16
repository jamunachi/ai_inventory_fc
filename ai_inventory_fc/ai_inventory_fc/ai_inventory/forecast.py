import datetime as dt
from collections import deque, defaultdict
import frappe

WINDOW = 30  # days moving window

def _date(d):
    return d.date() if hasattr(d, "date") else d

def moving_average(values, window):
    q = deque(maxlen=window)
    out = []
    for v in values:
        q.append(v)
        out.append(sum(q)/len(q))
    return out[-1] if out else 0.0

def get_item_daily_consumption(company, item_code, days=WINDOW):
    # Pull from Stock Ledger Entry or Sales Invoice Item
    since = dt.date.today() - dt.timedelta(days=days)
    rows = frappe.db.sql(
        """
        select posting_date, abs(actual_qty) as qty
        from `tabStock Ledger Entry`
        where company=%s and item_code=%s
          and posting_date >= %s and voucher_type in ('Delivery Note','Sales Invoice')
        order by posting_date
        """,
        (company, item_code, since),
        as_dict=True,
    )
    by_date = defaultdict(float)
    for r in rows:
        by_date[_date(r.posting_date)] += float(r.qty or 0)
    # fill missing dates
    series = []
    day = since
    today = dt.date.today()
    while day <= today:
        series.append(by_date.get(day, 0.0))
        day += dt.timedelta(days=1)
    return series

def generate_forecast(company, item_code, horizon_days=14):
    cons = get_item_daily_consumption(company, item_code)
    avg = moving_average(cons, WINDOW) or 0.0
    # naive forecast = moving average per day * horizon
    return avg * horizon_days

def generate_forecasts_for_all_companies():
    companies = [r.name for r in frappe.get_all("Company")]
    for company in companies:
        items = [r.name for r in frappe.get_all("Item", filters={{"is_stock_item": 1}})]
        for item in items:
            value = generate_forecast(company, item)
            doc = frappe.new_doc("AI Forecast Result")
            doc.company = company
            doc.item_code = item
            doc.horizon_days = 14
            doc.predicted_qty = value
            doc.insert(ignore_permissions=True)
    frappe.db.commit()
