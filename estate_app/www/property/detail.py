import frappe

def get_context(context):

    try:
        docname = frappe.form_dict.docname
        context.property = frappe.get_doc("Property", docname)
        context.agent = frappe.get_doc("Agent", context.property.agent)
        related_properties = frappe.db.sql(f"""
            SELECT name, property_name, status, address, property_price, 
            image FROM `tabProperty` WHERE property_type='{context.property.property_type}' 
            AND name != '{context.property.name}' ORDER BY creation DESC LIMIT 3;
            """, as_dict=True)
        context.related_properties = related_properties
    except Exception as e:
        frappe.local.flags.redirect_location = '/404'
        raise frappe.Redirect

    return context
