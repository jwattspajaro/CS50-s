from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Add shirtificate image to the header
        self.image("./shirtificate.png", 10, 70, 190)
        # Set font and size for the title
        self.set_font("Arial", "", 48)
        # Add title to the header
        self.cell(0, 57, "CS50 Shirtificate", align="C")
        # Move the cursor to the next line
        self.ln(20)

def main():
    # Prompt the user for their name
    name = input("Name: ")
    # Generate the shirtificate with the user's name
    shirt(name)

def shirt(s):
    # Create a new PDF object
    pdf = PDF()
    # Add a new page with portrait orientation and A4 format
    pdf.add_page(orientation="portrait", format="a4")
    # Set font and size for the user's name
    pdf.set_font("Arial", size=24)
    # Set text color to white for the user's name
    pdf.set_text_color(255, 255, 255)
    # Add user's name to the PDF
    pdf.cell(0, 213, f"{s} took CS50", align="C")
    # Save the PDF as "shirtificate.pdf"
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
