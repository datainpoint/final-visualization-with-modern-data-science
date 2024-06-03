# final-visualization-with-modern-data-science
Final: Visualization with Modern Data Science.

## 01. Define a function `import_time_series_confirmed_deaths()` which imports `time_series_covid19_confirmed_global.csv` and `time_series_covid19_deaths_global.csv` in working directory.

```python
def import_time_series_confirmed_deaths() -> tuple:
    """
    >>> time_series_confirmed, time_series_deaths = import_time_series_confirmed_deaths()
    >>> type(time_series_confirmed)
    pandas.core.frame.DataFrame
    >>> type(time_series_deaths)
    pandas.core.frame.DataFrame
    >>> time_series_confirmed.shape
    (289, 1147)
    >>> time_series_deaths.shape
    (289, 1147)
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 02. Define a function `transform_time_series_confirmed_deaths()` which transforms both `time_series_covid19_confirmed_global.csv` and `time_series_covid19_deaths_global.csv` from wide format into long format.

```
       Province/State        Country/Region        Lat        Long     Date  \
0                 NaN           Afghanistan  33.939110   67.709953  1/22/20   
1                 NaN               Albania  41.153300   20.168300  1/22/20   
2                 NaN               Algeria  28.033900    1.659600  1/22/20   
3                 NaN               Andorra  42.506300    1.521800  1/22/20   
4                 NaN                Angola -11.202700   17.873900  1/22/20   
...               ...                   ...        ...         ...      ...   
330322            NaN    West Bank and Gaza  31.952200   35.233200   3/9/23   
330323            NaN  Winter Olympics 2022  39.904200  116.407400   3/9/23   
330324            NaN                 Yemen  15.552727   48.516388   3/9/23   
330325            NaN                Zambia -13.133897   27.849332   3/9/23   
330326            NaN              Zimbabwe -19.015438   29.154857   3/9/23   

        Confirmed  
0               0  
1               0  
2               0  
3               0  
4               0  
...           ...  
330322     703228  
330323        535  
330324      11945  
330325     343135  
330326     264276  

[330327 rows x 6 columns]
```

```
       Province/State        Country/Region        Lat        Long     Date  \
0                 NaN           Afghanistan  33.939110   67.709953  1/22/20   
1                 NaN               Albania  41.153300   20.168300  1/22/20   
2                 NaN               Algeria  28.033900    1.659600  1/22/20   
3                 NaN               Andorra  42.506300    1.521800  1/22/20   
4                 NaN                Angola -11.202700   17.873900  1/22/20   
...               ...                   ...        ...         ...      ...   
330322            NaN    West Bank and Gaza  31.952200   35.233200   3/9/23   
330323            NaN  Winter Olympics 2022  39.904200  116.407400   3/9/23   
330324            NaN                 Yemen  15.552727   48.516388   3/9/23   
330325            NaN                Zambia -13.133897   27.849332   3/9/23   
330326            NaN              Zimbabwe -19.015438   29.154857   3/9/23   

        Deaths  
0            0  
1            0  
2            0  
3            0  
4            0  
...        ...  
330322    5708  
330323       0  
330324    2159  
330325    4057  
330326    5671  

[330327 rows x 6 columns]
```


```python
def transform_time_series_confirmed_deaths() -> tuple:
    """
    >>> time_series_confirmed_long, time_series_deaths_long = transform_time_series_confirmed_deaths()
    >>> type(time_series_confirmed_long)
    pandas.core.frame.DataFrame
    >>> type(time_series_deaths_long)
    pandas.core.frame.DataFrame
    >>> time_series_confirmed_long.shape
    (330327, 6)
    >>> time_series_deaths_long.shape
    (330327, 6)
    """
    ### BEGIN SOLUTION
    time_series_confirmed, time_series_deaths = import_time_series_confirmed_deaths()
    idVars = ["Province/State", "Country/Region" , "Lat", "Long"]
    time_series_confirmed_long = pd.melt(time_series_confirmed, id_vars=idVars, var_name="Date", value_name="Confirmed")
    time_series_deaths_long = pd.melt(time_series_deaths, id_vars=idVars, var_name="Date", value_name="Deaths")
    return time_series_confirmed_long, time_series_deaths_long
    ### END SOLUTION
```

## 03. Define a function `merge_time_series()` which merges the long formatted `time_series_covid19_confirmed_global.csv` and `time_series_covid19_deaths_global.csv` into one data frame.

```
           Date Province/State        Country/Region        Lat        Long  \
0       1/22/20            NaN           Afghanistan  33.939110   67.709953   
1       1/22/20            NaN               Albania  41.153300   20.168300   
2       1/22/20            NaN               Algeria  28.033900    1.659600   
3       1/22/20            NaN               Andorra  42.506300    1.521800   
4       1/22/20            NaN                Angola -11.202700   17.873900   
...         ...            ...                   ...        ...         ...   
330322   3/9/23            NaN    West Bank and Gaza  31.952200   35.233200   
330323   3/9/23            NaN  Winter Olympics 2022  39.904200  116.407400   
330324   3/9/23            NaN                 Yemen  15.552727   48.516388   
330325   3/9/23            NaN                Zambia -13.133897   27.849332   
330326   3/9/23            NaN              Zimbabwe -19.015438   29.154857   

        Confirmed  Deaths  
0               0       0  
1               0       0  
2               0       0  
3               0       0  
4               0       0  
...           ...     ...  
330322     703228    5708  
330323        535       0  
330324      11945    2159  
330325     343135    4057  
330326     264276    5671  

[330327 rows x 7 columns]
```

```python
def merge_time_series() -> pd.core.frame.DataFrame:
    """
    >>> merged_time_series = merge_time_series()
    >>> type(merged_time_series)
    pandas.core.frame.DataFrame
    >>> merged_time_series.shape
    (330327, 7)
    """
    ### BEGIN SOLUTION

    ### END SOLUTION
```

## 04. Define a function `groupby_date_country()` which summarizes `Confirmed` and `Death` by `Date` and `Country/Region` given merged, long formatted time_series dataframe.

```
          Date        Country/Region  Confirmed  Deaths
0       1/1/21           Afghanistan      52513    2201
1       1/1/21               Albania      58316    1181
2       1/1/21               Algeria      99897    2762
3       1/1/21               Andorra       8117      84
4       1/1/21                Angola      17568     405
...        ...                   ...        ...     ...
229738  9/9/22    West Bank and Gaza     702591    5706
229739  9/9/22  Winter Olympics 2022        535       0
229740  9/9/22                 Yemen      11932    2155
229741  9/9/22                Zambia     333204    4017
229742  9/9/22              Zimbabwe     256859    5596

[229743 rows x 4 columns]
```

```python
def groupby_date_country() -> pd.core.frame.DataFrame:
    """
    >>> groupby_time_series = groupby_date_country()
    >>> type(groupby_time_series)
    pandas.core.frame.DataFrame
    >>> groupby_time_series.shape
    (229743, 4)
    """
    ### BEGIN SOLUTION

    ### END SOLUTION
```

## 05. Define a function `format_date_column()` which formats `Date` column with ISO-8601 format `yyyy-mm-dd`(`%Y-%m-%d`) given summarized time_series dataframe.

```
             Date        Country/Region  Confirmed  Deaths
0      2020-01-22           Afghanistan          0       0
1      2020-01-22               Albania          0       0
2      2020-01-22               Algeria          0       0
3      2020-01-22               Andorra          0       0
4      2020-01-22                Angola          0       0
...           ...                   ...        ...     ...
229738 2023-03-09    West Bank and Gaza     703228    5708
229739 2023-03-09  Winter Olympics 2022        535       0
229740 2023-03-09                 Yemen      11945    2159
229741 2023-03-09                Zambia     343135    4057
229742 2023-03-09              Zimbabwe     264276    5671

[229743 rows x 4 columns]
```

```python
def format_date_column() -> pd.core.frame.DataFrame:
    """
    >>> formatted_time_series = format_date_column()
    >>> type(formatted_time_series)
    pandas.core.frame.DataFrame
    >>> formatted_time_series.shape
    (229743, 4)
    """
    ### BEGIN SOLUTION

    ### END SOLUTION
```

## 06. Define a function `snapshot_last_day()` which retrieved the cummulative confirmed and deaths by country as of 2023-03-09 given the formatted time_series dataframe.

```
             Date        Country/Region  Confirmed  Deaths
229542 2023-03-09           Afghanistan     209451    7896
229543 2023-03-09               Albania     334457    3598
229544 2023-03-09               Algeria     271496    6881
229545 2023-03-09               Andorra      47890     165
229546 2023-03-09                Angola     105288    1933
...           ...                   ...        ...     ...
229738 2023-03-09    West Bank and Gaza     703228    5708
229739 2023-03-09  Winter Olympics 2022        535       0
229740 2023-03-09                 Yemen      11945    2159
229741 2023-03-09                Zambia     343135    4057
229742 2023-03-09              Zimbabwe     264276    5671

[201 rows x 4 columns]
```

```python
def snapshot_last_day() -> pd.core.frame.DataFrame:
    """
    >>> last_day = snapshot_last_day()
    >>> type(last_day)
    pandas.core.frame.DataFrame
    >>> last_day.shape
    (201, 4)
    """
    ### BEGIN SOLUTION

    ### END SOLUTION
```

## 07. Define a function `summarize_table_shapes()` which summarizes the shapes of table in `taiwan_election_2024.db` in working directory as a dataframe. Given table names as following: `["aboriginal_legislators", "candidates", "districts", "election_types", "parties", "party_legislators", "polling_places", "presidents", "regional_legislators", "villages"]`

```
                    table    rows  columns
0  aboriginal_legislators  338105        7
1              candidates     331        4
2               districts   17795        5
3          election_types       5        2
4                 parties      35        2
5       party_legislators  284720        7
6          polling_places   88975        8
7              presidents   53385        7
8    regional_legislators   77032        8
9                villages    5227        2
```

```python
def summarize_table_shapes() -> pd.core.frame.DataFrame:
    """
    >>> table_shapes = summarize_table_shapes()
    >>> type(table_shapes)
    pandas.core.frame.DataFrame
    >>> table_shapes.shape
    (10, 3)
    """
    ### BEGIN SOLUTION

    ### END SOLUTION
```

## 08. Define a function `summarize_presidential_votes()` which summarizes the votes of president/vice president election.

```
   party candidates    votes
0  民主進步黨    賴清德/蕭美琴  5586019
1  中國國民黨    侯友宜/趙少康  4671021
2  台灣民眾黨    柯文哲/吳欣盈  3690466
```

```python
def summarize_presidential_votes() -> pd.core.frame.DataFrame:
    """
    >>> presidential_votes = summarize_presidential_votes()
    >>> type(presidential_votes)
    pandas.core.frame.DataFrame
    >>> presidential_votes.shape
    (3, 3)
    """
    ### BEGIN SOLUTION

    ### END SOLUTION
```

## 09. Define a function `summarize_regional_aborinal_legislator_votes()` which summarizes the votes of regional and aboriginal legislator election by party.

```
   election_type      party    votes
0       區域及原住民立委      民主進步黨  6095276
1       區域及原住民立委      中國國民黨  5510850
2       區域及原住民立委          無  1069758
3       區域及原住民立委      台灣民眾黨   403357
4       區域及原住民立委       時代力量    96589
5       區域及原住民立委  小民參政歐巴桑聯盟    78138
6       區域及原住民立委      社會民主黨    74375
7       區域及原住民立委    臺灣雙語無法黨    55937
8       區域及原住民立委      司法改革黨    38685
9       區域及原住民立委       台灣維新    33347
10      區域及原住民立委       台灣基進    32583
11      區域及原住民立委      人民最大黨    25216
12      區域及原住民立委       台灣綠黨    15557
13      區域及原住民立委      喜樂島聯盟    15433
14      區域及原住民立委    中華統一促進黨    13203
15      區域及原住民立委      制度救世島    11260
16      區域及原住民立委         新黨     9143
17      區域及原住民立委    台灣麻將最大黨     7839
18      區域及原住民立委      復康聯盟黨     7441
19      區域及原住民立委        勞動黨     6453
20      區域及原住民立委      司法正義黨     6331
21      區域及原住民立委      中華聯合黨     4139
22      區域及原住民立委      台灣國民黨     3293
23      區域及原住民立委      台灣革命黨     3072
24      區域及原住民立委    中華文化共和黨     2583
25      區域及原住民立委     家庭基本收入     2361
26      區域及原住民立委  台灣整復師聯盟工黨     1881
27      區域及原住民立委      中華婦女黨     1029
28      區域及原住民立委      人民民主黨      836
29      區域及原住民立委        經濟黨      472
30      區域及原住民立委    中華愛國同心黨      310
31      區域及原住民立委     合一行動聯盟      174
32      區域及原住民立委      興中同盟會      136
```

```python
def summarize_regional_aborinal_legislator_votes() -> pd.core.frame.DataFrame:
    """
    >>> regional_aborinal_legislator_votes = summarize_regional_aborinal_legislator_votes()
    >>> type(regional_aborinal_legislator_votes)
    pandas.core.frame.DataFrame
    >>> regional_aborinal_legislator_votes.shape
    (33, 3)
    """
    ### BEGIN SOLUTION

    ### END SOLUTION
```

## 10. Define a function `summarize_party_legislator_votes()` which summarizes the votes of party legislator election.

```
   election_type      party    votes
0          不分區立委      民主進步黨  4982062
1          不分區立委      中國國民黨  4764576
2          不分區立委      台灣民眾黨  3040615
3          不分區立委       時代力量   353412
4          不分區立委  小民參政歐巴桑聯盟   128613
5          不分區立委       台灣綠黨   117298
6          不分區立委       台灣基進    95078
7          不分區立委        親民黨    69818
8          不分區立委    臺灣雙語無法黨    44852
9          不分區立委     台灣團結聯盟    43375
10         不分區立委         新黨    40288
11         不分區立委      司法改革黨    37615
12         不分區立委      制度救世島    19665
13         不分區立委    中華統一促進黨    17423
14         不分區立委      人民最大黨    11746
15         不分區立委       台灣維新    10300
```

```python
def summarize_party_legislator_votes() -> pd.core.frame.DataFrame:
    """
    >>> party_legislator_votes = summarize_party_legislator_votes()
    >>> type(party_legislator_votes)
    pandas.core.frame.DataFrame
    >>> party_legislator_votes.shape
    (16, 3)
    """
    ### BEGIN SOLUTION

    ### END SOLUTION
```