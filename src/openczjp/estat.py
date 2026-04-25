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
API_URLS: Final = {
"Population_en":"http://api.e-stat.go.jp/rest/3.0/app/getSimpleStatsData?cdCat01=A1101&cdTime={YEAR}100000&appId=&lang=E&statsDataId=0000020101&metaGetFlg=Y&cntGetFlg=N&explanationGetFlg=Y&annotationGetFlg=Y&sectionHeaderFlg=1&replaceSpChars=0",
"Population_ja":"http://api.e-stat.go.jp/rest/3.0/app/getSimpleStatsData?cdCat01=A1101&cdTime={YEAR}100000&appId=&lang=J&statsDataId=0000020101&metaGetFlg=Y&cntGetFlg=N&explanationGetFlg=Y&annotationGetFlg=Y&sectionHeaderFlg=1&replaceSpChars=0"
}
"""
`API_URLS` are canned urls for API calls to e-Stat that are used in this module. They are coded with `typing.Final`_ to prevent redefinition. 

.. _typing.Final: https://docs.python.org/3/library/typing.html#typing.Final

"""

