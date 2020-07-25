package com.example;

import com.example.Example.PubSubMessage;
import com.google.cloud.functions.BackgroundFunction;
import com.google.cloud.functions.Context;
import java.util.Base64;
import java.util.Map;
import java.util.logging.Logger;

public class Example implements BackgroundFunction<PubSubMessage> {
  private static final Logger logger = Logger.getLogger(Example.class.getName());

  @Override
  public void accept(PubSubMessage message, Context context) {
    String data = message.data != null
      ? clockAngle(new String(Base64.getDecoder().decode(message.data)))
      : "Please Provide Correct Input";
    logger.info(data);
  }
    // Function to calculate the clock angle 
    // Calculate each angle with reference to 12
    static String clockAngle(String time) 
    {
	String[] timeInHoursMinutes = time.split(":",0);

        // split the input 
        double hours = Double.parseDouble(timeInHoursMinutes[0]);
        double minutes = Double.parseDouble(timeInHoursMinutes[1]);

	// validate the input
        if (hours < 0 || hours > 12 || minutes < 0 || minutes > 60) 
            logger.info("Invalid_Time_Format/Wrong_Input"); 

	// if hour is 12 then change it to 0
        if (hours == 12) 
            hours = 0;

	// if minutes are 60 then change it to 0 and add 1 in hours
        if (minutes == 60) 
	{
		minutes = 0;
        	hours += 1;
		// if hours are greater than 12 then substract it from 12 
		if(hours > 12) 
          		hours -= 12;
	}
  
        // Calculate the angles moved by hours and minutes hands 
        double hourAngle = (double)(hours*30); 
        double minuteAngle = (double)(6*minutes);
	double offset = ((minutes/60)*30);
	double correctedHourAngle = hourAngle + offset;
  
        // get the difference between two angles 
        double finalAngleValue = Math.abs(correctedHourAngle - minuteAngle); 
  
        // which ever is smaller angle b/w two angles 
        finalAngleValue = Math.min(360-finalAngleValue, finalAngleValue); 

  	// return as string vale
        return String.valueOf(finalAngleValue); 
    }

  public static class PubSubMessage {
    String data;
    Map<String, String> attributes;
    String messageId;
    String publishTime;
  }
}
