using System;
using System.Collections.Generic;
using System.Text;

namespace Schlumberger.Calculators.ClockAngles.Dal.Interface
{
    public interface IClockAngleCalculatorDal
    {
        int SaveAngels(int hour, int minutes, int angle);
    }
}
