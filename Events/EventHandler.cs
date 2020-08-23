using Microsoft.Extensions.Logging;
using Newtonsoft.Json;
using SLB_Clock.Business;
using SLB_Clock.Models.DomainModel;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace SLB_Clock.Events
{
    /// <summary>
    /// EventHandler
    /// </summary>
    public class EventHandler : IHandler
    {
        readonly IClockBusiness _ClockBusiness;
        private readonly ILogger _logger;
        string timeSeparator = ":";

        /// <summary>
        /// Constructor EventHandler
        /// </summary>
        /// <param name="ClockBusiness"></param>
        /// <param name="logger"></param>
        public EventHandler(IClockBusiness ClockBusiness, ILogger<EventHandler> logger)
        {
            _ClockBusiness = ClockBusiness ?? throw new ArgumentNullException(nameof(ClockBusiness));
            _logger = logger ?? throw new ArgumentNullException(nameof(logger));
        }

        /// <summary>
        /// Handler
        /// </summary>
        /// <param name="eventdate"></param>
        /// <returns></returns>
        public async Task Handler(object eventdate)
        {
            if (eventdate != null)
            {

                var eventData = JsonConvert.DeserializeObject<EventData>(eventdate.ToString());
                var splittedValues = eventData.Data.Split(timeSeparator);
                var timeModel = new ClockModel
                {
                    Hour = Convert.ToInt32(splittedValues[0]),
                    Min = Convert.ToInt32(splittedValues[1])
                };
                try
                {
                    var angleValue = await _ClockBusiness.GetAngle(timeModel);
                    // TODo Save in to database; 
                    // Call to Database repo
                }
                catch (Exception ex)
                {

                    _logger.LogError(ex.Message);
                }



            }

        }
    }
}
