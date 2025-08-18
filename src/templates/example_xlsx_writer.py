import xlsxwriter
from ..utils.styles_xw import *

def create_example_xlsxwriter_template():
    workbook = xlsxwriter.Workbook("example_report_xw.xlsx")
    worksheet = workbook.add_worksheet("Example Report")

    # Define formats
    header_format = workbook.add_format({
        'bold': True,
        'align': 'center',
        'valign': 'vcenter',
        'bg_color': '#00FFCC',
        'border': 1
    })
    title_format = workbook.add_format({
        'bold': True,
        'align': 'center',
        'valign': 'vcenter',
        'border': 1
    })
    currency_format = format_currency_xlsxwriter(workbook)
    percentage_format = format_percentage_xlsxwriter(workbook)
    border_format = set_border_xlsxwriter(workbook)

    # Merge and center title row
    worksheet.merge_range(0, 0, 0, 2, "Sales Report", title_format)
    #merge_and_center_xlsxwriter(worksheet, "A1:C1", "Sales Report", workbook)

    # Set header values
    headers = ["Item", "Amount", "Percentage"]
    worksheet.write_row(1, 0, headers, header_format)



    # Add blank row between header and data
    # (Row 2 is left blank)

    # Add data
    data = [
        ["Item A", 1000, 0.25],
        ["Item B", 1500, 0.50],
        ["Item C", 2000, 0.75],
    ]

    for idx, (item, amount, percentage) in enumerate(data):
        row = idx + 2  # Data starts at row 3 (zero-indexed)
        worksheet.write(row, 0, item, border_format)
        worksheet.write(row, 1, amount, currency_format)
        worksheet.write(row, 2, percentage, percentage_format)
    
    # Autofit the worksheet.
    worksheet.autofit()

    # Apply borders to all cells (including header and title)
    # for r in range(0, len(data) + 3):
    #     for c in range(0, 3):
    #         worksheet.write_blank(r, c, None, border_format)

    workbook.close()

if __name__ == "__main__":
    create_example_xlsxwriter_template()