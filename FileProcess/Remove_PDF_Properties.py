
# run: python Remove_PDF_Properties.py

import fitz  # PyMuPDF


def clear_pdf_metadata(input_path, output_path):
    # Open the PDF file
    doc = fitz.open(input_path)

    # Clear the metadata dictionary entirely
    doc.set_metadata({})

    # Save the cleaned file
    doc.save(output_path)
    doc.close()
    print(f"Metadata successfully cleared! Saved to: {output_path}")


# Example usage:
clear_pdf_metadata("your_file.pdf", "your_file_cleaned.pdf")
