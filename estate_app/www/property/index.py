import frappe

def get_context(context):

    properties = frappe.db.sql("""SELECT name, property_name, status, address, property_price, image FROM `tabProperty` ORDER BY creation DESC;""",
        as_dict=True)
    context.properties = properties

    return  context