import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pathlib import Path

base = Path("D:/Github/exercise-4-RobFisch/")
data = base / "data/"
output = base / "output/"

output.mkdir (parents = True, exist_ok = True)

# Import both data tables into python using pandas. Set the index column to "MESS_DATUM" and parse the column values as dates. [1P]
garmisch = pd.read_csv(data / "produkt_klima_tag_20171010_20190412_01550.txt", sep = ";", index_col="MESS_DATUM", parse_dates=["MESS_DATUM"], na_values=-999.0)

zugspitze = pd.read_csv(data / "produkt_klima_tag_20171010_20190412_05792.txt", sep = ";", index_col="MESS_DATUM", parse_dates=["MESS_DATUM"], na_values=-999.0)

zugspitze.head()
garmisch.head()

# Clip the tables to the year 2018: [1P]

garmisch  = garmisch.loc["2018"]
zugspitze = zugspitze.loc["2018"]


# Resample the temperature data to monthly averages (" TMK") and store them in simple lists: [1P]
garmisch_agg  = list(garmisch.resample("1M").mean()[" TMK"])
zugspitze_agg = list(zugspitze.resample("1M").mean()[" TMK"])

# Define a plotting function that draws a simple climate diagram
# Add the arguments as mentioned in the docstring below [1P]
# Set the default temperature range from -15°C to 20°C and the precipitation range from 0mm to 370mm [1P]
def create_climate_diagram(df,
                           temp_col,
                           prec_col,
                           title,
                           filename,
                           temp_min=-15,
                           temp_max=20,
                           prec_min=0,
                           prec_max=370):
    """
    Draw a climate diagram.
    
    Parameters
    ----------
    df : pd.DataFrame
        Dataframe with values to plot from
    temp_col : str
        Name of temperature column
    prec_col : str
        Name of precipitation column
    title : String
        The title for the figure
    filename : String
        The name of the output figure
    temp_min : Number
        The minimum temperature value to display
    temp_max : Number
        The maximum temperature value to display
    prec_min : Number
        The minimum precipitation value to display
    prec_max : Number
        The maximum precipitation value to display

    Returns
    -------
    The figure
    
    """
    fig = plt.figure(figsize=(10,8))
    plt.rcParams['font.size'] = 16

    ax2 = fig.add_subplot(111)
    ax1 = ax2.twinx()

    # Draw temperature values as a red line and precipitation values as blue bars: [1P]
    # Hint: Check out the matplotlib documentation how to plot barcharts. Try to directly set the correct
    #       x-axis labels (month shortnames).
    ax2.bar(...)
    ax1.plot(...)
    
    # Set appropiate limits to each y-axis using the function arguments: [1P]
    ax2.
    ax1.
    
    # Set appropiate labels to each y-axis: [1P]
    ax2.
    ax1.

    # Give your diagram the title from the passed arguments: [1P]
    plt.title(...)

    # Save the figure as png image in the "output" folder with the given filename. [1P]
    
    return fig

# Use this function to draw a climate diagram for 2018 for both stations and save the result: [1P]
create_climate_diagram(...)
create_climate_diagram(...)
