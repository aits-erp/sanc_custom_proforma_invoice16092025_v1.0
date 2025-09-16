frappe.ui.form.on("Sales Order", {
    refresh: function (frm) {
        if (!frm.doc.__islocal && frm.doc.docstatus === 1) {
            frm.add_custom_button(
                __("Proforma Invoice"),
                function () {
                    frappe.call({
                        method: "customproformainvoice.customproformainvoice.utils.make_proforma_invoice",   // ✅ Update with correct path
                        args: {
                            source_name: frm.doc.name,
                        },
                        callback: function (r) {
                            if (!r.exc) {
                                var doc = frappe.model.sync(r.message)[0];
                                frappe.set_route("Form", doc.doctype, doc.name);
                            }
                        },
                    });
                },
                __("Create")   // Button will appear under "Create"
            );
        }
    },
});



// frappe.ui.form.on('Sales Order', {
//     refresh: function(frm) {
//         if (!frm.is_new() && frappe.model.can_create("Proforma Invoice")) {
//             frm.add_custom_button(
//                 __("Proforma Invoice"),
//                 () => {
//                     frm.events.make_proforma_invoice(frm);
//                 },
//                 __("Create")
//             );
//         }
//     },

//     make_proforma_invoice: function(frm) {
//         frappe.model.open_mapped_doc({
//             method: "customproformainvoice.customproformainvoice.utils.make_proforma_invoice",
//             frm: frm
//         });
//     }
// });
