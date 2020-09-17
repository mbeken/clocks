package com.schlumberger.clock

import com.schlumberger.clock.config.ReadConfig
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.types._
import com.schlumberger.clock.utils.ParseKafkaMessage
import com.schlumberger.clock.utils.StreamingDataFrameWriter
import com.schlumberger.clock.processing.AngleProcessing

/**
 * @author Piyush
 * Main Class to read data from Kafka topic,
 * calculate angle and insert into database
 */
object CalculateClockAngle {
  def main(args: Array[String]): Unit = {

    val spark = SparkSession.builder
      .appName("Spark Streaming Application to calculate angle")
      .getOrCreate()


    val clockSchema = StructType(Seq(
      StructField("time", FloatType)))

    val server = ReadConfig.getConfig("server")
    val topic = ReadConfig.getConfig("topic")
    val clockStreamingData = spark.readStream.
      format("kafka").
      option("kafka.bootstrap.servers", server).
      option("subscribe", topic).
      option("startingOffsets", "latest").
      load()


    //    read data from kafka topic
    val filteredDF = ParseKafkaMessage.parseDataFromKafkaMessage(clockStreamingData, clockSchema)

    //    calculate angle
    val dfWithCalculatedAngle = AngleProcessing.calculateAngle(filteredDF, spark)

    //    store data into DB
    StreamingDataFrameWriter.StreamingDataFrameDBWriter(dfWithCalculatedAngle)

    spark.stop()

  }
}
