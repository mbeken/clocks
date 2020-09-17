package com.schlumberger.clock.utils

import org.apache.spark.sql.functions.split
import org.apache.spark.sql.types._
import org.apache.spark.sql.DataFrame

object ParseKafkaMessage {
  def parseDataFromKafkaMessage(sdf: DataFrame, schema: StructType): DataFrame = {
    sdf.selectExpr("CAST(key AS FLOAT)")
      .as[(Float)]
    sdf
  }
}
