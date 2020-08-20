import java.io.FileInputStream

import org.apache.spark.sql.SparkSession
import java.util.Properties

object clockExercise {

  def angleCalculator(hour:Int,min:Int): Double = {
    var inputHour = hour
    var inputMinute = min
    if(inputHour == 12) {
      inputHour = 0
    }
    if(inputMinute == 60){
      inputMinute = 0
      inputHour = inputHour + 1
    }

    val angleOfHourHand = (inputHour * 60 + inputMinute ) * 0.5
    val angleOfMinute = inputMinute * 6
    val hourMinDiffAngle = (angleOfHourHand - angleOfMinute)
    val absoluteDiff = hourMinDiffAngle.abs
    val diffList = List(absoluteDiff, 360 - absoluteDiff)
    val angle = diffList.min
    return angle

  }

  def main(args: Array[String]): Unit = {

    //Build spark session
    val spark = SparkSession.builder().master("local").appName("clockExercise").getOrCreate()

    //load properties file at run time for input
    val file_prop = new Properties()
    val filePath = args(0)
    file_prop.load(new FileInputStream(filePath))

    //read input time from properties file

    val inputTime = file_prop.getProperty("INPUT_TIME")
    //val inputTime="03:30"

    val hour = inputTime.split(":"){0}.toInt
    val min = inputTime.split(":"){1}.toInt

    println("Input Time : "+inputTime)
    println("Input Hour : "+ hour)
    println("Input Minute : "+ min)

    val angle = angleCalculator (hour,min)
    println ("Angle Difference : "+angle)

  }
}
