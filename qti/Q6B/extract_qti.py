import os
import re
import xml.etree.ElementTree as ET

output_filename = "quiz_questions.txt"

def clean_text(text):
    if not text:
        return ""
    # Strip HTML tags
    clean = re.sub(r'<[^>]+>', ' ', text)
    # Normalize whitespaces
    return ' '.join(clean.split())

with open(output_filename, "w", encoding="utf-8") as out_file:
    question_count = 0
    
    # Walk through the items folder
    for root, dirs, files in os.walk("./items"):
        for file in files:
            if file.startswith("qti_item_") and file.endswith(".xml"):
                file_path = os.path.join(root, file)
                question_count += 1
                
                out_file.write(f"========================================\n")
                out_file.write(f"QUESTION #{question_count}  ({file})\n")
                out_file.write(f"========================================\n")
                
                try:
                    # Read the raw XML content
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        raw_content = f.read()
                    
                    # Extract everything inside CDATA or text nodes
                    # Find all text content between tags or inside HTML snippets
                    # ET.fromstring can fail on custom QTI tags, so we parse all text elements
                    parsed_text = re.findall(r'>([^<]+)<', raw_content)
                    
                    lines_written = set()
                    for snippet in parsed_text:
                        cleaned = clean_text(snippet)
                        # Filter out XML boilerplate/attributes and duplicates
                        if cleaned and len(cleaned) > 1 and not cleaned.startswith("http") and cleaned not in lines_written:
                            out_file.write(f"• {cleaned}\n")
                            lines_written.add(cleaned)
                            
                except Exception as e:
                    out_file.write(f"Error reading file: {e}\n")
                    
                out_file.write("\n\n")

print(f"Done! Successfully processed {question_count} questions into {output_filename}")