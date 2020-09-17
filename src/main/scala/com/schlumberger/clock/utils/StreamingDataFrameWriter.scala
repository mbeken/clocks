package com.schlumberger.clock.utils

import com.schlumberger.clock.config.ReadConfig
import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.streaming.StreamingQuery

/**
 * @author Piyush
 * Class to Write data to Database
 */
object StreamingDataFrameWriter {

  def StreamingDataFrameDBWriter(dfWithCalculatedAngle: DataFrame): StreamingQuery = {

    val url = ReadConfig.getConfig("url")
    val user = ReadConfig.getConfig("user")
    val password = ReadConfig.getConfig("password")

    val write = new JDBCSink(url, user, password)

    val query = dfWithCalculatedAngle.writeStream
      .foreach(writer)
      .format("parquet")
      .outputMode("append")
      .option("checkpointLocation", "/tmp/clock")
      .option("truncate", false)
      .start()
  }
}
