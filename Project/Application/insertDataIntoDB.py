from model import RegionData
import SOAPpy
data = {'region':"Padilla Bay, WA", 'stations':[
                    {'station':"Bayview Channel", 'code': "pdbbywq", 'lat':"48.496139",'lng':"122.502114"},
                    {'station':"Ploeg Channel", 'code': "pdbbpwq", 'lat':"48.556322",'lng':"122.530894"},
                    {'station':"Joe Leary Estuary", 'code': "pdbjewq", 'lat':"48.518264",'lng':"122.474189"},
                    ]}

obj = RegionData()

server = SOAPpy.SOAPProxy("http://cdmo.baruch.sc.edu/webservices2/requests.cfc?wsdl")
responsedata =  server.exportAllParamsDateRangeXMLNew('pdbjewq', '2014-12-30', '2014-12-31','*')

pythonObject = SOAPpy.Types.simplify(responsedata)

dataArray =  pythonObject["returnData"]["data"]
print dataArray


