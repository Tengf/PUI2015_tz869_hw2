import json
import sys
import urllib2

if __name__=='__main__':
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' %(sys.argv[1],sys.argv[2])
# key = 7e09165b-603b-4801-a1cc-8b273f0b6c5a, bus_number = B52   
    request = urllib2.urlopen(url)
    metadata = json.load(request)
    meta = metadata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    num = len( meta)
    
    print "Bue Line: %s" %(sys.argv[2])
    print "Number of Active Buses: %d" %(num)
    
    for i in range(num):
        lat  = meta[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        lon = meta[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        print "Bus %d is at latitude: %f and longitude at %f."   %(i+1,lat,lon)