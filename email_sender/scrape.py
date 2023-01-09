# import the required libraries
import requests
from requests_html import HTML
 
# a function to remove redundant qotation from string
def adjust(str_val):
    if '[' in str_val:
        x = str_val.index('[')
        return str_val[:x]
    return str_val

# a function to parse the values
def parse_and_extract(url):
    # load the page
    r = requests.get(url)
    
    if r.status_code in range(200, 299):
        r_text = r.text
        # store it as HTML to use selection function find()
        r_html = HTML(html = r_text)
        table_class = ".wikitable"
        r_table = r_html.find(table_class)
        
        # if at least a table exists
        if len(r_table) >= 1:
            table_data = []
            header_name = []
            parsed_table = r_table[0]
            
            rows = parsed_table.find('tr')
            header_row = rows[0]
            header_cols = header_row.find('th')
            # we only want 'number', 'video name' and 'view in billions', which correspond to 0, 1 and 3
            necessary_cols = [0,1,3]
            for i in necessary_cols:
                header_name.append(header_cols[i].text)
            table_data.append(header_name)
            
            # for other rows
            for i in range(1, 11):
                cols = rows[i].find('td')
                row_data = []
                for i in necessary_cols:
                    row_data.append(adjust(cols[i].text))
                
                #append the row data to the final table data
                table_data.append(row_data)
            return table_data
    
# a function to make table data into string
def makeString(table):
    strVal = ''
    for i in range(len(table)):
        for j in range(len(table[i])):
            strVal = strVal+ f'{table[i][j]}| '
        strVal+='\n'
    return strVal

    

                
