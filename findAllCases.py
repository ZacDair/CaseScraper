import urllib.request
urls = []
# Function to get the url of each case
def getUrlsFromContents(pageContents):
    print("Getting Case URLS...")
    data = (str(pageContents).split('<a class="market_listing_row_link" href='))
    max = len(data)
    i = 1
    while i < max:
        temp = data[i].split('id="resultlink')
        urls.append(temp[0])
        print(temp[0])
        i = i + 1
    print(urls)


# Read in the contents of the URL
i = 1
max = 1
list = []
while i <= max:
    # Get a list of every CS:GO case (name and url)
    url = "https://steamcommunity.com/market/search?q=case&category_730_ItemSet%5B%5D=any&category_730_" \
          "ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730" \
          "_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730#p3_name_asc"
    with urllib.request.urlopen(url) as url:
        contents = url.read()
        list.append(contents)
    getUrlsFromContents(contents)
    # Get a list of every CS:GO case (name and url)
    url1 = "https://steamcommunity.com/market/search?q=case&category_730_ItemSet%5B%5D=any&category_730_" \
        "ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730" \
        "_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730#p2_name_asc"
    with urllib.request.urlopen(url1) as url:
        contents = url.read()
        list.append(contents)
    getUrlsFromContents(contents)
    i = i + 1

for value in urls:
    print(value)