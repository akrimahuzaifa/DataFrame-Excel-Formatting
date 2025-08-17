# Excel Formatting Project

This project provides a set of utilities for formatting Excel output files. It includes features such as filling cells with colors, adding dollar and percentage signs to specific columns, merging and centering rows, styling headers and apply cborders to cells.


## Project Structure

```
excel-formatting-project
├── src
│   ├── formatter.py          # Main entry point for formatting Excel files
│   ├── utils
│   │   └── styles.py        # Utility functions for styling Excel cells
│   └── templates
│       └── example_template.py # Example template for formatting an Excel file
├── requirements.txt          # List of dependencies required for the project
├── README.md                 # Documentation for the project
└── tests
    └── test_formatter.py     # Unit tests for the formatting functions
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd excel-formatting-project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
Example template: to run and check the functionalities in action:
```bash
python -m src.templates.example_template
```

To format an Excel file, you can use the functions defined in `src/formatter.py`. Here’s a brief overview of the available functions:

- **apply_styles(sheet)**: Applies predefined styles to the specified Excel sheet.
- **fill_cell_color(sheet, cell, color)**: Fills the specified cell with the given color.
- **add_dollar_sign(sheet, column)**: Adds dollar signs to all values in the specified column.
- **add_percentage_sign(sheet, column)**: Adds percentage signs to all values in the specified column.
- **merge_and_center_rows(sheet, start_row, end_row)**: Merges the specified rows and centers the content.

## Example

Refer to `src/templates/example_template.py` for an example of how to use the formatting functions to create a formatted Excel report.

## Testing

Unit tests for the formatting functions can be found in `tests/test_formatter.py`. To run the tests, use the following command:

```
pytest tests/
```

This will ensure that all formatting functions work as expected and that the output Excel files are correctly formatted.