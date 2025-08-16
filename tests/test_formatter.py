import unittest
from openpyxl import Workbook
from src.formatter import format_excel_file

class TestExcelFormatter(unittest.TestCase):

    def setUp(self):
        self.workbook = Workbook()
        self.sheet = self.workbook.active

    def test_fill_cell_color(self):
        format_excel_file.fill_cell_color(self.sheet['A1'], 'FF0000')  # Red color
        self.assertEqual(self.sheet['A1'].fill.start_color, 'FF0000')

    def test_add_dollar_sign(self):
        format_excel_file.add_dollar_sign(self.sheet['B1'], 1000)
        self.assertEqual(self.sheet['B1'].number_format, '$#,##0.00')
        self.assertEqual(self.sheet['B1'].value, 1000)

    def test_add_percentage_sign(self):
        format_excel_file.add_percentage_sign(self.sheet['C1'], 0.25)
        self.assertEqual(self.sheet['C1'].number_format, '0.00%')
        self.assertEqual(self.sheet['C1'].value, 0.25)

    def test_merge_and_center_rows(self):
        self.sheet.merge_cells('D1:D2')
        format_excel_file.merge_and_center(self.sheet['D1'])
        self.assertTrue(self.sheet['D1'].alignment.horizontal, 'center')
        self.assertTrue(self.sheet['D1'].alignment.vertical, 'center')

    def test_bold_header(self):
        self.sheet['E1'] = 'Header'
        format_excel_file.bold_header(self.sheet['E1'])
        self.assertTrue(self.sheet['E1'].font.bold)

    def tearDown(self):
        self.workbook.close()

if __name__ == '__main__':
    unittest.main()