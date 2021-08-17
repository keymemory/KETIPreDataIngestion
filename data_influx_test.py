import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import numpy as np
import pandas as pd
from influxdb import InfluxDBClient, DataFrameClient

from KETI_setting import influx_setting_KETI as ins
from data_influx import ingestion_measurement as ing
from data_influx import ingestion_partial_dataset as ipd
       
def test1(db_name, measurement, time_start, time_end):
    
    print("dbname:",db_name, "table:", measurement)
    influx_c = ing.Influx_management(ins.host_, ins.port_, ins.user_, ins.pass_, db_name, ins.protocol)
    result = influx_c.get_df_by_time(time_start,time_end,measurement)
    print(result)


def test2():
    
    client = InfluxDBClient(host = ins.host_, port= ins.port_, username = ins.user_,  verify_ssl=True)
    db_list = client.get_list_database()

    db_list = [list(item.values())[0] for item in db_list]
    return db_list

if __name__ =='__main__':
    
    db_list = test2()
    print(db_list)
    
    
    #from . KETI_setting import influx_setting_KETI as ins
    #dbnames=['INNER_AIR','OUTDOOR_AIR','OUTDOOR_WEATHER']
    #measurement=['KDS1','KDS2','HS1','HS2','sangju']

    start='2020-09-10'
    end='2021-09-25'
    
    db_name= "INNER_AIR"
    measurement = "HS1"
    
    test1(db_name, measurement, start, end) 
    ###
    influx_parameter = ins
    intDataInfo = {"db_info":
                   [{"db_name":"INNER_AIR","measurement":"HS1","domain":"farm","subdomain":"airQuality","start":str(start),"end":str(end)},
                 {"db_name":"OUTDOOR_AIR","measurement":"sangju","domain":"city","subdomain":"airQuality","start":str(start),"end":str(end)},
                 {"db_name":"OUTDOOR_WEATHER","measurement":"sangju","domain":"city","subdomain":"weather","start":str(start),"end":str(end)}]}
    result = ipd.partial_dataSet_ingestion(intDataInfo, influx_parameter)