from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("KafkaStream").getOrCreate()
df = spark.readStream.format("kafka").option("subscribe", "events").load()
df.writeStream.format("console").start().awaitTermination()
