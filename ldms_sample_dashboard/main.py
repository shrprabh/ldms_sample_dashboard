import ipywidgets as widgets
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from IPython.display import display

def create_dashboard():
    """Create an interactive dashboard with static data"""
    # Create some static sample data
    dates = pd.date_range('2023-01-01', periods=30)
    data = {
        'Temperature': np.random.normal(25, 5, 30),
        'Humidity': np.random.normal(60, 10, 30),
        'Pressure': np.random.normal(1013, 5, 30)
    }
    df = pd.DataFrame(data, index=dates)
    
    # Create widgets
    metric_dropdown = widgets.Dropdown(
        options=['Temperature', 'Humidity', 'Pressure'],
        value='Temperature',
        description='Metric:'
    )
    
    plot_type = widgets.RadioButtons(
        options=['Line', 'Bar', 'Histogram'],
        value='Line',
        description='Plot Type:',
        layout={'width': 'max-content'}
    )
    
    output = widgets.Output()
    
    # Define the update function
    def update_plot(*args):
        with output:
            output.clear_output(wait=True)
            plt.figure(figsize=(10, 6))
            
            selected_metric = metric_dropdown.value
            selected_plot = plot_type.value
            
            if selected_plot == 'Line':
                plt.plot(df.index, df[selected_metric], marker='o')
            elif selected_plot == 'Bar':
                plt.bar(df.index, df[selected_metric])
            else:  # Histogram
                plt.hist(df[selected_metric], bins=10)
                
            plt.title(f"{selected_metric} over time")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
    
    # Connect the widgets to the update function
    metric_dropdown.observe(update_plot, 'value')
    plot_type.observe(update_plot, 'value')
    
    # Create the layout
    controls = widgets.VBox([metric_dropdown, plot_type])
    dashboard = widgets.HBox([controls, output])
    
    # Initial call to update the plot
    update_plot()
    
    return dashboard

def display_dashboard():
    """Display the dashboard in a Jupyter notebook."""
    dashboard = create_dashboard()
    display(dashboard)