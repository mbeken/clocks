using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace SLB_Clock.Events
{
    /// <summary>
    /// Event Gandler
    /// </summary>
    public interface IHandler
    {
        /// <summary>
        /// Method which is invoked for handling event
        /// </summary>
        /// <param name="eventdate"></param>
        Task Handler(object eventdate);
    }
}
