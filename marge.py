import PyPDF2
import os

input_path = r'./Lin-Algebra-Schaum-6th-Edition (1) (1).pdf'
output_folder = r'E:\sta\read\12\Linear Algebra'
output_filename = "Linear_Algebra_Refined_Section.pdf"
final_output_path = os.path.join(output_folder, output_filename)

def extract_page_range_safe(input_pdf, output_pdf, start_page, end_page):
    try:
        if not os.path.exists(input_pdf):
            print("Error: Input file path is invalid.")
            return

        with open(input_pdf, 'rb') as infile:
            reader = PyPDF2.PdfReader(infile)
            writer = PyPDF2.PdfWriter()

            total_pages = len(reader.pages)

            if start_page > total_pages or start_page < 1:
                print(f"Error: Start page {start_page} is out of range.")
                return

            actual_end = min(end_page, total_pages)

            for i in range(start_page - 1, actual_end):
                writer.add_page(reader.pages[i])

            with open(output_pdf, 'wb') as outfile:
                writer.write(outfile)

        print(f"Success! Pages {start_page} to {actual_end} saved as '{output_filename}'")

    except Exception as e:
        print(f"Technical Error: {e}")

extract_page_range_safe(input_path, final_output_path, 173, 203)