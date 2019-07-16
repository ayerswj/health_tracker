##  1/15/2019
##  By: Jackson W. Ayers
##  Program to track weight lifting and gains progress
##  Utilizes SQLite3 as a tracking database for GAINS
##
import time
import sqlite3


def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn


def is_connected(conn):
    if conn:
        print(50*'-')
        print('\t\tConnected to:')
        print(conn)
        print(50*'-')
        print('\n\n\tWelcome to the Health Tracking set up!')
        print(50*'*')
        print(50*'*')
    else:
        print('-------------- You are not connected ---------')


def add_workout(conn):
    cur = conn.cursor()
    localtime = time.asctime( time.localtime(time.time()) )
    print('Enter the date of workout: (in form year-month-day)')
    print(50*'-')
    print(localtime + ' press Y if this is correct (case sensitive)')
    flag = input('Enter -------> ')
    if(flag =='Y'):
        date = localtime
    else:
        print('Well then just input your own time!')
        date = input('Enter -------> ')
    print('Enter the weight at the end: (in pounds)')
    print(50*'-')
    weight = input('Enter -------> ')
    print('Enter total time worked out: (in minutes)')
    print(50*'-')
    time = input('Enter -------> ')
    print('What kind of workout did you do?')
    print(50*'-')
    workout = input('Enter -------> ')
    count = cur.lastrowid
    cur.execute('INSERT INTO routine VALUES (?,?,?,?,?)', (date,weight,time,workout,count))
    conn.commit()
    return count


def clear_workouts(conn):
    cur = conn.cursor()
    print('Enter Y to continue (case sensitive)')
    flag = input('Enter -------> ')
    if (flag == 'Y'):
        command = 'DELETE FROM routine'
        cur.execute(command)
        conn.commit()
    else:
        print('-------------- Clear Table Cancelled ---------')


def display_data(conn):
    cur = conn.cursor()
    # fixed name for table 'routine'
    cur.execute("SELECT * FROM routine")
    # store all the fetched data in the ans variable
    data = cur.fetchall()
    
    # loop to print all the data
    for i in data:
        print(i)
    return None

#def total_time(c)


def create_table(conn, database):
    cur = conn.cursor()
    command = """CREATE TABLE routine (    
        date DATE,  
        weight FlOAT,  
        time INTEGER,  
        workout STRING);"""
    cur.execute(command)
    conn.commit()


def  menu():
    print(50*'-')
    print('\t1. Log a new workout')
    print('\t2. Display past workouts')
    print('\t3. Clear workout table')
    print('\t4. Total time workout out *** unbuilt ***')
    print('\t5. Total weight lost *** unbuilt ***')
    print('\t6. QUIT THE PROGRAM')
    print(50*'-')
    print('\t\tYour choice:')
    print(50*'-')
    choice = int(input('Enter -------> '))
    return choice

def main():
    try:
        # establish what database user wants to connect to
        database = 'getSwole.db'
        # create a database connection
        conn = create_connection(database)
        is_connected(conn)

        choice = menu()
        while not choice == 7:
            print(choice)
            if choice==1:            
                # add a new workout to SQL database
                workout_count = str(add_workout(conn))
                print('******************  You added workout number: *************\n')
                print('                           ' + workout_count)
                print('\n              KEEP GRINDING HARD WORK PAYS OFF\n')
                print(50*'-' + '\n')
                choice = menu()
            elif choice==2:
                # print data from SQL database
                display_data(conn)
                choice = menu()

#            todo: Delete last inputted workout
            elif choice == 3:
                clear_workouts(conn)
                choice = menu()

#           todo: Total time workout out
#            elif choice == 4:
#                total_time_worked(conn)
#                choice = menu()

#            todo: Total weight lost
#            elif choice == 5:
#                total_weight_lost(conn)
#                choice = menu()

            # exit option
            elif choice==6:
                print(50*'*' + '\n')
                print('\t\tExiting program\n')
                print(50*'*' + '\n')

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



  
