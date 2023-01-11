############################# TO DO #####################################
##### write import statements #####

try:
    # connection to database

    connection = get_connected()

    # creates cursor
    cursor = connection.cursor()
  
############################# TO DO #####################################
    ############# SQL QUERIES TO EXTRACT INFORMATION #################

    #### create master_query variable

    #### create outdoors_query variable

    #### create garden_query variable

    #### create product_revenue variable

############################# TO DO ####################################
    ############ COPYING SQL QUERY OUTPUTS TO CSV FILES #############

    #### create master_output variable with formatted master_query

    #### create outdoors_output variable with formatted outdoors_query

    #### create garden_output variable with formatted garden_query

    #### create product_revenue_output variable with formatted product_revenue_query

############################# TO DO ####################################
############## CREATING CSV FILES FROM OUTPUTS #########################

    #### create master.csv with open(...) function ####

    #### create outdoors.csv with open(...) function ####

    #### create garden.csv with open(...) function ####

    #### create product_revenue.csv with open(...) function ####

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL DB", error)

finally:
    if (connection):
        cursor.close()
        connection.close()
        print("DB connection is closed.")