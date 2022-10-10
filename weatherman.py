from ast import arg
from cmath import e
import csv
import os
import sys
import pdb
import datetime
from termcolor import colored

class Weather:
 
    def function():

        option = sys.argv[1]
        year = sys.argv[2]
        path = sys.argv[3]
        try:
            list_of_files = os.listdir(path)
        except:
            print("Wrong Path.")
            exit()
        
        if option not in '-e' '-a' '-c':
            print("Wrong input.")

        if option == "-e":

            # print("Option = ",option)
            Weather.option_e(year,path,list_of_files)

        if option == "-a":
            # print("Option = ",option)
            Weather.option_a(year,path,list_of_files)
          
        if option == "-c":
            # print("Option = ",option)
            Weather.option_c(year,path,list_of_files)
            
                
    def convert_date(date):

        format = "%Y-%m-%d"
        x = datetime.datetime.strptime(date,format)
        new_date = x.strftime("%B %d")
        return new_date
   
    def option_e(year,path,list_of_files):

        maximum_temperature_date= 0
        minimum_temperature_date= "Jan 1"
        most_humidity_date= 0
        maximum_temperature = 0
        minimum_temperature = 0
        most_humidity = 0
        for files in list_of_files:

                if year in files:
                    
                    with open(f"{path}/{files}", "r") as weather:
                        next(weather)
                        content = weather.readlines()[1:]
                        
                        for lines in content:
                            
                            line = lines.split(",")
                            
                            if ('!' not in line[0] and line[1] and line[1]!='\n' and int(float(line[1])) > int(maximum_temperature)):
                                maximum_temperature = line[1]
                                maximum_temperature_date = Weather.convert_date(line[0])

                            if ('!' not in line[0] and line[3] and line[3]!='\n' and int(float(line[3])) < int(minimum_temperature)):
                                minimum_temperature = line[3]
                                minminimum_temperature_date = Weather.convert_date(line[0])

                            if ('!' not in line[0] and line[7] and line[7]!='\n' and int(float(line[7])) > int(most_humidity)):
                                most_humidity = line[7]
                                most_humidity_date = Weather.convert_date(line[0])

        if ( maximum_temperature==0 and minimum_temperature==0 and most_humidity==0):
            print("No Data for this year.")
                            
        else:    
            print("----------------------------------")
            print(f"Highest: {maximum_temperature}C on {maximum_temperature_date}")
            print(f"Lowest: {minimum_temperature}C on {minimum_temperature_date}")
            print(f"Humid: {most_humidity}% on {most_humidity_date}")
            print("----------------------------------")  

        
    
    def option_a(year,path,list_of_files):
            total_highest_temperature = 0 
            total_lowest_temperature = 0
            total_humidity = 0
            input_year= year.split("/")
            year= input_year[0]
            input_month = input_year[1]

            convert_month = datetime.datetime.strptime(input_month,"%m")
            month = convert_month.strftime("%b")

            no_of_files = [file for file in list_of_files if year in file]
            if no_of_files == [] :
                print("No Data for this Year.")

            no_of_file = [file for file in no_of_files if month in file]
            if no_of_file == [] :
                print("No Data for this Month.")

            for file in list_of_files:

                if year in file:
                    if month in file:
                    
                        with open(f"{path}/{file}", "r") as weather:
                            next(weather)
                            content = weather.readlines()[1:]

                            for lines in content:
                
                                line = lines.split(",")
                                if ('!' not in line[0] and line[1] and line[1]!='\n'):
                                    total_highest_temperature += int(line[1])
                                    
                                if ('!' not in line[0] and line[3] and line[3]!='\n'):
                                    total_lowest_temperature += int(line[3])
                                    
                                if ('!' not in line[0] and line[8] and line[8]!='\n'):
                                    total_humidity += int(line[8])

                            number_of_days= len(content)-1
                            highest_average = total_highest_temperature / number_of_days  
                            lowest_average = total_lowest_temperature / number_of_days   
                            humidity_average = int( total_humidity / number_of_days ) % 100   

                            print("----------------------------")
                            print(f"Highest Temperature Average: {int(highest_average)}C")
                            print(f"Lowest Temperature Average: {int(lowest_average)}C")
                            print(f"Humidity Average: {int(humidity_average)}%")
                            print("----------------------------")
            


    def option_c(year,path,list_of_files):
    
        input_year= year.split("/")
        year= input_year[0]
        input_month = input_year[1]
        convert_month = datetime.datetime.strptime(input_month,"%m")
        month = convert_month.strftime("%b")

        print(f"\n{month} {year}\n")   

        no_of_files = [file for file in list_of_files if year in file]
        if no_of_files == [] :
            print("No Data for this Year.")

        no_of_file = [file for file in no_of_files if month in file]
        if no_of_file == [] :
            print("No Data for this month.")    

        for file in list_of_files:

            if year in file:
                if month in file:

                    with open(f"{path}/{file}", "r") as weather:
                        next(weather)
                        content = weather.readlines()
                        
                        for lines in content:
                    
                            line = lines.split(",")                            

                            if ('!' not in line[0] and lines[1] and line[1]!='\n' and line[0] != "PKT" and line[0]!= "PKST"):
                                maximum_temperature = line[1]
                                date = line[0]
                                format_date= datetime.datetime.strptime(date ,"%Y-%m-%d")
                                new_date = format_date.strftime("%d")
                                plus_red = (colored("+"*int(maximum_temperature), "red"))
                                print(f"{new_date} {plus_red} {line[1]}C ")


                            if('!' not in line[0] and line[3] and line[3]!='\n' and line[0]!="PKT" and line[0]!="PKST"):
                                minimum_temperature = line[3]
                                date = line[0]
                                format_date = datetime.datetime.strptime(date , "%Y-%m-%d")
                                new_date = format_date.strftime("%d")
                                plus_blue = (colored("+"*int(minimum_temperature), "blue"))
                                print(f"{new_date} {plus_blue} {line[3]}C ")


Weather.function()

