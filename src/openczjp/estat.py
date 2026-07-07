"""
The estat module provides funtionality for querying `e-Stat portal (English)`_ and `e-Stat portal (Japanese)`_.

.. _e-Stat portal (English): https://www.e-stat.go.jp/en/
.. _e-Stat portal (Japanese): https://www.e-stat.go.jp

"""
import estatjp as e
from typing import Final

JP_POP_CENSUS_YEARS: Final = [1980,1985,1990,1995,2000,2005,2010,2015,2020]
"""
e-Stat's `System of Social and Demographic Statistics (SSDS)`_ provides annual data for prefectures and municipalities. Population censuses are carried out every 5 years. `JP_POP_CENSUS_YEARS` specifies the available census years and can be used for sampling only the census years from SSDS.

See, for example:

* `Municipal codes in English`_ (Note: When this link is first clicked, e-Stat may respond with a "page not found" message. Reloading the page brings up the database page.)
* `Municipal codes in Japanese`_

.. _System of Social and Demographic Statistics (SSDS): https://www.e-stat.go.jp/en/stat-search/database?page=1&toukei=00200502
.. _Municipal codes in English: https://www.e-stat.go.jp/en/dbview?sid=0000020101
.. _Municipal codes in Japanese: https://www.e-stat.go.jp/dbview?sid=0000020101

"""

API_URLS: Final = dict(
Population_en = "http://api.e-stat.go.jp/rest/3.0/app/getSimpleStatsData?cdCat01=A1101&appId=&lang=E&statsDataId=0000020101&metaGetFlg=Y&cntGetFlg=N&explanationGetFlg=Y&annotationGetFlg=Y&sectionHeaderFlg=1&replaceSpChars=0",
Population_ja = "http://api.e-stat.go.jp/rest/3.0/app/getSimpleStatsData?cdCat01=A1101&appId=&lang=J&statsDataId=0000020101&metaGetFlg=Y&cntGetFlg=N&explanationGetFlg=Y&annotationGetFlg=Y&sectionHeaderFlg=1&replaceSpChars=0"
)
"""
`API_URLS` are canned urls for API calls to e-Stat that are used in this module. They are coded with `typing.Final`_ to prevent redefinition. These particular calls download a table of total populations simply because the API cannot download the index column by itself.

.. _typing.Final: https://docs.python.org/3/library/typing.html#typing.Final

Canned urls
-----------
Population_en
    Population table with municipal names in English
Population_ja
    Population table with municipal names in Japanese

API_URLS : Final = dict(

Population_en = `"http://api.e-stat.go.jp/rest/3.0/app/getSimpleStatsData?cdCat01=A1101
&appId=&lang=E&statsDataId=0000020101
&metaGetFlg=Y&cntGetFlg=N&explanationGetFlg=Y
&annotationGetFlg=Y&sectionHeaderFlg=1&replaceSpChars=0"`,

Population_ja = `"http://api.e-stat.go.jp/rest/3.0/app/getSimpleStatsData?cdCat01=A1101
&appId=&lang=J&statsDataId=0000020101
&metaGetFlg=Y&cntGetFlg=N&explanationGetFlg=Y
&annotationGetFlg=Y&sectionHeaderFlg=1&replaceSpChars=0"`

)

"""

def municipal_code_download_csv(file = "../data/municipal-codes.csv"):
    """Download Japanese and English municipal names and codes from [System of Social and Demographic Statistics A Population and Households](https://www.e-stat.go.jp/en/dbview?sid=0000020101) and construct a Japanese-English code dataframe stored in csv format.

    The source dataset is updated every five years after each population census. As displayed at the e-Stat website, the table appears to contain annual survey data thereby requiring a filter to retrieve only census years. In the contrary, it contains data only for census years; omitting the year filter still retrieves data from only census years.


    """
    import datetime
    from estatjp import api
    from estatjp import exceptions as xs
    import pandas as pd

    # get urls
    url_en = API_URLS.get('Population_en')
    url_ja = API_URLS.get('Population_ja')

    columns = ['census_year','muni_code','muni_name_en','muni_name_ja','population']
    
    # Get the codes with municipal names in English.
    try:
        dfs_en = api.get_csv_data(url_en,description=datetime.datetime.now())
    except Exception as e:
        print(type(e))
        print(e.args)
        print(e.with_traceback)

    # Get the codes with municipal names in Japanese.
    try:
        dfs_ja = api.get_csv_data(url_ja,description=datetime.datetime.now())
    except Exception as e:
        print(type(e))
        print(e.args)
        print(e.with_traceback)

    # Merge the results
    main_en = dfs_en.get('Main')
    main_en = main_en[["SURVEY YEAR","time_code","area_code","AREA","value"]]
    main_ja = dfs_ja.get('Main')
    main_ja = main_ja[["調査年","time_code","area_code","地域","value"]]
    maindf = pd.merge(main_en,main_ja, on=["time_code","area_code","value"] )
    df_result = maindf[["SURVEY YEAR","area_code","AREA","地域","value"]]
    df_result.columns = columns

    df_result.to_csv(file, index=False)

    return df_result