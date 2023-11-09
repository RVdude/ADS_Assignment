# Import required Python packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset using pandas
fifa_players = pd.read_csv("Fifa 23 Players Data.csv")

# Sort the dataset by both Potential and Overall ratings and select the top 10 players
top_10_players = fifa_players.nlargest(10, ['Potential', 'Overall'])

# Count player nationalities and age groups
player_nationalities_count = fifa_players['Nationality'].value_counts().head(10)

age_groups = ['16-20', '21-25', '26-30', '31-35', '36-40', '41-45']
age_bins = [16, 21, 26, 31, 36, 41, 46]

fifa_players['Age Group'] = pd.cut(fifa_players['Age'], bins=age_bins, labels=age_groups)
age_group_count = fifa_players['Age Group'].value_counts()

# Define a function to plot line graphs
def PlotLineGraph(players, overall_ratings, potential_ratings):
    """Plotting line graph using the given data and column name.
    
    Returns:
    None
    """
    plt.figure(figsize=(10, 6))
    plt.plot(players, overall_ratings, color='#5865f2', marker='o', linestyle='-', label='Overall Rating')
    plt.plot(players, potential_ratings, color='#a60096', marker='o', linestyle='-', label='Potential Rating')
    plt.xlabel("Player Name")
    plt.ylabel('Rating')
    plt.xticks(rotation=45)  # Rotate x-axis labels for readability
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.title('Top 10 Players with Highest Overall and Potential Ratings')
    plt.legend()
    plt.tight_layout()
    plt.show()

# Define functions to plot bar and pie charts
def PlotBar(data, title, xlabel, ylabel):
    """Plotting bar graph using the given data.
    
    Returns:
    None
    """
    plt.figure(figsize=(12, 6))
    data.plot(kind='bar', color='#5865f2')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def PlotPie(data, title):
    """Plotting pie graph using the given data.
    
    Returns:
    None
    """
#     data= data.head(5)
    plt.figure(figsize=(6, 6))
    plt.pie(data, labels=data.index, autopct='%1.1f%%', colors=['#5865f2', '#a60096', '#00cc66', '#ff9900', '#990099', '#99cc33'])
    plt.title(title)
    plt.tight_layout()  # Remove the extra space here
    plt.show()

# Call the functions to plot the graphs
PlotLineGraph(top_10_players['Full Name'], top_10_players['Overall'], top_10_players['Potential'])
PlotBar(player_nationalities_count, 'Top 10 Player Nationalities in FIFA 23', 'Nationality', 'Number of Players')
PlotPie(age_group_count, 'Player Age Distribution in FIFA 23')
