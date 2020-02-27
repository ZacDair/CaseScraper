import urllib3
import casePriceChecker as cpc


# Generalized function to get specific data in between the preIndex and postIndex
# preIndex is a unique string before the data you want
# postIndex is a unique string directly after the data you want
def getDataFromContents(sourceCode, preIndex, postIndex):
    data = str(sourceCode).split(preIndex)
    res = []
    length = len(data)
    i = 1
    while i < length:
        temp = data[i].split(postIndex)
        res.append(temp[0])
        i = i + 1
    return res


# Cycle through each page (doesn't work, only gives us first page of results)
pageIndex = 1
while pageIndex <= 1:
    # Read in the contents of the URL
    # Get a list of every CS:GO case (name and url)
    url = "https://steamcommunity.com/market/search?q=case&category_730_ItemSet%5B%5D=any&category_730_" \
        "ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730" \
        "_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730#p"+str(pageIndex)+"_name_asc"
    http = urllib3.PoolManager()
    request = http.request('GET', url)
    contents = request.data
    urls = getDataFromContents(contents, '<a class="market_listing_row_link" href=', 'id="resultlink')
    print("We found these urls...")
    for item in urls:
        item = item.replace('"', "")
        cpc.getItemPrices(item)
    pageIndex = pageIndex + 1



