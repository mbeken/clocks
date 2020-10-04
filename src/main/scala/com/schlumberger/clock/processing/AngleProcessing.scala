package com.schlumberger.clock.processing

import org.apache.spark.sql.{DataFrame, SparkSession}

/**
 * @author Piyush
 * Business logic to calculate angle between
 * hands of clock
 */
object AngleProcessing {
  def calculateAngle(filteredDF: DataFrame, spark: SparkSession): DataFrame = {

    def doCalculation (time: String):String = {
      import spark.implicits._
      if(time.contains(":")) {
        val hour = time.split(":")(0).toFloat
        val minute = time.split(":")(1).toFloat

        // find position of hour's hand
        val h = (hour * 360) / 12 + (minute * 360) / (12 * 60)
        // find position of minute's hand
        val m = (minute * 360) / 60
        // calculate the angle difference
        var angle = Math.abs(h - m)
        // consider shorter angle and return it
        if (angle > 180) angle = 360 - angle
        println("calculated angle is : "+angle)
        angle.toString
      }
      else {
        println("calculated angle is else : "+time)
        time
      }
    }

    val doCalculationUDF = spark.udf.register("doCalculation",doCalculation _)

    println("calculating angle")

    val dfWithCalculatedAngle = filteredDF.withColumn("angle", doCalculationUDF(filteredDF.col("value")))

    dfWithCalculatedAngle
  }
}