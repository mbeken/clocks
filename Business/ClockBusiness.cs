using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using SLB_Clock.Models.DomainModel;

namespace SLB_Clock.Business
{
    /// <summary>
    /// ClockBusiness
    /// </summary>
    public class ClockBusiness : IClockBusiness
    {
        /// <summary>
        /// Get Angle
        /// </summary>
        /// <param name="ClockModel"></param>
        /// <returns></returns>
        public async Task<int> GetAngle(ClockModel ClockModel)
        {
            var hour = ClockModel.Hour;
            var min = ClockModel.Min;
            // Validation
            if (hour < 0 || min < 0 || hour > 12 || min > 60)
                throw new Exception("Invalid Input");
            // Handle 24 hr 
            if (hour == 12)
                hour = 0;
            if (min == 60)
            {
                min = 0;
                hour += 1;
                if (hour > 12)
                    hour = hour - 12;
            }
            int hour_angle = (int)(0.5 * (hour * 60 + min));
            int minute_angle = (int)(6 * min);
            int angle = Math.Abs(hour_angle - minute_angle);
            angle = Math.Min(360 - angle, angle);
            return angle;
        }
    }
}
