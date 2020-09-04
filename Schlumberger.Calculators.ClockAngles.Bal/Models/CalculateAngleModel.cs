using System;
using System.Collections.Generic;
using System.Text;

namespace Schlumberger.Calculators.ClockAngles.Bal.Models
{
    public class CalculateAngleModel
    {
        public int hour { get; set; }
        public int minute { get; set; }
        public bool isValid { get; set; }
        public int angle { get; set; }
    }
}
