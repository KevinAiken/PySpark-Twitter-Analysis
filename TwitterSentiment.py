from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from textblob import TextBlob

def simplify(inputFloat):
    if inputFloat > 0.0:
        return "POSITIVE"
    elif inputFloat < 0.0:
        return "NEGATIVE"
    else:
        return "NEUTRAL"

sc = SparkContext(appName="TwitterSentiment")
ssc = StreamingContext(sc, 5)
socket_stream = ssc.socketTextStream("0.0.0.0", 5555)

socket_stream.map(lambda v: "SENTIMENT: " + simplify(TextBlob(v).sentiment[0]) + "TWEET: " + v).saveAsTextFiles("./twitters/data")
#socket_stream.map(lambda v: "SENTIMENT: " + simplify(TextBlob(v).sentiment[0]) + "TWEET: " + v).pprint(100)

ssc.start()
ssc.awaitTermination()
