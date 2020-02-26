# CaseScraper
  
Currently uses URLlib3 in python to access the Steam marketplace  
Searches for CS:GO items, specifically containers, with cases in the name  
Removes extra HTML source code and leaves us with a list of urls to be analysed further
  
## Project Structure:  
1) Python Scripts - backend data gathering and manipulation  
2) SQL Database - data storage solution  
3) Standard Webpage - result visualization  
These three sections can be filtered even further  
  
### Python Scrips:  
1) One time data gathering scripts - (ran once on launch, and when a new case is added)  
2) Daily data gathering scripts - (ran once per day, mainly price checks)  
3) Python - Database connection - (ran when required, consider it a sub script)  

### SQL Database:  
Standard database storing our results - to be analysed what needs to be stored  
URLs and Item names will need to be stored  
Price and a timestamp will need to be stored  
Extra data may need to be stored (admin logins, etc...)  

### Webpage:  
Webpage built to display our results, by default can be quite basic, but it may be nice to have images for each item.  
Webpage will connect to the database to display the data.  
Admin section may be required to add new cases or this may be automated.  


