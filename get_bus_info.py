import json
import sys
import urllib2
import csv

if __name__=='__main__':
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' %(sys.argv[1],sys.argv[2])
# key = 7e09165b-603b-4801-a1cc-8b273f0b6c5a, bus_number = B52   
    request = urllib2.urlopen(url)
    metadata = json.load(request)
    
    num = metadata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    
    with open(sys.argv[3], 'wb') as csvFile:
        csv = csv.writer(csvFile)
        headers = ['Latitude','Longitude','Stop Name','Stop Status']
        csv.writerow(headers)
        
        
        for i in num:
            lat = i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
            lon = i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        
            if i["MonitoredVehicleJourney"]["OnwardCalls"] == {}:
                sn = "N/A"
                ss = "N/A"
        
        else:
            sn = i['MonitoredVehicleJourney']["MonitoredCall"]['StopPointName']
            ss = i['MonitoredVehicleJourney']["MonitoredCall"]["Extensions"]["Distances"]["PresentableDistance"]

        row = [lat,lon,sn,ss]
        csv.writerow(row)