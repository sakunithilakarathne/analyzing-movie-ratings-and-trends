import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from jinja2 import Environment, FileSystemLoader
import os
from src.data_visualization.creating_plots import *

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the reports directory
reports_dir = os.path.join(script_dir, '../../reports')

output_report_file_path = os.path.join(reports_dir, 'eda_report.html')

def generate_pdf_report(movie_data):

    # Generate visualizations
    generate_visualizations(movie_data)

    # Load Jinja2 template
    env = Environment(loader=FileSystemLoader(reports_dir))
    template = env.get_template('report_template.html')

    # Prepare data for the report
    no_of_records = movie_data.shape[0]

    numeric_columns = ["Movie Runtime", "Domestic Gross", "IMDB Rating", "Metacritic Rating", "IMDB Vote Count",
                       "Release Month", "director_popularity", "actor_popularity", "writer_popularity",
                       "Language_Count", "Country_Count"]


    summary_numerical = movie_data[numeric_columns].describe().to_html()

    # Render the template with data
    html_out = template.render(
        no_of_records=no_of_records,
        summary_numerical=summary_numerical
    )

    # Save the HTML report to the reports folder

    with open(output_report_file_path, 'w') as f:
        f.write(html_out)

    print(f"Report saved successfully at {output_report_file_path}")