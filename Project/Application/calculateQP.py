
class QualityParameterCalculation:
    from pymongo import MongoClient
    client = MongoClient()
    # Select appropriate database
    db = client.dataQuality
    # Select appropriate collection
    coll = db.SanFranciscoBayWaterQuality
    # Select the first document
    doc = coll.find_one()
    # Find the total number of documents
    total_docs = coll.find().count()
    parameters = {"completeness": 0, "accuracy": 0, "timeliness": 0, "uniqueness": 0,
                  "validity":0, "consistency":0, "reliability":0, "usability":0}



    def __init__(self):
        pass
    def getCompleteness(self):
        total_null = 0
        count = 0
        # Iterate over keys pulled from first document
        for key in QualityParameterCalculation.doc:
            #print key
            total_null = total_null + QualityParameterCalculation.coll.count({key: ""})
            count += 1  # Keep track of total number of keys/columns
        # Adds the value of completeness to parameters
        completeness = (total_null * 100.0) / (QualityParameterCalculation.total_docs * count)
        QualityParameterCalculation.parameters["completeness"] = completeness

    def getAccuracy(self):
        pass

    def getTimeliness(self):
        pass

    def getUniqueness(self):
        print "Enter key to find unique rows: \n a. Date \n b. Time"
        s = raw_input()
        u_key = s.lower()

        if u_key == "date":
            cursor = QualityParameterCalculation.db.SanFranciscoBayWaterQuality.aggregate([{"$group": {"_id": "$Date", "count": {"$sum": 1}}}])
        if u_key == "time":
            cursor = QualityParameterCalculation.db.SanFranciscoBayWaterQuality.aggregate([{"$group": {"_id": "$Time", "count": {"$sum": 1}}}])

        u_count = 0
        u_rows = 0

        for _ in cursor:
            if _[u'count'] > 1:
                # print _
                u_count += _[u'count']
                u_rows += 1

        # print u_count
        # print u_rows
        print QualityParameterCalculation.total_docs

        unique_rows = QualityParameterCalculation.total_docs - u_count + u_rows

        # print "Unique rows based on",u_key,"are",unique_rows
        uniqueness = unique_rows * 100.0 / QualityParameterCalculation.total_docs
        QualityParameterCalculation.parameters[uniqueness] = uniqueness

    def getValidity(self):
        pass
    def getConsistency(self):
        pass
    def getReliability(self):
        pass
    def getUsability(self):
        pass
