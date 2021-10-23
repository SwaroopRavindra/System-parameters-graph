import time
import importlib
import textfsm_influxdb
cpu,mem=0,0
for i in range(2):
    print("###")
    importlib.reload(textfsm_influxdb)
    cpu = textfsm_influxdb.current_cpu
    mem = textfsm_influxdb.current_memory
    json_body = [
        {
            "measurement": "system_health_params",
            "tags": {
                "cpu": cpu
            },
            "fields": {
                "memory": mem
            }
        }
    ]
    print(textfsm_influxdb.current_cpu)
    print(textfsm_influxdb.current_memory)
    print(json_body)
    print("Done")
    time.sleep(2)