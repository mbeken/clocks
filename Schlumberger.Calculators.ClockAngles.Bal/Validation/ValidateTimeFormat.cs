using Schlumberger.Calculators.ClockAngles.Bal.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;

namespace Schlumberger.Calculators.ClockAngles.Bal.Validation
{
    public static class ValidateTimeFormat
    {

        public static async Task <CalculateAngleModel> IsValildTimeFormat(string inputTime)
        {
            CalculateAngleModel calculatedAngleModel = new CalculateAngleModel
            {
                angle = 0,
                hour = 0,
                minute = 0,
                isValid = false
            };


            if (inputTime.Trim().Length != 5)
            {
                return calculatedAngleModel;
            }
            else if (!inputTime.Contains(":"))
            {
                return calculatedAngleModel;
            }
            else
            {
                string hour = inputTime.Substring(0, 2);
                string minutes = inputTime.Substring(3);

                if ((!hour.All(char.IsDigit)) || (!minutes.All(char.IsDigit)))
                {
                    return calculatedAngleModel;
                }
                else
                {
                    int hh = Convert.ToInt32(inputTime.Substring(0, 2));
                    int mm = Convert.ToInt32(inputTime.Substring(3));
                    if (hh < 0 || mm < 0 || hh > 12 || mm > 60)
                    {
                        return calculatedAngleModel;
                    }
                    calculatedAngleModel.angle = 0;
                    calculatedAngleModel.hour = hh;
                    calculatedAngleModel.minute = mm;
                    calculatedAngleModel.isValid = true;
                    return calculatedAngleModel;
                }

            }
        }
    }
}
