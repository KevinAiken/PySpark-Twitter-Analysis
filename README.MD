# PySpark Live Twitter Sentiment

You'll need keys to run this in a config.py file.

To run first run TwitterStream.py, then run TwitterSentiment.py. TwitterSentiment will use TwitterStream as the source for the Spark Streaming Context.

Resulting saved files will be tweets and whether their sentiment is neutral, positive, or negative.