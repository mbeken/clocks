using System;
using System.Collections.Generic;
using System.Text;
using Microsoft.Extensions.Logging;
namespace ClockAngel
{
    internal class CalculateAngel
    {

        internal static float CalculateAngelfromDateTime(string clockTime, ILogger log)
        {
            float angle = 0;
            try
            {
                // Assign date time received in event hub  
                DateTime dateTimeClocked = Convert.ToDateTime(clockTime);

                float hours = dateTimeClocked.Hour;
                float minutes = dateTimeClocked.Minute;
                // Minutes angles bases on 60 minutes and 360 degree
                float angleMinute = minutes / 60 * 360;  
                if (hours >= 12)
                {
                    hours -= 12;
                }
                // The angle measure between any two consecutive numbers on a clock is 360/12 = 30
                // hour hand angle calculation
                float angleHour = hours * 30 + minutes / 60 * 30;
                angle = Math.Abs(angleHour - angleMinute);


            }
            catch (Exception ex)
            {

                log.LogInformation($"error in clculating Angel. error description is :  {ex.Message}");
            }
            return angle;

        }



    }
}
