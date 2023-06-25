#	Marketing Strategy and Branding Services File

#Import Necessary Libraries
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

#Data Creation
brands = ['Brand A', 'Brand B', 'Brand C', 'Brand D', 'Brand E']
emp_size = [25, 30, 35, 40, 45]
market_share = [32, 28, 20, 17, 5]

#Creating DataFrame
market_data = pd.DataFrame({'Brands':brands,'Employee Size':emp_size,'Market Share':market_share})

#Visualization
sns.set_style('whitegrid')
plt.figure(figsize=(10,6))
sns.barplot(x='Brands',y='Employee Size',data=market_data)
plt.title('Employee Size by Brand')

#Show Plot
plt.show()

#Set Markdown
markdown_by_brand = '''
## Employee Size by Brand

| Brand | Employee Size |
|------|---------------|
'''

#Loop through Data
for i,row in market_data.iterrows():
    markdown_by_brand += '|' + row['Brands'] + '|' + str(row['Employee Size']) + '|\n'

#Create Pie Chart
plt.pie(market_data['Market Share'], labels=market_data['Brands'], autopct='%1.1f%%')
plt.title('Market Share by Brand')

#Show Plot
plt.show()

#Create Markdown
markdown_by_share = '''
## Market Share by Brand

| Brand | Market Share |
|------|---------------|
'''

#Loop through Data
for i,row in market_data.iterrows():
    markdown_by_share += '|' + row['Brands'] + '|' + str(row['Market Share']) + '|\n'

#Create Function to Analyze Data
def analyze_data(markdown_by_brand,markdown_by_share):
    '''
    Analyze Data Function
    
    Inputs:
    markdown_by_brand: contains markdown of employee sizes
    markdown_by_share: contains markdown of market shares
    
    Outputs:
    analysis_data: contains analysis of both markdowns
    '''
    
    #Create Empty List
    analysis_data = []
    
    #Add Markdowns to List
    analysis_data.append(markdown_by_brand)
    analysis_data.append(markdown_by_share)
    
    #Add Analysis of Market Share
    if market_data['Market Share'].min() == 5:
        analysis_data.append('Brand E has the lowest market share of 5%\n')
    if market_data['Market Share'].max() == 32:
        analysis_data.append('Brand A has the highest market share of 32%\n')
        
    #Add Analysis of Employee Size
    if market_data['Employee Size'].min() == 25:
        analysis_data.append('Brand A has the lowest number of employees of 25\n')
    if market_data['Employee Size'].max() == 45:
        analysis_data.append('Brand E has the highest number of employees of 45\n')
        
    #Return Analysis
    return analysis_data

#Run Analysis
analysis_data = analyze_data(markdown_by_brand,markdown_by_share)

#Print Analysis
for analysis in analysis_data:
    print(analysis)