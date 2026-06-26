# Calculated Fields — To Solve Later

_777 computed fields across 40 tables. These are **not** stored columns; recreate them as views / generated columns after base data is syncing._

## Proposed recreation by type

| Airtable type | Count | Proposed Postgres approach |
|---|---|---|
| formula | 322 | Postgres generated column or view expression |
| multipleLookupValues | 297 | JOIN to the linked table in a view (returns array) |
| rollup | 127 | Aggregate (SUM/AVG/etc.) in a view over the linked child rows |
| lastModifiedTime | 13 | updated_at timestamptz via trigger |
| createdTime | 8 | created_at timestamptz default now() |
| lastModifiedBy | 6 | set by app / auth.uid() |
| autoNumber | 2 | bigserial / row_number() — usually drop |
| createdBy | 1 | set by app / auth.uid() |
| button | 1 | UI-only — drop |

## Investments  (151)
| Field | Type | Result | Logic |
|---|---|---|---|
| Est_PIP_cost | multipleLookupValues | currency | Asset_detail.[Est_PIP_cost] via link [Asset_detail_link] |
| Operating_balance | rollup | currency | Cash_accounts.[Latest_cash_balance] via link [Cash_accounts_link] |
| Quarter_end_operating_balance | rollup | currency | Cash_accounts.[Quarter_end_cash_balance] via link [Cash_accounts_link] |
| Reserve_balance | rollup | currency | Cash_accounts.[Latest_cash_balance] via link [Cash_accounts_link] |
| Quarter_end_reserve_balance | rollup | currency | Cash_accounts.[Quarter_end_cash_balance] via link [Cash_accounts_link] |
| PIP_balance | rollup | currency | Cash_accounts.[Latest_cash_balance] via link [Cash_accounts_link] |
| Quarter_end_PIP_balance | rollup | currency | Cash_accounts.[Quarter_end_cash_balance] via link [Cash_accounts_link] |
| TTM_total_operating_revenue | rollup | currency | Asset_detail.[TTM_total_operating_revenue] via link [Asset_detail_link] |
| TTM_NOI | rollup | currency | Asset_detail.[TTM_NOI] via link [Asset_detail_link] |
| Adj_TTM_NOI | rollup | currency | Asset_detail.[TTM_adjusted_NOI] via link [Asset_detail_link] |
| Latest_cap_rate_date | rollup | date | Investments_market_value.[Cap_rate_date] via link [Investments_market_value_link] |
| Latest_cap_rate | multipleLookupValues | percent | Investments_market_value.[Latest_cap_rate] via link [Investments_market_value_link] |
| TTM_valuation | formula | currency | {Adj_TTM_NOI}/{Latest_cap_rate} |
| Latest_valuation_date | rollup | date | Investments_market_value.[Date] via link [Investments_market_value_link] |
| Latest_valuation_method | multipleLookupValues | singleSelect | Investments_market_value.[Valuation_method] via link [Investments_market_value_link] |
| Latest_valuation | rollup | currency | Investments_market_value.[Latest_valuation] via link [Investments_market_value_link] |
| Appfolio_value | rollup | currency | Investments_market_value.[Appfolio_value] via link [Investments_market_value_link] |
| Asset_number | multipleLookupValues | singleLineText | Asset_detail.[Asset_number] via link [Asset_detail_link] |
| Latest_debt_balance_date | rollup | date | Loan_summary_data.[Latest_balance_date] via link [Loan_summary_data_link] |
| Latest_debt_balance | rollup | currency | Loan_summary_data.[Latest_debt_balance] via link [Loan_summary_data_link] |
| Latest_net_equity | formula | currency | {Latest_valuation}-{Latest_debt_balance} |
| Sale_cash_disbursement | formula | currency | {Sale_price}-{Selling_expense} |
| Taxable_capital_gain | formula | currency | {Sale_cash_disbursement}-{2024_tax_net_book_val.} |
| Total_capital_gain | formula | currency | {ST_capital_gain}+{LT_capital_gain} |
| Monthly_debt_payment | rollup | currency | Loan_summary_data.[Monthly_debt_payment] via link [Loan_summary_data_link] |
| TTM_debt_payment | rollup | currency | Asset_detail.[TTM_debt_payment] via link [Asset_detail_link] |
| TTM_cash_flow | rollup | currency | Hotel_actuals.[Cash_flow] via link [Hotel_actuals_link] |
| 2022_tax_net_book_value | formula | currency | {Tax_cost}-{2022_tax_end_depreciation} |
| TTM_valuation_variance | formula | currency | {Latest_valuation}-{TTM_valuation} |
| LTV | formula | percent | {Latest_debt_balance}/{Latest_valuation} |
| Room_count | multipleLookupValues | number | Asset_detail.[Room_count] via link [Asset_detail_link] |
| Value_per_key | formula | currency | {Latest_valuation}/{Room_count} |
| Debt_per_key | formula | currency | {Latest_debt_balance}/{Room_count} |
| Equity_recap | formula | currency | {Latest_valuation}-{Latest_debt_balance}-({Latest_valuation}*.05) |
| City | multipleLookupValues | singleSelect | Asset_detail.[City] via link [Asset_detail_link] |
| State | multipleLookupValues | singleSelect | Asset_detail.[State] via link [Asset_detail_link] |
| MOIC | formula | number | {Total_distributed}/{Total_contributed} |
| TTM_LTV | formula | percent | {Latest_debt_balance}/{TTM_valuation} |
| Renovation_internal_target_end_date | multipleLookupValues | date | Asset_detail.[Renovation_internal_target_end_date] via link [Asset_detail_link] |
| Implied_cap_rate_TTM | formula | percent | {TTM_NOI}/{Latest_valuation} |
| Hotel_brand | multipleLookupValues | multipleRecordLinks | Asset_detail.[Hotel_brand_metrics_link] via link [Asset_detail_link] |
| Open_year | multipleLookupValues | number | Asset_detail.[Open_year] via link [Asset_detail_link] |
| YE23_est_interest_expense | rollup | currency | Loan_summary_data.[YE23_est_interest_expense] via link [Loan_summary_data_link] |
| YE24_est_interest_expense | rollup | currency | Loan_summary_data.[YE24_est_interest_expense] via link [Loan_summary_data_link] |
| YE25_est_interest_expense | rollup | currency | Loan_summary_data.[YE25_est_interest_expense] via link [Loan_summary_data_link] |
| YE26_est_interest_expense | rollup | currency | Loan_summary_data.[YE26_est_interest_expense] via link [Loan_summary_data_link] |
| YE27_est_interest_expense | rollup | currency | Loan_summary_data.[YE27_est_interest_expense] via link [Loan_summary_data_link] |
| YE28_est_interest_expense | rollup | currency | Loan_summary_data.[YE28_est_interest_expense] via link [Loan_summary_data_link] |
| Last_updated | lastModifiedTime | dateTime |  |
| Latest_cash_balance_date | rollup | date | Cash_accounts.[Latest_balance_date] via link [Cash_accounts_link] |
| Debt_recourse | multipleLookupValues | singleSelect | Loan_summary_data.[Debt_recourse] via link [Loan_summary_data_link] |
| Latest_financials_date | rollup | date | Hotel_actuals.[Date] via link [Hotel_actuals_link] |
| Latest_forecast_date | rollup | date | Hotel_forecast.[Forecast_period] via link [Hotel_forecast_link] |
| Hotel_anonymous_reference | multipleLookupValues | singleLineText | Asset_detail.[Hotel_anonymous_reference] via link [Asset_detail_link] |
| Asset_age | multipleLookupValues | number | Asset_detail.[Asset_age] via link [Asset_detail_link] |
| PIP_funding_strategy | multipleLookupValues | singleSelect | Asset_detail.[PIP_funding_strategy] via link [Asset_detail_link] |
| Est_PIP_cost_per_key | formula | currency | {Est_PIP_cost}/{Room_count} |
| Open_committment | formula | currency | {Total_committed}- {Total_contributed} |
| Years_until_PIP | formula | number | IF({Renovation_internal_target_end_date}=BLANK(),BLANK(),DATETIME_DIFF({Renovation_internal_target_end_date},TODAY(),'days')/365) |
| Remaining_franchise_term_years | multipleLookupValues | number | Asset_detail.[Remaining_franchise_term_years] via link [Asset_detail_link] |
| 2024_NOI | rollup | currency | Hotel_actuals.[EBITDA_NOI] via link [Hotel_actuals_link] |
| 2024_taxable_income | formula | currency | {2024_NOI}-{2024_total_depreciation}-{YE24_est_interest_expense} |
| 2024_cash_flow | rollup | currency | Hotel_actuals.[Cash_flow] via link [Hotel_actuals_link] |
| Forecasted_cash_flow_for_PIP | formula | currency | IF(
  {Years_until_PIP}=BLANK()
,BLANK()
,IF({Years_until_PIP}<0,BLANK(),{2025_Act+Bud_cash_flow}*{Years_until_PIP})) |
| Post_PIP_cash_reserve | formula | currency | IF(OR({Est_PIP_cost}=0,{Est_PIP_cost}=BLANK())
,
BLANK()
,
{Forecasted_cash_flow_for_PIP}
+{Reserve_balance}
-{Est_PIP_cost}) |
| TTM_DSCR | formula | number | IF({TTM_debt_payment}=BLANK(),BLANK(),{Adj_TTM_NOI}/{TTM_debt_payment}) |
| Loan_maturity | multipleLookupValues | date | Loan_summary_data.[Loan_maturity] via link [Loan_summary_data_link] |
| PIP_funding_status | formula | singleSelect | IF(OR({Years_until_PIP}<=0,"",{Post_PIP_cash_reserve}>0),"Property Funded","Needs Capital") |
| Latest_month_NOI | rollup | currency | Hotel_actuals.[EBITDA_NOI] via link [Hotel_actuals_link] |
| Latest_month_cash_flow | rollup | currency | Hotel_actuals.[Cash_flow] via link [Hotel_actuals_link] |
| TTM_GOP | rollup | currency | Asset_detail.[TTM_GOP] via link [Asset_detail_link] |
| Latest_month_DSCR | formula | number | IF(OR({Monthly_debt_payment}=BLANK(),{Latest_month_adjusted_NOI}=BLANK()),BLANK(),ROUND({Latest_month_adjusted_NOI},2)/{Monthly_debt_payment}) |
| 2024_total_depreciation | formula | currency | {2024_depreciation}+
({2024_acquisition_bonus_depreciation}+
{2024_PIP_depreciation}+
{2024_new_build_depreciation})*.6 |
| YE24_actual_interest_expense | rollup | currency | Hotel_actuals.[Interest_expense] via link [Hotel_actuals_link] |
| TTM_debt_yield | formula | percent | IF(OR({Latest_debt_balance}=BLANK(),{TTM_NOI}=BLANK()),BLANK(),{TTM_NOI}/{Latest_debt_balance}) |
| Interest_rate_reset_date | multipleLookupValues | date | Loan_summary_data.[Interest_rate_reset_date] via link [Loan_summary_data_link] |
| Interest_rate | multipleLookupValues | number | Loan_summary_data.[Interest_rate] via link [Loan_summary_data_link] |
| Total_loan_principal | rollup | currency | Loan_summary_data.[Initial_principal] via link [Loan_summary_data_link] |
| Quarterly_loan_paydown_rollup | rollup | currency | Loan_summary_data.[Latest_quarter_debt_paydown] via link [Loan_summary_data_link] |
| Quarterly_loan_paydown | formula | currency | IF({Quarterly_loan_paydown_rollup}=0,BLANK(),
IF({Quarter_loan_paydown_manual_adj}>BLANK(),
{Quarter_loan_paydown_manual_adj},{Quarterly_loan_paydown_rollup}
)) |
| 2025_NOI_actuals | rollup | currency | Hotel_actuals.[EBITDA_NOI] via link [Hotel_actuals_link] |
| 2025_NOI_budget | rollup | currency | Hotel_budget.[EBITDA_NOI] via link [Hotel_budget_link] |
| 2025_NOI_Act+Bud | formula | currency | {2025_NOI_actuals}+{2025_NOI_budget}*.8
 |
| 2025_Act+Bud_cash_flow | formula | currency | {2025_NOI_Act+Bud}-{TTM_debt_payment} |
| 2025_Act+Bud_taxable_income | formula | currency | IF(OR({Investment_status}="Active",{Investment_status}="Active - Construction"),{2025_NOI_Act+Bud}+{CY_cash_interest_income_estimate}-{2025_total_depreciation}-{YE25_est_interest_expense},BLANK()) |
| 2025_total_depreciation | formula | currency | {2025_depreciation}+
({2025_acquisition_bonus_depreciation}+
{2025_PIP_depreciation}+
{2025_new_build_depreciation}) |
| 2025_distributions | rollup | currency | Distributions.[Amount] via link [Distributions] |
| NOI_needed_to_exit | formula | currency | {Target_exit_value}*{Target_exit cap_rate} |
| NOI_gap_vs._target | formula | currency | {NOI_needed_to_exit}-{TTM_NOI} |
| NOI_gap_vs._target_% | formula | percent | IF({NOI_needed_to_exit}=BLANK(),BLANK(),({NOI_needed_to_exit}-{TTM_NOI})/{TTM_NOI}) |
| 25_yr_refi_variance | multipleLookupValues | currency | Debt_resizing.[25_yr_refi_variance] via link [Debt_resizing_link] |
| Monthly_debt_payment_date | multipleLookupValues | number | Loan_summary_data.[Monthly_debt_payment_date] via link [Loan_summary_data_link] |
| 2025_NOI_forecast | rollup | currency | Hotel_forecast.[EBITDA_NOI] via link [Hotel_forecast_link] |
| 2025_NOI_budget_ex_fcst | rollup | currency | Hotel_budget.[EBITDA_NOI] via link [Hotel_budget_link] |
| 2025_NOI_Act+Fcst+Bud | formula | currency | {2025_NOI_actuals}+{2025_NOI_forecast}+{2025_NOI_budget_ex_fcst}
 |
| Hotel_franchise | multipleLookupValues | multipleRecordLinks | Asset_detail.[Hotel_brand_metrics_link] via link [Asset_detail_link] |
| CY_cash_interest_income_estimate | rollup | currency | Cash_accounts.[CY_interest_income_estimate] via link [Cash_accounts_link] |
| 2025_cash_flow_Act+Fcst+Bud | formula | currency | {2025_NOI_actuals}+{2025_NOI_forecast}+{2025_NOI_budget_ex_fcst}-{TTM_debt_payment}
 |
| YTD_cash_flow | rollup | currency | Hotel_actuals.[Cash_flow] via link [Hotel_actuals_link] |
| YE29_est_interest_expense | rollup | currency | Loan_summary_data.[YE29_est_interest_expense] via link [Loan_summary_data_link] |
| YE30_est_interest_expense | rollup | currency | Loan_summary_data.[YE30_est_interest_expense] via link [Loan_summary_data_link] |
| YE31_est_interest_expense | rollup | currency | Loan_summary_data.[YE31_est_interest_expense] via link [Loan_summary_data_link] |
| YE32_est_interest_expense | rollup | currency | Loan_summary_data.[YE32_est_interest_expense] via link [Loan_summary_data_link] |
| YE33_est_interest_expense | rollup | currency | Loan_summary_data.[YE33_est_interest_expense] via link [Loan_summary_data_link] |
| YE34_est_interest_expense | rollup | currency | Loan_summary_data.[YE34_est_interest_expense] via link [Loan_summary_data_link] |
| YE35_est_interest_expense | rollup | currency | Loan_summary_data.[YE35_est_interest_expense] via link [Loan_summary_data_link] |
| Latest_month_adjusted_NOI | rollup | currency | Hotel_actuals.[Adjusted_NOI] via link [Hotel_actuals_link] |
| TTM_DSCR_non_adjusted | formula | number | IF({TTM_debt_payment}=BLANK(),BLANK(),{TTM_NOI}/{TTM_debt_payment}) |
| Guarantee_structure | multipleLookupValues | singleSelect | Loan_summary_data.[Guarantee_structure] via link [Loan_summary_data_link] |
| 2026_NOI_actuals | rollup | currency | Hotel_actuals.[EBITDA_NOI] via link [Hotel_actuals_link] |
| Internal_asset_name | multipleLookupValues | singleLineText | Asset_detail.[Internal_asset_name] via link [Asset_detail_link] |
| SP_ownership | rollup | percent | Investment_positions.[L1_ownership_percentage] via link [Investment_positions_link] |
| Reporting_category_breakdown | multipleLookupValues | singleSelect | Investment_positions.[Reporting_category_breakdown] via link [Investment_positions_link] |
| Lenders | multipleLookupValues | multipleRecordLinks | Loan_summary_data.[Lenders_link] via link [Loan_summary_data_link] |
| 2026_NOI_budget | rollup | currency | Hotel_budget.[EBITDA_NOI] via link [Hotel_budget_link] |
| 2026_Act+Bud_cash_flow | formula | currency | {2026_NOI_Act+Bud}-{TTM_debt_payment} |
| 2026_NOI_Act+Bud | formula | currency | {2026_NOI_actuals}+{2026_NOI_budget}
 |
| 2026_NOI_forecast | rollup | currency | Hotel_forecast.[EBITDA_NOI] via link [Hotel_forecast_link] |
| 2026_NOI_Act+Fcst+Bud | formula | currency | {2026_NOI_actuals}+{2026_NOI_forecast}+{2026_NOI_budget_ex_fcst}
 |
| 2026_NOI_budget_ex_fcst | rollup | currency | Hotel_budget.[EBITDA_NOI] via link [Hotel_budget_link] |
| 2026_total_depreciation | formula | currency | {2026_depreciation}+
({2026_acquisition_bonus_depreciation}+
{2026_PIP_depreciation}+
{2026_new_build_depreciation}) |
| 2026_Act+Bud_taxable_income | formula | currency | IF(OR({Investment_status}="Active",{Investment_status}="Active - Construction"),{2026_NOI_Act+Bud}+{CY_cash_interest_income_estimate}-{2026_total_depreciation}-{YE26_est_interest_expense},BLANK()) |
| 2026_DSCR_non_adjusted_Act+Fcst+Bud | formula | number | {2026_NOI_Act+Fcst+Bud}/{Monthly_debt_payment}*12 |
| Amortization | multipleLookupValues | singleLineText | Loan_summary_data.[Amortization_months] via link [Loan_summary_data_link] |
| Purchase_price | multipleLookupValues | currency | Asset_detail.[Purchase_price] via link [Asset_detail_link] |
| AP_FamCo_ownership_flowthrough | rollup | percent | Investment_positions.[AP_FamCo_ownership_flowthrough] via link [Investment_positions_link] |
| SP_FamCo_ownership_flowthrough | rollup | percent | Investment_positions.[SP_FamCo_ownership_flowthrough] via link [Investment_positions_link] |
| AP_FamCo_ownership_L1 | rollup | percent | Investment_positions.[L1_ownership_percentage] via link [Investment_positions_link] |
| SP_FamCo_ownership_L1 | rollup | percent | Investment_positions.[L1_ownership_percentage] via link [Investment_positions_link] |
| AP_FamCo_ownership | formula | percent | {AP_FamCo_ownership_flowthrough}+{AP_FamCo_ownership_L1} |
| SP_FamCo_ownership | formula | percent | {SP_FamCo_ownership_flowthrough}+{SP_FamCo_ownership_L1} |
| EPL_ownership | rollup | percent | Investment_positions.[L1_ownership_percentage] via link [Investment_positions_link] |
| Founders_Fund_ownership | formula | percent | {Founders_fund_ownership_L1}+{Founders_fund_ownership_flowthrough} |
| Witness_external_ownership_L1 | rollup | percent | Investment_positions.[L1_ownership_percentage] via link [Investment_positions_link] |
| Witness_external_ownership_flowthrough | rollup | percent | Investment_positions.[Witness_external_ownership_flowthrough] via link [Investment_positions_link] |
| Witness_external_ownership | formula | percent | {Witness_external_ownership_L1}+{Witness_external_ownership_flowthrough} |
| Founders_fund_ownership_L1 | rollup | percent | Investment_positions.[L1_ownership_percentage] via link [Investment_positions_link] |
| Founders_fund_ownership_flowthrough | rollup | percent | Investment_positions.[Founders_fund_ownership_flowthrough] via link [Investment_positions_link] |
| AP_loan_guarantee | multipleLookupValues | singleSelect | Loan_summary_data.[AP_guarantee] via link [Loan_summary_data_link] |
| SP_loan_guarantee | multipleLookupValues | singleSelect | Loan_summary_data.[SP_guarantee] via link [Loan_summary_data_link] |
| Pre-Payment | multipleLookupValues | date | Loan_summary_data.[Pre_payment_end_date] via link [Loan_summary_data_link] |
| Loan_origination_date | multipleLookupValues | date | Loan_summary_data.[Loan_origination_date] via link [Loan_summary_data_link] |
| Record_id | formula | singleLineText | RECORD_ID() |
| Annual_debt_payment_rollup | rollup | currency | Loan_summary_data.[Annual_debt_payment] via link [Loan_summary_data_link] |
| 2026_cash_flow_act+fcst+bud | formula | currency | {2026_NOI_Act+Fcst+Bud} - {Annual_debt_payment_rollup} |
| 2026_fcst_CoC_Return | formula | percent | {2026_cash_flow_act+fcst+bud}/{Equity_contributed} |
| 2026_distributions | rollup | currency | Distributions.[Amount] via link [Distributions] |
| annual_debt_payment | formula | number | {Monthly_debt_payment} * 12 |
| RE_tax_1st_half_date | formula | date | IF(
  {RE_tax_1st_half_due_date} = BLANK(), BLANK(),
  IF(
    DATETIME_PARSE({RE_tax_1st_half_due_date} & "/" & YEAR(TODAY()), "M/D/YYYY") < TODAY(),
    DATETIME_PARSE({RE_tax_1st_half_due_date} & "/" & (YEAR(TODAY())+1), "M/D/YYYY"),
    DATETIME_PARSE({RE_tax_1st_half_due_date} & "/" & YEAR(TODAY()), "M/D/YYYY")
  )
) |
| RE_tax_2nd_half_date | formula | date | IF(
  {RE_tax_2nd_half_due_date} = BLANK(), BLANK(),
  IF(
    DATETIME_PARSE({RE_tax_2nd_half_due_date} & "/" & YEAR(TODAY()), "M/D/YYYY") < TODAY(),
    DATETIME_PARSE({RE_tax_2nd_half_due_date} & "/" & (YEAR(TODAY())+1), "M/D/YYYY"),
    DATETIME_PARSE({RE_tax_2nd_half_due_date} & "/" & YEAR(TODAY()), "M/D/YYYY")
  )
) |
| Date added | createdTime | date |  |

## Asset_detail  (97)
| Field | Type | Result | Logic |
|---|---|---|---|
| Asset_detail_id | formula | singleLineText | {Asset_number} |
| Open_year | formula | number | YEAR({Open_date}) |
| Last_renovation_year | multipleLookupValues | number | STR_comp_set.[Latest_renovation_date] via link [STR_comp_set_link] |
| Latest_actuals_date | rollup | date | Hotel_actuals.[Date] via link [Hotel_actuals_link] |
| Investment_status | multipleLookupValues | singleSelect | Investments.[Investment_status] via link [Investments_link] |
| Asset_subclass | multipleLookupValues | singleSelect | Investments.[Asset_subclass] via link [Investments_link] |
| Hotel_brand | multipleLookupValues | singleSelect | Hotel_brand_metrics.[Hotel_brand] via link [Hotel_brand_metrics_link] |
| Brand_acronym | multipleLookupValues | singleSelect | Hotel_brand_metrics.[Brand_acronym] via link [Hotel_brand_metrics_link] |
| Scale | multipleLookupValues | singleSelect | Hotel_brand_metrics.[Scale] via link [Hotel_brand_metrics_link] |
| Renovation_plan_start | formula | date | IF({PIP_brand_renovation_due_date}=BLANK()
,BLANK()
,DATEADD(
  DATEADD({PIP_brand_renovation_due_date},1,'day')
  ,-9,'month')
) |
| Est_PIP_cost | formula | currency | {Est_PIP_cost_per_key}*{Room_count} |
| Appfolio_valuation | multipleLookupValues | currency | Investments.[Appfolio_value] via link [Investments_link] |
| LTV | multipleLookupValues | percent | Investments.[LTV] via link [Investments_link] |
| TTM_LTV | multipleLookupValues | percent | Investments.[TTM_LTV] via link [Investments_link] |
| Target_operating_balance | multipleLookupValues | currency | Investments.[Target_operating_balance] via link [Investments_link] |
| Target_reserve_balance | multipleLookupValues | currency | Investments.[Target_reserve_balance] via link [Investments_link] |
| TTM_total_operating_revenue | rollup | currency | Hotel_actuals.[Total_operating_revenue] via link [Hotel_actuals_link] |
| TTM_NOI | rollup | currency | Hotel_actuals.[EBITDA_NOI] via link [Hotel_actuals_link] |
| TTM_adjusted_NOI | rollup | currency | Hotel_actuals.[Adjusted_NOI] via link [Hotel_actuals_link] |
| TTM_debt_payment | rollup | currency | Hotel_actuals.[Monthly_debt_payment_manual_input] via link [Hotel_actuals_link] |
| Monthly_debt_payment | multipleLookupValues | currency | Investments.[Monthly_debt_payment] via link [Investments_link] |
| TTM_cash_flow | formula | currency | {TTM_NOI}-{TTM_debt_payment} |
| Latest_month_NOI | rollup | currency | Hotel_actuals.[EBITDA_NOI] via link [Hotel_actuals_link] |
| Latest_month_dscr | formula | number | {Latest_month_adjusted_NOI}/{Monthly_debt_payment} |
| Latest_debt_balance | rollup | currency | Investments.[Latest_debt_balance] via link [Investments_link] |
| Total_contributed | multipleLookupValues | currency | Investments.[Total_contributed] via link [Investments_link] |
| Total_cost | formula | currency | {Total_contributed}+{Total_loan_principal} |
| TTM_DSCR | formula | number | {TTM_adjusted_NOI}/{TTM_debt_payment} |
| TTM_debt_yield | formula | percent | {TTM_NOI}/{Latest_debt_balance} |
| TTM_ADR | formula | currency | IF(ISERROR({TTM_room_revenue}/{TTM_rooms_sold}),0,{TTM_room_revenue}/{TTM_rooms_sold}) |
| TTM_occupancy_% | formula | percent | IF(ISERROR({TTM_rooms_sold}/{TTM_available_rooms}),0,{TTM_rooms_sold}/{TTM_available_rooms}) |
| TTM_RevPar | formula | currency | {TTM_ADR}*{TTM_occupancy_%} |
| Tax_sale_year | formula | number | IF({Sale_date}=BLANK(),BLANK(),YEAR({Sale_date})) |
| Renovation_plan_start_year | formula | number | IF({Renovation_plan_start}=BLANK()
,BLANK()
,YEAR({Renovation_plan_start})
) |
| TTM_GOP | rollup | currency | Hotel_actuals.[Gross_operating_profit] via link [Hotel_actuals_link] |
| TTM_GOP_% | formula | percent | IF(ISERROR({TTM_GOP}/{TTM_total_operating_revenue}),0,{TTM_GOP}/{TTM_total_operating_revenue}) |
| Created_time | createdTime | dateTime |  |
| Last_modified_by | lastModifiedBy |  |  |
| TTM_valuation | multipleLookupValues | currency | Investments.[TTM_valuation] via link [Investments_link] |
| Valuation_variance | formula | currency |  {TTM_valuation}-{Appfolio_valuation} |
| TTM_cap_rate | multipleLookupValues | percent | Investments.[Latest_cap_rate] via link [Investments_link] |
| YTD_rooms_sold | rollup | number | Hotel_actuals.[Occupied_rooms] via link [Hotel_actuals_link] |
| YTD_available_rooms | rollup | number | Hotel_actuals.[Available_rooms] via link [Hotel_actuals_link] |
| YTD_occupancy_% | formula | percent | IF(ISERROR({YTD_rooms_sold}/{YTD_available_rooms}),0,{YTD_rooms_sold}/{YTD_available_rooms}) |
| YTD_room_revenue | rollup | currency | Hotel_actuals.[Rooms_sales] via link [Hotel_actuals_link] |
| YTD_ADR | formula | currency | IF(ISERROR({YTD_room_revenue}/{YTD_rooms_sold}),0,{YTD_room_revenue}/{YTD_rooms_sold}) |
| YTD_RevPAR | formula | currency | {YTD_occupancy_%}*{YTD_ADR} |
| TTM_rooms_sold | rollup | number | Hotel_actuals.[Occupied_rooms] via link [Hotel_actuals_link] |
| TTM_available_rooms | rollup | number | Hotel_actuals.[Available_rooms] via link [Hotel_actuals_link] |
| TTM_room_revenue | rollup | currency | Hotel_actuals.[Rooms_sales] via link [Hotel_actuals_link] |
| Asset_age | formula | number | IF({Open_year}=BLANK(),{Open_year},YEAR(TODAY())-{Open_year}) |
| Rate_reset | multipleLookupValues | date | Investments.[Interest_rate_reset_date] via link [Investments_link] |
| DOS_tenure_years | formula | number | IF({DOS_hire_date} = BLANK(), BLANK(), DATETIME_DIFF(TODAY(), {DOS_hire_date}, 'Months')/12) |
| GM_tenure_years | formula | number | IF({GM_hire_date} = BLANK(), BLANK(), DATETIME_DIFF(TODAY(), {GM_hire_date}, 'months')/12) |
| SM_tenure_years | formula | number | IF({SM_hire_date} = BLANK(), BLANK(), DATETIME_DIFF(TODAY(), {SM_hire_date}, 'months')/12) |
| YTD_Revenue_actual | rollup | currency | Hotel_actuals.[Total_operating_revenue] via link [Hotel_actuals_link] |
| YTD_Revenue_budget | rollup | currency | Hotel_budget.[Total_operating_revenue] via link [Hotel_budget_link] |
| YTD_GOP_actual | rollup | currency | Hotel_actuals.[Gross_operating_profit] via link [Hotel_actuals_link] |
| YTD_GOP_budget | rollup | currency | Hotel_budget.[Gross_operating_profit] via link [Hotel_budget_link] |
| Loan_maturity | multipleLookupValues | date | Investments.[Loan_maturity] via link [Investments_link] |
| Latest_valuation_balance | multipleLookupValues | currency | Investments.[Latest_valuation] via link [Investments_link] |
| Construction_start_quarter | formula | singleLineText | IF({Construction_start_date}=BLANK(),BLANK(),"Q"&DATETIME_FORMAT({Construction_start_date},'Q')) |
| Construction_start_year | formula | number | IF({Construction_start_date}=BLANK(),BLANK(),YEAR({Construction_start_date})) |
| Construction_start_month | formula | number | IF({Construction_start_date}=BLANK(),BLANK(),MONTH({Construction_start_date})) |
| Renovation_target_year | formula | number | IF(
  {Renovation_internal_target_end_date}=BLANK(),
  BLANK(),
  YEAR({Renovation_internal_target_end_date})
) |
| Renovation_target_quarter | formula | singleLineText | IF({Renovation_internal_target_end_date}=BLANK(),BLANK(),"Q"&DATETIME_FORMAT(({Renovation_internal_target_end_date}),'Q')) |
| Renovation_target_month | formula | number | IF({Renovation_internal_target_end_date}=BLANK(),BLANK(),MONTH({Renovation_internal_target_end_date})
) |
| Brand_renovation_due_date_year | formula | number | IF(ISERROR(YEAR({PIP_brand_renovation_due_date})),BLANK(),YEAR({PIP_brand_renovation_due_date})) |
| Hotel_franchise | multipleLookupValues | multipleRecordLinks | Investments.[Hotel_franchise] via link [Investments_link] |
| Latest_forecast_date | rollup | date | Hotel_forecast.[Forecast_date] via link [Hotel_forecast_link] |
| Clickup_asset_naming | formula | singleLineText | {Asset_number}&" - "&{Franchise_acronym}&" "&{Market} |
| Franchise_acronym | multipleLookupValues | singleLineText | Hotel_brand_metrics.[Franchise_acronym] via link [Hotel_brand_metrics_link] |
| Remaining_franchise_term_years | formula | number | IF({Franchise_expiration}=BLANK(),BLANK(),DATETIME_DIFF({Franchise_expiration},TODAY(),'months')/12) |
| Total_loan_principal | multipleLookupValues | currency | Investments.[Total_loan_principal] via link [Investments_link] |
| Reporting_category | multipleLookupValues | multipleSelects | Investments.[Reporting_category] via link [Investments_link] |
| Latest_STR_28_day_trend_date | rollup | date | STR_28_day_trend.[End_date] via link [STR_28_day_trend_link] |
| Latest_STR_weekly_trend_date | rollup | date | STR_weekly_data.[End_date] via link [STR_weekly_data_link] |
| Latest_month_adjusted_NOI | rollup | currency | Hotel_actuals.[Adjusted_NOI] via link [Hotel_actuals_link] |
| Operating_balance | multipleLookupValues | currency | Investments.[Operating_balance] via link [Investments_link] |
| Reserve_balance | multipleLookupValues | currency | Investments.[Reserve_balance] via link [Investments_link] |
| Latest_str_actuals_date | rollup | date | STR_actuals.[Date] via link [STR_actuals_link] |
| YTD_NOI | rollup | currency | Hotel_actuals.[EBITDA_NOI] via link [Hotel_actuals_link] |
| YTD_cash_flow | formula | currency | {YTD_NOI}- {Annual_debt_service} |
| YTD_distributions | multipleLookupValues | currency | Investments.[2026_distributions] via link [Investments_link] |
| Debt_per_key | multipleLookupValues | currency | Investments.[Debt_per_key] via link [Investments_link] |
| Market_valuation | multipleLookupValues | currency | Investments.[Latest_valuation] via link [Investments_link] |
| Market_value_per_key | multipleLookupValues | currency | Investments.[Value_per_key] via link [Investments_link] |
| Supply_ttm | rollup | number | STR_actuals.[Supply] via link [STR_actuals_link] |
| Demand_ttm | rollup | number | STR_actuals.[Demand] via link [STR_actuals_link] |
| Revenue_ttm | rollup | currency | STR_actuals.[Revenue] via link [STR_actuals_link] |
| ADR_TTM | formula | currency |  {Revenue_ttm} / {Demand_ttm}  |
| Occupancy_TTM | formula | percent | {Demand_ttm} / {Supply_ttm} |
| RevPAR_TTM | formula | currency | {Revenue_ttm} / {Supply_ttm} |
| Annual_debt_service | rollup | currency | Hotel_actuals.[Monthly_debt_payment_manual_input] via link [Hotel_actuals_link] |
| EBITDA_actuals_fcst_bud_2026 | multipleLookupValues | currency | Investments.[2026_NOI_Act+Fcst+Bud] via link [Investments_link] |
| Annual_debt_payment | multipleLookupValues | currency | Investments.[annual_debt_payment] via link [Investments_link] |
| Cashflow_Payment_type | rollup | singleLineText | Cash_flow_tracking.[Payment_type] via link [Cash_flow_tracking] |

## Investments_market_value  (35)
| Field | Type | Result | Logic |
|---|---|---|---|
| Investments_market_value_id | formula | singleLineText | {Investments_link}&" - "&MONTH({Date})&"_"&YEAR({Date}) |
| Contributed_capital | multipleLookupValues | currency | Investments.[Total_contributed] via link [Investments_link] |
| Investment_status | multipleLookupValues | singleSelect | Investments.[Investment_status] via link [Investments_link] |
| TTM_adjusted_NOI | multipleLookupValues | currency | Investments.[Adj_TTM_NOI] via link [Investments_link] |
| TTM_valuation | formula | currency | {TTM_adjusted_NOI}/{Cap_rate} |
| TTM_vs_market_value | formula | currency | {TTM_valuation}-{Market_value} |
| Latest_cap_rate_date | multipleLookupValues | date | Investments.[Latest_cap_rate_date] via link [Investments_link] |
| Latest_cap_rate | formula | percent | IF({Latest_cap_rate_date}={Date},{Cap_rate},BLANK()) |
| Latest_valuation_date | multipleLookupValues | date | Investments.[Latest_valuation_date] via link [Investments_link] |
| Latest_valuation | formula | currency | IF({Date}={Latest_valuation_date},{Market_value}) |
| Cash_flow | multipleLookupValues | currency | Investments.[TTM_cash_flow] via link [Investments_link] |
| Latest_debt_balance | multipleLookupValues | currency | Investments.[Latest_debt_balance] via link [Investments_link] |
| Net_equity_market_value | formula | currency | {Appfolio_value}-{Latest_debt_balance} |
| Room_count | multipleLookupValues | number | Investments.[Room_count] via link [Investments_link] |
| LTV | multipleLookupValues | percent | Investments.[LTV] via link [Investments_link] |
| Value_per_key | multipleLookupValues | currency | Investments.[Value_per_key] via link [Investments_link] |
| TTM_value_per_key | formula | number | {TTM_valuation}/{Room_count} |
| TTM_vs_market_value_per_key | formula | currency | {TTM_value_per_key}-{Value_per_key} |
| TTM_LTV | formula | percent | {Latest_debt_balance}/{TTM_valuation} |
| Debt_per_key | formula | currency | {Latest_debt_balance}/{Room_count} |
| Net_equity_per_key_market_value | formula | currency | {Net_equity_market_value}/{Room_count} |
| Net_equity_per_key_TTM | formula | currency | ({TTM_valuation}-{Latest_debt_balance})/{Room_count} |
| TTM_vs_market_LTV_variance | formula | percent | {TTM_LTV}- {LTV} |
| Net_equity_TTM | formula | currency | {TTM_valuation}-{Latest_debt_balance}
 |
| Hotel_brand | multipleLookupValues | multipleRecordLinks | Investments.[Hotel_franchise] via link [Investments_link] |
| Asset_number | multipleLookupValues | singleLineText | Investments.[Asset_number] via link [Investments_link] |
| Est_PIP_cost | multipleLookupValues | currency | Investments.[Est_PIP_cost] via link [Investments_link] |
| TTM_valuation_variance | multipleLookupValues | currency | Investments.[TTM_valuation_variance] via link [Investments_link] |
| Implied_cap_rate_TTM | multipleLookupValues | percent | Investments.[Implied_cap_rate_TTM] via link [Investments_link] |
| Latest_debt_balance_date | multipleLookupValues | date | Investments.[Latest_debt_balance_date] via link [Investments_link] |
| Renovation_plan_target_end_date | multipleLookupValues | date | Investments.[Renovation_internal_target_end_date] via link [Investments_link] |
| Asset_age | multipleLookupValues | number | Investments.[Asset_age] via link [Investments_link] |
| Appfolio_value_per_key | formula | currency | {Appfolio_value}/{Room_count} |
| Est_PIP_cost_per_key | multipleLookupValues | currency | Investments.[Est_PIP_cost_per_key] via link [Investments_link] |
| Remaining_franchise_term_years | multipleLookupValues | number | Investments.[Remaining_franchise_term_years] via link [Investments_link] |

## Investment_positions  (27)
| Field | Type | Result | Logic |
|---|---|---|---|
| Investment_positions_id | formula | singleLineText | 
{Investment_id}&"_"&{Investing_entities_link} |
| Distributions_rollup | rollup | currency | Distributions.[Amount] via link [Distributions_link] |
| Reporting_category_breakdown | multipleLookupValues | singleSelect | Investing_entities.[Reporting_category_breakdown] via link [Investing_entities_link] |
| Created_time | createdTime | dateTime |  |
| Last_modified_time | lastModifiedTime | dateTime |  |
| Last_modified_by | lastModifiedBy |  |  |
| L1_ownership_percentage_rollup | rollup | percent | Investment_positions.[L1_ownership_percentage] via link [L2_ownership_link] |
| L2_net_ownership_percentage | formula | percent | ({L1_ownership_percentage}*{L1_ownership_percentage_rollup}) |
| AP_FamCo_ownership_flowthrough | formula | percent | {AP_FamCo_ownership_L2}+{AP_FamCo_ownership_L3} |
| SP_FamCo_ownership_flowthrough | formula | percent | {SP_FamCo_ownership_L2}+{SP_FamCo_ownership_L3} |
| L2_ownership_percentage_rollup | rollup | percent | Investment_positions.[L1_ownership_percentage] via link [L3_ownership_link] |
| L3_net_ownership_percentage | formula | percent | ({L1_ownership_percentage}*{L2_ownership_percentage_rollup}) |
| AP_FamCo_ownership_L2 | rollup | percent | Investment_positions.[L2_net_ownership_percentage] via link [From field: L2_ownership_link] |
| SP_FamCo_ownership_L2 | rollup | percent | Investment_positions.[L2_net_ownership_percentage] via link [From field: L2_ownership_link] |
| AP_FamCo_ownership_L3_helper | rollup | percent | Investment_positions.[L3_net_ownership_percentage] via link [From field: L3_ownership_link] |
| SP_FamCo_ownership_L3_helper | rollup | percent | Investment_positions.[L3_net_ownership_percentage] via link [From field: L3_ownership_link] |
| Associated_asset_number | multipleLookupValues | singleLineText | Investments.[Associated_asset_number] via link [Investments_link] |
| Founders_Fund_ownership_L2 | rollup | percent | Investment_positions.[L2_net_ownership_percentage] via link [From field: L2_ownership_link] |
| Witness_external_ownership_flowthrough | formula | percent | {Witness_external_ownership_L2}+ {Witness_external_ownership_L3} |
| Witness_external_ownership_L2 | rollup | percent | Investment_positions.[L2_net_ownership_percentage] via link [From field: L2_ownership_link] |
| Witness_external_ownership_L3_helper | rollup | percent | Investment_positions.[L3_net_ownership_percentage] via link [From field: L3_ownership_link] |
| AP_FamCo_ownership_L3 | rollup | percent | Investment_positions.[AP_FamCo_ownership_L3_helper] via link [From field: L2_ownership_link] |
| SP_FamCo_ownership_L3 | rollup | percent | Investment_positions.[SP_FamCo_ownership_L3_helper] via link [From field: L2_ownership_link] |
| Witness_external_ownership_L3 | rollup | percent | Investment_positions.[Witness_external_ownership_L3_helper] via link [From field: L2_ownership_link] |
| Founders_fund_ownership_flowthrough | formula | percent | {Founders_Fund_ownership_L2}+{Founders_fund_ownership_L3} |
| Founders_fund_ownership_L3_helper | rollup | percent | Investment_positions.[L3_net_ownership_percentage] via link [From field: L3_ownership_link] |
| Founders_fund_ownership_L3 | rollup | percent | Investment_positions.[Founders_fund_ownership_L3_helper] via link [From field: L2_ownership_link] |

## Distributions  (13)
| Field | Type | Result | Logic |
|---|---|---|---|
| Distributions_id | formula | singleLineText | {Investment_positions_link_helper}&"_"&{Ref} |
| Month_number | formula | number | MONTH({Effective Date}) |
| Year | formula | number | YEAR({Effective Date}) |
| Quarter | formula | singleLineText | LEFT({Period},2) |
| Investment_positions_link_helper | formula | singleLineText | REGEX_REPLACE(CONCATENATE({Investments_link},"_",{Investing_entities_link}), '"', "") |
| Ref | autoNumber |  |  |
| Cash_flow_distribution | formula | currency | IF({Source}="Cash Flow",{Amount},0) |
| Sale_of_property_distribution | formula | currency | IF({Source}="Sale of Property",{Amount},0) |
| KV_FamCo | multipleLookupValues | singleSelect | Investment_positions.[Reporting_category_breakdown] via link [Investment_positions_link] |
| Last_modified_by | lastModifiedBy |  |  |
| Last_modified_time | lastModifiedTime | dateTime |  |
| FamCo_family_unit | multipleLookupValues |  | ?.[None] via link [Investing_entities_link] |
| Ownership % | multipleLookupValues | percent | Investment_positions.[L1_ownership_percentage] via link [Investment_positions_link] |

## Cash_accounts  (37)
| Field | Type | Result | Logic |
|---|---|---|---|
| Cash_accounts_id | formula | singleLineText | {Investments_link}&" - "&{Lenders_link}&" "&{Cash_account_subclass} |
| Asset_number | multipleLookupValues | singleLineText | Investments.[Asset_number] via link [Investments_link] |
| Latest_cash_balance | rollup | currency | Cash_balance_input.[Latest_balance] via link [Cash_balance_input_link] |
| Reserve_balance | rollup | currency | Cash_balance_input.[Latest_balance] via link [Cash_balance_input_link] |
| Asset_subclass | multipleLookupValues | singleSelect | Investments.[Asset_subclass] via link [Investments_link] |
| Operating_target_balance | multipleLookupValues | currency | Investments.[Target_operating_balance] via link [Investments_link] |
| Reserve_target_balance | multipleLookupValues | currency | Investments.[Target_reserve_balance] via link [Investments_link] |
| Latest_balance_date | rollup | date | Cash_balance_input.[Date] via link [Cash_balance_input_link] |
| Quarter_end_cash_balance | rollup | currency | Cash_balance_input.[Balance] via link [Cash_balance_input_link] |
| Cash_balance_variance | formula | currency | IF(
IF(
  OR({Cash_account_subclass} = "Operating - PIP", {Cash_account_subclass} = BLANK()),
    BLANK(),
    IF(
      {Cash_account_subclass} = "Operating",

        {Latest_cash_balance} - {Operating_target_balance},
        IF(
        OR({Cash_account_subclass} = "Reserve", {Cash_account_subclass} = "Reserve-Holding"),
          {Latest_cash_balance} - {Reserve_target_balance},
          BLANK()
      )
    )
) <0
,BLANK(),
IF(
  OR({Cash_account_subclass} = "Operating - PIP", {Cash_account_subclass} = BLANK()),
    BLANK(),
    IF(
      {Cash_account_subclass} = "Operating",

        {Latest_cash_balance} - {Operating_target_balance},
        IF(
        OR({Cash_account_subclass} = "Reserve", {Cash_account_subclass} = "Reserve-Holding"),
          {Latest_cash_balance} - {Reserve_target_balance},
          BLANK()
      )
    )
)
) |
| Operating_balance | rollup | currency | Cash_balance_input.[Latest_balance] via link [Cash_balance_input_link] |
| Operating_balance_variance | formula | currency | {Operating_balance}-{Operating_target_balance} |
| Reserve_balance_by_entity | multipleLookupValues | currency | Investments.[Reserve_balance] via link [Investments_link] |
| Reserve_balance_entity_variance | formula | currency | {Reserve_balance_by_entity}-{Reserve_target_balance} |
| Reserve_balance_variance | formula | currency | {Reserve_balance}-{Reserve_target_balance} |
| Renovation_plan_target_end_date | multipleLookupValues | date | Investments.[Renovation_internal_target_end_date] via link [Investments_link] |
| Est_PIP_cost | multipleLookupValues | currency | Investments.[Est_PIP_cost] via link [Investments_link] |
| Upcoming_PIP_target_met | formula | singleLineText | IF(
  AND(
    {PIP_funding_strategy} = "Cash Flow",
    {Reserve_balance_by_entity} > {Est_PIP_cost},
    {Time_until_PIP} <= 730,
    {Time_until_PIP} > 0,
    {Time_until_PIP}!= BLANK()
    ),
    "Yes",
    IF(
      AND(
        {PIP_funding_strategy} = "Cash Flow",
        {Reserve_balance_by_entity} < {Est_PIP_cost},
        {Time_until_PIP} <= 730,
        {Time_until_PIP} > 0,
        {Time_until_PIP}!= BLANK()
      ),
      "No",
      ""
    )
) |
| Reserve_to_PIP_variance | formula | currency | IF({Reserve_last_four}=BLANK()
,BLANK()
,{Reserve_balance_by_entity}-{Est_PIP_cost}
) |
| Investment_status | multipleLookupValues | singleSelect | Investments.[Investment_status] via link [Investments_link] |
| Cresset_naming_convention | formula | singleLineText | {Investments_link}&"_"&{Lenders_link}&"_"&{Cash_account_subclass}&"_"&{Account_last_four} |
| Cash_balance_action | formula | singleLineText | IF(
  AND(
    {Account_status} = "Active",
    {Cash_account_subclass} = "Operating",
    OR(
      {Investment_status} = "Active",
      {Investment_status} = "Active - Construction",
      {Investment_status} = "Pending Sale",
      {Investment_status} = "Recap"
    ),
    {Cash_account_subclass} = "Operating",
    {Operating_balance_variance} < 0,
    {Reserve_balance_by_entity} > 0
  ),
  "Monitor Operating account or Fund with Reserve",
  IF(
    AND(
      {Account_status} = "Active",
      {Cash_account_subclass} = "Operating",
      OR(
        {Investment_status} = "Active",
        {Investment_status} = "Active - Construction",
        {Investment_status} = "Pending Sale",
        {Investment_status} = "Recap"
      ),
      {Cash_account_subclass} = "Operating",
      {Operating_balance} + {Reserve_balance_by_entity} < {Operating_target_balance}
    ),
    "Consider Capital Call",
    IF(
      AND(
        {Account_status} = "Active",
        {Cash_account_subclass} = "Operating",
        OR(
          {Investment_status} = "Active",
          {Investment_status} = "Active - Construction",
          {Investment_status} = "Pending Sale",
          {Investment_status} = "Recap"
        ),
        {Cash_account_subclass} = "Operating",
        {Operating_balance_variance} > 50000,
        {Reserve_balance_entity_variance} < 0
      ),
      "Fund Reserve",
      IF(
        AND(
          {Account_status} = "Active",
          {Cash_account_subclass} = "Operating",
          OR(
            {Investment_status} = "Active",
            {Investment_status} = "Active - Construction",
            {Investment_status} = "Pending Sale",
            {Investment_status} = "Recap"
          ),
          {Cash_account_subclass} = "Operating",
          {Operating_balance_variance} > 100000,
          {Reserve_balance_entity_variance} >= 0
        ),
        "Distribute funds",
        IF(
          AND(
            {Account_status} = "Active",
            {Cash_account_subclass} = "Reserve",
            OR(
              {Investment_status} = "Active",
              {Investment_status} = "Active - Construction",
              {Investment_status} = "Pending Sale",
              {Investment_status} = "Recap"
            ),
            {Cash_account_subclass} = "Reserve",
            OR(
              {Upcoming_PIP_target_met} = "Yes",
              {Upcoming_PIP_target_met} = BLANK()
            ),
            {Reserve_balance_entity_variance} > 100000
          ),
          "Transfer to Operating for Distribution",
          ""
        )
      )
    )
  )
) |
| Cash_action_amount | formula | currency | IF(AND({Cash_balance_action}="Monitor Operating account or Fund with Reserve", {Cash_account_subclass}="Operating"),
    -ROUNDDOWN({Operating_balance_variance},-3),
IF(
  {Cash_balance_action}="Consider Capital Call",
  ROUNDUP({Operating_target_balance} - {Operating_balance} - {Reserve_balance_by_entity},-4),
  IF(
    {Cash_balance_action}="Fund Reserve",
    ROUNDDOWN({Operating_balance_variance},-4),
    IF(AND({Cash_balance_action}="Distribute funds", {Cash_account_subclass}="Operating"),
    ROUNDDOWN({Operating_balance_variance},-4),
    IF(AND({Cash_balance_action}="Transfer to Operating for Distribution", {Cash_account_subclass}="Reserve"),
    ROUNDDOWN({Reserve_balance_variance},-4),
    BLANK()

    )

    )
  )
)
) |
| PIP_funding_strategy | multipleLookupValues | singleSelect | Investments.[PIP_funding_strategy] via link [Investments_link] |
| Time_until_PIP | formula | number | IF({Renovation_plan_target_end_date}=BLANK(),BLANK(),DATETIME_DIFF({Renovation_plan_target_end_date},TODAY(),'days')) |
| Operating_balance_by_entity | multipleLookupValues | currency | Investments.[Operating_balance] via link [Investments_link] |
| Monthly_debt_payment | multipleLookupValues | currency | Investments.[Monthly_debt_payment] via link [Investments_link] |
| Owner_comment_last_modified_time | lastModifiedTime | dateTime |  |
| Owner_comment_last_modified_by | lastModifiedBy |  |  |
| Monthly_debt_payment_date | multipleLookupValues | number | Investments.[Monthly_debt_payment_date] via link [Investments_link] |
| Last_modified_time_cresset_position_ID | lastModifiedTime | dateTime |  |
| Created_time | createdTime | dateTime |  |
| CY_interest_income_estimate | formula | currency | IF({YTD_avg_daily_interest_income}>0,
{YTD_avg_daily_interest_income}*365
,
BLANK()
) |
| YTD_avg_daily_interest_income | rollup | currency | Cash_balance_input.[Daily_interest] via link [Cash_balance_input_link] |
| State | multipleLookupValues | singleSelect | Investments.[State] via link [Investments_link] |
| Record_id | formula | singleLineText | RECORD_ID() |
| Reporting_category | multipleLookupValues | multipleSelects | Investments.[Reporting_category] via link [Investments_link] |

## Cash_balance_input  (14)
| Field | Type | Result | Logic |
|---|---|---|---|
| Cash_balance_input_id | formula | singleLineText | {Cash_accounts_link}&" - "&MONTH({Date})&"_"&DAY({Date})&"_"&YEAR({Date}) |
| Month | formula | number | MONTH({Date}) |
| Day | formula | number | DAY({Date}) |
| Year | formula | number | YEAR({Date}) |
| Lender | multipleLookupValues | multipleRecordLinks | Cash_accounts.[Lenders_link] via link [Cash_accounts_link] |
| Cash_account_subclass | multipleLookupValues | singleSelect | Cash_accounts.[Cash_account_subclass] via link [Cash_accounts_link] |
| Latest_balance_date | multipleLookupValues | date | Cash_accounts.[Latest_balance_date] via link [Cash_accounts_link] |
| Latest_balance | formula | currency | IF({Latest_balance_date}={Date},{Balance}) |
| Included_in_YTD | formula | singleLineText | IF({Year}=YEAR(TODAY()),"Yes","") |
| Daily_interest | formula | currency | IF(OR({Cash_account_subclass}="Reserve", {Cash_account_subclass}="Reserve-Holding")
,{Balance}*.043/365
,BLANK()
) |
| Asset_number | multipleLookupValues | singleLineText | Investments.[Asset_number] via link [Investments_link] |
| Created_time | createdTime | dateTime |  |
| Last_modified_by | lastModifiedBy |  |  |
| Last_modified_time | lastModifiedTime | dateTime |  |

## Loan_summary_data  (29)
| Field | Type | Result | Logic |
|---|---|---|---|
| Loan_summary_data_id | formula | singleLineText | {Investments_link}&"_"&{Loan_type} |
| Latest_balance_date | rollup | date | Loan_balance_input.[Date] via link [Loan_balance_input_link] |
| Latest_debt_balance | rollup | currency | Loan_balance_input.[Latest_balance] via link [Loan_balance_input_link] |
| Investment_location_state | multipleLookupValues | singleSelect | Investments.[State] via link [Investments_link] |
| Asset_number | multipleLookupValues | singleLineText | Investments.[Asset_number] via link [Investments_link] |
| Reporting_category | multipleLookupValues | multipleSelects | Investments.[Reporting_category] via link [Investments_link] |
| Investment_status | multipleLookupValues | singleSelect | Investments.[Investment_status] via link [Investments_link] |
| Annual_debt_payment | formula | currency | {Monthly_debt_payment}*12 |
| TTM_noi | multipleLookupValues | currency | Investments.[TTM_NOI] via link [Investments_link] |
| TTM_debt_yield | multipleLookupValues | percent | Investments.[TTM_debt_yield] via link [Investments_link] |
| TTM_dscr | multipleLookupValues | number | Investments.[TTM_DSCR] via link [Investments_link] |
| TTM_debt_yield_variance | formula | percent | IF(OR({TTM_debt_yield}=BLANK(),{Debt_yield_covenant}=BLANK()),
BLANK(),
{TTM_debt_yield}-{Debt_yield_covenant}) |
| TTM_dscr_variance | formula | number | IF(OR({TTM_dscr}=BLANK(),{DSCR_covenant}=BLANK()),
BLANK(),
  {TTM_dscr}-{DSCR_covenant}) |
| TTM_dscr_covenant_test | formula | singleLineText | IF({TTM_dscr_variance}<0,"Non-Compliant","") |
| Rate_maturity_year | formula | singleLineText | IF(ISERROR(YEAR({Interest_rate_reset_date})),"",YEAR({Interest_rate_reset_date})) |
| Loan_maturity_year | formula | number | YEAR({Loan_maturity}) |
| Hotel_anonymous_reference | multipleLookupValues | singleLineText | Investments.[Hotel_anonymous_reference] via link [Investments_link] |
| Market_LTV | multipleLookupValues | percent | Investments.[LTV] via link [Investments_link] |
| TTM_LTV | multipleLookupValues | percent | Investments.[TTM_LTV] via link [Investments_link] |
| LTV_variance | formula | percent | {Market_LTV}-{TTM_LTV} |
| Latest_quarter_debt_paydown | formula | currency | {Latest_quarter_beginning_balance}-{Latest_debt_balance} |
| Latest_quarter_beginning_balance | rollup | currency | Loan_balance_input.[Debt_balance] via link [Loan_balance_input_link] |
| Latest_month_DSCR | multipleLookupValues | number | Investments.[Latest_month_DSCR] via link [Investments_link] |
| TTM_GOP | multipleLookupValues | currency | Investments.[TTM_GOP] via link [Investments_link] |
| TTM_total_operating_revenue | multipleLookupValues | currency | Investments.[TTM_total_operating_revenue] via link [Investments_link] |
| Internal_asset_name | multipleLookupValues | singleLineText | Investments.[Internal_asset_name] via link [Investments_link] |
| Asset_subclass | multipleLookupValues | singleSelect | Investments.[Asset_subclass] via link [Investments_link] |
| SP_guarantee | multipleLookupValues | singleSelect | Guarantor_Compliance.[Liability_structure] via link [Guarantor_Compliance] |
| AP_guarantee | multipleLookupValues | singleSelect | Guarantor_Compliance.[Liability_structure] via link [Guarantor_Compliance] |

## Loan_balance_input  (8)
| Field | Type | Result | Logic |
|---|---|---|---|
| Loan_balance_input_id | formula | singleLineText | {Loan_summary_data_link}&"_"&MONTH({Date})&"_"&YEAR({Date}) |
| Asset_number | multipleLookupValues | singleLineText | Investments.[Asset_number] via link [Investments_link] |
| Month | formula | number | MONTH({Date}) |
| Year | formula | number | YEAR({Date}) |
| Latest_balance_date | multipleLookupValues | date | Loan_summary_data.[Latest_balance_date] via link [Loan_summary_data_link] |
| Latest_balance | formula | currency | IF({Latest_balance_date}={Date},{Debt_balance}) |
| Record_created_by | createdBy |  |  |
| Modified_by | lastModifiedTime | dateTime |  |

## Short_term_loans  (4)
| Field | Type | Result | Logic |
|---|---|---|---|
| Balance Sheet Primary Key | formula | singleLineText | {Asset Owner}&" - "&{Investment Name} |
| Asset Owner Helper | formula | singleLineText | IF({Lender (Individual)}=BLANK(),{Lender (Business)},{Lender (Individual)}) |
| Investment Name | formula | singleLineText | "Loan to "&{Borrower} |
| Cresset_naming_convention | formula | singleLineText | {Investment Name} |

## Hotel_budget  (23)
| Field | Type | Result | Logic |
|---|---|---|---|
| Hotel_budget_id | formula | singleLineText | {Asset_number}&"_"&MONTH({Date})&"_"&YEAR({Date}) |
| Internal_asset_name | multipleLookupValues | singleLineText | Asset_detail.[Internal_asset_name] via link [Asset_detail_link] |
| Month | formula | number | MONTH({Date}) |
| Year | formula | number | YEAR({Date}) |
| Asset_number | multipleLookupValues | singleLineText | Asset_detail.[Asset_number] via link [Asset_detail_link] |
| Occupancy_% | formula | percent | IF({Available_rooms}=BLANK(),BLANK(),
{Occupied_rooms}/{Available_rooms}) |
| GOP_% | formula | percent | {Gross_operating_profit}/{Total_operating_revenue} |
| Monthly_debt_payment | formula | currency | {Monthly_debt_payment_lookup} |
| Cash_flow | formula | currency | {EBITDA_NOI} -{Monthly_debt_payment_lookup} |
| DSCR | formula | number | {Adjusted_NOI}/{Monthly_debt_payment_lookup} |
| Brand | multipleLookupValues | multipleRecordLinks | Asset_detail.[Hotel_brand_metrics_link] via link [Asset_detail_link] |
| NOI_less_donation | formula | currency | {EBITDA_NOI}-{Occupied_rooms} |
| NOI_% | formula | percent | {EBITDA_NOI}/{Total_operating_revenue} |
| Full_year_total_GOP_% | formula | percent | {Full_year_total_GOP}/{Full_year_total_operating_revenue} |
| Prior_year_total_GOP_% | formula | percent | {Prior_year_total_GOP}/{Prior_year_total_operating_revenue} |
| Latest_financials_date | multipleLookupValues | date | Asset_detail.[Latest_actuals_date] via link [Asset_detail_link] |
| Included_in_YTD | formula | singleLineText | IF( 
  AND(YEAR({Latest_financials_date}) = YEAR({Date}), 
  OR({Acquisition_date}, {Open_date}), 
  NOT( IS_BEFORE( {Date}, IF({Acquisition_date}, {Acquisition_date}, {Open_date}) ) ), 
  NOT(IS_AFTER({Date}, {Latest_financials_date})) ), 
  "Yes", 
  "No" 
  ) |
| Latest_forecast_date | multipleLookupValues | date | Investments.[Latest_forecast_date] via link [Investments_link] |
| Included_in_budget_ex_fcst | formula | singleLineText | IF(
  {Latest_forecast_date},
  IF(IS_AFTER({Date}, {Latest_forecast_date}), "Yes", ""),
  IF(IS_AFTER({Date}, DATEADD({Latest_financials_date}, 1, 'months')), "Yes", "")
) |
| Adjusted_NOI | formula | currency | {EBITDA_NOI}-{Total_operating_revenue}*0.04 |
| Acquisition_date | multipleLookupValues | date | Asset_detail.[Acquired_date] via link [Asset_detail_link] |
| Open_date | multipleLookupValues | date | Asset_detail.[Open_date] via link [Asset_detail_link] |
| Monthly_debt_payment_lookup | multipleLookupValues | currency | Hotel_actuals.[Monthly_debt_payment_manual_input] via link [Hotel_actuals] |

## Witness_AM_forecast  (21)
| Field | Type | Result | Logic |
|---|---|---|---|
| Witness_AM_forecast_id | formula | singleLineText | {Asset_number}&"_"&MONTH({Date})&"_"&YEAR({Date}) |
| Internal_asset_name | multipleLookupValues | singleLineText | Asset_detail.[Internal_asset_name] via link [Asset_detail_link] |
| Month | formula | number | MONTH({Date}) |
| Year | formula | number | YEAR({Date}) |
| Asset_number | multipleLookupValues | singleLineText | Asset_detail.[Asset_number] via link [Asset_detail_link] |
| Occupancy_% | formula | percent | IF({Available_rooms}=BLANK(),BLANK(),
{Occupied_rooms}/{Available_rooms}) |
| GOP_% | formula | percent | {Gross_operating_profit}/{Total_operating_revenue} |
| Monthly_debt_payment | multipleLookupValues | currency | Asset_detail.[Monthly_debt_payment] via link [Asset_detail_link] |
| Cash_flow | formula | currency | {EBITDA_NOI} -{Monthly_debt_payment} |
| DSCR | formula | number | {EBITDA_NOI}/{Monthly_debt_payment} |
| NOI_less_reserve | formula | currency | {EBITDA_NOI}-({Total_operating_revenue}*.03) |
| Brand | multipleLookupValues | multipleRecordLinks | Asset_detail.[Hotel_brand_metrics_link] via link [Asset_detail_link] |
| NOI_less_donation | formula | currency | {EBITDA_NOI}-{Occupied_rooms} |
| NOI_% | formula | percent | {EBITDA_NOI}/{Total_operating_revenue} |
| Full_year_total_GOP_% | formula | percent | {Full_year_total_GOP}/{Full_year_total_operating_revenue} |
| Prior_year_total_GOP_% | formula | percent | {Prior_year_total_GOP}/{Prior_year_total_operating_revenue} |
| Latest_financials_date | multipleLookupValues | date | Asset_detail.[Latest_actuals_date] via link [Asset_detail_link] |
| Included_in_YTD | formula | singleLineText | IF(
  AND(
    YEAR({Date}) = YEAR({Latest_financials_date}),
    {Date} <= {Latest_financials_date}
  ),
  "Yes",
  "No"
) |
| Latest_forecast_date | multipleLookupValues | date | Investments.[Latest_forecast_date] via link [Investments_link] |
| Included_in_budget_ex_fcst | formula | singleLineText | IF(
  ({Latest_forecast_date}=BLANK())+({Date}<={Latest_forecast_date})
  ,"","Yes") |
| Adjusted_NOI | formula | currency | {EBITDA_NOI}-{Total_operating_revenue}*0.04 |

## Hotel_forecast  (14)
| Field | Type | Result | Logic |
|---|---|---|---|
| Hotel_forecast_id | formula | singleLineText | {Asset_number}&"_"&(MONTH({Forecast_period}))&"_"&YEAR({Forecast_date})&"_"&{Forecast_type} |
| Forecast_period | formula | date | IF(
  {Forecast_type} = "30",
    DATEADD(DATEADD({Forecast_date}, 1, 'month'), -1, 'day'),
    IF(
      {Forecast_type} = "60",
        DATEADD(DATEADD({Forecast_date}, 2, 'month'), -1, 'day'),
        IF(
          {Forecast_type} = "90",
            DATEADD(DATEADD({Forecast_date}, 3, 'month'), -1, 'day'),
            BLANK()
        )
    )
) |
| Latest_forecast_check | formula | singleLineText | IF(
  OR(
    {Forecast_date} = {Latest_forecast_date},
    {Forecast_type} = 30
  ),
  "Yes",
  ""
) |
| Latest_forecast_date | multipleLookupValues | date | Asset_detail.[Latest_forecast_date] via link [Asset_detail_link] |
| Profitsword_hotel_name | multipleLookupValues | singleLineText | Asset_detail.[Profitsword_hotel_name] via link [Asset_detail_link] |
| Asset_number | multipleLookupValues | singleLineText | Asset_detail.[Asset_number] via link [Asset_detail_link] |
| Latest_actuals_date | multipleLookupValues | date | Asset_detail.[Latest_actuals_date] via link [Asset_detail_link] |
| GOP_% | formula | percent | {Gross_operating_profit}/{Total_operating_revenue} |
| NOI_% | formula | percent | {EBITDA_NOI}/{Total_operating_revenue} |
| Year | formula | number | YEAR({Forecast_period}) |
| Adjusted_NOI | formula | currency | {EBITDA_NOI}-{Total_operating_revenue}*0.04 |
| Monthly_debt_payment | multipleLookupValues | currency | Hotel_actuals.[Monthly_debt_payment_manual_input] via link [Hotel_actuals_link] |
| Hotel_forecast_id copy | formula | singleLineText | {Asset_number}&"_"&(MONTH({Forecast_period}))&"_"&YEAR({Forecast_date}) |
| Latest_forecast_rollup_filter | formula | singleLineText | IF(
  AND(
    {Latest_forecast_check} = "Yes",
      IS_AFTER({Forecast_period}, {Latest_actuals_date})
    )
  ,
  "Yes",
  ""
) |

## Quarterly_hotel_actuals  (22)
| Field | Type | Result | Logic |
|---|---|---|---|
| Quarterly_hotel_actuals_id | formula | singleLineText | {Asset_number}&"_"&"Q"&DATETIME_FORMAT({Date},"Q_YYYY") |
| Internal_asset_name | multipleLookupValues | singleLineText | Asset_detail.[Internal_asset_name] via link [Asset_detail_link] |
| Investment_status | multipleLookupValues | singleSelect | Asset_detail.[Investment_status] via link [Asset_detail_link] |
| Asset_number | multipleLookupValues | singleLineText | Asset_detail.[Asset_number] via link [Asset_detail_link] |
| GOP_per_available_room | formula | currency | {Gross_operating_profit}/{Available_rooms} |
| EBITDA_per_available_room | formula | currency | {EBITDA}/{Available_rooms} |
| Budget_GOP_per_available_room | formula | currency | {Budget_gross_operating_profit}/{Budget_available_rooms} |
| Budget_EBITDA_per_available_room | formula | currency | {Budget_EBITDA}/{Budget_available_rooms} |
| PY_GOP_per_available_room | formula | currency | {PY_gross_operating_profit}/{PY_Available Rooms} |
| PY_EBITDA_per_available_room | formula | currency | {PY_EBITDA}/{PY_Available Rooms} |
| Latest_quarter_debt_paydown | multipleLookupValues | currency | Investments.[Quarterly_loan_paydown] via link [Investments_link] |
| Operating_balance | multipleLookupValues | currency | Investments.[Operating_balance] via link [Investments_link] |
| Reserve_balance | multipleLookupValues | currency | Investments.[Reserve_balance] via link [Investments_link] |
| PIP_balance | multipleLookupValues | currency | Investments.[PIP_balance] via link [Investments_link] |
| Initial_principal | multipleLookupValues | currency | Investments.[Total_loan_principal] via link [Investments_link] |
| Latest_quarter_DSCR_reserve_adjusted | formula | number | ({EBITDA}-{Total_operating_revenue}*.04)/(3*{Monthly_debt_payment}) |
| Monthly_debt_payment | multipleLookupValues | currency | Investments.[Monthly_debt_payment] via link [Investments_link] |
| Latest_debt_balance | multipleLookupValues | currency | Investments.[Latest_debt_balance] via link [Investments_link] |
| TTM_DSCR_reserve_adjusted | multipleLookupValues | number | Investments.[TTM_DSCR] via link [Investments_link] |
| Latest_quarter_DSCR_non_adjusted | formula | number | ({EBITDA})/(3*{Monthly_debt_payment}) |
| TTM_DSCR_non_adjusted | multipleLookupValues | number | Investments.[TTM_DSCR_non_adjusted] via link [Investments_link] |
| Acquired_date | multipleLookupValues | date | Asset_detail.[Acquired_date] via link [Asset_detail_link] |

## Hotel_actuals  (40)
| Field | Type | Result | Logic |
|---|---|---|---|
| Hotel_actuals_id | formula | singleLineText | {Asset_number}&"_"&MONTH({Date})&"_"&YEAR({Date}) |
| Internal_asset_name | multipleLookupValues | singleLineText | Asset_detail.[Internal_asset_name] via link [Asset_detail_link] |
| Investment_status | multipleLookupValues | singleSelect | Asset_detail.[Investment_status] via link [Asset_detail_link] |
| Month | formula | number | MONTH({Date}) |
| Year | formula | number | YEAR({Date}) |
| Quarter_year | formula | singleLineText | "Q"&DATETIME_FORMAT({Date},'Q_YYYY') |
| Asset_number | multipleLookupValues | singleLineText | Asset_detail.[Asset_number] via link [Asset_detail_link] |
| Occupancy_% | formula | percent | {Occupied_rooms}/{Available_rooms} |
|  ADR  | formula | currency | {Rooms_sales}/{Occupied_rooms} |
| RevPAR | formula | currency | {Rooms_sales}/{Available_rooms} |
| GOP_% | formula | percent | {Gross_operating_profit}/{Total_operating_revenue} |
| Latest_actuals_date | multipleLookupValues | date | Asset_detail.[Latest_actuals_date] via link [Asset_detail_link] |
| Included_in_TTM | formula | singleLineText | IF(
  AND(
    OR({Acquisition_date}, {Open_date}),

    DATETIME_DIFF({Latest_actuals_date}, {Date}, 'months') >= 0,
    DATETIME_DIFF({Latest_actuals_date}, {Date}, 'months') <= 11,

    DATETIME_DIFF(
      {Date},
      IF({Acquisition_date}, {Acquisition_date}, {Open_date}),
      'months'
    ) >= 0
  ),
  "Yes","No"
) |
| Latest_month_financials | formula | singleLineText | IF({Date}={Latest_actuals_date},"Yes","") |
| Cash_flow | formula | currency | {EBITDA_NOI}-{Monthly_debt_payment_manual_input} |
| Hotel_brand | multipleLookupValues | singleSelect | Asset_detail.[Hotel_brand] via link [Asset_detail_link] |
| Created_time | createdTime | date |  |
| Adjusted_NOI | formula | currency | {EBITDA_NOI}-({Total_operating_revenue}*.04) |
| NOI_% | formula | percent | {EBITDA_NOI}/{Total_operating_revenue} |
| Latest_updated | createdTime | dateTime |  |
| Cost_per_occupied_room | formula | currency | {Rooms_expense}/{Occupied_rooms} |
| Included_in_YTD | formula | singleLineText | IF( 
  AND(YEAR({Latest_actuals_date}) = YEAR({Date}), 
  OR({Acquisition_date}, {Open_date}), 
  NOT( IS_BEFORE( {Date}, IF({Acquisition_date}, {Acquisition_date}, {Open_date}) ) ), 
  NOT(IS_AFTER({Date}, {Latest_actuals_date})) ), 
  "Yes", 
  "No" 
  ) |
| Budget_gross_operating_profit | multipleLookupValues | currency | Hotel_budget.[Gross_operating_profit] via link [Hotel_budget_link] |
| Budget_total_operating_revenue | multipleLookupValues | currency | Hotel_budget.[Total_operating_revenue] via link [Hotel_budget_link] |
| Expense_flex | formula | percent | IF(
  OR({Total_operating_revenue}=BLANK(),{Budget_total_operating_revenue}=BLANK(),{Gross_operating_profit}=BLANK(), {Budget_gross_operating_profit}=BLANK(),{Total_operating_revenue}-{Budget_total_operating_revenue}>=0)
  ,
  BLANK()
  ,
 1- (({Gross_operating_profit}-{Budget_gross_operating_profit})/({Total_operating_revenue}-{Budget_total_operating_revenue}))
) |
| Expense_flow | formula | percent | IF(
  OR({Total_operating_revenue}=BLANK(),{Budget_total_operating_revenue}=BLANK(),{Gross_operating_profit}=BLANK(), {Budget_gross_operating_profit}=BLANK(),{Total_operating_revenue}-{Budget_total_operating_revenue}<0)
  ,
  BLANK()
  ,
({Gross_operating_profit}-{Budget_gross_operating_profit})/({Total_operating_revenue}-{Budget_total_operating_revenue})
) |
| Last_modified_by | lastModifiedBy |  |  |
| Last_modified_time | lastModifiedTime | dateTime |  |
| Monthly_debt_payment_lookup | multipleLookupValues | currency | Asset_detail.[Monthly_debt_payment] via link [Asset_detail_link] |
| Acquisition_date | multipleLookupValues | date | Asset_detail.[Acquired_date] via link [Asset_detail_link] |
| Open_date | multipleLookupValues | date | Asset_detail.[Open_date] via link [Asset_detail_link] |
| Acquired_date_lookup | multipleLookupValues | date | Asset_detail.[Acquired_date] via link [Asset_detail_link] |
| Management_fee_% | formula | percent | {Management_fees}/{Total_operating_revenue} |
| Clickup_task_id | multipleLookupValues | singleLineText | Asset_detail.[Clickup_task_id] via link [Asset_detail_link] |
| Flex_flow | formula | singleLineText | IF(({Total_operating_revenue} - {PY_total_operating_revenue}) > 0,"Flow","Flex") |
| Flex_flow_pct | formula | percent | IF(
  {Total_operating_revenue} - {PY_total_operating_revenue} = 0,
  BLANK(),
  IF(
    {Flex_flow} = "Flow",
    ({Gross_operating_profit} - {PY_gross_operating_profit}) / ({Total_operating_revenue} - {PY_total_operating_revenue}),
    1 - (({Gross_operating_profit} - {PY_gross_operating_profit}) / ({Total_operating_revenue} - {PY_total_operating_revenue}))
  )
) |
| PY_total_operating_revenue | multipleLookupValues | currency | Hotel_actuals.[Total_operating_revenue] via link [PY_record] |
| PY_gross_operating_profit | multipleLookupValues | currency | Hotel_actuals.[Gross_operating_profit] via link [PY_record] |
| Occ_es | formula | percent | {Extended_stay_rooms} / {Available_rooms} |
| monthly_DSCR | formula | number | {EBITDA_NOI}/{Monthly_debt_payment_manual_input} |

## Balance_sheet  (1)
| Field | Type | Result | Logic |
|---|---|---|---|
| Balance_sheet_id | formula | singleLineText | {Asset_detail_link}&"_"&MONTH({Date})&"_"&YEAR({Date}) |

## Hotel_segmentation  (6)
| Field | Type | Result | Logic |
|---|---|---|---|
| Hotel_segmentation_id | formula | singleLineText | {Asset_number}&"_"&{Segment}&"_"&MONTH({Date})&"_"&YEAR({Date}) |
| Asset_number | multipleLookupValues | singleLineText | Asset_detail.[Asset_number] via link [Asset_detail_link] |
| Internal_asset_name | multipleLookupValues | singleLineText | Asset_detail.[Internal_asset_name] via link [Asset_detail_link] |
| Segment | formula | singleLineText | RIGHT({Property_segment_concat},LEN({Property_segment_concat})-FIND("_",{Property_segment_concat})) |
| Month | formula | number | MONTH({Date}) |
| Year | formula | number | YEAR({Date}) |

## Hotel_CapEx_2026  (8)
| Field | Type | Result | Logic |
|---|---|---|---|
| Internal_asset_name | multipleLookupValues | singleLineText | Asset_detail.[Internal_asset_name] via link [Asset_detail_link] |
| Days_since_ticket_opened | formula | number | IF({Ivy_Request_Date}, MAX(0, DATETIME_DIFF(TODAY(), {Ivy_Request_Date}, 'days')), BLANK()) |
| Reporting_category | multipleLookupValues | multipleSelects | Asset_detail.[Reporting_category] via link [Asset_detail_link] |
| CapEx_request_id | formula | singleLineText | "https://forms.fillout.com/t/ragsZYuLeeus?id=" & RECORD_ID() |
| Update_request_hyperlink | button |  |  |
| Last_modified_time | lastModifiedTime | dateTime |  |
| Renovation_plan_start | multipleLookupValues | date | Asset_detail.[Renovation_plan_start] via link [Asset_detail_link] |
| Automation_required | formula | singleLineText | IF(
  {Approved_y_n} = "1. Requires Ownership Approval", "Yes",
  IF(
    AND({Approved_y_n} = "2. Under AM Review"), "Yes",
    IF(
      AND({Approved_y_n} = "3. Denied", DATETIME_DIFF(TODAY(), {Last_modified_time}, 'days') < 14), "Yes",
      IF(
        AND({Approved_y_n} = "4. Approved", DATETIME_DIFF(TODAY(), {Last_modified_time}, 'days') < 14), "Yes"
      )
    )
  )
) |

## STR_budget  (6)
| Field | Type | Result | Logic |
|---|---|---|---|
| STR_budget_id | formula | singleLineText | {Asset_number}&"_"&MONTH({Date})&"_"&YEAR({Date}) |
| Internal_asset_name | multipleLookupValues | singleLineText | Asset_detail.[Internal_asset_name] via link [Asset_detail_link] |
| Month | formula | number | MONTH({Date}) |
| Year | formula | number | YEAR({Date}) |
| Asset_number | multipleLookupValues | singleLineText | Asset_detail.[Asset_number] via link [Asset_detail_link] |
| STR_code | multipleLookupValues | number | Asset_detail.[STR_code] via link [Asset_detail_link] |

## STR_actuals  (36)
| Field | Type | Result | Logic |
|---|---|---|---|
| STR_actuals_id | formula | singleLineText | {Asset_number}&"_"&{Month}&"_"&{Year} |
| Internal_asset_name | multipleLookupValues | singleLineText | Asset_detail.[Internal_asset_name] via link [Asset_detail_link] |
| Month | formula | number | MONTH({Date}) |
| Day | formula | number | DAY({Date}) |
| Year | formula | number | YEAR({Date}) |
| Asset_number | multipleLookupValues | singleLineText | Asset_detail.[Asset_number] via link [Asset_detail_link] |
| STR_code | multipleLookupValues | number | Asset_detail.[STR_code] via link [Asset_detail_link] |
| Helper_STR_market_trend_link | formula | singleLineText | {Market}&"_"&{Month}&"_"&{Year} |
| Market_occupancy_TTM | multipleLookupValues | percent | STR_market_trend.[Occupancy_TTM] via link [STR_market_trend_link] |
| Market_ADR_TTM | multipleLookupValues | currency | STR_market_trend.[ADR_TTM] via link [STR_market_trend_link] |
| Market_RevPAR_TTM | multipleLookupValues | currency | STR_market_trend.[RevPar_TTM] via link [STR_market_trend_link] |
| Market_supply_TTM | multipleLookupValues | number | STR_market_trend.[Supply_TTM] via link [STR_market_trend_link] |
| Market_demand_TTM | multipleLookupValues | number | STR_market_trend.[Demand_TTM] via link [STR_market_trend_link] |
| Market_revenue_TTM | multipleLookupValues | currency | STR_market_trend.[Revenue_TTM] via link [STR_market_trend_link] |
| Days_in_month | formula | number | DAY({Date}) |
| Comp_set_room_count | multipleLookupValues | number | Asset_detail.[Comp_set_room_count] via link [Asset_detail_link] |
| My_property_room_count | multipleLookupValues | number | Asset_detail.[Room_count] via link [Asset_detail_link] |
| Comp_set_revenue | formula | currency | ({Occupancy_comp_set})*{Comp_set_room_count}*{ADR_comp_set}*{Days_in_month} |
| My_property_revenue | formula | currency | ({Occupancy_my_property})*{My_property_room_count}*{ADR_my_property}*{Days_in_month} |
| Market_revenue | formula | currency | {Comp_set_revenue}+{My_property_revenue} |
| My_property_market_share | formula | percent | {My_property_revenue}/{Market_revenue} |
| Hotel_franchise | multipleLookupValues | multipleRecordLinks | Asset_detail.[Hotel_franchise] via link [Asset_detail_link] |
| Hotel_brand | multipleLookupValues | singleSelect | Asset_detail.[Hotel_brand] via link [Asset_detail_link] |
| Investment_status | multipleLookupValues | singleSelect | Asset_detail.[Investment_status] via link [Asset_detail_link] |
| City | multipleLookupValues | singleSelect | Asset_detail.[City] via link [Asset_detail_link] |
| Market | multipleLookupValues | singleSelect | Asset_detail.[Market] via link [Asset_detail_link] |
| Last_updated | lastModifiedTime | dateTime |  |
| Market_occupancy_TTM_%_chg | multipleLookupValues | percent | STR_market_trend.[Occupancy_TTM_%_chg] via link [STR_market_trend_link] |
| Market_ADR_TTM_%_chg | multipleLookupValues | percent | STR_market_trend.[ADR_TTM_%_chg] via link [STR_market_trend_link] |
| Market_RevPAR_TTM_%_chg | multipleLookupValues | percent | STR_market_trend.[RevPAR_TTM_%_chg] via link [STR_market_trend_link] |
| Health_trend_str | formula | singleLineText | IF(
  OR(
    {RevPAR_my_property_%_chg} = BLANK(),
    {RevPAR_index_rgi_%_chg} = BLANK()
  ),
  BLANK(),
  IF(
    AND({RevPAR_my_property_%_chg} > 0, {RevPAR_index_rgi_%_chg} > 0),
    "4. Healthy",
    IF(
      AND({RevPAR_my_property_%_chg} > 0, {RevPAR_index_rgi_%_chg} < 0),
      "3. Momentum",
      IF(
        AND({RevPAR_my_property_%_chg} < 0, {RevPAR_index_rgi_%_chg} > 0),
        "2. Defensive",
        IF(
          AND({RevPAR_my_property_%_chg} < 0, {RevPAR_index_rgi_%_chg} < 0),
          "1. Underperforming",
          BLANK()
        )
      )
    )
  )
) |
| Latest_str_actuals_date | multipleLookupValues | date | Asset_detail.[Latest_str_actuals_date] via link [Asset_detail_link] |
| Latest_str_actuals_day | formula | singleLineText | IF( {Date} = {Latest_str_actuals_date},"Yes", BLANK() ) |
| Acquisition_date | multipleLookupValues | date | Asset_detail.[Acquired_date] via link [Asset_detail_link] |
| Open_date | multipleLookupValues | date | Asset_detail.[Open_date] via link [Asset_detail_link] |
| Included_in_TTM | formula | singleLineText | IF(
  AND(
    OR({Acquisition_date}, {Open_date}),

    DATETIME_DIFF({Latest_str_actuals_date}, {Date}, 'months') >= 0,
    DATETIME_DIFF({Latest_str_actuals_date}, {Date}, 'months') <= 11,

    DATETIME_DIFF(
      {Date},
      IF({Acquisition_date}, {Acquisition_date}, {Open_date}),
      'months'
    ) >= 0
  ),
  "Yes","No"
) |

## STR_weekly_data  (18)
| Field | Type | Result | Logic |
|---|---|---|---|
| STR_weekly_data_id | formula | singleLineText | {Asset_number}&"_"&{Month}&"_"&{Day}&"_"&{Year} |
| Internal_asset_name | multipleLookupValues | singleLineText | Asset_detail.[Internal_asset_name] via link [Asset_detail_link] |
| Month | formula | number | MONTH({End_date}) |
| Day | formula | number | DAY({End_date}) |
| Day_of_week | formula | singleLineText | DATETIME_FORMAT({End_date},"dddd") |
| Year | formula | number | YEAR({End_date}) |
| Asset_number | multipleLookupValues | singleLineText | Asset_detail.[Asset_number] via link [Asset_detail_link] |
| STR_code | multipleLookupValues | number | Asset_detail.[STR_code] via link [Asset_detail_link] |
| Investment_status | multipleLookupValues | singleSelect | Asset_detail.[Investment_status] via link [Asset_detail_link] |
| Last_updated | lastModifiedTime | dateTime |  |
| Budgeted_strategy | multipleLookupValues | multipleSelects | Asset_detail.[Budgeted_strategy] via link [Asset_detail_link] |
| Budget_RevPAR_rank | multipleLookupValues | number | STR_budget.[RevPAR_rank] via link [STR_budget_link] |
| Budget_ADR_rank | multipleLookupValues | number | STR_budget.[ADR_rank] via link [STR_budget_link] |
| Budget_occupancy_rank | multipleLookupValues | number | STR_budget.[Occupancy_rank] via link [STR_budget_link] |
| STR_weekly_performance | formula | singleLineText | IF(
  OR(
    {RevPAR_index_rgi} = BLANK(),
    {RevPAR_index_rgi_%_chg} = BLANK()
  ),
  BLANK(),
  IF(
    AND({RevPAR_index_rgi} > 100, {RevPAR_index_rgi_%_chg} > 0),
    "4. Ahead and Gaining",
    IF(
      AND({RevPAR_index_rgi}> 100, {RevPAR_index_rgi_%_chg} < 0),
      "3. Ahead and Losing",
      IF(
        AND({RevPAR_index_rgi} < 100, {RevPAR_index_rgi_%_chg} > 0),
        "2. Behind and Gaining",
        IF(
          AND({RevPAR_index_rgi} < 100, {RevPAR_index_rgi_%_chg} < 0),
          "1. Behind and Losing",
          BLANK()
        )
      )
    )
  )
) |
| Latest_STR_weekly_trend_date | multipleLookupValues | date | Asset_detail.[Latest_STR_weekly_trend_date] via link [Asset_detail_link] |
| Latest_STR_weekly_trend | formula | singleLineText | IF( {End_date} = {Latest_STR_weekly_trend_date},"Yes", BLANK() ) |
| Clickup_task_id | multipleLookupValues | singleLineText | Asset_detail.[Clickup_task_id] via link [Asset_detail_link] |

## STR_daily_data  (11)
| Field | Type | Result | Logic |
|---|---|---|---|
| STR_daily_data_id | formula | singleLineText | {Asset_number}&"_"&DATETIME_FORMAT({Date},'MM_DD_YYYY') |
| Internal_asset_name | multipleLookupValues | singleLineText | Asset_detail.[Internal_asset_name] via link [Asset_detail_link] |
| Month | formula | singleLineText | DATETIME_FORMAT({Date},'M') |
| Day | formula | number | DAY({Date}) |
| Day_of_week | formula | singleLineText | DATETIME_FORMAT({Date},'dddd') |
| Year | formula | number | YEAR({Date}) |
| Asset_number | multipleLookupValues | singleLineText | Asset_detail.[Asset_number] via link [Asset_detail_link] |
| STR_code | multipleLookupValues | number | Asset_detail.[STR_code] via link [Asset_detail_link] |
| City | multipleLookupValues | singleSelect | Asset_detail.[City] via link [Asset_detail_link] |
| Market | multipleLookupValues | singleSelect | Asset_detail.[Market] via link [Asset_detail_link] |
| Hotel_brand | multipleLookupValues | singleSelect | Asset_detail.[Hotel_brand] via link [Asset_detail_link] |

## STR_28_day_trend  (27)
| Field | Type | Result | Logic |
|---|---|---|---|
| STR_weekly_data_id | formula | singleLineText | {Asset_number}&"_"&{Month}&"_"&{Day}&"_"&{Year} |
| Internal_asset_name | multipleLookupValues | singleLineText | Asset_detail.[Internal_asset_name] via link [Asset_detail_link] |
| Month | formula | number | MONTH({End_date}) |
| Day | formula | number | DAY({End_date}) |
| Day_of_week | formula | singleLineText | DATETIME_FORMAT({End_date},"dddd") |
| Year | formula | number | YEAR({End_date}) |
| Asset_number | multipleLookupValues | singleLineText | Asset_detail.[Asset_number] via link [Asset_detail_link] |
| STR_code | multipleLookupValues | number | Asset_detail.[STR_code] via link [Asset_detail_link] |
| Latest_28_day_trend | formula | number | MAX({End_date}) |
| Investment_status | multipleLookupValues | singleSelect | Asset_detail.[Investment_status] via link [Asset_detail_link] |
| Last_updated | lastModifiedTime | dateTime |  |
| Budgeted_strategy | multipleLookupValues | multipleSelects | Asset_detail.[Budgeted_strategy] via link [Asset_detail_link] |
| Budget_RevPAR_rank | multipleLookupValues | number | STR_budget.[RevPAR_rank] via link [STR_budget_link] |
| Budget_ADR_rank | multipleLookupValues | number | STR_budget.[ADR_rank] via link [STR_budget_link] |
| Budget_occupancy_rank | multipleLookupValues | number | STR_budget.[Occupancy_rank] via link [STR_budget_link] |
| STR_28_day_performance | formula | singleLineText | IF(
  OR(
    {RevPAR_index_rgi} = BLANK(),
    {RevPAR_index_rgi_%_chg} = BLANK()
  ),
  BLANK(),
  IF(
    AND({RevPAR_index_rgi} > 100, {RevPAR_index_rgi_%_chg} >= 0),
    "4. Ahead and Gaining",
    IF(
      AND({RevPAR_index_rgi} > 100, {RevPAR_index_rgi_%_chg} <= 0),
      "3. Ahead and Losing",
      IF(
        AND({RevPAR_index_rgi} < 100, {RevPAR_index_rgi_%_chg} >= 0),
        "2. Behind and Gaining",
        IF(
          AND({RevPAR_index_rgi} < 100, {RevPAR_index_rgi_%_chg} <= 0),
          "1. Behind and Losing",
          BLANK()
        )
      )
    )
  )
) |
| Latest_STR_28_day_trend_date | multipleLookupValues | date | Asset_detail.[Latest_STR_28_day_trend_date] via link [Asset_detail_link] |
| Latest_STR_28_day | formula | singleLineText | IF( {End_date} = {Latest_STR_28_day_trend_date},"Yes", BLANK() ) |
| 1_week_prior_week | formula | singleLineText | {Asset_number} & "_" & DATETIME_FORMAT(DATEADD({End_date}, -7, 'days'), 'M_D_YYYY') |
| 2_week_prior_key | formula | singleLineText | {Asset_number} & "_" & DATETIME_FORMAT(DATEADD({End_date}, -14, 'days'), 'M_D_YYYY') |
| 3_week_prior_key | formula | singleLineText | {Asset_number} & "_" & DATETIME_FORMAT(DATEADD({End_date}, -21, 'days'), 'M_D_YYYY') |
| 4_week_prior_key | formula | singleLineText | {Asset_number} & "_" & DATETIME_FORMAT(DATEADD({End_date}, -28, 'days'), 'M_D_YYYY') |
| Prior_bucket_1 | multipleLookupValues | singleLineText | STR_28_day_trend.[STR_28_day_performance] via link [1_week_prior] |
| Prior_bucket_2 | multipleLookupValues | singleLineText | STR_28_day_trend.[STR_28_day_performance] via link [2_week_prior] |
| Prior_bucket_3 | multipleLookupValues | singleLineText | STR_28_day_trend.[STR_28_day_performance] via link [3_week_prior] |
| Prior_bucket_4 | multipleLookupValues | singleLineText | STR_28_day_trend.[STR_28_day_performance] via link [4_week_prior] |
| Streak_28_day | formula | singleLineText | IF(
  {Latest_STR_28_day} = "Yes",
  IF(
    {STR_28_day_performance} = BLANK(),
    "",
    IF(
      AND({STR_28_day_performance}={Prior_bucket_1}, {STR_28_day_performance}={Prior_bucket_2}, {STR_28_day_performance}={Prior_bucket_3}, {STR_28_day_performance}={Prior_bucket_4}),
      "4+ weeks",
      IF(
        AND({STR_28_day_performance}={Prior_bucket_1}, {STR_28_day_performance}={Prior_bucket_2}, {STR_28_day_performance}={Prior_bucket_3}),
        "4 weeks",
        IF(
          AND({STR_28_day_performance}={Prior_bucket_1}, {STR_28_day_performance}={Prior_bucket_2}),
          "3 weeks",
          IF(
            {STR_28_day_performance}={Prior_bucket_1},
            "2 weeks",
            "1 week"
          )
        )
      )
    )
  ),
  ""
) |

## STR_market_trend  (3)
| Field | Type | Result | Logic |
|---|---|---|---|
| STR_market_trend_id | formula | singleLineText | {Market}&"_"&{Month}&"_"&{Year} |
| Month | formula | number | MONTH({Date}) |
| Year | formula | number | YEAR({Date}) |

## STR_comp_set  (10)
| Field | Type | Result | Logic |
|---|---|---|---|
| STR_comp_set_id | formula | singleLineText | {Asset_detail_link}&"_"&{Subject_property_STR_code}&IF({Subject_property_STR_code}={STR_code},"_subject","")
 |
| Subject_property_STR_code | multipleLookupValues | number | Asset_detail.[STR_code] via link [Asset_detail_link] |
| Comp_set_room_count | multipleLookupValues | number | Asset_detail.[Comp_set_room_count] via link [Asset_detail_link] |
| Subject_property_room_count | multipleLookupValues | number | Asset_detail.[Room_count] via link [Asset_detail_link] |
| Asset_number | multipleLookupValues | singleLineText | Asset_detail.[Asset_number] via link [Asset_detail_link] |
| Subject_property_city | multipleLookupValues | singleSelect | Asset_detail.[City] via link [Asset_detail_link] |
| Rooms_percent_of_market | formula | percent | {Subject_property_room_count}/({Comp_set_room_count}+{Subject_property_room_count}) |
| Subject_last_renovation_year | multipleLookupValues | number | Asset_detail.[Last_renovation_year] via link [Asset_detail_link] |
| lmt | lastModifiedTime | dateTime |  |
| Subject_property | formula | singleLineText | IF({Subject_property_STR_code} = {STR_code},"Yes","No") |

## Hotel_onthebooks  (4)
| Field | Type | Result | Logic |
|---|---|---|---|
| Hotel_onthebooks_id | formula | singleLineText | {Asset_detail}&"_"&MONTH({Date})&"_"&YEAR({Date})&"_"&DAY({Upload Date})&"_"&MONTH({Upload Date}) |
| Month | formula | number | MONTH({Date}) |
| Year | formula | number | YEAR({Date}) |
| Asset_name | multipleLookupValues | singleLineText | Asset_detail.[Internal_asset_name] via link [Asset_detail] |

## Full_hotel_comp_landscape  (9)
| Field | Type | Result | Logic |
|---|---|---|---|
| Full_hotel_comp_landscape_id | formula | singleLineText | {Asset_number}&"_"&{STR_code} |
| Asset_number | multipleLookupValues | singleLineText | Asset_detail.[Asset_number] via link [Asset_detail_link] |
| Subject_property_STR_code | multipleLookupValues | number | Asset_detail.[STR_code] via link [Asset_detail_link] |
| Age | formula | number | DATETIME_DIFF(TODAY(),{Open_date},'years') |
| Subject_internal_asset_name | multipleLookupValues | singleLineText | Asset_detail.[Internal_asset_name] via link [Asset_detail_link] |
| Subject_city | multipleLookupValues | singleSelect | Asset_detail.[City] via link [Asset_detail_link] |
| Subject_state | multipleLookupValues | singleSelect | Asset_detail.[State] via link [Asset_detail_link] |
| Target_property | formula | singleLineText | IF({Subject_property_STR_code}={STR_code},"Yes","No") |
| Autonumber | autoNumber |  |  |

## Hotel_brand_metrics  (7)
| Field | Type | Result | Logic |
|---|---|---|---|
| Witness_active_portfolio_properties | rollup | number | Asset_detail.[Asset_detail_id] via link [Asset_detail_link] |
| Witness_active_construction_portfolio_properties | rollup | number | Asset_detail.[Asset_detail_id] via link [Asset_detail_link] |
| Total_room_count_Witness_active_portfolio | rollup | number | Asset_detail.[Room_count] via link [Asset_detail_link] |
| Total_development_room_count | rollup | number | Asset_detail.[Room_count] via link [Asset_detail_link] |
| Asset_number_Witness_active_portfolio | multipleLookupValues | singleLineText | Asset_detail.[Asset_number] via link [Asset_detail_link] |
| Created_time | createdTime | dateTime |  |
| Witness_active_portfolio_valuation | rollup | currency | Asset_detail.[Latest_valuation_balance] via link [Asset_detail_link] |

## Lenders  (4)
| Field | Type | Result | Logic |
|---|---|---|---|
| Lead_contact | multipleLookupValues | singleSelect | Loan_summary_data.[Lead_contact] via link [Loan_summary_data_link] |
| Total_debt_balance | rollup | currency | Loan_summary_data.[Latest_debt_balance] via link [Loan_summary_data_link] |
| Total_cash_balance | rollup | currency | Cash_accounts.[Latest_cash_balance] via link [Cash_accounts_link] |
| Latest_lending_transaction_date | rollup | date | Hotel_sale_comps.[Sale_date] via link [Hotel_sale_comps_link] |

## Hotel_sale_comps  (1)
| Field | Type | Result | Logic |
|---|---|---|---|
| Helper_Lenders_link | formula | singleLineText | IF(
  FIND(",",{First_trust_deed_lender})>0,REGEX_REPLACE({First_trust_deed_lender},",.*",""),
IF(FIND(" NA",{First_trust_deed_lender})>0,REGEX_REPLACE({First_trust_deed_lender}," NA",""),
{First_trust_deed_lender})) |

## Debt_resizing  (17)
| Field | Type | Result | Logic |
|---|---|---|---|
| Debt_resizing_id | formula | singleLineText | {Investments_link} |
| Est_PIP_cost | multipleLookupValues | currency | Investments.[Est_PIP_cost] via link [Investments_link] |
| Loan_maturity | multipleLookupValues | date | Investments.[Loan_maturity] via link [Investments_link] |
| TTM_total_operating_revenue | multipleLookupValues | currency | Investments.[TTM_total_operating_revenue] via link [Investments_link] |
| Adj_TTM_NOI | multipleLookupValues | currency | Investments.[Adj_TTM_NOI] via link [Investments_link] |
| TTM_DSCR | multipleLookupValues | number | Investments.[TTM_DSCR] via link [Investments_link] |
| Latest_debt_balance | multipleLookupValues | currency | Investments.[Latest_debt_balance] via link [Investments_link] |
| Annual_debt_payment | multipleLookupValues | currency | Investments.[TTM_debt_payment] via link [Investments_link] |
| Refi_debt_payment_1.5_DCSR | formula | currency | {Adj_TTM_NOI} / 1.5 |
| 20yr_refi_loan | formula | currency | ({Refi_debt_payment_1.5_DCSR}/12) 
/ 
(
  (({5yr_UST}+{Spread})/12)
  /
  (
    1-
    POWER((1+(({5yr_UST}+{Spread})/12)),-{20_year_AM_payments})
  )
) |
| 25_yr_refi_loan | formula | currency | ({Refi_debt_payment_1.5_DCSR}/12) 
/ 
(
  (({5yr_UST}+{Spread})/12)
  /
  (
    1-
    POWER((1+(({5yr_UST}+{Spread})/12)),-{25_year_AM_payments})
  )
) |
| 25_yr_refi_variance | formula | currency | ROUNDDOWN({25_yr_refi_loan} - {Latest_debt_balance},-4) |
| 30_yr_refi_loan | formula | currency | ({Refi_debt_payment_1.5_DCSR}/12) 
/ 
(
  (({5yr_UST}+{Spread})/12)
  /
  (
    1-
    POWER((1+(({5yr_UST}+{Spread})/12)),-{30_year_AM_payments})
  )
) |
| 20_year_AM_payments | formula | number | 20*12 |
| 25_year_AM_payments | formula | number | 25*12 |
| 30_year_AM_payments | formula | number | 30*12 |
| Interest_rate | formula | percent | {5yr_UST}+{Spread} |

## Year_end_financials  (5)
| Field | Type | Result | Logic |
|---|---|---|---|
| Year_end_financials_id | formula | singleLineText | {Asset_detail_link}&"_"&{Year} |
| Investments_link | multipleLookupValues | multipleRecordLinks | Asset_detail.[Investments_link] via link [Asset_detail_link] |
| GOP_% | formula | percent | {GOP}/{Total_operating_revenue} |
| Market | multipleLookupValues | singleSelect | Asset_detail.[Market] via link [Asset_detail_link] |
| Brand | multipleLookupValues | singleSelect | Asset_detail.[Hotel_brand] via link [Asset_detail_link] |

## Hotel_GSS_data  (10)
| Field | Type | Result | Logic |
|---|---|---|---|
| Hotel_GSS_data_id | formula | singleLineText | {Asset_detail_link}&"_"&{Month}&"_"&{Year} |
| Month | formula | singleLineText | DATETIME_FORMAT({Date},'M') |
| Year | formula | number | YEAR({Date}) |
| Internal_asset_name | multipleLookupValues | singleLineText | Asset_detail.[Internal_asset_name] via link [Asset_detail_link] |
| Hotel_brand | multipleLookupValues | singleSelect | Asset_detail.[Hotel_brand] via link [Asset_detail_link] |
| Consolidated_survey_count | formula | number | IF({Hotel_brand} = "Marriott" , {Marriott_responses}, IF({Hotel_brand} = "Hilton", {Hilton_responses}, IF({Hotel_brand} = "IHG", {IHG_responses_QTD}))) |
| Consolidated_intent_to_recommend | formula | number | IF({Hotel_brand} = "Marriott" , {Marriott_intent_to_recommend}, IF({Hotel_brand} = "Hilton", {Hilton_stay_score}, IF({Hotel_brand} = "IHG", {IHG_likely_to_recommend_QTD}, IF({Hotel_brand} = "Hyatt", {Hyatt_NPS_net_promoter_scores})))) |
| Consolidated_cleanliness | formula | number | IF({Hotel_brand} = "Marriott" , {Marriott_cleanliness}, IF({Hotel_brand} = "Hilton", {Hilton_overall_cleanliness}, IF({Hotel_brand} = "IHG", {IHG_room_cleanliness_QTD}, IF({Hotel_brand} = "Hyatt", {Hyatt_room_cleanliness})))) |
| Consolidated_loyalty_recognition | formula | number | IF({Hotel_brand} = "Marriott" , {Marriott_elite_appreciation}, IF({Hotel_brand} = "Hilton", {Hilton_HH_appreciation}, IF({Hotel_brand} = "IHG", {IHG_loyalty_recognition_QTD}))) |
| Consolidated_staff_service | formula | number | IF({Hotel_brand} = "Marriott" , {Marriott_staff_service}, IF({Hotel_brand} = "Hilton", {Hilton_service_quality}, IF({Hotel_brand} = "IHG", {IHG_overall_service_QTD}, IF({Hotel_brand} = "Hyatt", {Hyatt_checkin_process})))) |

## Hotel_QA_data  (9)
| Field | Type | Result | Logic |
|---|---|---|---|
| Hotel_QA_data_id | formula | singleLineText | {Internal_asset_name}&"_"&{Month}&"_"&{Year} |
| Month | formula | singleLineText | DATETIME_FORMAT({Date},'M') |
| Year | formula | number | YEAR({Date}) |
| Internal_asset_name | multipleLookupValues | singleLineText | Asset_detail.[Internal_asset_name] via link [Asset_detail_link] |
| Hotel_brand | multipleLookupValues | singleSelect | Asset_detail.[Hotel_brand] via link [Asset_detail_link] |
| Consolidated_cleanliness | formula | number | IF({Hotel_brand} = "Marriott" , {Marriott_cleanliness}, IF({Hotel_brand} = "Hilton", {Hilton_cleanliness}, IF({Hotel_brand} = "IHG", {IHG_cleanliness}, IF({Hotel_brand} = "Hyatt", {Hyatt_cleanliness})))) |
| Consolidated_brand_standards | formula | number | IF({Hotel_brand} = "Marriott" , {Marriott_brand_promise}, IF({Hotel_brand} = "Hilton", {Hilton_brand_standards}, IF({Hotel_brand} = "IHG", {IHG_brand_standard_important}, IF({Hotel_brand} = "Hyatt", {Hyatt_brand_standard})))) |
| Consolidated_QA_score | formula | number | IF({Hotel_brand} = "Marriott" , {Marriott_BSA_score}, IF({Hotel_brand} = "Hilton", {Hilton_overall_QA_score}, IF({Hotel_brand} = "IHG", {IHG_brand_safety_standard}, IF({Hotel_brand} = "Hyatt", {Hyatt_score})))) |
| Consolidated_condition_upkeep | formula | number | IF({Hotel_brand} = "Marriott" , {Marriott_maintenance_upkeep}, IF({Hotel_brand} = "Hilton", {Hilton_guest_rooms}, IF({Hotel_brand} = "IHG", {IHG_condition}, IF({Hotel_brand} = "Hyatt", {Hyatt_working_order})))) |

## Guarantor_Compliance  (6)
| Field | Type | Result | Logic |
|---|---|---|---|
| Loan_summary_id | multipleLookupValues | singleLineText | Loan_summary_data.[Loan_summary_data_id] via link [Loan_summary_link] |
| Lenders_id | multipleLookupValues | singleLineText | Lenders.[Lenders_id] via link [Lenders_link] |
| Latest_debt_balance | multipleLookupValues | currency | Loan_summary_data.[Latest_debt_balance] via link [Loan_summary_link] |
| Contingent_liability | formula | currency | {Latest_debt_balance} * {%_Guarantee} |
| Loan_maturity | multipleLookupValues | date | Loan_summary_data.[Loan_maturity] via link [Loan_summary_link] |
| Interest_rate | multipleLookupValues | number | Loan_summary_data.[Interest_rate] via link [Loan_summary_link] |

## Hotel_PIP_history  (34)
| Field | Type | Result | Logic |
|---|---|---|---|
| Hotel_PIP_history_ID | formula | singleLineText | {Asset_detail_link} |
| Last_renovation_year | multipleLookupValues | number | Asset_detail.[Last_renovation_year] via link [Asset_detail_link] |
| Open_date | multipleLookupValues | date | Asset_detail.[Open_date] via link [Asset_detail_link] |
| Acquired_date | multipleLookupValues | date | Asset_detail.[Acquired_date] via link [Asset_detail_link] |
| Renovation_plan_start | multipleLookupValues | date | Asset_detail.[Renovation_plan_start] via link [Asset_detail_link] |
| PIP_brand_renovation_due_date | multipleLookupValues | date | Asset_detail.[PIP_brand_renovation_due_date] via link [Asset_detail_link] |
| Est_PIP_cost_per_key | multipleLookupValues | currency | Asset_detail.[Est_PIP_cost_per_key] via link [Asset_detail_link] |
| Est_PIP_cost | multipleLookupValues | currency | Asset_detail.[Est_PIP_cost] via link [Asset_detail_link] |
| Renovation_plan_start_year | multipleLookupValues | number | Asset_detail.[Renovation_plan_start_year] via link [Asset_detail_link] |
| PIP_overview | multipleLookupValues | singleLineText | Asset_detail.[PIP_overview] via link [Asset_detail_link] |
| Renovation_internal_target_end_date | multipleLookupValues | date | Asset_detail.[Renovation_internal_target_end_date] via link [Asset_detail_link] |
| PIP_requirements_link | multipleLookupValues | url | Asset_detail.[PIP_requirements_link] via link [Asset_detail_link] |
| PIP_owner_approval_status | multipleLookupValues | singleSelect | Asset_detail.[PIP_owner_approval_status] via link [Asset_detail_link] |
| PIP_construction_vendor | multipleLookupValues | singleSelect | Asset_detail.[PIP_construction_vendor] via link [Asset_detail_link] |
| Renovation_plan_start_manual_target | multipleLookupValues | date | Asset_detail.[Renovation_plan_start_manual_target] via link [Asset_detail_link] |
| Renovation_target_year | multipleLookupValues | number | Asset_detail.[Renovation_target_year] via link [Asset_detail_link] |
| Renovation_target_quarter | multipleLookupValues | singleLineText | Asset_detail.[Renovation_target_quarter] via link [Asset_detail_link] |
| Renovation_target_month | multipleLookupValues | number | Asset_detail.[Renovation_target_month] via link [Asset_detail_link] |
| PIP_comments | multipleLookupValues | singleLineText | Asset_detail.[PIP_comments] via link [Asset_detail_link] |
| PIP_design_vendor | multipleLookupValues | singleSelect | Asset_detail.[PIP_design_vendor] via link [Asset_detail_link] |
| PIP_budget_link | multipleLookupValues | url | Asset_detail.[PIP_budget_link] via link [Asset_detail_link] |
| Brand_renovation_due_date_year | multipleLookupValues | number | Asset_detail.[Brand_renovation_due_date_year] via link [Asset_detail_link] |
| PIP_deposit_estimate | multipleLookupValues | currency | Asset_detail.[PIP_deposit_estimate] via link [Asset_detail_link] |
| PIP_estimated_deposit_date | multipleLookupValues | date | Asset_detail.[PIP_estimated_deposit_date] via link [Asset_detail_link] |
| PIP_procurement_vendor | multipleLookupValues | singleSelect | Asset_detail.[PIP_procurement_vendor] via link [Asset_detail_link] |
| PIP_funding_secured | multipleLookupValues | singleSelect | Asset_detail.[PIP_funding_secured] via link [Asset_detail_link] |
| PIP_owner_contact | multipleLookupValues | singleSelect | Asset_detail.[PIP_owner_contact] via link [Asset_detail_link] |
| PIP_design_approver | multipleLookupValues | singleSelect | Asset_detail.[PIP_design_approver] via link [Asset_detail_link] |
| PIP_scope | multipleLookupValues | multipleSelects | Asset_detail.[PIP_scope] via link [Asset_detail_link] |
| PIP_design_review_status | multipleLookupValues | singleSelect | Asset_detail.[PIP_design_review_status] via link [Asset_detail_link] |
| PIP_owner_rep_contact | multipleLookupValues | singleSelect | Asset_detail.[PIP_owner_rep_contact] via link [Asset_detail_link] |
| PIP_funding_strategy | multipleLookupValues | singleSelect | Asset_detail.[PIP_funding_strategy] via link [Asset_detail_link] |
| PIP Authorization Req'd By | multipleLookupValues | date | Asset_detail.[PIP Authorization Req'd By] via link [Asset_detail_link] |
| Internal_asset_name (from Asset_detail_link) | multipleLookupValues | singleLineText | Asset_detail.[Internal_asset_name] via link [Asset_detail_link] |

## Cash_flow_tracking  (7)
| Field | Type | Result | Logic |
|---|---|---|---|
| Cash_flow_ID | formula | singleLineText | {Asset_detail_link}&"_"&{Month}&"_"&{Year} |
| Internal_asset_name | multipleLookupValues | singleLineText | Asset_detail.[Internal_asset_name] via link [Asset_detail_link] |
| Investments_link | multipleLookupValues | multipleRecordLinks | Asset_detail.[Investments_link] via link [Asset_detail_link] |
| Month | formula | number | MONTH({Date}) |
| Year | formula | number | YEAR({Date})
 |
| Automation_trigger | formula | singleLineText | IF({Date}, IF(DATETIME_FORMAT({Date}, 'MM') = DATETIME_FORMAT(DATEADD(TODAY(), 1, 'months'), 'MM'), 'Yes', 'No')) |
| Tax_flag | multipleLookupValues | singleLineText | Asset_detail.[Cashflow_Payment_type] via link [Asset_detail_link] |

## Hotel_GSS_data_v2  (3)
| Field | Type | Result | Logic |
|---|---|---|---|
| GSS_hotel_ID | formula | singleLineText | {Asset_detail_link}&"_"&{Month}&"_"&{Year} |
| Month | formula | singleLineText | DATETIME_FORMAT({Date},'M') |
| Year | formula | number | YEAR({Date}) |
