from bson.json_util import dumps
from flask import jsonify, request, session
from flask import Flask, render_template, app
import json
from model import RegionData, ValidatedData, RawData
import json
from bson import ObjectId

app = Flask(__name__) #define app using Flask

@app.route('/')
def test1():
    return "Welcome to the BigData QA Assurance and Validation Platform"

#api to return all the regions and station information
@app.route('/getallregioninfo',methods = ['GET'])
def getRegionInformation():
    obj = RegionData()
    data = obj.getAllRegionInfo()
    return jsonify(result = dumps( data))


#api to search the station record in the validated dataset
@app.route('/search',methods = ['POST'])
def searchData():
    """
    searches the record for the station into database
    :return: if data is found into the database
                return { found: "yes", data: { record}}
            else
                return { found: "no", data: {}}
    """

    #extract the parameters from the request body
    input_json = request.get_json(force=True)
    region = request.json["region"]  # region name
    print "region: "+region
    station = request.json["station"]  # station name
    print "station: "+station
    if len(station) is 0:
        station = None
    start_date = request.json["from"]  # start_date name
    print "from: "+start_date
    if len(start_date) is 0:
        start_date = None
    end_date = request.json["to"]  # end_date name
    print "to: "+end_date
    if len(end_date) is 0:
        end_date = None

    #query the database
    obj = ValidatedData()
    if(region != None and station != None and start_date!= None and end_date != None ):
        print "getting data for staion for given date range"
        records = obj.searchValidatedDataForStation(region,station,start_date,end_date)
    elif (region!=None and station!= None):
        print "getting data for station for all available dates"
        records = obj.searchAllValidatedDataForStation(region, station)
    elif (region != None):
        print "getting data for all the stations in the region"
        records = obj.searchAllValidatedDataForRegion(region)

    if(records is not None):
        return jsonify(data={'found': 'yes', 'records':dumps(records)})
    else:
        print "data is not available in the validated database for this station"
        return jsonify(data={'found': "no"})

#api to collect user input file
@app.route('/getUserFile', methods=['POST'])
def getUserDataFile():
    input_json = request.get_json(force=True)

    region = request.json["region"]  # region name
    print "region: " + region

    station = request.json["station"]  # station name
    print "station: " + station

    start_date = request.json["from"]  # start_date name
    print "from: " + start_date

    end_date = request.json["to"]  # end_date name
    print "to: " + end_date
    #code for uploading file


#api to collect user input filters to collect data from webservice
@app.route('/getDataFromWebService', methods=['POST'])
def getDataFromAPI():
    input_json = request.get_json(force=True)

    region = request.json["region"]  # region name
    print "region: " + region

    station = request.json["station"]  # station name
    print "station: " + station

    start_date = request.json["from"]  # start_date name
    print "from: " + start_date

    end_date = request.json["to"]  # end_date name
    print "to: " + end_date
    #code for downloading data



#api to calculate the quality parameters
@app.route('/calculateWQ',methods = ['POST'])
def getWaterQuality():
    """
    this api collects the user input and then process the data to calculate the quality paramaters
    :return: result = {"region": regionname , "station": stationname,
         "from": startdate, "to": enddate, "TotalWaterQuality": totalquality,
        "qualityParameters": {"completeness": cp, "accuracy": a, "timeliness": t, "uniqueness": un, "validity" : v, "consistency": c,
         reliability: r, "usability"": us} }
    """
    result = {}
    return jsonify(data = result)


if __name__ == "__main__" :
    app.run( host='0.0.0.0',port = 5000, debug = True) # run app in debug mode
