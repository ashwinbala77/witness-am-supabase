# Field Mapping Review — Airtable → Supabase

_Auto-generated. One row per **stored** field; computed fields are listed in `03-calculated-fields-todo.md`._

**Conventions:** every table keyed by `airtable_id` (text). Links stored as `text[]` of Airtable record IDs. Selects stored as `text`/`text[]` (not enums). Numbers use unconstrained `numeric` to avoid sync rounding. Each table gets `_synced_at`.

## `airtable.investments`  (Investments)
_106 stored columns · 151 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Investments_id | singleLineText | investments_id | text |
| Associated_asset_number | singleLineText | associated_asset_number | text |
| Investing_entity_owner | singleLineText | investing_entity_owner | text |
| Investment_status | singleSelect | investment_status | text |
| Asset_class | singleSelect | asset_class | text |
| Asset_subclass | singleSelect | asset_subclass | text |
| Reporting_category | multipleSelects | reporting_category | text[] |
| Appfolio | singleSelect | appfolio | text |
| Total_committed | currency | total_committed | numeric |
| Total_contributed | currency | total_contributed | numeric |
| Total_distributed | currency | total_distributed | numeric |
| Investments_market_value_link | multipleRecordLinks | investments_market_value_link | text[] |
| Asset_detail_link | multipleRecordLinks | asset_detail_link | text[] |
| Cash_accounts_link | multipleRecordLinks | cash_accounts_link | text[] |
| Cash_balance_input_link | multipleRecordLinks | cash_balance_input_link | text[] |
| Loan_summary_data_link | multipleRecordLinks | loan_summary_data_link | text[] |
| Loan_balance_input_link | multipleRecordLinks | loan_balance_input_link | text[] |
| Target_operating_balance | currency | target_operating_balance | numeric |
| Target_reserve_balance | currency | target_reserve_balance | numeric |
| Hotel_actuals_link | multipleRecordLinks | hotel_actuals_link | text[] |
| Hotel_budget_link | multipleRecordLinks | hotel_budget_link | text[] |
| Sale_price | currency | sale_price | numeric |
| Selling_expense | currency | selling_expense | numeric |
| ST_capital_gain | currency | st_capital_gain | numeric |
| LT_capital_gain | currency | lt_capital_gain | numeric |
| Tax_cost | currency | tax_cost | numeric |
| 2022_depreciation | currency | n_2022_depreciation | numeric |
| 2022_tax_end_depreciation | currency | n_2022_tax_end_depreciation | numeric |
| 2023_depreciation | currency | n_2023_depreciation | numeric |
| 2023_tax_end_depr. | currency | n_2023_tax_end_depr | numeric |
| 2023_tax_net_book_val. | currency | n_2023_tax_net_book_val | numeric |
| 2024_depreciation | currency | n_2024_depreciation | numeric |
| 2024_tax_end_depr. | currency | n_2024_tax_end_depr | numeric |
| 2024_tax_net_book_val. | currency | n_2024_tax_net_book_val | numeric |
| Recapitalization_comment | singleLineText | recapitalization_comment | text |
| Debt_resizing_link | multipleRecordLinks | debt_resizing_link | text[] |
| 2025_depreciation | currency | n_2025_depreciation | numeric |
| 2026_depreciation | currency | n_2026_depreciation | numeric |
| 2027_depreciation | currency | n_2027_depreciation | numeric |
| 2028_depreciation | currency | n_2028_depreciation | numeric |
| 2029_depreciation | currency | n_2029_depreciation | numeric |
| 2024_acquisition_bonus_depreciation | currency | n_2024_acquisition_bonus_depreciation | numeric |
| 2024_ST_capital_gains | currency | n_2024_st_capital_gains | numeric |
| 2024_LT_capital_gains | currency | n_2024_lt_capital_gains | numeric |
| 2024_PIP_depreciation | currency | n_2024_pip_depreciation | numeric |
| 2024_new_build_depreciation | currency | n_2024_new_build_depreciation | numeric |
| 2024_capex | currency | n_2024_capex | numeric |
| 2024_BS_construction_in_process_acct | currency | n_2024_bs_construction_in_process_acct | numeric |
| 2023_taxable_income | currency | n_2023_taxable_income | numeric |
| 2023_interest_expense | currency | n_2023_interest_expense | numeric |
| Quarterly_hotel_actuals_link | multipleRecordLinks | quarterly_hotel_actuals_link | text[] |
| Quarter_loan_paydown_manual_adj | currency | quarter_loan_paydown_manual_adj | numeric |
| 2025_capex | currency | n_2025_capex | numeric |
| 2025_acquisition_bonus_depreciation | currency | n_2025_acquisition_bonus_depreciation | numeric |
| 2025_ST_capital_gains | currency | n_2025_st_capital_gains | numeric |
| 2025_LT_capital_gains | currency | n_2025_lt_capital_gains | numeric |
| 2025_PIP_depreciation | currency | n_2025_pip_depreciation | numeric |
| 2025_new_build_depreciation | currency | n_2025_new_build_depreciation | numeric |
| Divestiture_target | singleSelect | divestiture_target | text |
| Target_exit_value | currency | target_exit_value | numeric |
| Hotel_QA_data_link | multipleRecordLinks | hotel_qa_data_link | text[] |
| Hotel_GSS_data_link | multipleRecordLinks | hotel_gss_data_link | text[] |
| YE24_TR_interest_expense | currency | ye24_tr_interest_expense | numeric |
| YE24_TR_depreciation_expense | currency | ye24_tr_depreciation_expense | numeric |
| YE24_TR_NOI | currency | ye24_tr_noi | numeric |
| YE23_TR_NOI | currency | ye23_tr_noi | numeric |
| YE23_TR_depreciation_expense | currency | ye23_tr_depreciation_expense | numeric |
| Hotel_forecast_link | multipleRecordLinks | hotel_forecast_link | text[] |
| Witness_forecast_link | multipleRecordLinks | witness_forecast_link | text[] |
| Key_money | currency | key_money | numeric |
| Cash_account_target_comment | singleLineText | cash_account_target_comment | text |
| 2030_depreciation | currency | n_2030_depreciation | numeric |
| 2035_depreciation | currency | n_2035_depreciation | numeric |
| 2034_depreciation | currency | n_2034_depreciation | numeric |
| 2033_depreciation | currency | n_2033_depreciation | numeric |
| 2032_depreciation | currency | n_2032_depreciation | numeric |
| 2031_depreciation | currency | n_2031_depreciation | numeric |
| Accounting | singleSelect | accounting | text |
| Investment_positions_link | multipleRecordLinks | investment_positions_link | text[] |
| 2026_estimated_distributions | currency | n_2026_estimated_distributions | numeric |
| 2026_capex | currency | n_2026_capex | numeric |
| 2026_acquisition_bonus_depreciation | currency | n_2026_acquisition_bonus_depreciation | numeric |
| 2026_ST_capital_gains | currency | n_2026_st_capital_gains | numeric |
| 2026_LT_capital_gains | currency | n_2026_lt_capital_gains | numeric |
| 2026_PIP_depreciation | currency | n_2026_pip_depreciation | numeric |
| 2026_new_build_depreciation | currency | n_2026_new_build_depreciation | numeric |
| Balance_sheet | multipleRecordLinks | balance_sheet | text[] |
| Distributions | multipleRecordLinks | distributions | text[] |
| AM_estimated_sale_range | singleLineText | am_estimated_sale_range | text |
| Target_exit cap_rate | percent | target_exit_cap_rate | numeric |
| Divestiture_comment | singleLineText | divestiture_comment | text |
| Google_maps_link | url | google_maps_link | text |
| Property_tax_record_site | url | property_tax_record_site | text |
| Target_start | singleLineText | target_start | text |
| Parcel_number | singleLineText | parcel_number | text |
| County | singleSelect | county | text |
| RE_tax_ACH_status | singleLineText | re_tax_ach_status | text |
| RE_tax_1st_half_due_date | singleLineText | re_tax_1st_half_due_date | text |
| RE_tax_2nd_half_due_date | singleLineText | re_tax_2nd_half_due_date | text |
| RE_tax_county_link | singleLineText | re_tax_county_link | text |
| Cash_balance_input copy | singleLineText | cash_balance_input_copy | text |
| Equity_contributed | currency | equity_contributed | numeric |
| RE_tax_amount | currency | re_tax_amount | numeric |
| Hotel_PIP_history | multipleRecordLinks | hotel_pip_history | text[] |
| Hotel_GSS_data_v2 | singleLineText | hotel_gss_data_v2 | text |
| Hotel_GSS_data_v2 (2) | multipleRecordLinks | hotel_gss_data_v2_2 | text[] |

## `airtable.asset_detail`  (Asset_detail)
_114 stored columns · 97 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Internal_asset_name | singleLineText | internal_asset_name | text |
| Investments_link | multipleRecordLinks | investments_link | text[] |
| Transaction_type | singleSelect | transaction_type | text |
| Room_count | number | room_count | numeric |
| Year_built | number | year_built | numeric |
| Acquired_date | date | acquired_date | date |
| Address | multilineText | address | text |
| Zip | number | zip | numeric |
| Purchase_price | currency | purchase_price | numeric |
| Asset_manager | singleLineText | asset_manager | text |
| Asset_number | singleLineText | asset_number | text |
| Management_company | singleSelect | management_company | text |
| City | singleSelect | city | text |
| State | singleSelect | state | text |
| Hotel_brand_metrics_link | multipleRecordLinks | hotel_brand_metrics_link | text[] |
| STR_hotel_name | multilineText | str_hotel_name | text |
| Profitsword_hotel_name | singleLineText | profitsword_hotel_name | text |
| STR_code | number | str_code | numeric |
| Brand_property_code | multilineText | brand_property_code | text |
| Hotel_website | multilineText | hotel_website | text |
| Franchise_expiration | date | franchise_expiration | date |
| Open_date | date | open_date | date |
| PIP_brand_renovation_due_date | date | pip_brand_renovation_due_date | date |
| Est_PIP_cost_per_key | currency | est_pip_cost_per_key | numeric |
| Number_of_stories | singleSelect | number_of_stories | text |
| Singles | number | singles | numeric |
| Double | number | double | numeric |
| Suites | number | suites | numeric |
| Sq_footage | number | sq_footage | numeric |
| Fitness_sq_footage | number | fitness_sq_footage | numeric |
| Meeting_room_details | multilineText | meeting_room_details | text |
| Hotel_actuals_link | multipleRecordLinks | hotel_actuals_link | text[] |
| Hotel_budget_link | multipleRecordLinks | hotel_budget_link | text[] |
| Sale_price | currency | sale_price | numeric |
| Hotel_anonymous_reference | singleLineText | hotel_anonymous_reference | text |
| Sale_date | date | sale_date | date |
| PIP_overview | singleLineText | pip_overview | text |
| Market | singleSelect | market | text |
| Director_of_sales | singleLineText | director_of_sales | text |
| DOS_hire_date | date | dos_hire_date | date |
| General_manager | singleLineText | general_manager | text |
| GM_hire_date | date | gm_hire_date | date |
| Sales_manager | singleLineText | sales_manager | text |
| SM_hire_date | date | sm_hire_date | date |
| Quarterly_hotel_actuals_link | multipleRecordLinks | quarterly_hotel_actuals_link | text[] |
| Budgeted_strategy | multipleSelects | budgeted_strategy | text[] |
| STR_weekly_data_link | multipleRecordLinks | str_weekly_data_link | text[] |
| Hotel_QA_data_link | multipleRecordLinks | hotel_qa_data_link | text[] |
| Hotel_GSS_data_link | multipleRecordLinks | hotel_gss_data_link | text[] |
| Renovation_internal_target_end_date | date | renovation_internal_target_end_date | date |
| PIP_requirements_link | url | pip_requirements_link | text |
| PIP_owner_approval_status | singleSelect | pip_owner_approval_status | text |
| PIP_construction_vendor | singleSelect | pip_construction_vendor | text |
| Construction_start_date | date | construction_start_date | date |
| Renovation_plan_start_manual_target | date | renovation_plan_start_manual_target | date |
| PIP_comments | singleLineText | pip_comments | text |
| PIP_design_vendor | singleSelect | pip_design_vendor | text |
| PIP_budget_link | url | pip_budget_link | text |
| PIP_deposit_estimate | currency | pip_deposit_estimate | numeric |
| PIP_estimated_deposit_date | date | pip_estimated_deposit_date | date |
| PIP_procurement_vendor | singleSelect | pip_procurement_vendor | text |
| PIP_funding_secured | singleSelect | pip_funding_secured | text |
| PIP_owner_contact | singleSelect | pip_owner_contact | text |
| PIP_design_approver | singleSelect | pip_design_approver | text |
| PIP_scope | multipleSelects | pip_scope | text[] |
| PIP_design_review_status | singleSelect | pip_design_review_status | text |
| PIP_owner_rep_contact | singleSelect | pip_owner_rep_contact | text |
| Hotel_forecast_link | multipleRecordLinks | hotel_forecast_link | text[] |
| Inn_code | singleLineText | inn_code | text |
| Year_end_financials_link | multipleRecordLinks | year_end_financials_link | text[] |
| Full_hotel_comp_landscape_link | multipleRecordLinks | full_hotel_comp_landscape_link | text[] |
| STR_daily_data_link | multipleRecordLinks | str_daily_data_link | text[] |
| STR_comp_set_link | multipleRecordLinks | str_comp_set_link | text[] |
| STR_actuals_link | multipleRecordLinks | str_actuals_link | text[] |
| Comp_set_room_count | number | comp_set_room_count | numeric |
| STR_budget_link | multipleRecordLinks | str_budget_link | text[] |
| Hotel_segmentation_link | multipleRecordLinks | hotel_segmentation_link | text[] |
| PIP_funding_strategy | singleSelect | pip_funding_strategy | text |
| Witness_forecast_link | multipleRecordLinks | witness_forecast_link | text[] |
| GM_outlook | singleSelect | gm_outlook | text |
| 2026_Witness_target_NOI | currency | n_2026_witness_target_noi | numeric |
| 2027_Witness_target_NOI | currency | n_2027_witness_target_noi | numeric |
| 2028_Witness_target_NOI | currency | n_2028_witness_target_noi | numeric |
| 2029_Witness_target_NOI | currency | n_2029_witness_target_noi | numeric |
| 2030_Witness_target_NOI | currency | n_2030_witness_target_noi | numeric |
| 2026_Witness_target_operating_revenue | currency | n_2026_witness_target_operating_revenue | numeric |
| 2027_Witness_target_operating_revenue | currency | n_2027_witness_target_operating_revenue | numeric |
| 2028_Witness_target_operating_revenue | currency | n_2028_witness_target_operating_revenue | numeric |
| 2029_Witness_target_operating_revenue | currency | n_2029_witness_target_operating_revenue | numeric |
| 2030_Witness_target_operating_revenue | currency | n_2030_witness_target_operating_revenue | numeric |
| M3_hotel_naming | singleLineText | m3_hotel_naming | text |
| Lighthouse_hotel_naming | singleLineText | lighthouse_hotel_naming | text |
| STR_28_day_trend_link | multipleRecordLinks | str_28_day_trend_link | text[] |
| Hotel_health | singleLineText | hotel_health | text |
| DOS_outlook | singleSelect | dos_outlook | text |
| F&B_outlet_details | multilineText | f_b_outlet_details | text |
| Hotel_CapEx_link | multipleRecordLinks | hotel_capex_link | text[] |
| Clickup_task_id | singleLineText | clickup_task_id | text |
| Hotel_CapEx_Budget | multipleRecordLinks | hotel_capex_budget | text[] |
| Balance_sheet | multipleRecordLinks | balance_sheet | text[] |
| Health_primary_driver | singleLineText | health_primary_driver | text |
| Health_trajectory | singleLineText | health_trajectory | text |
| Health_secondary_driver | singleLineText | health_secondary_driver | text |
| PIP Authorization Req'd By | date | pip_authorization_req_d_by | date |
| Key_focus | singleLineText | key_focus | text |
| People | singleSelect | people | text |
| Prop_leadership | singleLineText | prop_leadership | text |
| Select | singleSelect | select | text |
| Hotel_onthebooks | multipleRecordLinks | hotel_onthebooks | text[] |
| Aquisition_cost | currency | aquisition_cost | numeric |
| Hotel_PIP_history | multipleRecordLinks | hotel_pip_history | text[] |
| Cash_flow_tracking | multipleRecordLinks | cash_flow_tracking | text[] |
| Hotel_GSS_data_v2 | singleLineText | hotel_gss_data_v2 | text |
| Hotel_GSS_data_v2 (2) | multipleRecordLinks | hotel_gss_data_v2_2 | text[] |

## `airtable.investments_market_value`  (Investments_market_value)
_8 stored columns · 35 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Investments_link | multipleRecordLinks | investments_link | text[] |
| Date | date | date | date |
| Market_value | currency | market_value | numeric |
| Valuation_method | singleSelect | valuation_method | text |
| Cap_rate | percent | cap_rate | numeric |
| Cap_rate_date | date | cap_rate_date | date |
| Appfolio_value | currency | appfolio_value | numeric |
| Valuation_note | singleLineText | valuation_note | text |

## `airtable.investing_entities`  (Investing_entities)
_6 stored columns · 0 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Investing_entities_id | singleLineText | investing_entities_id | text |
| Primary_contact | singleLineText | primary_contact | text |
| Email | singleLineText | email | text |
| Reporting_category_breakdown | singleSelect | reporting_category_breakdown | text |
| Investment_positions_link | multipleRecordLinks | investment_positions_link | text[] |
| Distributions_link | multipleRecordLinks | distributions_link | text[] |

## `airtable.investment_positions`  (Investment_positions)
_13 stored columns · 27 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Investments_link | multipleRecordLinks | investments_link | text[] |
| Investment_id | singleLineText | investment_id | text |
| Investing_entities_link | multipleRecordLinks | investing_entities_link | text[] |
| L1_ownership_percentage | percent | l1_ownership_percentage | numeric |
| Committed | currency | committed | numeric |
| Contributed | currency | contributed | numeric |
| Distributions | currency | distributions | numeric |
| Distributions_link | multipleRecordLinks | distributions_link | text[] |
| Position_update_notes | singleLineText | position_update_notes | text |
| L2_ownership_link | multipleRecordLinks | l2_ownership_link | text[] |
| From field: L2_ownership_link | multipleRecordLinks | from_field_l2_ownership_link | text[] |
| L3_ownership_link | multipleRecordLinks | l3_ownership_link | text[] |
| From field: L3_ownership_link | multipleRecordLinks | from_field_l3_ownership_link | text[] |

## `airtable.distributions`  (Distributions)
_11 stored columns · 13 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Investment_positions_link | multipleRecordLinks | investment_positions_link | text[] |
| Date | date | date | date |
| Effective Date | date | effective_date | date |
| Period | singleLineText | period | text |
| Investments_link | multipleRecordLinks | investments_link | text[] |
| Investing_entities_link | multipleRecordLinks | investing_entities_link | text[] |
| Description | singleLineText | description | text |
| Source | singleSelect | source | text |
| Type | singleSelect | type | text |
| Amount | currency | amount | numeric |
| Modification_notes | singleLineText | modification_notes | text |

## `airtable.cash_accounts`  (Cash_accounts)
_25 stored columns · 37 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Lenders_link | multipleRecordLinks | lenders_link | text[] |
| Account_last_four | singleLineText | account_last_four | text |
| Operating_last_four | singleLineText | operating_last_four | text |
| Reserve_last_four | singleLineText | reserve_last_four | text |
| Addepar_cash_report_status | singleSelect | addepar_cash_report_status | text |
| Investments_link | multipleRecordLinks | investments_link | text[] |
| Chase_account_naming | singleLineText | chase_account_naming | text |
| Account_status | singleSelect | account_status | text |
| Cash_account_subclass | singleSelect | cash_account_subclass | text |
| Cash_balance_input_link | multipleRecordLinks | cash_balance_input_link | text[] |
| Cash_account_subclass_comments | singleLineText | cash_account_subclass_comments | text |
| Cresset_asset_position_ID | singleLineText | cresset_asset_position_id | text |
| Ivy_reviewed | checkbox | ivy_reviewed | boolean |
| Ivy_comments | singleLineText | ivy_comments | text |
| Transfer_completed | checkbox | transfer_completed | boolean |
| Transfer_comments | singleLineText | transfer_comments | text |
| Owner_comment | multilineText | owner_comment | text |
| JPM_email | checkbox | jpm_email | boolean |
| Bank_login_access | singleSelect | bank_login_access | text |
| Cash_balance_input copy | singleLineText | cash_balance_input_copy | text |
| Bank_interest_rate | percent | bank_interest_rate | numeric |
| Interest_rate_last_updated | date | interest_rate_last_updated | date |
| Cash_flow_2026 | singleLineText | cash_flow_2026 | text |
| Cash_flow_2026 copy | singleLineText | cash_flow_2026_copy | text |
| Recommendation  | singleSelect | recommendation | text |

## `airtable.cash_balance_input`  (Cash_balance_input)
_5 stored columns · 14 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Cash_accounts_link | multipleRecordLinks | cash_accounts_link | text[] |
| Investments_link | multipleRecordLinks | investments_link | text[] |
| Date | date | date | date |
| Balance | currency | balance | numeric |
| Data_source | singleSelect | data_source | text |

## `airtable.loan_summary_data`  (Loan_summary_data)
_70 stored columns · 29 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Interest_rate | number | interest_rate | numeric |
| Field 95 | singleLineText | field_95 | text |
| Monthly_debt_payment | currency | monthly_debt_payment | numeric |
| Monthly_debt_payment_date | number | monthly_debt_payment_date | numeric |
| Investments_link | multipleRecordLinks | investments_link | text[] |
| Loan_type | singleSelect | loan_type | text |
| Loan_status | singleSelect | loan_status | text |
| Lenders_link | multipleRecordLinks | lenders_link | text[] |
| Lender_location_city | singleLineText | lender_location_city | text |
| Lender_location_state | singleSelect | lender_location_state | text |
| Lead_contact | singleSelect | lead_contact | text |
| Lead_email | singleSelect | lead_email | text |
| Loan_origination_date | date | loan_origination_date | date |
| Initial_principal | currency | initial_principal | numeric |
| Loan_term | multilineText | loan_term | text |
| Loan_maturity | date | loan_maturity | date |
| Interest_rate_comment | singleLineText | interest_rate_comment | text |
| Interest_rate_fix_variable | singleSelect | interest_rate_fix_variable | text |
| Interest_rate_reset_comment | multilineText | interest_rate_reset_comment | text |
| Interest_rate_reset_date | date | interest_rate_reset_date | date |
| Amortization_months | singleLineText | amortization_months | text |
| Amortization_statement | singleSelect | amortization_statement | text |
| Original_monthly_payment | currency | original_monthly_payment | numeric |
| Pre_payment_penalty | checkbox | pre_payment_penalty | boolean |
| Pre_payment_detail | singleLineText | pre_payment_detail | text |
| Pre_payment_exclusion | singleLineText | pre_payment_exclusion | text |
| Pre_payment_end_date | date | pre_payment_end_date | date |
| DSCR_covenant | number | dscr_covenant | numeric |
| Debt_yield_covenant | percent | debt_yield_covenant | numeric |
| Covenant_testing_method | singleSelect | covenant_testing_method | text |
| Covenant_testing_timing | singleSelect | covenant_testing_timing | text |
| Debt_recourse | singleSelect | debt_recourse | text |
| Required_deposit_relationship | singleSelect | required_deposit_relationship | text |
| Guarantee_structure | singleSelect | guarantee_structure | text |
| Guarantors | multilineText | guarantors | text |
| PACE_comment | singleLineText | pace_comment | text |
| Loan_balance_input_link | multipleRecordLinks | loan_balance_input_link | text[] |
| YE22_est_interest_expense | currency | ye22_est_interest_expense | numeric |
| YE23_est_interest_expense | currency | ye23_est_interest_expense | numeric |
| YE24_est_interest_expense | currency | ye24_est_interest_expense | numeric |
| YE25_est_interest_expense | currency | ye25_est_interest_expense | numeric |
| YE26_est_interest_expense | currency | ye26_est_interest_expense | numeric |
| YE27_est_interest_expense | currency | ye27_est_interest_expense | numeric |
| YE28_est_interest_expense | currency | ye28_est_interest_expense | numeric |
| YE29_est_interest_expense | currency | ye29_est_interest_expense | numeric |
| YE30_est_interest_expense | currency | ye30_est_interest_expense | numeric |
| YE31_est_interest_expense | currency | ye31_est_interest_expense | numeric |
| YE32_est_interest_expense | currency | ye32_est_interest_expense | numeric |
| YE33_est_interest_expense | currency | ye33_est_interest_expense | numeric |
| YE34_est_interest_expense | currency | ye34_est_interest_expense | numeric |
| YE35_est_interest_expense | currency | ye35_est_interest_expense | numeric |
| Loan_balance_at_maturity | currency | loan_balance_at_maturity | numeric |
| Participating_banks | multipleSelects | participating_banks | text[] |
| Participating_banks_notes | multilineText | participating_banks_notes | text |
| Guarantor_Compliance | multipleRecordLinks | guarantor_compliance | text[] |
| P&L_Frequency | singleSelect | p_l_frequency | text |
| BS_Frequency | singleSelect | bs_frequency | text |
| TR_Frequency | singleSelect | tr_frequency | text |
| Compliance_certificate_Frequency | singleSelect | compliance_certificate_frequency | text |
| STR_Frequency | singleSelect | str_frequency | text |
| Compliance_comments | singleLineText | compliance_comments | text |
| DSCR_Data_basis | multipleSelects | dscr_data_basis | text[] |
| DSCR_calculation_measure | multilineText | dscr_calculation_measure | text |
| Lender_reserve_required | checkbox | lender_reserve_required | boolean |
| Loan_action | singleSelect | loan_action | text |
| Bank_login_access | singleSelect | bank_login_access | text |
| Asset_detail | singleLineText | asset_detail | text |
| Payment_type | singleSelect | payment_type | text |
| Payment_type_comment | singleLineText | payment_type_comment | text |
| DSCR_covenant_comment | singleLineText | dscr_covenant_comment | text |

## `airtable.loan_balance_input`  (Loan_balance_input)
_4 stored columns · 8 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Loan_summary_data_link | multipleRecordLinks | loan_summary_data_link | text[] |
| Investments_link | multipleRecordLinks | investments_link | text[] |
| Date | date | date | date |
| Debt_balance | currency | debt_balance | numeric |

## `airtable.short_term_loans`  (Short_term_loans)
_29 stored columns · 4 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Loan Status | singleSelect | loan_status | text |
| Estate Planning Unit | singleSelect | estate_planning_unit | text |
| Asset Owner | singleSelect | asset_owner | text |
| Taxable Status | singleSelect | taxable_status | text |
| Investment Category | singleSelect | investment_category | text |
| Lender (Business) | singleSelect | lender_business | text |
| Lender (Individual) | singleSelect | lender_individual | text |
| Borrower | singleSelect | borrower | text |
| Cresset_asset_position_id | singleLineText | cresset_asset_position_id | text |
| Loan Start Date | date | loan_start_date | date |
| Loan Target End Date | date | loan_target_end_date | date |
| Loan End Date | date | loan_end_date | date |
| Original Principal Balance | currency | original_principal_balance | numeric |
| Current Loan Balance | currency | current_loan_balance | numeric |
| Interest % | percent | interest | numeric |
| Interest Rate Comment | singleLineText | interest_rate_comment | text |
| Purpose | singleLineText | purpose | text |
| Due from Source | singleSelect | due_from_source | text |
| Notes | multilineText | notes | text |
| Comments | singleLineText | comments | text |
| Payment Frequency | singleSelect | payment_frequency | text |
| Payment Method | singleSelect | payment_method | text |
| Promissory Note | multipleAttachments | promissory_note | jsonb |
| Promissory Note Completed | singleSelect | promissory_note_completed | text |
| Interest Accrued | currency | interest_accrued | numeric |
| Final Interest Owed | currency | final_interest_owed | numeric |
| Update Data Source | singleSelect | update_data_source | text |
| Review? | multilineText | review | text |
| Attachment | multipleAttachments | attachment | jsonb |

## `airtable.hotel_budget`  (Hotel_budget)
_58 stored columns · 23 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Asset_detail_link | multipleRecordLinks | asset_detail_link | text[] |
| Investments_link | multipleRecordLinks | investments_link | text[] |
| Date | date | date | date |
| Available_rooms | number | available_rooms | numeric |
| Occupied_rooms | number | occupied_rooms | numeric |
|  ADR  | currency | adr | numeric |
| RevPAR | currency | revpar | numeric |
| Rooms_sales | currency | rooms_sales | numeric |
| Food_and_beverage_sales | currency | food_and_beverage_sales | numeric |
| Minor_operated_department_sales | currency | minor_operated_department_sales | numeric |
| Miscellaneous_income_sales | currency | miscellaneous_income_sales | numeric |
| Total_operating_revenue | currency | total_operating_revenue | numeric |
| Rooms_expense | currency | rooms_expense | numeric |
| Food_and_beverage_expense | currency | food_and_beverage_expense | numeric |
| Minor_operated_department_expense | currency | minor_operated_department_expense | numeric |
| Total_departmental_expenses | currency | total_departmental_expenses | numeric |
| Total_department_profit | currency | total_department_profit | numeric |
| Administrative_and_general | currency | administrative_and_general | numeric |
| Information_and_telecommunication_systems | currency | information_and_telecommunication_systems | numeric |
| Sales_and_marketing | currency | sales_and_marketing | numeric |
| Adj_sales_and_marketing | currency | adj_sales_and_marketing | numeric |
| Repair_and_maintenance | currency | repair_and_maintenance | numeric |
| Utilities | currency | utilities | numeric |
| Total_undistributed_expenses | currency | total_undistributed_expenses | numeric |
| House_profit | currency | house_profit | numeric |
| Management_fees | currency | management_fees | numeric |
| Centralized_accounting_charges | currency | centralized_accounting_charges | numeric |
| Franchise_fees_royalties | currency | franchise_fees_royalties | numeric |
| Gross_operating_profit | currency | gross_operating_profit | numeric |
| Rent | currency | rent | numeric |
| Property_and_other_taxes | currency | property_and_other_taxes | numeric |
| Property_and_liability_insurance | currency | property_and_liability_insurance | numeric |
| Other_non_operating_expenses | currency | other_non_operating_expenses | numeric |
| Total_non_operating_income_and_expenses | currency | total_non_operating_income_and_expenses | numeric |
| Replacement_reserve | currency | replacement_reserve | numeric |
| EBITDA_NOI | currency | ebitda_noi | numeric |
| Interest_expense | currency | interest_expense | numeric |
| Amortization_expense | currency | amortization_expense | numeric |
| Total_interest_depreciation_and_amortization | currency | total_interest_depreciation_and_amortization | numeric |
| Net_income | currency | net_income | numeric |
| Total_extraordinary_expenditures | currency | total_extraordinary_expenditures | numeric |
| Capital_expenditures | currency | capital_expenditures | numeric |
| Prior_year_expenses | currency | prior_year_expenses | numeric |
| Extraordinary_expense_misc_income_non_taxable | currency | extraordinary_expense_misc_income_non_taxable | numeric |
| Total_extraordinary_items | currency | total_extraordinary_items | numeric |
| Net_income_less_extraordinary_items | currency | net_income_less_extraordinary_items | numeric |
| Out_of_order_rooms | number | out_of_order_rooms | numeric |
| Complimentary_rooms | number | complimentary_rooms | numeric |
| Full_year_total_operating_revenue | currency | full_year_total_operating_revenue | numeric |
| Prior_year_total_operating_revenue | currency | prior_year_total_operating_revenue | numeric |
| Full_year_total_GOP | currency | full_year_total_gop | numeric |
| Prior_year_total_GOP | currency | prior_year_total_gop | numeric |
| Full_year_total_NOI | currency | full_year_total_noi | numeric |
| Prior_year_total_NOI | currency | prior_year_total_noi | numeric |
| Hotel_actuals | multipleRecordLinks | hotel_actuals | text[] |
| Debt_payment_input | currency | debt_payment_input | numeric |
| Asset_detail copy | singleLineText | asset_detail_copy | text |
| Asset_detail copy 2 | singleLineText | asset_detail_copy_2 | text |

## `airtable.witness_am_forecast`  (Witness_AM_forecast)
_56 stored columns · 21 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Asset_detail_link | multipleRecordLinks | asset_detail_link | text[] |
| Investments_link | multipleRecordLinks | investments_link | text[] |
| Date | date | date | date |
| Available_rooms | number | available_rooms | numeric |
| Occupied_rooms | number | occupied_rooms | numeric |
|  ADR  | currency | adr | numeric |
| RevPAR | currency | revpar | numeric |
| Rooms_sales | currency | rooms_sales | numeric |
| Food_and_beverage_sales | currency | food_and_beverage_sales | numeric |
| Minor_operated_department_sales | currency | minor_operated_department_sales | numeric |
| Miscellaneous_income_sales | currency | miscellaneous_income_sales | numeric |
| Total_operating_revenue | currency | total_operating_revenue | numeric |
| Rooms_expense | currency | rooms_expense | numeric |
| Food_and_beverage_expense | currency | food_and_beverage_expense | numeric |
| Minor_operated_department_expense | currency | minor_operated_department_expense | numeric |
| Total_departmental_expenses | currency | total_departmental_expenses | numeric |
| Total_department_profit | currency | total_department_profit | numeric |
| Administrative_and_general | currency | administrative_and_general | numeric |
| Information_and_telecommunication_systems | currency | information_and_telecommunication_systems | numeric |
| Sales_and_marketing | currency | sales_and_marketing | numeric |
| Adj_sales_and_marketing | currency | adj_sales_and_marketing | numeric |
| Repair_and_maintenance | currency | repair_and_maintenance | numeric |
| Utilities | currency | utilities | numeric |
| Total_undistributed_expenses | currency | total_undistributed_expenses | numeric |
| House_profit | currency | house_profit | numeric |
| Management_fees | currency | management_fees | numeric |
| Centralized_accounting_charges | currency | centralized_accounting_charges | numeric |
| Franchise_fees_royalties | currency | franchise_fees_royalties | numeric |
| Gross_operating_profit | currency | gross_operating_profit | numeric |
| Rent | currency | rent | numeric |
| Property_and_other_taxes | currency | property_and_other_taxes | numeric |
| Property_and_liability_insurance | currency | property_and_liability_insurance | numeric |
| Other_non_operating_expenses | currency | other_non_operating_expenses | numeric |
| Total_non_operating_income_and_expenses | currency | total_non_operating_income_and_expenses | numeric |
| Replacement_reserve | currency | replacement_reserve | numeric |
| EBITDA_NOI | currency | ebitda_noi | numeric |
| Interest_expense | currency | interest_expense | numeric |
| Amortization_expense | currency | amortization_expense | numeric |
| Total_interest_depreciation_and_amortization | currency | total_interest_depreciation_and_amortization | numeric |
| Net_income | currency | net_income | numeric |
| Total_extraordinary_expenditures | currency | total_extraordinary_expenditures | numeric |
| Capital_expenditures | currency | capital_expenditures | numeric |
| Prior_year_expenses | currency | prior_year_expenses | numeric |
| Extraordinary_expense_misc_income_non_taxable | currency | extraordinary_expense_misc_income_non_taxable | numeric |
| Total_extraordinary_items | currency | total_extraordinary_items | numeric |
| Net_income_less_extraordinary_items | currency | net_income_less_extraordinary_items | numeric |
| Out_of_order_rooms | number | out_of_order_rooms | numeric |
| Complimentary_rooms | number | complimentary_rooms | numeric |
| Full_year_total_operating_revenue | currency | full_year_total_operating_revenue | numeric |
| Prior_year_total_operating_revenue | currency | prior_year_total_operating_revenue | numeric |
| Full_year_total_GOP | currency | full_year_total_gop | numeric |
| Prior_year_total_GOP | currency | prior_year_total_gop | numeric |
| Full_year_total_NOI | currency | full_year_total_noi | numeric |
| Prior_year_total_NOI | currency | prior_year_total_noi | numeric |
| Asset_detail copy | singleLineText | asset_detail_copy | text |
| Asset_detail copy 2 | singleLineText | asset_detail_copy_2 | text |

## `airtable.hotel_forecast`  (Hotel_forecast)
_44 stored columns · 14 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Forecast_date | date | forecast_date | date |
| Forecast_type | singleSelect | forecast_type | text |
| Asset_detail_link | multipleRecordLinks | asset_detail_link | text[] |
| Investments_link | multipleRecordLinks | investments_link | text[] |
| Available_rooms | number | available_rooms | numeric |
| Occupied_rooms | number | occupied_rooms | numeric |
| Sold_rooms | number | sold_rooms | numeric |
| Occupancy_% | percent | occupancy | numeric |
|  ADR  | currency | adr | numeric |
| RevPAR | currency | revpar | numeric |
| Rooms_sales | currency | rooms_sales | numeric |
| Food_and_beverage_sales | currency | food_and_beverage_sales | numeric |
| Minor_operated_department_sales | currency | minor_operated_department_sales | numeric |
| Miscellaneous_income_sales | currency | miscellaneous_income_sales | numeric |
| Total_operating_revenue | currency | total_operating_revenue | numeric |
| Rooms_expense | currency | rooms_expense | numeric |
| Food_and_beverage_expense | currency | food_and_beverage_expense | numeric |
| Minor_operated_department_expense | currency | minor_operated_department_expense | numeric |
| Total_departmental_expenses | currency | total_departmental_expenses | numeric |
| Total_department_profit | currency | total_department_profit | numeric |
| Administrative_and_general | currency | administrative_and_general | numeric |
| Information_and_telecommunication_systems | currency | information_and_telecommunication_systems | numeric |
| Sales_and_marketing | currency | sales_and_marketing | numeric |
| Repair_and_maintenance | currency | repair_and_maintenance | numeric |
| Utilities | currency | utilities | numeric |
| Total_undistributed_expenses | currency | total_undistributed_expenses | numeric |
| House_profit | currency | house_profit | numeric |
| Franchise_fees_royalties | currency | franchise_fees_royalties | numeric |
| Gross_operating_profit | currency | gross_operating_profit | numeric |
| Management_fees | currency | management_fees | numeric |
| Income_before_non_operating_income_and_expense | currency | income_before_non_operating_income_and_expense | numeric |
| Property_and_other_taxes | currency | property_and_other_taxes | numeric |
| Insurance | currency | insurance | numeric |
| Other_non_operating_expenses | currency | other_non_operating_expenses | numeric |
| Total_non_operating_expense | currency | total_non_operating_expense | numeric |
| EBITDA_NOI | currency | ebitda_noi | numeric |
| Interest_expense | currency | interest_expense | numeric |
| Net_income | currency | net_income | numeric |
| Mortgage_interest | currency | mortgage_interest | numeric |
| Interest_income | currency | interest_income | numeric |
| Total_interest_depreciation_and_amortization | currency | total_interest_depreciation_and_amortization | numeric |
| Capital_expenditures | currency | capital_expenditures | numeric |
| Net_income_less_extraordinary_items | currency | net_income_less_extraordinary_items | numeric |
| Hotel_actuals_link | multipleRecordLinks | hotel_actuals_link | text[] |

## `airtable.quarterly_hotel_actuals`  (Quarterly_hotel_actuals)
_72 stored columns · 22 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Date | date | date | date |
| Asset_detail_link | multipleRecordLinks | asset_detail_link | text[] |
| MPI | number | mpi | numeric |
| ARI | number | ari | numeric |
| RGI | number | rgi | numeric |
| MPI_%_change | percent | mpi_change | numeric |
| ARI_%_change | percent | ari_change | numeric |
| RGI_%_change | percent | rgi_change | numeric |
| Available_rooms | number | available_rooms | numeric |
| Rooms_sold | number | rooms_sold | numeric |
| Occupancy_% | percent | occupancy | numeric |
|  ADR  | currency | adr | numeric |
| RevPAR | currency | revpar | numeric |
| Total_operating_revenue | currency | total_operating_revenue | numeric |
| Total_departmental_profit | currency | total_departmental_profit | numeric |
| Gross_operating_profit | currency | gross_operating_profit | numeric |
| EBITDA | currency | ebitda | numeric |
| Budget_available_rooms | number | budget_available_rooms | numeric |
| Budget_rooms_sold | number | budget_rooms_sold | numeric |
| Budget_occupancy_% | percent | budget_occupancy | numeric |
| Budget_ADR | currency | budget_adr | numeric |
| Budget_RevPAR | currency | budget_revpar | numeric |
| Budget_total_operating_revenue | currency | budget_total_operating_revenue | numeric |
| Budget_total_departmental_profit | currency | budget_total_departmental_profit | numeric |
| Budget_gross_operating_profit | currency | budget_gross_operating_profit | numeric |
| Budget_EBITDA | currency | budget_ebitda | numeric |
| PY_Available Rooms | number | py_available_rooms | numeric |
| PY_rooms_sold | number | py_rooms_sold | numeric |
| PY_occupancy_% | percent | py_occupancy | numeric |
| PY_ADR | currency | py_adr | numeric |
| PY_RevPAR | currency | py_revpar | numeric |
| PY_total_operating_revenue | currency | py_total_operating_revenue | numeric |
| PY_total_departmental_profit | currency | py_total_departmental_profit | numeric |
| PY_gross_operating_profit | currency | py_gross_operating_profit | numeric |
| PY_EBITDA | currency | py_ebitda | numeric |
| Investments_link | multipleRecordLinks | investments_link | text[] |
| YTD_MPI | number | ytd_mpi | numeric |
| YTD_ARI | number | ytd_ari | numeric |
| YTD_RGI | number | ytd_rgi | numeric |
| YTD_MPI_%_change | percent | ytd_mpi_change | numeric |
| YTD_ARI_%_change | percent | ytd_ari_change | numeric |
| YTD_RGI_%_change | percent | ytd_rgi_change | numeric |
| YTD_available_rooms | number | ytd_available_rooms | numeric |
| YTD_rooms_sold | number | ytd_rooms_sold | numeric |
| YTD_occupancy_% | percent | ytd_occupancy | numeric |
| YTD_ADR | currency | ytd_adr | numeric |
| YTD_RevPAR | currency | ytd_revpar | numeric |
| YTD_total_operating_revenue | currency | ytd_total_operating_revenue | numeric |
| YTD_total_departmental_profit | currency | ytd_total_departmental_profit | numeric |
| YTD_gross_operating_profit | currency | ytd_gross_operating_profit | numeric |
| YTD_EBITDA | currency | ytd_ebitda | numeric |
| YTD_budget_available_rooms | number | ytd_budget_available_rooms | numeric |
| YTD_budget_rooms_sold | number | ytd_budget_rooms_sold | numeric |
| YTD_budget_occupancy_% | percent | ytd_budget_occupancy | numeric |
| YTD_Budget_ADR | currency | ytd_budget_adr | numeric |
| YTD_Budget_RevPAR | currency | ytd_budget_revpar | numeric |
| YTD_budget_total_operating_revenue | currency | ytd_budget_total_operating_revenue | numeric |
| YTD_budget_total_departmental_profit | currency | ytd_budget_total_departmental_profit | numeric |
| YTD_budget_gross_operating_profit | currency | ytd_budget_gross_operating_profit | numeric |
| YTD_Budget_EBITDA | currency | ytd_budget_ebitda | numeric |
| PY_YTD_available_rooms | number | py_ytd_available_rooms | numeric |
| PY_YTD_rooms_sold | number | py_ytd_rooms_sold | numeric |
| PY_YTD_occupancy_% | percent | py_ytd_occupancy | numeric |
| PY_YTD_ADR | currency | py_ytd_adr | numeric |
| PY_YTD_RevPAR | currency | py_ytd_revpar | numeric |
| PY_YTD_total_operating_revenue | currency | py_ytd_total_operating_revenue | numeric |
| PY_YTD_total_departmental_profit | currency | py_ytd_total_departmental_profit | numeric |
| PY_YTD_gross_operating_profit | currency | py_ytd_gross_operating_profit | numeric |
| PY_YTD_EBITDA | currency | py_ytd_ebitda | numeric |
| DSCR_adjusted | number | dscr_adjusted | numeric |
| Asset_detail copy | singleLineText | asset_detail_copy | text |
| Asset_detail copy 2 | singleLineText | asset_detail_copy_2 | text |

## `airtable.hotel_actuals`  (Hotel_actuals)
_65 stored columns · 40 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Asset_detail_link | multipleRecordLinks | asset_detail_link | text[] |
| Investments_link | multipleRecordLinks | investments_link | text[] |
| Date | date | date | date |
| Available_rooms | number | available_rooms | numeric |
| Occupied_rooms | number | occupied_rooms | numeric |
| Rooms_sales | currency | rooms_sales | numeric |
| Food_and_beverage_sales | currency | food_and_beverage_sales | numeric |
| Minor_operated_department_sales | currency | minor_operated_department_sales | numeric |
| Miscellaneous_income_sales | currency | miscellaneous_income_sales | numeric |
| Total_operating_revenue | currency | total_operating_revenue | numeric |
| Rooms_expense | currency | rooms_expense | numeric |
| Food_and_beverage_expense | currency | food_and_beverage_expense | numeric |
| Minor_operated_department_expense | currency | minor_operated_department_expense | numeric |
| Total_departmental_expenses | currency | total_departmental_expenses | numeric |
| Total_department_profit | currency | total_department_profit | numeric |
| Administrative_and_general | currency | administrative_and_general | numeric |
| Information_and_telecommunication_systems | currency | information_and_telecommunication_systems | numeric |
| Sales_and_marketing | currency | sales_and_marketing | numeric |
| Adj_sales_and_marketing | currency | adj_sales_and_marketing | numeric |
| Repair_and_maintenance | currency | repair_and_maintenance | numeric |
| Utilities | currency | utilities | numeric |
| Total_undistributed_expenses | currency | total_undistributed_expenses | numeric |
| House_profit | currency | house_profit | numeric |
| Management_fees | currency | management_fees | numeric |
| Centralized_accounting_charges | currency | centralized_accounting_charges | numeric |
| Franchise_fees_royalties | currency | franchise_fees_royalties | numeric |
| Credit_card_commissions | currency | credit_card_commissions | numeric |
| Gross_operating_profit | currency | gross_operating_profit | numeric |
| Rent | currency | rent | numeric |
| Property_and_other_taxes | currency | property_and_other_taxes | numeric |
| Property_and_liability_insurance | currency | property_and_liability_insurance | numeric |
| Other_non_operating_expenses | currency | other_non_operating_expenses | numeric |
| Total_non_operating_income_and_expenses | currency | total_non_operating_income_and_expenses | numeric |
| EBITDA_NOI | currency | ebitda_noi | numeric |
| Replacement_reserve | currency | replacement_reserve | numeric |
| Interest_expense | currency | interest_expense | numeric |
| Total_interest_depreciation_and_amortization | currency | total_interest_depreciation_and_amortization | numeric |
| Net_income | currency | net_income | numeric |
| Extraordinary_expense | currency | extraordinary_expense | numeric |
| Prior_year_expenses | currency | prior_year_expenses | numeric |
| Extraordinary_non_operating_expense | currency | extraordinary_non_operating_expense | numeric |
| Extraordinary_non_taxable_income | currency | extraordinary_non_taxable_income | numeric |
| Capital_expenditures | currency | capital_expenditures | numeric |
| Total_extraordinary_items | currency | total_extraordinary_items | numeric |
| Net_income_less_extraordinary_items | currency | net_income_less_extraordinary_items | numeric |
| Monthly_debt_payment_manual_input | currency | monthly_debt_payment_manual_input | numeric |
| Hotel_budget_link | multipleRecordLinks | hotel_budget_link | text[] |
| Hotel_health | singleLineText | hotel_health | text |
| Asset_manager | singleLineText | asset_manager | text |
| Health_trajectory | singleLineText | health_trajectory | text |
| Health_secondary_driver | singleLineText | health_secondary_driver | text |
| Health_primary_driver | singleLineText | health_primary_driver | text |
| PY_record | multipleRecordLinks | py_record | text[] |
| General_manager | singleLineText | general_manager | text |
| GM_hire_date | date | gm_hire_date | date |
| Director_of_sales | singleLineText | director_of_sales | text |
| DOS_hire_date | date | dos_hire_date | date |
| People_outlook | singleLineText | people_outlook | text |
| GM_outlook | singleLineText | gm_outlook | text |
| DOS_outlook | singleLineText | dos_outlook | text |
| Prop_leadership | singleLineText | prop_leadership | text |
| Extended_stay_rooms | number | extended_stay_rooms | numeric |
| Extended_stay_adr | currency | extended_stay_adr | numeric |
| From field: PY_record | multipleRecordLinks | from_field_py_record | text[] |
| Hotel_forecast | multipleRecordLinks | hotel_forecast | text[] |

## `airtable.balance_sheet`  (Balance_sheet)
_131 stored columns · 1 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Investments_link | multipleRecordLinks | investments_link | text[] |
| Balance_sheet_naming | multilineText | balance_sheet_naming | text |
| Asset_detail_link | multipleRecordLinks | asset_detail_link | text[] |
| Date | date | date | date |
| Cash_operating_account | currency | cash_operating_account | numeric |
| Cash_operating_account_2 | currency | cash_operating_account_2 | numeric |
| Cash_construction_pip_account | currency | cash_construction_pip_account | numeric |
| Cash_reserve_account | currency | cash_reserve_account | numeric |
| Cash_petty_cash_account | currency | cash_petty_cash_account | numeric |
| Cash_money_market_account | currency | cash_money_market_account | numeric |
| Cash_long_term_investment | currency | cash_long_term_investment | numeric |
| Cash_depository_account | currency | cash_depository_account | numeric |
| Cash_operating_account_3 | currency | cash_operating_account_3 | numeric |
| Cash_ff_e_reserve_account | currency | cash_ff_e_reserve_account | numeric |
| Cash_net_spend | currency | cash_net_spend | numeric |
| E_pay_clearing_account | currency | e_pay_clearing_account | numeric |
| Total_cash | currency | total_cash | numeric |
| AR_guest_ledger | currency | ar_guest_ledger | numeric |
| AR_city_ledger | currency | ar_city_ledger | numeric |
| AR_advance_deposit | currency | ar_advance_deposit | numeric |
| AR_tray_doubtful_allowance | currency | ar_tray_doubtful_allowance | numeric |
| AR_reward_stay | currency | ar_reward_stay | numeric |
| AR_prorations | currency | ar_prorations | numeric |
| AR_other_receivables_1 | currency | ar_other_receivables_1 | numeric |
| AR_hilton_advance_deposits | currency | ar_hilton_advance_deposits | numeric |
| AR_intercompany_receivables | currency | ar_intercompany_receivables | numeric |
| AR_shareholder_receivable | currency | ar_shareholder_receivable | numeric |
| AR_combined_tray_ledgers_do_not_use | currency | ar_combined_tray_ledgers_do_not_use | numeric |
| AR_other_receivables_2 | currency | ar_other_receivables_2 | numeric |
| AR_other_receivables_4 | currency | ar_other_receivables_4 | numeric |
| AR_other_receivables_misc | currency | ar_other_receivables_misc | numeric |
| AR_ach_payments | currency | ar_ach_payments | numeric |
| AR_hgi_keystone_llc | currency | ar_hgi_keystone_llc | numeric |
| Total_accounts_receivable | currency | total_accounts_receivable | numeric |
| Inventory_food | currency | inventory_food | numeric |
| Inventory_beverage | currency | inventory_beverage | numeric |
| Inventory_linen | currency | inventory_linen | numeric |
| Inventory_pantry_market | currency | inventory_pantry_market | numeric |
| Total_inventories | currency | total_inventories | numeric |
| Prepaid_expense | currency | prepaid_expense | numeric |
| Prepaid_general_insurance | currency | prepaid_general_insurance | numeric |
| Prepaid_workers_comp | currency | prepaid_workers_comp | numeric |
| Prepaid_sales_tax | currency | prepaid_sales_tax | numeric |
| Total_prepaid_expenses | currency | total_prepaid_expenses | numeric |
| Total_current_assets | currency | total_current_assets | numeric |
| Property_and_equipment | currency | property_and_equipment | numeric |
| Development_expense | currency | development_expense | numeric |
| Land | currency | land | numeric |
| Land_improvement | currency | land_improvement | numeric |
| Buildings | currency | buildings | numeric |
| Building_improvement | currency | building_improvement | numeric |
| Furniture_fix_other_hotel | currency | furniture_fix_other_hotel | numeric |
| Swimming_pool | currency | swimming_pool | numeric |
| Paving_parking_lot | currency | paving_parking_lot | numeric |
| Construction_in_progress | currency | construction_in_progress | numeric |
| 3_year_property | currency | n_3_year_property | numeric |
| 5_year_property | currency | n_5_year_property | numeric |
| 7_year_property | currency | n_7_year_property | numeric |
| Furniture_equipment | currency | furniture_equipment | numeric |
| 15_year_property | currency | n_15_year_property | numeric |
| 39_year_property | currency | n_39_year_property | numeric |
| Leasehold_improvements | currency | leasehold_improvements | numeric |
| Goodwill | currency | goodwill | numeric |
| Total_property_and_equipment | currency | total_property_and_equipment | numeric |
| Accumulated_depreciation | currency | accumulated_depreciation | numeric |
| Accumulated_amortization | currency | accumulated_amortization | numeric |
| Net_property_and_equipment | currency | net_property_and_equipment | numeric |
| Other_assets | currency | other_assets | numeric |
| Deposit_utility | currency | deposit_utility | numeric |
| Organization_cost | currency | organization_cost | numeric |
| Loan_cost | currency | loan_cost | numeric |
| Franchise_fees | currency | franchise_fees | numeric |
| Proceeds_from_sale_of_assets | currency | proceeds_from_sale_of_assets | numeric |
| Pre_opening_expense | currency | pre_opening_expense | numeric |
| Total_other_assets | currency | total_other_assets | numeric |
| Total_assets | currency | total_assets | numeric |
| AP_trade | currency | ap_trade | numeric |
| AP_construction_pip_acct | currency | ap_construction_pip_acct | numeric |
| AP_construction_retainage | currency | ap_construction_retainage | numeric |
| Garnishments_payable | currency | garnishments_payable | numeric |
| Gratuities_payable | currency | gratuities_payable | numeric |
| Inter_company_payable | currency | inter_company_payable | numeric |
| Due_to_parnter | currency | due_to_parnter | numeric |
| Total_accounts_payable | currency | total_accounts_payable | numeric |
| Accrued_AP | currency | accrued_ap | numeric |
| Accrued_sales_tax | currency | accrued_sales_tax | numeric |
| Accrued_workers_compensation | currency | accrued_workers_compensation | numeric |
| Accrued_state_occupancy_tax | currency | accrued_state_occupancy_tax | numeric |
| Accrued_city_occupancy_tax | currency | accrued_city_occupancy_tax | numeric |
| Accrued_401k | currency | accrued_401k | numeric |
| Accrued_other_payroll_w_h | currency | accrued_other_payroll_w_h | numeric |
| Accrued_real_estate_tax | currency | accrued_real_estate_tax | numeric |
| Accrued_bonus | currency | accrued_bonus | numeric |
| Accrued_group_health_insurance | currency | accrued_group_health_insurance | numeric |
| Accrued_interest | currency | accrued_interest | numeric |
| Accrued_franchise_expenses | currency | accrued_franchise_expenses | numeric |
| Accrued_payroll | currency | accrued_payroll | numeric |
| Accrued_expenses | currency | accrued_expenses | numeric |
| Accrued_payroll_taxes | currency | accrued_payroll_taxes | numeric |
| Accrued_utilities | currency | accrued_utilities | numeric |
| Accrued_insurance | currency | accrued_insurance | numeric |
| Accrued_intercompany_shared_expenses | currency | accrued_intercompany_shared_expenses | numeric |
| Payroll_clearing | currency | payroll_clearing | numeric |
| Total_accrued_expenses | currency | total_accrued_expenses | numeric |
| Gift_certificate_purchase | currency | gift_certificate_purchase | numeric |
| Unclaimed_property | currency | unclaimed_property | numeric |
| Deferred_income | currency | deferred_income | numeric |
| Advance_deposit_events | currency | advance_deposit_events | numeric |
| Total_other_liabilities | currency | total_other_liabilities | numeric |
| Total_current_liabilities | currency | total_current_liabilities | numeric |
| Mortgage_payable | currency | mortgage_payable | numeric |
| Mortgage_payable_2 | currency | mortgage_payable_2 | numeric |
| Loan_payable | currency | loan_payable | numeric |
| Sba_grant_loan | currency | sba_grant_loan | numeric |
| Pace_loan | currency | pace_loan | numeric |
| Loc | currency | loc | numeric |
| St_loan_intercompany | currency | st_loan_intercompany | numeric |
| St_loan_owner | currency | st_loan_owner | numeric |
| Total_long_term_liabilities | currency | total_long_term_liabilities | numeric |
| Total_liabilities | currency | total_liabilities | numeric |
| Retained_earnings | currency | retained_earnings | numeric |
| Owner_capital | currency | owner_capital | numeric |
| Owner_contributions | currency | owner_contributions | numeric |
| Owner_distribution | currency | owner_distribution | numeric |
| Partners_beginning_capital | currency | partners_beginning_capital | numeric |
| Retained_earnings_2 | currency | retained_earnings_2 | numeric |
| Current_earnings | currency | current_earnings | numeric |
| Total_owners_equity | currency | total_owners_equity | numeric |
| Total_liabilities_owners_equity | currency | total_liabilities_owners_equity | numeric |
| Asset_detail copy | singleLineText | asset_detail_copy | text |
| Asset_detail copy 2 | singleLineText | asset_detail_copy_2 | text |

## `airtable.hotel_segmentation`  (Hotel_segmentation)
_16 stored columns · 6 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Date | date | date | date |
| Property_segment_concat | singleLineText | property_segment_concat | text |
| Room_nights | number | room_nights | numeric |
| PY_room_nights | number | py_room_nights | numeric |
| Rooms_contribution | percent | rooms_contribution | numeric |
| PY_rooms_contribution | percent | py_rooms_contribution | numeric |
| ADR | currency | adr | numeric |
| PY_ADR | currency | py_adr | numeric |
| Revenue | currency | revenue | numeric |
| PY_revenue | currency | py_revenue | numeric |
| Revenue_contribution | percent | revenue_contribution | numeric |
| PY_revenue_contribution | percent | py_revenue_contribution | numeric |
| Asset_detail_link | multipleRecordLinks | asset_detail_link | text[] |
| Upload_date | date | upload_date | date |
| Asset_detail copy | singleLineText | asset_detail_copy | text |
| Asset_detail copy 2 | singleLineText | asset_detail_copy_2 | text |

## `airtable.hotel_capex`  (Hotel_CapEx)
_14 stored columns · 0 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Hotel_Name | singleLineText | hotel_name | text |
| Asset_detail_link | multipleRecordLinks | asset_detail_link | text[] |
| Batch_number | number | batch_number | numeric |
| Date_posted | date | date_posted | date |
| Type | singleSelect | type | text |
| Description | multilineText | description | text |
| Amount | currency | amount | numeric |
| Transaction_type | singleSelect | transaction_type | text |
| Vendor_id | singleLineText | vendor_id | text |
| Vendor_name | singleSelect | vendor_name | text |
| Invoice_memo | singleLineText | invoice_memo | text |
| Invoice_date | date | invoice_date | date |
| Asset_detail copy | singleLineText | asset_detail_copy | text |
| Asset_detail copy 2 | singleLineText | asset_detail_copy_2 | text |

## `airtable.hotel_capex_2026`  (Hotel_CapEx_2026)
_36 stored columns · 8 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Hotel_Name | singleLineText | hotel_name | text |
| Asset_detail_link | multipleRecordLinks | asset_detail_link | text[] |
| Approver | singleLineText | approver | text |
| Project_justification | singleSelect | project_justification | text |
| Project_description | multilineText | project_description | text |
| Priority_justification | singleSelect | priority_justification | text |
| Unit_description | multilineText | unit_description | text |
| Quantity | singleLineText | quantity | text |
| Cost_per_unit | currency | cost_per_unit | numeric |
| Year_last_replaced | number | year_last_replaced | numeric |
| Cost_by_project | currency | cost_by_project | numeric |
| Notes | multilineText | notes | text |
| Budgeted_y_n | singleSelect | budgeted_y_n | text |
| Approved_y_n | singleSelect | approved_y_n | text |
| Ownership_approval | singleSelect | ownership_approval | text |
| Meets_brand_standard_y_n | singleSelect | meets_brand_standard_y_n | text |
| Insurance_claim_y_n | singleSelect | insurance_claim_y_n | text |
| Previously_approved_capex | singleSelect | previously_approved_capex | text |
| Useful_life_years | multilineText | useful_life_years | text |
| Form_submitted_by | singleLineText | form_submitted_by | text |
| Ivy_Request_Date | date | ivy_request_date | date |
| Vendor Name_1 | multilineText | vendor_name_1 | text |
| Vendor Address_1 | multilineText | vendor_address_1 | text |
| Vendor_quote_1 | currency | vendor_quote_1 | numeric |
| Vendor Name_2 | multilineText | vendor_name_2 | text |
| Vendor Address_2 | multilineText | vendor_address_2 | text |
| Vendor_quote_2 | currency | vendor_quote_2 | numeric |
| Document_upload | multipleAttachments | document_upload | jsonb |
| Ownership_approval_notes | singleLineText | ownership_approval_notes | text |
| Vendor_quote_attachment | multipleAttachments | vendor_quote_attachment | jsonb |
| Ivy_notes | multilineText | ivy_notes | text |
| Ivy_approval_priority | singleSelect | ivy_approval_priority | text |
| AM Commentary | multilineText | am_commentary | text |
| Ownership_approval_UPDATES | singleSelect | ownership_approval_updates | text |
| Asset_detail copy | singleLineText | asset_detail_copy | text |
| Asset_detail copy 2 | singleLineText | asset_detail_copy_2 | text |

## `airtable.str_budget`  (STR_budget)
_49 stored columns · 6 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Asset_detail_link | multipleRecordLinks | asset_detail_link | text[] |
| Date | date | date | date |
| Occupancy_my_property | percent | occupancy_my_property | numeric |
| Occupancy_comp_set | percent | occupancy_comp_set | numeric |
| Occupancy_industry | percent | occupancy_industry | numeric |
| Occupancy_rank | number | occupancy_rank | numeric |
| Occupancy_my_property_%_chg | percent | occupancy_my_property_chg | numeric |
| Occupancy_comp_set_%_chg | percent | occupancy_comp_set_chg | numeric |
| Occupancy_industry_%_chg | percent | occupancy_industry_chg | numeric |
| Occupancy_rank_chg | number | occupancy_rank_chg | numeric |
| Occupancy_index_mpi | number | occupancy_index_mpi | numeric |
| Occupancy_index_mpi_%_chg | percent | occupancy_index_mpi_chg | numeric |
| ADR_my_property | currency | adr_my_property | numeric |
| ADR_comp_set | currency | adr_comp_set | numeric |
| ADR_industry | currency | adr_industry | numeric |
| ADR_rank | number | adr_rank | numeric |
| ADR_my_property_%_chg | percent | adr_my_property_chg | numeric |
| ADR_comp_set_%_chg | percent | adr_comp_set_chg | numeric |
| ADR_industry_%_chg | percent | adr_industry_chg | numeric |
| ADR_rank_chg | number | adr_rank_chg | numeric |
| ADR_index_ari | number | adr_index_ari | numeric |
| ADR_index_ari_%_chg | percent | adr_index_ari_chg | numeric |
| RevPAR_my_property | currency | revpar_my_property | numeric |
| RevPAR_comp_set | currency | revpar_comp_set | numeric |
| RevPAR_industry | currency | revpar_industry | numeric |
| RevPAR_rank | number | revpar_rank | numeric |
| RevPAR_my_property_%_chg | percent | revpar_my_property_chg | numeric |
| RevPAR_comp_set_%_chg | percent | revpar_comp_set_chg | numeric |
| RevPAR_industry_%_chg | percent | revpar_industry_chg | numeric |
| RevPAR_rank_chg | number | revpar_rank_chg | numeric |
| RevPAR_index_rgi | number | revpar_index_rgi | numeric |
| RevPAR_index_rgi_%_chg | percent | revpar_index_rgi_chg | numeric |
| Occupancy_target_rank | number | occupancy_target_rank | numeric |
| ADR_target_rank | number | adr_target_rank | numeric |
| RevPAR_target_rank | number | revpar_target_rank | numeric |
| Ranking_commentary | singleLineText | ranking_commentary | text |
| Occupancy_CY_budget | percent | occupancy_cy_budget | numeric |
| ADR_CY_budget | currency | adr_cy_budget | numeric |
| RevPAR_CY_budget | currency | revpar_cy_budget | numeric |
| Occupancy_PY_actual | percent | occupancy_py_actual | numeric |
| ADR_PY_actual | currency | adr_py_actual | numeric |
| RevPAR_PY_actual | currency | revpar_py_actual | numeric |
| RevPAR_rank_PY | number | revpar_rank_py | numeric |
| Occupancy_rank_PY | number | occupancy_rank_py | numeric |
| ADR_rank_PY | number | adr_rank_py | numeric |
| STR_weekly_data_link | multipleRecordLinks | str_weekly_data_link | text[] |
| STR_weekly_data copy | multipleRecordLinks | str_weekly_data_copy | text[] |
| Asset_detail copy | singleLineText | asset_detail_copy | text |
| Asset_detail copy 2 | singleLineText | asset_detail_copy_2 | text |

## `airtable.str_actuals`  (STR_actuals)
_44 stored columns · 36 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Asset_detail_link | multipleRecordLinks | asset_detail_link | text[] |
| Date | date | date | date |
| Occupancy_my_property | percent | occupancy_my_property | numeric |
| Occupancy_comp_set | percent | occupancy_comp_set | numeric |
| Occupancy_rank | number | occupancy_rank | numeric |
| Occupancy_my_property_%_chg | percent | occupancy_my_property_chg | numeric |
| Occupancy_comp_set_%_chg | percent | occupancy_comp_set_chg | numeric |
| Occupancy_rank_chg | number | occupancy_rank_chg | numeric |
| Occupancy_index_mpi | number | occupancy_index_mpi | numeric |
| Occupancy_index_mpi_%_chg | percent | occupancy_index_mpi_chg | numeric |
| ADR_my_property | number | adr_my_property | numeric |
| ADR_comp_set | number | adr_comp_set | numeric |
| ADR_rank | number | adr_rank | numeric |
| ADR_my_property_%_chg | percent | adr_my_property_chg | numeric |
| ADR_comp_set_%_chg | percent | adr_comp_set_chg | numeric |
| ADR_rank_chg | number | adr_rank_chg | numeric |
| ADR_index_ari | number | adr_index_ari | numeric |
| ADR_index_ari_%_chg | percent | adr_index_ari_chg | numeric |
| RevPAR_my_property | number | revpar_my_property | numeric |
| RevPAR_comp_set | number | revpar_comp_set | numeric |
| RevPAR_rank | number | revpar_rank | numeric |
| RevPAR_my_property_%_chg | percent | revpar_my_property_chg | numeric |
| RevPAR_comp_set_%_chg | percent | revpar_comp_set_chg | numeric |
| RevPAR_rank_chg | number | revpar_rank_chg | numeric |
| RevPAR_index_rgi | number | revpar_index_rgi | numeric |
| RevPAR_index_rgi_%_chg | percent | revpar_index_rgi_chg | numeric |
| STR_market_trend_link | multipleRecordLinks | str_market_trend_link | text[] |
| Supply | number | supply | numeric |
| Demand | number | demand | numeric |
| Revenue | currency | revenue | numeric |
| Comp_set_supply | number | comp_set_supply | numeric |
| Comp_set_demand | number | comp_set_demand | numeric |
| Comp_set_revenu | currency | comp_set_revenu | numeric |
| Occupancy_rank_3M | number | occupancy_rank_3m | numeric |
| Occupancy_rank_YTD | number | occupancy_rank_ytd | numeric |
| Occupancy_rank_12M | number | occupancy_rank_12m | numeric |
| ADR_rank_3M | number | adr_rank_3m | numeric |
| ADR_rank_YTD | number | adr_rank_ytd | numeric |
| ADR_rank_12M | number | adr_rank_12m | numeric |
| RevPAR_rank_3M | number | revpar_rank_3m | numeric |
| RevPAR_rank_YTD | number | revpar_rank_ytd | numeric |
| RevPAR_rank_12M | number | revpar_rank_12m | numeric |
| Asset_detail copy | singleLineText | asset_detail_copy | text |
| Asset_detail copy 2 | singleLineText | asset_detail_copy_2 | text |

## `airtable.str_weekly_data`  (STR_weekly_data)
_66 stored columns · 18 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Asset_detail_link | multipleRecordLinks | asset_detail_link | text[] |
| Start_date | date | start_date | date |
| End_date | date | end_date | date |
| STR_budget_link | multipleRecordLinks | str_budget_link | text[] |
| Occupancy_my_property | percent | occupancy_my_property | numeric |
| Occupancy_comp_set | percent | occupancy_comp_set | numeric |
| Occupancy_rank | number | occupancy_rank | numeric |
| Occupancy_my_property_%_chg | percent | occupancy_my_property_chg | numeric |
| Occupancy_comp_set_%_chg | percent | occupancy_comp_set_chg | numeric |
| Occupancy_rank_chg | number | occupancy_rank_chg | numeric |
| Occupancy_index_mpi | number | occupancy_index_mpi | numeric |
| Occupancy_index_mpi_%_chg | percent | occupancy_index_mpi_chg | numeric |
| ADR_my_property | currency | adr_my_property | numeric |
| ADR_comp_set | currency | adr_comp_set | numeric |
| ADR_rank | number | adr_rank | numeric |
| ADR_my_property_%_chg | percent | adr_my_property_chg | numeric |
| ADR_comp_set_%_chg | percent | adr_comp_set_chg | numeric |
| ADR_rank_chg | number | adr_rank_chg | numeric |
| ADR_index_ari | number | adr_index_ari | numeric |
| ADR_index_ari_%_chg | percent | adr_index_ari_chg | numeric |
| RevPAR_my_property | currency | revpar_my_property | numeric |
| RevPAR_comp_set | currency | revpar_comp_set | numeric |
| RevPAR_rank | number | revpar_rank | numeric |
| RevPAR_my_property_%_chg | percent | revpar_my_property_chg | numeric |
| RevPAR_comp_set_%_chg | percent | revpar_comp_set_chg | numeric |
| RevPAR_rank_chg | number | revpar_rank_chg | numeric |
| RevPAR_index_rgi | number | revpar_index_rgi | numeric |
| RevPAR_index_rgi_%_chg | percent | revpar_index_rgi_chg | numeric |
| Occupancy_my_property_py | percent | occupancy_my_property_py | numeric |
| Occupancy_my_property_%_chg_py | percent | occupancy_my_property_chg_py | numeric |
| Occupancy_comp_set_py | percent | occupancy_comp_set_py | numeric |
| Occupancy_comp_set_%_chg_py | percent | occupancy_comp_set_chg_py | numeric |
| Occupancy_index_mpi_py | number | occupancy_index_mpi_py | numeric |
| Occupancy_index_mpi_%_chg_py | percent | occupancy_index_mpi_chg_py | numeric |
| Occupancy_rank_py | number | occupancy_rank_py | numeric |
| Occupancy_rank_chg_py | number | occupancy_rank_chg_py | numeric |
| ADR_my_property_py | currency | adr_my_property_py | numeric |
| ADR_my_property_%_chg_py | percent | adr_my_property_chg_py | numeric |
| ADR_comp_set_py | currency | adr_comp_set_py | numeric |
| ADR_comp_set_%_chg_py | percent | adr_comp_set_chg_py | numeric |
| ADR_index_ari_py | number | adr_index_ari_py | numeric |
| ADR_index_ari_%_chg_py | percent | adr_index_ari_chg_py | numeric |
| ADR_rank_py | number | adr_rank_py | numeric |
| ADR_rank_chg_py | number | adr_rank_chg_py | numeric |
| RevPAR_my_property_py | currency | revpar_my_property_py | numeric |
| RevPAR_my_property_%_chg_py | percent | revpar_my_property_chg_py | numeric |
| RevPAR_comp_set_py | currency | revpar_comp_set_py | numeric |
| RevPAR_comp_set_%_chg_py | percent | revpar_comp_set_chg_py | numeric |
| RevPAR_index_rgi_py | number | revpar_index_rgi_py | numeric |
| RevPAR_index_rgi_%_chg_py | percent | revpar_index_rgi_chg_py | numeric |
| RevPAR_rank_py | number | revpar_rank_py | numeric |
| RevPAR_rank_chg_py | number | revpar_rank_chg_py | numeric |
| Supply | number | supply | numeric |
| Supply_py | number | supply_py | numeric |
| Demand | number | demand | numeric |
| Demand_py | number | demand_py | numeric |
| Revenue | currency | revenue | numeric |
| Revenue_py | currency | revenue_py | numeric |
| Comp_set_supply | number | comp_set_supply | numeric |
| Comp_set_supply_py | number | comp_set_supply_py | numeric |
| Comp_set_demand | number | comp_set_demand | numeric |
| Comp_set_demand_py | number | comp_set_demand_py | numeric |
| Comp_set_revenue | currency | comp_set_revenue | numeric |
| Comp_set_revenue_py | currency | comp_set_revenue_py | numeric |
| Asset_detail copy | singleLineText | asset_detail_copy | text |
| Asset_detail copy 2 | singleLineText | asset_detail_copy_2 | text |

## `airtable.str_daily_data`  (STR_daily_data)
_70 stored columns · 11 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Date | date | date | date |
| Occupancy_my_property | percent | occupancy_my_property | numeric |
| Occupancy_comp_set | percent | occupancy_comp_set | numeric |
| Occupancy_industry | percent | occupancy_industry | numeric |
| Occupancy_rank | number | occupancy_rank | numeric |
| Occupancy_my_property_%_chg | percent | occupancy_my_property_chg | numeric |
| Occupancy_comp_set_%_chg | percent | occupancy_comp_set_chg | numeric |
| Occupancy_industry_%_chg | percent | occupancy_industry_chg | numeric |
| Occupancy_rank_chg | number | occupancy_rank_chg | numeric |
| Occupancy_index_mpi | number | occupancy_index_mpi | numeric |
| Occupancy_index_mpi_%_chg | percent | occupancy_index_mpi_chg | numeric |
| ADR_my_property | currency | adr_my_property | numeric |
| ADR_comp_set | currency | adr_comp_set | numeric |
| ADR_industry | currency | adr_industry | numeric |
| ADR_rank | number | adr_rank | numeric |
| ADR_my_property_%_chg | percent | adr_my_property_chg | numeric |
| ADR_comp_set_%_chg | percent | adr_comp_set_chg | numeric |
| ADR_industry_%_chg | percent | adr_industry_chg | numeric |
| ADR_rank_chg | number | adr_rank_chg | numeric |
| ADR_index_ari | number | adr_index_ari | numeric |
| ADR_index_ari_%_chg | percent | adr_index_ari_chg | numeric |
| RevPAR_my_property | currency | revpar_my_property | numeric |
| RevPAR_comp_set | currency | revpar_comp_set | numeric |
| RevPAR_industry | currency | revpar_industry | numeric |
| RevPAR_rank | number | revpar_rank | numeric |
| RevPAR_my_property_%_chg | percent | revpar_my_property_chg | numeric |
| RevPAR_comp_set_%_chg | percent | revpar_comp_set_chg | numeric |
| RevPAR_industry_%_chg | percent | revpar_industry_chg | numeric |
| RevPAR_rank_chg | number | revpar_rank_chg | numeric |
| RevPAR_index_rgi | number | revpar_index_rgi | numeric |
| RevPAR_index_rgi_%_chg | percent | revpar_index_rgi_chg | numeric |
| Asset_detail_link | multipleRecordLinks | asset_detail_link | text[] |
| Occupancy_my_property_py | percent | occupancy_my_property_py | numeric |
| Occupancy_my_property_%_chg_py | percent | occupancy_my_property_chg_py | numeric |
| Occupancy_comp_set_py | percent | occupancy_comp_set_py | numeric |
| Occupancy_comp_set_%_chg_py | percent | occupancy_comp_set_chg_py | numeric |
| Occupancy_index_mpi_py | number | occupancy_index_mpi_py | numeric |
| Occupancy_index_mpi_%_chg_py | percent | occupancy_index_mpi_chg_py | numeric |
| Occupancy_rank_py | number | occupancy_rank_py | numeric |
| Occupancy_rank_chg_py | number | occupancy_rank_chg_py | numeric |
| ADR_my_property_py | currency | adr_my_property_py | numeric |
| ADR_my_property_%_chg_py | percent | adr_my_property_chg_py | numeric |
| ADR_comp_set_py | currency | adr_comp_set_py | numeric |
| ADR_comp_set_%_chg_py | percent | adr_comp_set_chg_py | numeric |
| ADR_index_ari_py | number | adr_index_ari_py | numeric |
| ADR_index_ari_%_chg_py | percent | adr_index_ari_chg_py | numeric |
| ADR_rank_py | number | adr_rank_py | numeric |
| ADR_rank_chg_py | number | adr_rank_chg_py | numeric |
| RevPAR_my_property_py | currency | revpar_my_property_py | numeric |
| RevPAR_my_property_%_chg_py | percent | revpar_my_property_chg_py | numeric |
| RevPAR_comp_set_py | currency | revpar_comp_set_py | numeric |
| RevPAR_comp_set_%_chg_py | percent | revpar_comp_set_chg_py | numeric |
| RevPAR_index_rgi_py | number | revpar_index_rgi_py | numeric |
| RevPAR_index_rgi_%_chg_py | percent | revpar_index_rgi_chg_py | numeric |
| RevPAR_rank_py | number | revpar_rank_py | numeric |
| RevPAR_rank_chg_py | number | revpar_rank_chg_py | numeric |
| Supply | number | supply | numeric |
| Supply_py | number | supply_py | numeric |
| Demand | number | demand | numeric |
| Demand_py | number | demand_py | numeric |
| Comp_set_supply | number | comp_set_supply | numeric |
| Revenue | currency | revenue | numeric |
| Revenue_py | currency | revenue_py | numeric |
| Comp_set_supply_py | number | comp_set_supply_py | numeric |
| Comp_set_demand | number | comp_set_demand | numeric |
| Comp_set_demand_py | number | comp_set_demand_py | numeric |
| Comp_set_revenue | currency | comp_set_revenue | numeric |
| Comp_set_revenue_py | currency | comp_set_revenue_py | numeric |
| Asset_detail copy | singleLineText | asset_detail_copy | text |
| Asset_detail copy 2 | singleLineText | asset_detail_copy_2 | text |

## `airtable.str_28_day_trend`  (STR_28_day_trend)
_74 stored columns · 27 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Asset_detail_link | multipleRecordLinks | asset_detail_link | text[] |
| Start_date | date | start_date | date |
| End_date | date | end_date | date |
| STR_budget_link | multipleRecordLinks | str_budget_link | text[] |
| Occupancy_my_property | percent | occupancy_my_property | numeric |
| Occupancy_comp_set | percent | occupancy_comp_set | numeric |
| Occupancy_rank | number | occupancy_rank | numeric |
| Occupancy_my_property_%_chg | percent | occupancy_my_property_chg | numeric |
| Occupancy_comp_set_%_chg | percent | occupancy_comp_set_chg | numeric |
| Occupancy_rank_chg | number | occupancy_rank_chg | numeric |
| Occupancy_index_mpi | number | occupancy_index_mpi | numeric |
| Occupancy_index_mpi_%_chg | percent | occupancy_index_mpi_chg | numeric |
| ADR_my_property | currency | adr_my_property | numeric |
| ADR_comp_set | currency | adr_comp_set | numeric |
| ADR_rank | number | adr_rank | numeric |
| ADR_my_property_%_chg | percent | adr_my_property_chg | numeric |
| ADR_comp_set_%_chg | percent | adr_comp_set_chg | numeric |
| ADR_rank_chg | number | adr_rank_chg | numeric |
| ADR_index_ari | number | adr_index_ari | numeric |
| ADR_index_ari_%_chg | percent | adr_index_ari_chg | numeric |
| RevPAR_my_property | currency | revpar_my_property | numeric |
| RevPAR_comp_set | currency | revpar_comp_set | numeric |
| RevPAR_rank | number | revpar_rank | numeric |
| RevPAR_my_property_%_chg | percent | revpar_my_property_chg | numeric |
| RevPAR_comp_set_%_chg | percent | revpar_comp_set_chg | numeric |
| RevPAR_rank_chg | number | revpar_rank_chg | numeric |
| RevPAR_index_rgi | number | revpar_index_rgi | numeric |
| RevPAR_index_rgi_%_chg | percent | revpar_index_rgi_chg | numeric |
| Occupancy_my_property_py | percent | occupancy_my_property_py | numeric |
| Occupancy_my_property_%_chg_py | percent | occupancy_my_property_chg_py | numeric |
| Occupancy_comp_set_py | percent | occupancy_comp_set_py | numeric |
| Occupancy_comp_set_%_chg_py | percent | occupancy_comp_set_chg_py | numeric |
| Occupancy_index_mpi_py | number | occupancy_index_mpi_py | numeric |
| Occupancy_index_mpi_%_chg_py | percent | occupancy_index_mpi_chg_py | numeric |
| Occupancy_rank_py | number | occupancy_rank_py | numeric |
| Occupancy_rank_chg_py | number | occupancy_rank_chg_py | numeric |
| ADR_my_property_py | currency | adr_my_property_py | numeric |
| ADR_my_property_%_chg_py | percent | adr_my_property_chg_py | numeric |
| ADR_comp_set_py | currency | adr_comp_set_py | numeric |
| ADR_comp_set_%_chg_py | percent | adr_comp_set_chg_py | numeric |
| ADR_index_ari_py | number | adr_index_ari_py | numeric |
| ADR_index_ari_%_chg_py | percent | adr_index_ari_chg_py | numeric |
| ADR_rank_py | number | adr_rank_py | numeric |
| ADR_rank_chg_py | number | adr_rank_chg_py | numeric |
| RevPAR_my_property_py | currency | revpar_my_property_py | numeric |
| RevPAR_my_property_%_chg_py | percent | revpar_my_property_chg_py | numeric |
| RevPAR_comp_set_py | currency | revpar_comp_set_py | numeric |
| RevPAR_comp_set_%_chg_py | percent | revpar_comp_set_chg_py | numeric |
| RevPAR_index_rgi_py | number | revpar_index_rgi_py | numeric |
| RevPAR_index_rgi_%_chg_py | percent | revpar_index_rgi_chg_py | numeric |
| RevPAR_rank_py | number | revpar_rank_py | numeric |
| RevPAR_rank_chg_py | number | revpar_rank_chg_py | numeric |
| Supply | number | supply | numeric |
| Supply_py | number | supply_py | numeric |
| Demand | number | demand | numeric |
| Demand_py | number | demand_py | numeric |
| Revenue | currency | revenue | numeric |
| Revenue_py | currency | revenue_py | numeric |
| Comp_set_supply | number | comp_set_supply | numeric |
| Comp_set_supply_py | number | comp_set_supply_py | numeric |
| Comp_set_demand | number | comp_set_demand | numeric |
| Comp_set_demand_py | number | comp_set_demand_py | numeric |
| Comp_set_revenue | currency | comp_set_revenue | numeric |
| Comp_set_revenue_py | currency | comp_set_revenue_py | numeric |
| 1_week_prior | multipleRecordLinks | n_1_week_prior | text[] |
| 2_week_prior | multipleRecordLinks | n_2_week_prior | text[] |
| 3_week_prior | multipleRecordLinks | n_3_week_prior | text[] |
| 4_week_prior | multipleRecordLinks | n_4_week_prior | text[] |
| Asset_detail copy | singleLineText | asset_detail_copy | text |
| Asset_detail copy 2 | singleLineText | asset_detail_copy_2 | text |
| From field: Prior_week | multipleRecordLinks | from_field_prior_week | text[] |
| From field: 2_week_prior copy | multipleRecordLinks | from_field_2_week_prior_copy | text[] |
| From field: 2_week_prior copy copy | multipleRecordLinks | from_field_2_week_prior_copy_copy | text[] |
| From field: 2_week_prior | multipleRecordLinks | from_field_2_week_prior | text[] |

## `airtable.str_market_trend`  (STR_market_trend)
_15 stored columns · 3 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Market | singleSelect | market | text |
| Date | date | date | date |
| Occupancy_TTM | percent | occupancy_ttm | numeric |
| Occupancy_TTM_%_chg | percent | occupancy_ttm_chg | numeric |
| ADR_TTM | currency | adr_ttm | numeric |
| ADR_TTM_%_chg | percent | adr_ttm_chg | numeric |
| RevPar_TTM | currency | revpar_ttm | numeric |
| RevPAR_TTM_%_chg | percent | revpar_ttm_chg | numeric |
| Supply_TTM | number | supply_ttm | numeric |
| Supply_TTM_%_chg | percent | supply_ttm_chg | numeric |
| Demand_TTM | number | demand_ttm | numeric |
| Demand_TTM_%_chg | percent | demand_ttm_chg | numeric |
| Revenue_TTM | currency | revenue_ttm | numeric |
| Revenue_TTM_%_chg | percent | revenue_ttm_chg | numeric |
| STR_actuals_link | multipleRecordLinks | str_actuals_link | text[] |

## `airtable.str_comp_set`  (STR_comp_set)
_16 stored columns · 10 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Asset_detail_link | multipleRecordLinks | asset_detail_link | text[] |
| STR_code | number | str_code | numeric |
| Property_name | multilineText | property_name | text |
| Room_count | number | room_count | numeric |
| Open_date | date | open_date | date |
| City | singleLineText | city | text |
| State | singleLineText | state | text |
| Portfolio_hotel | checkbox | portfolio_hotel | boolean |
| Comments | singleLineText | comments | text |
| Latest_renovation_date | number | latest_renovation_date | numeric |
| Latest_renovation_scope | singleLineText | latest_renovation_scope | text |
| Future_renovations_planned | singleLineText | future_renovations_planned | text |
| Latest_renovation_comments | singleLineText | latest_renovation_comments | text |
| Asset_detail | singleLineText | asset_detail | text |
| Asset_detail copy | singleLineText | asset_detail_copy | text |
| Asset_detail copy 2 | singleLineText | asset_detail_copy_2 | text |

## `airtable.hotel_onthebooks`  (Hotel_onthebooks)
_26 stored columns · 4 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Upload Date | date | upload_date | date |
| Date | date | date | date |
| Asset_detail | multipleRecordLinks | asset_detail | text[] |
| Occ_otb | percent | occ_otb | numeric |
| Adr_otb | currency | adr_otb | numeric |
| Rev_otb | currency | rev_otb | numeric |
| Revpar_otb | number | revpar_otb | numeric |
| Occ_stly | percent | occ_stly | numeric |
| Adr_stly | currency | adr_stly | numeric |
| Rev_stly | currency | rev_stly | numeric |
| Revpar_stly | number | revpar_stly | numeric |
| Occ_py | percent | occ_py | numeric |
| Adr_py | currency | adr_py | numeric |
| Rev_py | currency | rev_py | numeric |
| Revpar_py | number | revpar_py | numeric |
| Occ_fcst_rms | percent | occ_fcst_rms | numeric |
| Adr_fcst_rms | currency | adr_fcst_rms | numeric |
| Rev_fcst_rms | currency | rev_fcst_rms | numeric |
| Occ_budget | percent | occ_budget | numeric |
| Adr_budget | currency | adr_budget | numeric |
| Rev_budget | currency | rev_budget | numeric |
| Occ_fcst_bi | percent | occ_fcst_bi | numeric |
| Adr_fcst_bi | currency | adr_fcst_bi | numeric |
| Rev_fcst_bi | currency | rev_fcst_bi | numeric |
| Asset_detail copy | singleLineText | asset_detail_copy | text |
| Asset_detail copy 2 | singleLineText | asset_detail_copy_2 | text |

## `airtable.full_hotel_comp_landscape`  (Full_hotel_comp_landscape)
_56 stored columns · 9 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Asset_detail_link | multipleRecordLinks | asset_detail_link | text[] |
| Property_name | singleLineText | property_name | text |
| STR_code | number | str_code | numeric |
| Distance | number | distance | numeric |
| Location | singleSelect | location | text |
| Rooms | number | rooms | numeric |
| Chain_scale | singleSelect | chain_scale | text |
| Last_month_data_available | checkbox | last_month_data_available | boolean |
| Open_date | date | open_date | date |
| Franchise | singleSelect | franchise | text |
| Parent_company | singleSelect | parent_company | text |
| Management_company | singleLineText | management_company | text |
| Owner | singleLineText | owner | text |
| 22-Jan | singleLineText | n_22_jan | text |
| 22-Feb | singleLineText | n_22_feb | text |
| 22-Mar | singleLineText | n_22_mar | text |
| 22-Apr | singleLineText | n_22_apr | text |
| 22-May | singleLineText | n_22_may | text |
| 22-Jun | singleLineText | n_22_jun | text |
| 22-Jul | singleLineText | n_22_jul | text |
| 22-Aug | singleLineText | n_22_aug | text |
| 22-Sep | singleLineText | n_22_sep | text |
| 22-Oct | singleLineText | n_22_oct | text |
| 22-Nov | singleLineText | n_22_nov | text |
| 22-Dec | singleLineText | n_22_dec | text |
| 23-Jan | singleLineText | n_23_jan | text |
| 23-Feb | singleLineText | n_23_feb | text |
| 23-Mar | singleLineText | n_23_mar | text |
| 23-Apr | singleLineText | n_23_apr | text |
| 23-May | singleLineText | n_23_may | text |
| 23-Jun | singleLineText | n_23_jun | text |
| 23-Jul | singleLineText | n_23_jul | text |
| 23-Aug | singleLineText | n_23_aug | text |
| 23-Sep | singleLineText | n_23_sep | text |
| 23-Oct | singleLineText | n_23_oct | text |
| 23-Nov | singleLineText | n_23_nov | text |
| 23-Dec | singleLineText | n_23_dec | text |
| 24-Jan | singleLineText | n_24_jan | text |
| 24-Feb | singleLineText | n_24_feb | text |
| 24-Mar | singleLineText | n_24_mar | text |
| 24-Apr | singleLineText | n_24_apr | text |
| 24-May | singleLineText | n_24_may | text |
| 24-Jun | singleLineText | n_24_jun | text |
| 24-Jul | singleLineText | n_24_jul | text |
| 24-Aug | singleLineText | n_24_aug | text |
| 24-Sep | singleLineText | n_24_sep | text |
| 24-Oct | singleLineText | n_24_oct | text |
| 24-Nov | singleLineText | n_24_nov | text |
| 24-Dec | singleLineText | n_24_dec | text |
| Current Comp Set | singleSelect | current_comp_set | text |
| Comp_set_review_comments | multilineText | comp_set_review_comments | text |
| Update_required | singleSelect | update_required | text |
| Target_property_update_reqd | singleSelect | target_property_update_reqd | text |
| Future_comp_set | singleSelect | future_comp_set | text |
| Asset_detail copy | singleLineText | asset_detail_copy | text |
| Asset_detail copy 2 | singleLineText | asset_detail_copy_2 | text |

## `airtable.hotel_brand_metrics`  (Hotel_brand_metrics)
_39 stored columns · 7 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Hotel_brand_metrics_id | singleLineText | hotel_brand_metrics_id | text |
| Franchise_acronym | singleLineText | franchise_acronym | text |
| Hotel_brand | singleSelect | hotel_brand | text |
| Brand_acronym | singleSelect | brand_acronym | text |
| Scale | singleSelect | scale | text |
| Asset_detail_link | multipleRecordLinks | asset_detail_link | text[] |
| 2022_ADR_avg | currency | n_2022_adr_avg | numeric |
| 2022_ADR_median | currency | n_2022_adr_median | numeric |
| 2023_ADR_avg | currency | n_2023_adr_avg | numeric |
| 2023_ADR_median | currency | n_2023_adr_median | numeric |
| 2022_occupancy_avg | percent | n_2022_occupancy_avg | numeric |
| 2022_occupancy_median | percent | n_2022_occupancy_median | numeric |
| 2023_occupancy_avg | percent | n_2023_occupancy_avg | numeric |
| 2023_occupancy_median | percent | n_2023_occupancy_median | numeric |
| 2022_RevPAR_index_avg | number | n_2022_revpar_index_avg | numeric |
| 2022_RevPAR_index_median | number | n_2022_revpar_index_median | numeric |
| 2023_RevPAR_index_avg | number | n_2023_revpar_index_avg | numeric |
| 2023_RevPAR_index_median | number | n_2023_revpar_index_median | numeric |
| 2022_occupancy_index_avg | number | n_2022_occupancy_index_avg | numeric |
| 2022_occupancy_index_median | number | n_2022_occupancy_index_median | numeric |
| 2023_occupancy_index_avg | number | n_2023_occupancy_index_avg | numeric |
| 2023_occupancy_index_median | number | n_2023_occupancy_index_median | numeric |
| 2024_ADR_avg | number | n_2024_adr_avg | numeric |
| 2024_ADR_median | number | n_2024_adr_median | numeric |
| 2024_occupancy_avg | number | n_2024_occupancy_avg | numeric |
| 2024_occupancy_median | number | n_2024_occupancy_median | numeric |
| 2024_RevPAR_index_avg | number | n_2024_revpar_index_avg | numeric |
| 2024_RevPAR_index_median | number | n_2024_revpar_index_median | numeric |
| 2024_occupancy_index_avg | number | n_2024_occupancy_index_avg | numeric |
| 2024_occupancy_index_median | number | n_2024_occupancy_index_median | numeric |
| 2024_RevPAR_avg | number | n_2024_revpar_avg | numeric |
| 2025_occupancy_avg | percent | n_2025_occupancy_avg | numeric |
| 2025_RevPAR_index_avg | number | n_2025_revpar_index_avg | numeric |
| 2025_RevPAR_index_median | number | n_2025_revpar_index_median | numeric |
| 2025_RevPAR_avg | number | n_2025_revpar_avg | numeric |
| 2025_ADR_avg | currency | n_2025_adr_avg | numeric |
| 2025_occupancy_median | percent | n_2025_occupancy_median | numeric |
| Asset_detail copy | singleLineText | asset_detail_copy | text |
| Asset_detail copy 2 | singleLineText | asset_detail_copy_2 | text |

## `airtable.lenders`  (Lenders)
_13 stored columns · 4 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Lenders_id | singleLineText | lenders_id | text |
| Investment_manager_type | singleSelect | investment_manager_type | text |
| Lender_type | singleSelect | lender_type | text |
| State | singleSelect | state | text |
| Contact_name | singleLineText | contact_name | text |
| Email | singleLineText | email | text |
| Loan_summary_data_link | multipleRecordLinks | loan_summary_data_link | text[] |
| Cash_accounts_link | multipleRecordLinks | cash_accounts_link | text[] |
| Hotel_sale_comps_link | multipleRecordLinks | hotel_sale_comps_link | text[] |
| Lending_footprint | multipleSelects | lending_footprint | text[] |
| Lending Product Types | multipleSelects | lending_product_types | text[] |
| Guarantor_Compliance | multipleRecordLinks | guarantor_compliance | text[] |
| Field 17 | singleLineText | field_17 | text |

## `airtable.hotel_sale_comps`  (Hotel_sale_comps)
_14 stored columns · 1 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Hotel_sale_comps_id | multilineText | hotel_sale_comps_id | text |
| First_trust_deed_terms | multilineText | first_trust_deed_terms | text |
| First_trust_deed_lender | singleSelect | first_trust_deed_lender | text |
| Lenders_link | multipleRecordLinks | lenders_link | text[] |
| First_trust_deed_payment | singleLineText | first_trust_deed_payment | text |
| Parent_company | singleSelect | parent_company | text |
| Property_address | multilineText | property_address | text |
| Property_city | singleSelect | property_city | text |
| Property_state | singleSelect | property_state | text |
| Brand | singleSelect | brand | text |
| Hotel_class | singleSelect | hotel_class | text |
| Scale | singleSelect | scale | text |
| First_trust_deed_balance | number | first_trust_deed_balance | numeric |
| Sale_date | date | sale_date | date |

## `airtable.debt_resizing`  (Debt_resizing)
_4 stored columns · 17 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Investments_link | multipleRecordLinks | investments_link | text[] |
| 5yr_UST | percent | n_5yr_ust | numeric |
| Spread | percent | spread | numeric |
| Interest Rate | number | interest_rate | numeric |

## `airtable.year_end_financials`  (Year_end_financials)
_12 stored columns · 5 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Asset_detail_link | multipleRecordLinks | asset_detail_link | text[] |
| Year | number | year | numeric |
| Total_operating_revenue | currency | total_operating_revenue | numeric |
| GOP | currency | gop | numeric |
| Occupancy | percent | occupancy | numeric |
| ADR | currency | adr | numeric |
| RevPAR | currency | revpar | numeric |
| MPI | number | mpi | numeric |
| ARI | number | ari | numeric |
| RGI | number | rgi | numeric |
| Asset_detail copy | singleLineText | asset_detail_copy | text |
| Asset_detail copy 2 | singleLineText | asset_detail_copy_2 | text |

## `airtable.hotel_gss_data`  (Hotel_GSS_data)
_44 stored columns · 10 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Asset_detail_link | multipleRecordLinks | asset_detail_link | text[] |
| Investments_link | multipleRecordLinks | investments_link | text[] |
| Date | date | date | date |
| Marriott_responses | number | marriott_responses | numeric |
| Marriott_intent_to_recommend | number | marriott_intent_to_recommend | numeric |
| Marriott_elite_appreciation | number | marriott_elite_appreciation | numeric |
| Marriott_cleanliness | number | marriott_cleanliness | numeric |
| Marriott_staff_service | number | marriott_staff_service | numeric |
| Marriott_maintenance_and_upkeep | number | marriott_maintenance_and_upkeep | numeric |
| Marriott_f&b | number | marriott_f_b | numeric |
| Marriott_select_tier_f&b_service | number | marriott_select_tier_f_b_service | numeric |
| Marriott_select_tier_f&b_quality | number | marriott_select_tier_f_b_quality | numeric |
| Marriott_select_comp_f&b_service | number | marriott_select_comp_f_b_service | numeric |
| Marriott_select_comp_f&b_quality | number | marriott_select_comp_f_b_quality | numeric |
| Marriott_fitness_center_satisfaction | number | marriott_fitness_center_satisfaction | numeric |
| Hilton_responses | number | hilton_responses | numeric |
| Hilton_stay_score | number | hilton_stay_score | numeric |
| Hilton_stay_score_survey | number | hilton_stay_score_survey | numeric |
| Hilton_stay_score_review_sites | number | hilton_stay_score_review_sites | numeric |
| Hilton_service_quality | number | hilton_service_quality | numeric |
| Hilton_overall_cleanliness | number | hilton_overall_cleanliness | numeric |
| Hilton_HH_appreciation | number | hilton_hh_appreciation | numeric |
| Hilton_HH_delivery | number | hilton_hh_delivery | numeric |
| Hilton_HH_recognition | number | hilton_hh_recognition | numeric |
| Hilton_problem | number | hilton_problem | numeric |
| IHG_responses_QTD | number | ihg_responses_qtd | numeric |
| IHG_overall_experience_QTD | number | ihg_overall_experience_qtd | numeric |
| IHG_likely_to_recommend_QTD | number | ihg_likely_to_recommend_qtd | numeric |
| IHG_loyalty_recognition_QTD | number | ihg_loyalty_recognition_qtd | numeric |
| IHG_overall_arrival_QTD | number | ihg_overall_arrival_qtd | numeric |
| IHG_overall_checkin_QTD | number | ihg_overall_checkin_qtd | numeric |
| IHG_overall_service_QTD | number | ihg_overall_service_qtd | numeric |
| IHG_room_cleanliness_QTD | number | ihg_room_cleanliness_qtd | numeric |
| IHG_overall_f&b_QTD | number | ihg_overall_f_b_qtd | numeric |
| IHG_breakfast_QTD | number | ihg_breakfast_qtd | numeric |
| IHG_problem_handling_index_QTD | number | ihg_problem_handling_index_qtd | numeric |
| Hyatt_NPS_net_promoter_scores | number | hyatt_nps_net_promoter_scores | numeric |
| Hyatt_customer_service | number | hyatt_customer_service | numeric |
| Hyatt_room_cleanliness | number | hyatt_room_cleanliness | numeric |
| Hyatt_checkin_process | number | hyatt_checkin_process | numeric |
| Hyatt_hotel_condition | number | hyatt_hotel_condition | numeric |
| GSS_file | multipleAttachments | gss_file | jsonb |
| Asset_detail copy | singleLineText | asset_detail_copy | text |
| Asset_detail copy 2 | singleLineText | asset_detail_copy_2 | text |

## `airtable.hotel_qa_data`  (Hotel_QA_data)
_32 stored columns · 9 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| QA_file | multipleAttachments | qa_file | jsonb |
| Date | date | date | date |
| Asset_detail_link | multipleRecordLinks | asset_detail_link | text[] |
| Investments_link | multipleRecordLinks | investments_link | text[] |
| Result | singleSelect | result | text |
| Marriott_staff_service | number | marriott_staff_service | numeric |
| Marriott_brand_promise | number | marriott_brand_promise | numeric |
| Marriott_MI_initiatives | number | marriott_mi_initiatives | numeric |
| Marriott_cleanliness | number | marriott_cleanliness | numeric |
| Marriott_maintenance_upkeep | number | marriott_maintenance_upkeep | numeric |
| Marriott_BSA_score | number | marriott_bsa_score | numeric |
| Hilton_brand_standards | number | hilton_brand_standards | numeric |
| Hilton_commercial_facilities | number | hilton_commercial_facilities | numeric |
| Hilton_f&b_facilities | number | hilton_f_b_facilities | numeric |
| Hilton_guest_rooms | number | hilton_guest_rooms | numeric |
| Hilton_index_score | number | hilton_index_score | numeric |
| Hilton_cleanliness | number | hilton_cleanliness | numeric |
| Hilton_multiplier | number | hilton_multiplier | numeric |
| Hilton_overall_QA_score | number | hilton_overall_qa_score | numeric |
| Hyatt_brand_standard | number | hyatt_brand_standard | numeric |
| Hyatt_cleanliness | number | hyatt_cleanliness | numeric |
| Hyatt_condition | number | hyatt_condition | numeric |
| Hyatt_working_order | number | hyatt_working_order | numeric |
| Hyatt_score | number | hyatt_score | numeric |
| IHG_guest_love | number | ihg_guest_love | numeric |
| IHG_brand_safety_standard | number | ihg_brand_safety_standard | numeric |
| IHG_brand_standard_important | number | ihg_brand_standard_important | numeric |
| IHG_brand_standard_major | number | ihg_brand_standard_major | numeric |
| IHG_cleanliness | number | ihg_cleanliness | numeric |
| IHG_condition | number | ihg_condition | numeric |
| Asset_detail copy | singleLineText | asset_detail_copy | text |
| Asset_detail copy 2 | singleLineText | asset_detail_copy_2 | text |

## `airtable.guarantor_compliance`  (Guarantor_Compliance)
_13 stored columns · 6 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Guarantor_compliance_id | singleLineText | guarantor_compliance_id | text |
| Bank_Guarantor_Name | singleLineText | bank_guarantor_name | text |
| Loan_summary_link | multipleRecordLinks | loan_summary_link | text[] |
| Lenders_link | multipleRecordLinks | lenders_link | text[] |
| Scope_of_liability | singleSelect | scope_of_liability | text |
| Scope_of_liability_comments | multilineText | scope_of_liability_comments | text |
| Liability_structure | singleSelect | liability_structure | text |
| Review | singleLineText | review | text |
| %_Guarantee | percent | guarantee | numeric |
| Release_requirement | multilineText | release_requirement | text |
| Financial_reports_required | multipleSelects | financial_reports_required | text[] |
| Financial_reports_required_frequency | singleSelect | financial_reports_required_frequency | text |
| Guarantor_Notes | multilineText | guarantor_notes | text |

## `airtable.hotel_pip_history`  (Hotel_PIP_history)
_6 stored columns · 34 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Asset_detail_link | multipleRecordLinks | asset_detail_link | text[] |
| Investments_link | multipleRecordLinks | investments_link | text[] |
| General_contractor | singleLineText | general_contractor | text |
| PIP_all_in_cost | currency | pip_all_in_cost | numeric |
| GDrive_link | multilineText | gdrive_link | text |
| Procurement | singleLineText | procurement | text |

## `airtable.cash_flow_tracking`  (Cash_flow_tracking)
_4 stored columns · 7 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Asset_detail_link | multipleRecordLinks | asset_detail_link | text[] |
| Date | date | date | date |
| Payment_type | singleSelect | payment_type | text |
| Amount | currency | amount | numeric |

## `airtable.hotel_gss_data_v2`  (Hotel_GSS_data_v2)
_45 stored columns · 3 computed (deferred)_

| Airtable field | Airtable type | Postgres column | Postgres type |
|---|---|---|---|
| Asset_detail_link | multipleRecordLinks | asset_detail_link | text[] |
| Investments_link | multipleRecordLinks | investments_link | text[] |
| Hotel Name | multilineText | hotel_name | text |
| Date | date | date | date |
| Hotel Brand | singleSelect | hotel_brand | text |
| ITR_Current | number | itr_current | numeric |
| ITR_Last_month | number | itr_last_month | numeric |
| ITR_six_month | number | itr_six_month | numeric |
| ITR_Benchmark | number | itr_benchmark | numeric |
| ITR_Variance_to_benchmark | number | itr_variance_to_benchmark | numeric |
| Service_Current | number | service_current | numeric |
| Service_Last_month | number | service_last_month | numeric |
| Service_six_month | number | service_six_month | numeric |
| Service_Benchmark | number | service_benchmark | numeric |
| Service_Variance_to_benchmark | number | service_variance_to_benchmark | numeric |
| Cleanliness_Current | number | cleanliness_current | numeric |
| Cleanliness_Last_month | number | cleanliness_last_month | numeric |
| Cleanliness_six_month | number | cleanliness_six_month | numeric |
| Cleanliness_Benchmark | number | cleanliness_benchmark | numeric |
| Cleanliness_Variance_to_benchmark | number | cleanliness_variance_to_benchmark | numeric |
| Honor_Current | number | honor_current | numeric |
| Honor_Last_month | number | honor_last_month | numeric |
| Honor_six_month | number | honor_six_month | numeric |
| Honor_Benchmark | number | honor_benchmark | numeric |
| Honor_Variance_to_benchmark | number | honor_variance_to_benchmark | numeric |
| Brand_Promise_Current | number | brand_promise_current | numeric |
| Brand_Promise_Last_month | number | brand_promise_last_month | numeric |
| Brand_Promise_six_month | number | brand_promise_six_month | numeric |
| Brand_Promise_Benchmark | number | brand_promise_benchmark | numeric |
| Brand_Promise_Variance_to_benchmark | number | brand_promise_variance_to_benchmark | numeric |
| F&B_Exp_Current | number | f_b_exp_current | numeric |
| F&B_Exp_Last_month | number | f_b_exp_last_month | numeric |
| F&B_Exp_six_month | number | f_b_exp_six_month | numeric |
| F&B_Exp_Benchmark | number | f_b_exp_benchmark | numeric |
| F&B_Exp_Variance_to_benchmark | number | f_b_exp_variance_to_benchmark | numeric |
| F&B_Svc_Current | number | f_b_svc_current | numeric |
| F&B_Svc_Last_month | number | f_b_svc_last_month | numeric |
| F&B_Svc_six_month | number | f_b_svc_six_month | numeric |
| F&B_Svc_Benchmark | number | f_b_svc_benchmark | numeric |
| F&B_Svc_Variance_to_benchmark | number | f_b_svc_variance_to_benchmark | numeric |
| Maint_Current | number | maint_current | numeric |
| Maint_Last_month | number | maint_last_month | numeric |
| Maint_six_month | number | maint_six_month | numeric |
| Maint_Benchmark | number | maint_benchmark | numeric |
| Maint_Variance_to_benchmark | number | maint_variance_to_benchmark | numeric |
