# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "event_stream": {
# META       "known_event_streams": [
# META         {
# META           "artifact_id": "a9d0d2ed-f5da-43b2-bf11-e85ec1bfa42c",
# META           "stream_id": "bbb8c65e-b8fc-417b-8815-d8974fbc7ea6"
# META         }
# META       ]
# META     }
# META   }
# META }

# PARAMETERS CELL ********************

# Set the event stream item and datasource IDs
__in_eventstream_item_id = "a9d0d2ed-f5da-43b2-bf11-e85ec1bfa42c"
__in_eventstream_datasource_id = "d14a8979-cbc3-4055-a697-c70f3566ece6"

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StringType
from pyspark.sql.dataframe import DataFrame


eventstream_options = {
    "eventstream.itemid": __in_eventstream_item_id,
    "eventstream.datasourceid": __in_eventstream_datasource_id
}


# Read from Kafka using the config map
df_raw = spark.readStream.format("kafka").options(**eventstream_options).load()

decoded_df = df_raw.select(
    col("key").cast(StringType()).alias("key"),
    col("value").cast(StringType()).alias("value"),
    col("partition"),
    col("offset")
)

def showDf(x:DataFrame, y:int):
    x.show()

# Print messages to the console
query = decoded_df.writeStream.foreachBatch(showDf).outputMode("append").start()
query.awaitTermination()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark",
# META   "frozen": false,
# META   "editable": true
# META }
