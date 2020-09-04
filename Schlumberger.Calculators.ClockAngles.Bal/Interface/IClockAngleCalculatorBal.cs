using Schlumberger.Calculators.ClockAngles.Bal.Models;
using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;

namespace Schlumberger.Calculators.ClockAngles.Bal.Interface
{
    public interface IClockAngleCalculatorBal
    {
        int GetAngles(int hour, int minutes);
        int SaveAngels(int hour, int minutes);
        Task<CalculateAngleModel> ValidateInputTime(string inputTime);
    }
}
