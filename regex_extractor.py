import re

# Load input 
sample_text = """
Contact me at user@example.com or firstname.lastname@company.co.uk
Visit https://www.example.com or https://sub.example.org/page
Call (123) 456-7890 or 123-456-7890 or 123.456.7890
My card is 1234-5678-9012-3456 or 1234 5678 9012 3456
Meeting time: 14:30 and 2:30 PM
Check <div class="example"> and <img src="pic.jpg">
Post with #Hashtag and #AnotherOne
Price: $19.99 and $1,234.56
"""

# Regex patterns
patterns = {
    "Emails": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
    "URLs": r"https?://[\w.-]+(?:\.[\w.-]+)+(?:/[\w./?%&=-]*)?",
    "Phone Numbers": r"(\(\d{3}\)\s?|\d{3}[-.])\d{3}[-.]\d{4}",
    "Credit Cards": r"\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}",
    "Time (24 & 12 hr)": r"\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b",
    "HTML Tags": r"<[^>]+>",
    "Hashtags": r"#\w+",
    "Currency": r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?",
}

# Extract and print
with open("test_output.txt", "w") as f:
    for label, pattern in patterns.items():
        matches = re.findall(pattern, sample_text)
        f.write(f"{label}:\n")
        for match in matches:
            f.write(f"  - {match}\n")
        f.write("\n")
