import mysql.connector
import datetime

def Data_updation(Details):
    if len(Details)!=2:
        return "Invalid Code"
    Datetime = datetime.datetime.now()
    date_str = Datetime.strftime("%Y-%m-%d")
    date= datetime.datetime.strptime(date_str,"%Y-%m-%d").date()

    name,rollno=Details
    
    try: 
        #Estabilishing Connection
        mydb = mysql.connector.connect(
        host="localhost",
        user="Sql_user_name",
        password="Sql_password",
        database="Database_Name"
        )
        
        #Getting the datas from the Database

        query1="select * from details where name=%s and rollNo=%s;"

        cursor= mydb.cursor()
        cursor.execute(query1,(name,rollno))
        datas=cursor.fetchall()

        #Checking the data and returning the result
        if datas and len(datas)==1 :
            data=datas[0]

            if  data[3]!=date:

                print("Enter the Password:")
                password=input().strip()

                if password==data[-1]:
                    total_days= data[2]+1
                    new_date=date

                    query2="update details set Days_present=%s,date=%s where name=%s and rollNo=%s;"
                    
                    cursor.execute(query2,(total_days,new_date,name,rollno))

                    mydb.commit()
                    mydb.close()
                    return "Updated successfully"
                
                else:
                    mydb.close()
                    return "incorrect password"

            else:
                mydb.close()
                return "Updated Already"

        else:
            mydb.close()
            return "Invalid Details" 
            
    except mysql.connector.errors as err:
        mydb.close()
        print (f"Database Error: {err}")
        return "Error"

    except Exception as e:
        mydb.close()
        print (F"Error Occured:{e}")
        return "Error"

    
