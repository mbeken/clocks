using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace SLB_Clock.Events
{
    /// <summary>
    /// Event data MOdel
    /// </summary>
    public class EventData
    {
        /// <summary>
        /// Device ID
        /// </summary>
        public string DeviceID { get; set; }
        /// <summary>
        /// Date
        /// </summary>
        public DateTime Date { get; set; }
        /// <summary>
        /// Data hh:mm
        /// </summary>
        public string Data { get; set; }
    }
}
