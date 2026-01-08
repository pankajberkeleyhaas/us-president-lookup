import os
import logging
import sys
from flask import Flask, render_template, request, jsonify

# Configure structured logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger()

app = Flask(__name__)

# Dictionary of US Presidents
PRESIDENTS = {
    1: "George Washington", 2: "John Adams", 3: "Thomas Jefferson", 4: "James Madison",
    5: "James Monroe", 6: "John Quincy Adams", 7: "Andrew Jackson", 8: "Martin Van Buren",
    9: "William Henry Harrison", 10: "John Tyler", 11: "James K. Polk", 12: "Zachary Taylor",
    13: "Millard Fillmore", 14: "Franklin Pierce", 15: "James Buchanan", 16: "Abraham Lincoln",
    17: "Andrew Johnson", 18: "Ulysses S. Grant", 19: "Rutherford B. Hayes", 20: "James A. Garfield",
    21: "Chester A. Arthur", 22: "Grover Cleveland", 23: "Benjamin Harrison", 24: "Grover Cleveland",
    25: "William McKinley", 26: "Theodore Roosevelt", 27: "William Howard Taft", 28: "Woodrow Wilson",
    29: "Warren G. Harding", 30: "Calvin Coolidge", 31: "Herbert Hoover", 32: "Franklin D. Roosevelt",
    33: "Harry S. Truman", 34: "Dwight D. Eisenhower", 35: "John F. Kennedy", 36: "Lyndon B. Johnson",
    37: "Richard Nixon", 38: "Gerald Ford", 39: "Jimmy Carter", 40: "Ronald Reagan",
    41: "George H. W. Bush", 42: "Bill Clinton", 43: "George W. Bush", 44: "Barack Obama",
    45: "Donald Trump", 46: "Joe Biden", 47: "Donald Trump"
}

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Renders the home page and handles the president lookup.
    """
    president_name = None
    error_message = None
    number = None

    if request.method == "POST":
        try:
            number_input = request.form.get("number")
            if number_input:
                number = int(number_input)
                president_name = PRESIDENTS.get(number)
                if not president_name:
                    error_message = f"No president found for number {number}. Please enter a number between 1 and 47."
            else:
                 error_message = "Please enter a number."
        except ValueError:
            error_message = "Invalid input. Please enter a valid integer."

    return render_template("index.html", president_name=president_name, error_message=error_message, number=number)

@app.route("/health")
def health_check():
    """
    Health check endpoint.
    """
    return jsonify({"status": "OK"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=True, host="0.0.0.0", port=port)
