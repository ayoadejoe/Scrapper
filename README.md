# Scrapper
This application is a GUI represensation of the assessment: IRTW001 Python Training: Level 2 | Mini data analysis project: It scraps data from nairaland.com

The application when launched, would first scrap Nairaland.com for latest posts. It collects approximately 500 rows of data. The data includes comments, likes and shares. Using Selenium, the data cleaned, errors and nulls removed. After which it saves the data in a .csv file.
The next step is to process the .csv file using Panda and displaying the dataFrame with Tkinter GUI. The GUI illustrates the descriptive statistics by comparing the outcomes of the data. With matplotlib Figure, it then displays the resulting set of visualisations - bar chart, scatter plot, pie chart on a canvas. 
Page 1: this page contains all data scrapped.
Page 2: contains the statistics.
Page 3: contains the plot. 
Please click above buttons to view it.

The script scrap1.py receives two parameters:

1. The latest version of firefox webdriver called geckodriver (version in this project is 0.29.1), GeckoDriver is a link between Selenium tests and the Firefox browser. 
2. The website url (https://www.nairaland.com)

The FrameArrange.py script is the GUI, coded with TKinter. On first launch, the Framearrange collects data, which may be 500 rows and a bit more. All visualisations take place in the GUI.
