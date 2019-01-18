##  1/15/2019
##  By: Jackson W. Ayers
##  Program to track weight lifting and gains progress
##  Utilizes SQL as the tracking database
##

import sqlite3

##     create a database connection to the SQLite database
##     specified by db_file
##    :param db_file: database file
##    :return: Connection object or None
def create_connection(db_file):
        conn = sqlite3.connect(db_file)
        return conn

##     create a new workout into the emp table
##    :param conn: connection to the db file
def add_workout(conn):
    # find total number of workouts and add 1
    cur = conn.cursor()
    # takes user input for workout information
    print('Enter the date of workout: (in form year-month-day)')
    print(50*'-')
    date = input('Enter-------> ')
    print('Enter the weight at the end: (in pounds)')
    print(50*'-')
    weight = input('Enter-------> ')
    print('Enter total time worked out: (in minutes)')
    print(50*'-')
    time = input('Enter-------> ')
    print('What kind of workout did you do?')
    print(50*'-')
    workout = input('Enter-------> ')

    cur.execute('INSERT INTO routine VALUES (?,?,?,?)', (date,weight,time,workout))
    # save changes 
    conn.commit()
    return cur.lastrowid

##      displays all the data in the SQL table
##    :param conn: connection to the db file
##    :param table name 
def display_data(conn):
    cur = conn.cursor()
    # fixed name for table 'routine'
    cur.execute("SELECT * FROM routine")
    # store all the fetched data in the ans variable 
    data = cur.fetchall()
    
    # loop to print all the data 
    for i in data: 
        print(i)
    # end function
    return None

def create_table(conn, database):
    cur = conn.cursor()
    command = """CREATE TABLE routine (    
        date DATE,  
        weight FlOAT,  
        time INTEGER,  
        workout STRING);"""
    cur.execute(command)
    # save changes 
    conn.commit()

def is_connected(conn):
        if conn:
                print(50*'-')
                print('\t\tConnected to:')
                print(conn)
                print(50*'-')
                print('\n\n\tWelcome to the Health Tracking Set up!')
                print(50*'*')
        else:
                print('You are not connected')
def  menu():
    print(50*'-')
    print('\t1. Log a new workout')
    print('\t2. Display past workouts')
    print('\t3. Delete last inputted workout')
    print('\t4. Total time workout out')
    print('\t5. Total weight lost')
    print('\t6. Most frequent workout')
    print('\t7. QUIT THE PROGRAM')
    print(50*'-')
    print('\t\tYour choice:')
    print(50*'-')
    choice = int(input('Enter-------> '))
    return choice

def main():
    try:
        # establish what database user wants to connect to
        database = 'getSwole.db'
        # create a database connection
        conn = create_connection(database)
        is_connected(conn)
        #create_table(conn, database)
        #display_data(conn, database)

        choice = menu()
        while not choice == 7:
            print(choice)
            if choice==1:            
                # add a new workout to SQL database
                workout_id = add_workout(conn)
                print('******************  You added workout number: *************\n')
                print('                           ', + workout_id, '\n')
                print('              KEEP GRINDING HARD WORK PAYS OFF\n')
                print(50*'-' + '\n')
                choice = menu()
            if choice==2:
                # print data from SQL database
                display_data(conn)
                choice = menu()
## In - progress
##            todo: Delete last inputted workout
##            elif choice == 3:
##                
##            todo: Total time workout out   
##            elif choice == 4:
##                
##            todo: Total weight lost
##            elif choice == 5:
##                
##            todo: Most frequent workout
##            elif choice == 6:

            # exit option
            if choice==7:
                print('Exiting program')
                # close the connection 
                conn.close()
                break

            else:
                print(50*'*')
                print('\tNot a valid option try again')
                print(50*'*')
                choice = menu()
            
    except Exception as error:
        print(error)

# execute main
if __name__ == '__main__':
    main()



  

