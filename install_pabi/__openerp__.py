# -*- coding: utf-8 -*-
{
    "name": "NSTDA :: Install PABI2 Addons",
    "summary": "",
    "version": "8.0.1.0.0",
    "category": "Uncategorized",
    "description": """


    """,
    "website": "https://nstda.or.th/",
    "author": "Kitit U.,",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        # Technical
        'dynamic_tree_view',
        'account_anglo_saxon',
        'purchase_partial_invoicing',
        'solt_odoo_update',
        'connector',
        'base_import_async',
        'mis_builder',
        'bi_sql_editor',
        'meta_groups',
        'sql_export',
        'web_menu_collapsible',
        'web_offline_warning',
        # 'web_searchbar_full_width',  # It cause page flicking when click
        'web_sheet_full_width',
        'web_translate_dialog',
        'web_invalid_tab',
        'web_widget_pattern',
        # 'account_voucher_no_auto_lines','
        'web_x2m_defaults_from_previous',
        'web_m2x_options',
        'auditlog',
        'web_export_view',
        'web_group_expand',
        'web_hide_duplicate',
        'web_hide_toolbar',
        'web_hideleftmenu',
        'base_name_search_improved',
        'change_menu_color',
        'currency_rate_update',
        # === OU
        # 'account_budget_activity_operating_unit',
        'account_operating_unit',
        'account_voucher_operating_unit',
        'hr_expense_operating_unit',
        'operating_unit',
        'pabi_asset_management_operating_unit',
        'procurement_operating_unit',
        'purchase_billing_operating_unit',
        'purchase_operating_unit',
        'purchase_request_operating_unit',
        'purchase_request_procurement_operating_unit',
        'purchase_request_to_requisition_operating_unit',
        'purchase_requisition_operating_unit',
        'purchase_work_acceptance_operating_unit',
        'sale_invoice_plan_operating_unit',
        'sale_operating_unit',
        'sale_stock_operating_unit',
        'stock_account_operating_unit',
        'stock_operating_unit',
        'stock_request_operating_unit',
        # === Generic
        'ir_cron_time',
        'account_pettycash',
        'account_easy_reconcile',
        'account_advanced_reconcile',
        'account_period_auto_close',
        'account_auto_fy_sequence',
        'account_bank_receipt',
        'account_bank_receipt_cancel_reason',
        'account_bank_receipt_deduction',
        'account_budget_activity',
        'account_cancel_reversal',
        'account_debitnote',
        'account_invoice_cancel_reason',
        'account_invoice_overwrite_duedate',
        'account_invoice_status_history',
        'account_model_purchase_invoice_plan',
        'account_partner_tax',
        'account_refund_linked_invoice',
        'account_subscription_enhanced',
        'account_trial_balance_report',
        # 'account_voucher_deduction',
        # 'account_voucher_netpay',
        'base_document_export',
        'currency_rate_update_th',
        'document_status_history',
        'hr_expense_advance_clearing',
        'hr_expense_auto_invoice',
        'hr_expense_cancel_reason',
        'hr_expense_status_history',
        'hr_expense_value_date',
        'ir_test_action',
        'l10n_th_account',
        'l10n_th_account_deduction',
        'l10n_th_account_pit',
        'l10n_th_account_pnd_form',
        'l10n_th_account_tax_detail',
        'l10n_th_address',
        'l10n_th_amount_text',
        'l10n_th_amount_text_ext',
        'l10n_th_doctype_base',
        'l10n_th_doctype_order',
        'l10n_th_doctype_invoice',
        'l10n_th_doctype_voucher',
        'l10n_th_doctype_stock',
        'l10n_th_doctype_expense',
        'l10n_th_doctype_salary',
        'l10n_th_doctype_reversal',
        'l10n_th_doctype_bank_receipt',
        'l10n_th_fields',
        'l10n_th_thai_holidays',
        # 'l10n_th_tax_report',  # we use pabi_th_tax_report
        'language_switcher',
        'multi_lang_search',
        'payment_export',
        'payment_export_status_history',
        'payment_export_text',
        # 'purchase_cancel_reason',  # problem when use with split_quote2order
        'purchase_cash_on_delivery',
        'purchase_force_done',
        'purchase_invoice_line_percentage',
        'purchase_invoice_plan',
        'purchase_invoice_plan_retention',
        'purchase_qty_invoiced_received',
        'purchase_request_reject_reason',
        # 'purchase_request_status_history',  # ERROR on install
        'purchase_requisition_cancel_reason',
        'purchase_requisition_status_history',
        'purchase_split_quote2order',
        'purchase_split_requisition_line',
        'purchase_status_history',
        'res_currency_rate_ext',
        'res_partner_ext',
        'sale_invoice_line_percentage',
        'sale_invoice_plan',
        # 'sale_split_quote2order',  We may use it for Sales, but not now
        'stock_request',
        'stock_request_reject_reason',
        'stock_request_status_history',
        # === Base NSTDA
        'pabi_bank',
        'pabi_base',
        # 'pabi_project_member',
        'pabi_user_profile',
        'pabi_workflow',
        # === PABI
        'pabi_apps_config',
        'pabi_account',
        'pabi_account_debt_transfer',
        'pabi_account_move_document_ref',
        'pabi_account_retention',
        'pabi_account_report',
        'pabi_account_deduction_chartfield',
        'pabi_account_financial_report_webkit',
        'pabi_account_financial_report_webkit_xls',
        'pabi_account_move_validator',
        'pabi_advance_dunning_letter',
        'pabi_ar_late_payment_penalty',
        'pabi_attachment_helper',
        'pabi_budget_fund_rule',
        'pabi_budget_interface',
        'pabi_budget_internal_charge',
        'pabi_budget_monitor',
        'pabi_budget_plan',
        'pabi_budget_plan_monitor',
        'pabi_budget_yearend_process',
        'pabi_budget_transfer',
        'pabi_bank_statement_reconcile',
        # 'pabi_budget_xls', # kittiu: Don't install, just keep for reference
        'pabi_chartfield',
        'pabi_chartfield_merged',
        'pabi_forms',
        'pabi_pos',
        'pabi_hr_expense',
        'pabi_hr_advance_status_report',
        'pabi_hr_advance_clearing_followup_report',
        'pabi_hr_expense_interface',
        'pabi_hr_salary',
        'pabi_interface',
        'pabi_invest_construction',
        'pabi_my_project',
        # 'pabi_name_search',  # Temp removed, it can't be installed
        'pabi_loan_receivable',
        'pabi_loan_installment',
        'pabi_operating_unit_ext',
        'pabi_partner_dunning_report',
        'pabi_procurement',
        'pabi_project_bank_check',
        'pabi_purchase_billing',
        'pabi_purchase_contract',
        'pabi_purchase_invoice_plan',
        'pabi_purchase_report',
        'pabi_purchase_work_acceptance',
        'pabi_receivable_type',
        'pabi_source_document',
        'pabi_asset_management',
        # 'pabi_stock_request',  <-- Eyu don't remember, it conflict with other
        'pabi_stock_request_url',
        'pabi_sale_invoice_plan',
        'pabi_th_doctype',
        'pabi_th_tax_report',
        'pabi_track_change',
        'pabi_web_config',
        # ================= BASE MODULES ===================
        # Functional
        'account_financial_report',
        # 'account_financial_report_webkit',
        # 'account_financial_report_webkit_xls',
        'account_journal_report_xls',
        'account_invoice_supplier_number_info',
        'account_payment_term_multi_day',
        'stock_transfer_only_available',
    ],
}
