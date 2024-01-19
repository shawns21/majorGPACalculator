import time

try:
    # Your existing code here
    import re
    from pdfminer.high_level import extract_pages, extract_text

    text = extract_text("transcript.pdf")
    print(text)
    time.sleep(20)

except Exception as e:
    print(f"An error occurred: {e}")
    time.sleep(10)  # Keep the console window open for 10 seconds (adjust as needed)

