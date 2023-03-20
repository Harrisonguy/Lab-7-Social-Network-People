"""
Description:
 Prints the name and age of all people in the Social Network database
 who are age 50 or older, and saves the information to a CSV file.

Usage:
 python old_people.py
"""
import os
import inspect 
import sqlite3
import pandas as pd
from pprint import pprint

def main():
    global db_path
    script_dir = get_script_dir()
    db_path = os.path.join(script_dir, 'social_network.db')

    # Get the names and ages of all old people
    old_people_list = get_old_people()

    # Print the names and ages of all old people
    print_name_and_age(old_people_list)

    # Save the names and ages of all old people to a CSV file
    old_people_csv = os.path.join(script_dir, 'old_people.csv')
    save_name_and_age_to_csv(old_people_list, old_people_csv)

def get_old_people():
    """Queries the Social Network database for all people who are at least 50 years old.

    Returns:
        list: (name, age) of old people 
    """
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    get_old_people_query = """
        SELECT name, age FROM people
        WHERE age > 49;
    """
    cur.execute(get_old_people_query)
    query_result = cur.fetchall()
    con.close()

    return query_result

def print_name_and_age(old_people_list):
    """Prints name and age of all people in provided list

    Args:
        name_and_age_list (list): (name, age) of people
    """
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    # Query the database for all information for all people.
    cur.execute('SELECT name, age FROM people')
    # Fetch all query results.
    # The fetchall() method returns a list, where each list item
    # is a tuple containing data from one row in the people table.
    all_people = cur.fetchall()
    # Pretty print (pprint) outputs data in an easier to read format.
    pprint(all_people)
    con.commit()
    con.close()
    return

def save_name_and_age_to_csv(old_people_list, old_people_csv):
    """Saves name and age of all people in provided list

    Args:
        name_and_age_list (list): (name, age) of people
        csv_path (str): Path of CSV file
    """
    report_df = pd.DataFrame(old_people_list)
    report_header = ('name', 'age')
    report_df.to_csv(old_people_csv, index=False, header=report_header)
    return

def get_script_dir():
    """Determines the path of the directory in which this script resides

    Returns:
        str: Full path of the directory in which this script resides
    """
    script_path = os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)
    return os.path.dirname(script_path)

if __name__ == '__main__':
   main()