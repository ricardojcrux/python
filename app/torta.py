import tools, charts, read
import pandas as pd

def porc():
    continent = input('Type a Continent: ')

    df = pd.read_csv('data.csv')
    df = df[df['Continent'] == continent]
    countries = df['Country'].values
    porc = df['World Population Percentage'].values
    charts.pie_chart(continent,countries,porc)

if __name__ == '__main__':
    porc()