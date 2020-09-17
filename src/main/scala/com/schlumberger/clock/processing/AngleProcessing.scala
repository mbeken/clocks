package com.schlumberger.clock.processing

import org.apache.spark.sql.{DataFrame, SparkSession}

/**
 * @author Piyush
 * Business logic to calculate angle between
 * hands of clock
 */
object AngleProcessing {
  def calculateAngle(filteredDF: DataFrame, spark: SparkSession): DataFrame = {

    val doCalculation = spark.udf.register("doCalculation", (time: Float) => {
      val hour = time.toString.split(":")(0).toFloat
      val minute = time.toString.split(":")(1).toFloat

      // find position of hour's hand
      val h = (hour * 360) / 12 + (minute * 360) / (12 * 60)
      // find position of minute's hand
      val m = (minute * 360) / 60
      // calculate the angle difference
      var angle = Math.abs(h - m)
      // consider shorter angle and return it
      if (angle > 180) angle = 360 - angle

      angle
    })

    val dfWithCalculatedAngle = filteredDF.withColumn("angle", doCalculation(filteredDF.col("time")))

    dfWithCalculatedAngle
  }
}