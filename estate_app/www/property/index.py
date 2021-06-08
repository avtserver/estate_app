import frappe

def get_context(context):

    properties = frappe.db.sql("""SELECT name, property_name, status, address, property_price, image FROM `tabProperty` ORDER BY creation DESC;""",
        as_dict=True)
    context.properties = properties

    wpadds = frappe.db.sql("""SELECT name, address, city, pin_code FROM `tabWPAddress` ORDER BY creation DESC;""",
                               as_dict=True)
    context.wpadds = wpadds
    return  context