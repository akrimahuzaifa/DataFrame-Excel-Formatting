# xlsxwriter equivalents for styling Excel cells
import xlsxwriter

def set_cell_color_xlsxwriter(workbook, color):
    return workbook.add_format({'bg_color': color})

def set_font_style_xlsxwriter(workbook, bold=False, italic=False):
    return workbook.add_format({'bold': bold, 'italic': italic})

def set_alignment_xlsxwriter(workbook, horizontal='center', vertical='center'):
    align_map = {'center': 'center', 'left': 'left', 'right': 'right'}
    vert_map = {'center': 'vcenter', 'top': 'top', 'bottom': 'bottom'}
    return workbook.add_format({
        'align': align_map.get(horizontal, 'center'),
        'valign': vert_map.get(vertical, 'vcenter')
    })

def format_currency_xlsxwriter(workbook):
    return workbook.add_format({'num_format': '$#,##0.00'})

def format_percentage_xlsxwriter(workbook):
    return workbook.add_format({'num_format': '0.00%'})

def merge_and_center_xlsxwriter(worksheet, first_row, first_col, last_row, last_col, data, workbook):
    fmt = set_alignment_xlsxwriter(workbook)
    worksheet.merge_range(first_row, first_col, last_row, last_col, data, fmt)

def merge_and_center_xlsxwriter(worksheet, rangeToMerge: str, data, workbook):
    fmt = set_alignment_xlsxwriter(workbook)
    worksheet.merge_range(rangeToMerge, data, fmt)

def set_border_xlsxwriter(workbook, border_style=1, color='#000000'):
    # border_style: 1=thin, 2=medium, etc.
    return workbook.add_format({'border': border_style, 'border_color': color})