package com.schlumberger.clock.utils

import java.sql.DriverManager

import com.schlumberger.clock.config.ReadConfig
import org.apache.spark.sql.{DataFrame, SparkSession}
import org.apache.spark.sql.streaming.{ProcessingTime, StreamingQuery}

/**
 * @author Piyush
 *         Class to Write data to Database
 */
object StreamingDataFrameWriter {

  def StreamingDataFrameDBWriter(dfWithCalculatedAngle: DataFrame, spark: SparkSession): Unit = {

    import spark.implicits._
    val url = ReadConfig.getConfig("url")
    val user = ReadConfig.getConfig("user")
    val password = ReadConfig.getConfig("password")


    val writer = new JDBCSink(url, user, password)


    val writeData = dfWithCalculatedAngle.writeStream
      .foreach(writer)
      .outputMode("Append")
      .trigger(ProcessingTime(100))
      .option("checkpointLocation", "F:\\kafkacheckpoint")
      .start()

    writeData.awaitTermination

  }


}
