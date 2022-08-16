# export-tools

This repo contains tools used to transform data exported from Genesis so that it can be effectively loaded into iDiamondCloud. 

There are two datapoints from Genesis that were exported in unruly formats:
## Notepad 
Field in the Customer table with a running list of comments regarding the customer's past orders. It is used when a customer refers to past order specifications. The csv has n rows and m columns, where n is the number of customers and m is the number of filled lines in that customer's note file + 2 (acct. key and company name). The tool mcolumns.py transforms the it into a csv with n rows and 3 columms, concatanating all the Notepad columns into one column separated by '/n'.   
## Screen3 
Field in the Customer table with a running list of references. It is used to document the trustabliity of a customer. The csv has p rows and 3 columns where p is the total numebr of lines in all the Screen3's a.k.a. sum n(lines(i)), where n is the number of customers and lines(i) is the number of lines in customer i's Screen3. The tool prows.py transforms it into a csv with n rows and 3 columns, where n is the number of customers, concatanating each customer's extra Screen3 rows into one column separated by '/n'.   

## Using the script:
1. Clone the folder
2. Move in the data files
3. Rename them to either "mcolumns.csv" or "prows.csv" depending on whether there are too many columns or too many rows. 
4. Run the appropriate script on macOS by running 
  python3 nameofscript.py 
