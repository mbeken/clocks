using SLB_Clock.Models.DomainModel;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace SLB_Clock.Business
{
    /// <summary>
    /// ClockBusiness
    /// </summary>
    public interface IClockBusiness
    {
        /// <summary>
        /// GetAngle
        /// </summary>
        /// <param name="ClockModel"></param>
        /// <returns></returns>
        Task<int> GetAngle(ClockModel ClockModel);
    }
}
