# Let's Visualize

"Let's Visualize" is a versatile and user-friendly web application designed to make data visualization accessible to everyone. With this tool, users can upload any CSV dataset and quickly generate interactive charts to explore and understand their data. The application supports various chart types, including line, bar, and pie charts, allowing users to customize their visualizations according to their needs. Built with Flask, Pandas, and Chart.js, "Let's Visualize" ensures a seamless experience from data upload to insightful visual representation.

## Features

- **CSV File Upload**: Users can upload their CSV files to the application for visualization.
- **Data Table Display**: The uploaded data is displayed in a scrollable table format.
- **Interactive Charts**: Users can generate line, bar, and pie charts from their data.
- **Customizable Axes**: Users can select which columns to use for the X and Y axes.
- **Responsive Design**: The application is designed to be responsive and user-friendly.

## Installation

1. **Clone the Repository**

   ```sh
   git clone https://github.com/yourusername/lets-visualize.git
   cd lets-visualize

2. **Install Dependencies**

   ```sh
   pip install -r requirements.txt
   
3. **Run the Application**

   ```sh
   flask run
```
lets-visualize/
├── app.py                  # Main Flask application
├── templates/
│   ├── upload.html         # File upload page template
│   └── dataReview.html     # Data review and chart generation page template
├── uploads/                # Directory to store uploaded files
├── requirements.txt        # Python dependencies
└── README.md               # Project readme file
```
## Dependencies

- Flask: Web framework for Python.
- Pandas: Data manipulation and analysis library.
- Chart.js: JavaScript library for creating interactive charts.
- Werkzeug: Comprehensive WSGI web application library.
