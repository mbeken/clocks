import com.typesafe.scalalogging.slf4j.Logger
//import org.apache.log4j._
import com.typesafe.scalalogging._
object clocksAngle {

    // Function to calculate the angle between hour and minute hand with reference to 12

  def angleCalcuator(time:String): String= {

   // split the input

    val timesplit = time.split(":")
    var hours = Integer.parseInt(timesplit(0))
    var minutes = Integer.parseInt(timesplit(1))

   //Input validation

    if (hours < 0 || hours > 12 || minutes < 0 || minutes > 60)
     println("Invalid time : please enter 12 hr format(HH:MM)")
    //logger.info("Invalid time : please enter 12 hr format(HH:MM)")
    if (hours.equals(12))
      hours = 0
    if (minutes.equals(60)) {
      minutes = 0
      hours += 1
      if (hours > 12)
        hours -= 12
    }

   // Calculate the angles moved by hours and minutes hands

    val hrangle:Double = 0.5 *(hours * 60 + minutes)
    val minangle:Double = 6 * minutes
    val hrmovement:Double = (minutes / 60) * 30
    val finalhrAngle:Double = hrangle + hrmovement

    var angle:Double = Math.abs(finalhrAngle - minangle)
    angle = Math.min(360 - angle, angle)
    String.valueOf(angle)
  }

 //GCP cloud function does not support scala language hence to give input to function is hardcoded 
 //We can use PubSub and cloud function service in java/python which supports deploment process
 
  def main(args: Array[String]): Unit = {
    val time="03:10"
    val finalAngle =angleCalcuator(time)
    println("Angle between Minute and Hour At "+time+" is "+finalAngle)
  }
}
