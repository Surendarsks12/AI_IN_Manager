import pandas as pd
from fpdf import FPDF

# Load the allocation sheet
sheet_path = "allocation_sheet.csv"  # export manually or use pygsheets
df = pd.read_csv(sheet_path)

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 14)
        self.cell(0, 10, "Production Allocation Report", ln=True, align='C')
        self.ln(10)

    def table(self, df):
        self.set_font("Arial", size=10)
        col_width = self.epw / len(df.columns)
        self.set_fill_color(200, 220, 255)

        for col in df.columns:
            self.cell(col_width, 10, col, border=1, fill=True)
        self.ln()

        for _, row in df.iterrows():
            for val in row:
                self.cell(col_width, 10, str(val), border=1)
            self.ln()

pdf = PDF()
pdf.add_page()
pdf.table(df)
pdf.output("production_allocation.pdf")
