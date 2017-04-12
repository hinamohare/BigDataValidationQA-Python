
class QualityParameterCalculation:
    parameters = {"completeness": 0, "accuracy": 0, "timeliness": 0, "uniqueness": 0,
                  "validity":0, "consistency":0, "reliability":0, "usability":0}
    def __init__(self):
        pass

    def getCompleteness(self):
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

        total_null = 0
        count = 0
        for key in doc:
            # Iterate over keys pulled from first document
            #print key
            total_null = total_null + coll.count({key: ""})
            count += 1  # Keep track of total number of keys/columns

        # Add % of completeness to parameters dictionary
        completeness = (total_null * 100.0) / (total_docs * count)
        QualityParameterCalculation.parameters.update({"completeness": completeness})
    def getAccuracy(self):
        pass
    def getTimeliness(self):
        pass
    def getUniqueness(self):

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

        print "Enter key to find unique rows: \n a. Date \n b. Time"
        s = raw_input()
        u_key = s.lower()

        if u_key == "date":
            cursor = db.SanFranciscoBayWaterQuality.aggregate([{"$group": {"_id": "$Date", "count": {"$sum": 1}}}])
        if u_key == "time":
            cursor = db.SanFranciscoBayWaterQuality.aggregate([{"$group": {"_id": "$Time", "count": {"$sum": 1}}}])

        u_count = 0
        u_rows = 0
        for _ in cursor:
            if _[u'count'] > 1:
                # print _
                u_count += _[u'count']
                u_rows += 1

        # print u_count
        # print u_rows
        print total_docs

        unique_rows = total_docs - u_count + u_rows

        # print "Unique rows based on",u_key,"are",unique_rows
        uniqueness = unique_rows * 100.0 / total_docs
        QualityParameterCalculation.parameters.update({"uniqueness": uniqueness})
        #QualityParameterCalculation.parameters["uniqueness"] = uniqueness

    def getValidity(self):
        pass
    def getConsistency(self):
        pass
    def getReliability(self):
        pass
    def getUsability(self):
        pass
