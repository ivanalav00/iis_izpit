from evidently.metric_preset import DataDriftPreset
from evidently.report import Report
import pandas as pd

reference_data = pd.read_csv('../../data/processed/reference_dataset.csv')
current_data = pd.read_csv('../../data/processed/current_data.csv')

report = Report(metrics=[
        DataDriftPreset(),
    ])

report.run(reference_data=reference_data, current_data=current_data)
report.save_html('../../reports/data_drift_report.html')
