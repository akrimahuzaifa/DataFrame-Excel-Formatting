from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font, Alignment
from ..utils.styles import set_cell_color, set_font_style, set_alignment

def create_example_template():
    # Create a new workbook and select the active worksheet
    wb = Workbook()
    ws = wb.active
    ws.title = "Example Report"

    # Set header values
    headers = ["Item", "Amount", "Percentage"]
    ws.append(headers)

    # Style the header
    for col in range(1, len(headers) + 1):
        cell = ws.cell(row=1, column=col)
        set_font_style(cell, bold=True)
        set_alignment(cell, horizontal='center')
        set_cell_color(cell, color="00FFCC")  # Light green background

    # Add data
    data = [
        ["Item A", 1000, 0.25],
        ["Item B", 1500, 0.50],
        ["Item C", 2000, 0.75],
    ]

    for item, amount, percentage in data:
        ws.append([item, amount, percentage])

    # Format Amount and Percentage columns
    for row in range(2, len(data) + 2):
        ws.cell(row=row, column=2).number_format = '"$"#,##0.00'  # Dollar format
        ws.cell(row=row, column=3).number_format = '0.00%'  # Percentage format

    # Merge and center a title row
    ws.merge_cells('A1:C1')
    title_cell = ws.cell(row=1, column=1)
    title_cell.value = "Sales Report"
    set_font_style(title_cell, bold=True)
    set_alignment(title_cell, horizontal='center', vertical='center')

    # Save the workbook
    wb.save("example_report.xlsx")

if __name__ == "__main__":
    create_example_template()