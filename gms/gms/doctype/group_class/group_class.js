// Copyright (c) 2023, Aadith and contributors
// For license information, please see license.txt

frappe.ui.form.on('Group Class', {
    setup:function(frm){
        frm.set_query("gym_trainer", function() {
		return{
            filters:{
                "trainer_category": frm.doc.class_type
            }
        };
	});
},
refresh:function(frm){
    if(!frm.doc.member){
        frm.set_value("member",frappe.user.full_name);
    }
}
});


