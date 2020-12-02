# Help in a SNAP
Many families depend on benefits like SNAP (previously known as "Food Stamps") to fully feed or supplement their grocery bills.  During times of economic insecurity certain communities are at greater risk.  And these communities are less likely to bounce back from economic turbulence. This study attempts to categorize these vulnerable groups for targeted additional help during financial uncertainty.  A previous geographical analysis determined a merging hotspot of San Juan County, NM for _increased_ SNAP benefits.  And an emerging cold spot of Cherry County, NE for _decreased_ SNAP benefits.  I will do a comparison between the states of New Mexico and Nebraska using SNAP datasets from 2007 and 2017. Some things of note:
1. The broad scope for the SNAP analysis will be at the state level since that is the lowest granularity that I can go with SNAP datasets.
1. 2007 and 2017 will be compared to see the characteristics of SNAP households before the 2008 crisis and those that continued to rely on SNAP 10 years after the housing crash, during an economic boom.  This will give us some insight on vulnerable populations during the COVID19 current crisis.

# The data science problem
What do food insecurity community characteristics look like?  I will put these into a model to predict communities at risk.  This will give me a risk assessment strategy for states vulnerable to food insecurity.

# The model
The target variable is `CAT_ELIG`.  It was recorded differently in 2007 and 2017. For uniformity, I calculated the column to be:
- 0 = Not Eligible
- 1 = Eligible

I started with almost 800 features. After addressing nulls and correlation analysis, I ended up with 32 features, including the target variable.

My intention was to use an interpretable model so I could see the coefficients that are influencing prediction of SNAP receipients.  After testing several models, I landed on a Vote Ensemble with Random Forest, Gradient Boost and Bagging Classifiers.  

# Acquiring the data
- The SNAP data was acquired through the USDA and is part of their [SNAP Quality Control Datasets](https://www.fns.usda.gov/resource/snap-quality-control-data). 
- The state shapefiles were acquired through the [US Census Bureau Boundary Shapefiles](https://www.census.gov/geographies/mapping-files/time-series/geo/carto-boundary-file.html)

Data dictionaries can be found in the reports folder for [2007](http://localhost:8888/lab/tree/reports/07_DataDict.pdf) and [2017](http://localhost:8888/lab/tree/reports/17_DataDict.pdf) datasets.  A note on government data, though it was processed by the same company "Mathmatica", I ran into data conversion issues.  For example, I used an online converter to turn the 07_DataDict.pdf into a CSV file, which ran great.  But, when I tried the same method on the 17DataDict.pdf there were different formatting issues (ie. unusual spaces) that caused the conversion to fail.

# The process
1. First, I broke the data into two states of interest: New Mexico and Nebraska. As well as a 10 year gap analysis by comparing 2007 and 2017 datasets, totaling 4 datasets. My target variable is the field `CAT_ELIG` which is whether someone is eligibile to receive benefits.
1. Next, I needed to address the large amount of null data present in both 2007 and 2017 datasets.
1. After that, I looked at correlations between sets of category defined in the technical documents as it related to `CAT_ELIG`. Those categories are "Unit Demographics", "Unit Countable Income", "Unit Countable Assets", "Unit Expenses and Deductions", "Person-level Characteristics: 1-16", and "Person-level Countable Income: 1-16".
1. I then combined my final 31 features + 1 target feature, across all 4 datasets into a single, combined dataset for processing through my model.
1. I used a Vote Ensemble with Random Forest, Gradient Boost and Bagging Classifier which gave me a CV best accuracy score of 95%.
1. I used sklearn.treeinterpreter to get a list of the most impactful classifiers on model prediction.

# Conclusions
The model correlations concluded that the most important indictor of receiving SNAP benefits is housing security. The top 4 most impactful features all relate to housing allowable housing deductions.  
- FSSLTDED and SHELDED are indicators of how much someone is paying for their home. 
- FSTOTDED & FSSTDDE2 are deductions relating to housing.

# Next Steps
1. A geographic analysis that consists of access to housing resources([HUD GIS](https://www.hudexchange.info/programs/coc/gis-tools/)), food pantries and counties showing high levels of SNAP dependency.  This would pinpoint areas where local governments or charitable organizations could present the most assistance to communities in need.  Especially during COVID, targeting high need areas would be good way to direct tight resources.  
1. Post this to an interactive dashboard such as Leaflet.json.  

# List of files:
1. Jupyter Files:
    1. [1_EDA](http://localhost:8888/lab/tree/1_EDA.ipynb)
    1. [2_Correlations](http://localhost:8888/lab/tree/2_Correlations.ipynb)
    1. [3_Model](http://localhost:8888/lab/tree/3_Model.ipynb)
    1. [4_Predictions](http://localhost:8888/lab/tree/4_Predictions.ipynb)
    1. [5_Insights](http://localhost:8888/lab/tree/5_Insights.ipynb)    
1. Folders: 
    1. [Reports (Incl Data Dictionaries and Technical Documents)](http://localhost:8888/lab/tree/reports)
    1. [GIS Analysis Files](http://localhost:8888/lab/tree/GIS.zip)
    1. [Data](http://localhost:8888/lab/tree/data)
    1. [Python Code](http://localhost:8888/lab/tree/python_code)
    1. [Images](http://localhost:8888/lab/tree/images)
1. [Final Model](http://localhost:8888/lab/tree/final_model.sav)

# Resources
- [SNAP Quality Control Datasets](https://www.fns.usda.gov/resource/snap-quality-control-data)
- [HUD GIS](https://www.hudexchange.info/programs/coc/gis-tools/)

# Author
Melissa Anthony
