from influxdb import InfluxDBClient
import time
import importlib
import textfsm_influxdb
cpu,mem=0,0

client = InfluxDBClient(host="localhost", port=8086)
print("List of databases : \n",client.get_list_database())
client.create_database("system_health_params")
print("\nNew list of databases : \n",client.get_list_database())

client.switch_database("system_health_params")                          
print("\nList of measurements/tables : \n",client.get_list_measurements())

while(True):
    importlib.reload(textfsm_influxdb)
    cpu = textfsm_influxdb.current_cpu
    mem = textfsm_influxdb.current_memory
    json_body = [
        {
            "measurement": "system_health_params",
            "fields": {
                "cpu": cpu,
                "memory": mem
            }
        }
    ]
    client.write_points(json_body)
    # res = client.query('select * from system_health_params')
    # print("\nQuery result :\n", res)
    time.sleep(1)