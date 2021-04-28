import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import pydeck as pdk
import numpy as npy

columns = ['Name', 'Metres', 'Year', 'Type', 'Main use', 'Country', 'City', 'Lat', 'Lon']

def csv_to_df(filename):
    df = pd.read_csv(filename)
    return df

def read_csv(filename):
    data_frame = pd.read_csv(filename)
    list = []

    columns = ['Name', 'Metres', 'Year', 'Type', 'Main use', 'Country', 'City', 'Lat', 'Lon']

    for index, row in data_frame.iterrows():
        sub = []
        #print(str(row[0] + '\n'))
        for col in columns:
            index_no = data_frame.columns.get_loc(col)
            sub.append(row[index_no])
        list.append(sub)

    return list


overalldata = read_csv('skyscrappers.csv')
#print(overalldata)

def countries(data):
    countries_list = []
    for i in range(len(data)):
        if data[i][5] not in countries_list:
            countries_list.append(data[i][5])
    return countries_list

allcountries = countries(overalldata)
#print(allcountries)

def freq_data(data, value, count_item = 'Country'):
    freq = 0
    index = columns.index(count_item)
    for i in range(len(data)):
        if data[i][index] == value:
            freq += 1
    return freq

#frequency = freq_data(overalldata, 'Country', ' China' )
#print(frequency)

def skyscrappers_list(data):
    skyscrappers = []

    for i in range(len(data)):
        if data[i][0] not in skyscrappers:
            skyscrappers.append(data[i][0])

    return skyscrappers

skyscrapperslist = skyscrappers_list(read_csv('skyscrappers.csv'))
#print(skyscrapperslist)

def height_data(data, skyscrappers):
    height_dict = {}
    #print(data)
    #print(skyscrappers)
    #print(len(data))

    for i in range(len(data)):
        building = skyscrappers[i]
        height_in_meter = data[i][1]
        #print(building)
        #print(height_in_meter)
        height_dict.update({building: height_in_meter})
    #print(height_dict)

    return height_dict

heightdatadict = height_data(overalldata, skyscrapperslist)
#print(heightdatalist)

def append_data(data, count_item, value, append_item):
    count_index = columns.index(count_item)
    append_index = columns.index(append_item)
    list = []
    for i in range(len(data)):
        if data[i][count_index] == value:
            list.append(data[i][append_index])
    #print(list)
    return list

def bar_chart(height_dict):
    building_name = height_dict.keys()
    building_height = height_dict.values()

    width = 0.3
    plt.bar(building_name, building_height, width=width)
    plt.xticks(rotation=20)
    plt.xlabel('Skyscrapper')
    plt.ylabel('Height (m)')
    plt.title("Skyscrapper Heights Comparison")

    plt.show()
    return plt

#bar_chart(heightdatadict)

def show_map(data, skyscrappers, rankings_included):
    locations = []
    for i in range(rankings_included):
        building = skyscrappers[i]
        #print(building)
        lati = data[i][7]
        #print(latitude)
        longi = data[i][8]
        #print(longitude)
        locations.append([building, lati, longi])
    #print(locations)

    map_df = pd.DataFrame(locations, columns=['Skyscrapper','lat','lon'])
    st.write(map_df)
    st.map(map_df)

#show_map(overalldata, skyscrapperslist)

def main():
    data_frame = csv_to_df('skyscrappers.csv')
    overalldata = read_csv('skyscrappers.csv')
    skyscrapperslist = skyscrappers_list(overalldata)
    allcountries = countries(overalldata)
    heightdatadict = height_data(overalldata, skyscrapperslist)
    bar_skyscrapper_dict = {}

    page = st.sidebar.selectbox("Choose a page: ", ['Homepage', 'Country', 'Comps', 'US Skyscrappers'])

    if page == 'Homepage':
        st.title('Skyscrappers around the world')
        st.write('Welcome!')

        ##Interactive Map that shows all skyscrappers in the data,
        ##allows user to choose how many skyscrappers to show on the map
        st.header('Skyscrapper Locations')
        st.write('Slide to see more skyscrappers:')
        top_count = st.slider("Rankings included:", 1, len(overalldata), 5, 1)
        st.write(f'Scatter World Map of Top {top_count} Skyscrappers:')
        show_map(overalldata, skyscrapperslist, top_count)

    elif page == 'Country':
        ##Generates quick profile about the country
        ##Includes image of country flag
        ##Tells users how many skyscrappers are in this country and average height
        st.header("Country Skyscrapper Profile")
        country = st.radio("Please select a country from the list:", allcountries)
        frequency = freq_data(overalldata, country)
        height_List = append_data(overalldata, 'Country', country, 'Metres')
        avg_height = npy.mean(height_List)
        st.text("="*15 + f"{country}" + "="*15)
        st.image(str(country[1:]) + '.jpg', width=300) ##images should be stored within same folder as main python file
        st.write(f'{country} has {frequency} skyscrapper(s) in the list! Wow!')
        st.write(f"{country}'s skyscrappers has an average height of {avg_height:.2f}m in its skyscrappers.")

    elif page == 'Comps':
        ##Compares heights of skyscrappers
        st.header('Skyscrapper Comparisons')
        comps = st.multiselect("Select Skyscrappers you want to compare: ", skyscrapperslist, default=['Burj Khalifa', 'Tokyo Skytree'])
        st.write("Bar Chart of Heights (m): \n"," and ".join([comp.upper() for comp in comps]))
        for comp in comps:
            if comp in heightdatadict.keys():
                bar_skyscrapper_dict.update({comp: heightdatadict[comp]})
        #print(bar_skyscrapper_dict)
        st.pyplot(bar_chart(bar_skyscrapper_dict))

        #freq_data function which uses non-default value
        chimney = freq_data(overalldata, "Chimney", "Type")
        st.write(f'Out of all the tall buildings, {chimney} are Chimneys.')

    else:
        ##Other interesting facts
        ##Uses remaining panda features to fulfill requirements
        st.header('US Skyscrapers')

        us_skyscrappers_df = data_frame[data_frame['Country'] ==' United States'] #Filters US Skyscrappers

        #delete irrelevant columns
        del us_skyscrappers_df['Country']
        del us_skyscrappers_df['Feet']
        del us_skyscrappers_df['Type']
        del us_skyscrappers_df['Remarks']
        del us_skyscrappers_df['Lat']
        del us_skyscrappers_df['Lon']
        del us_skyscrappers_df['Main use']

        #Reorgainize rows so that Year comes first
        us_skyscrappers_df = us_skyscrappers_df[['Year', 'Name', 'Metres', 'City']]

        #Sorts the data frame by oldest buildings to newest
        us_skyscrappers_df = us_skyscrappers_df.sort_values('Year', axis=0, ascending=True)

        st.write(us_skyscrappers_df)

main()
