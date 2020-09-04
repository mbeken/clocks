using Schlumberger.Calculators.ClockAngles.Bal.Interface;
using Schlumberger.Calculators.ClockAngles.Bal.Models;
using Schlumberger.Calculators.ClockAngles.Bal.Validation;
using Schlumberger.Calculators.ClockAngles.Dal.Interface;
using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;

namespace Schlumberger.Calculators.ClockAngles.Bal.Implement
{
    public class ClockAngleCalculatorBal : IClockAngleCalculatorBal
    {
        /// <summary>
        /// to access operations in DAL layer of Calendar
        /// </summary>
        private readonly IClockAngleCalculatorDal _clockAngleCalculatorDal;

        public ClockAngleCalculatorBal(IClockAngleCalculatorDal clockAngleCalculatorDal)
        {
            _clockAngleCalculatorDal = clockAngleCalculatorDal;
        }

        /// <summary>
        /// Get the Angles between two hands of clock
        /// </summary>
        /// <param name="hour"></param>
        /// <param name="minutes"></param>
        /// <returns></returns>
        public int GetAngles(int hour, int minutes)
        {
            if (hour == 12)
                hour = 0;

            if (minutes == 60)
            {
                minutes = 0;
                hour += 1;
                if (hour > 12)
                    hour -= 12;
            }
            int hourAngle = (int)(0.5 * (hour * 60 + minutes));
            int minuteAngle = (int)(6 * minutes);
            int angle = Math.Abs(hourAngle - minuteAngle);
            angle = Math.Min(360 - angle, angle);

            return angle;
        }

        /// <summary>
        /// To Save the Angles - for Future use
        /// </summary>
        /// <param name="hour"></param>
        /// <param name="minutes"></param>
        /// <returns></returns>
        public int SaveAngels(int hour, int minutes)
        {
            throw new NotImplementedException();
        }

        /// <summary>
        /// to validate the input parameter
        /// </summary>
        /// <param name="inputTime"></param>
        /// <returns></returns>
        public async Task<CalculateAngleModel> ValidateInputTime(string inputTime)
        {
            return await ValidateTimeFormat.IsValildTimeFormat(inputTime);
        }
    }
}
