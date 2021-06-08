import frappe

def get_context(context):

    try:
        docname = frappe.form_dict.docname
        context.wpaddress = frappe.get_doc("WPAddress", docname)

    except Exception as e:
        frappe.local.flags.redirect_location = '/404'
        raise frappe.Redirect

    return context
