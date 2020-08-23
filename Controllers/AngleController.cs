using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using SLB_Clock.Business;
using SLB_Clock.Models.DomainModel;
using System;
using System.Threading.Tasks;

namespace SLB_Clock.Controllers
{

    /// <summary>
    /// Sample Conteroller for Testing purpose
    /// </summary>
    [Route("api/[controller]")]
    [ApiController]
    public class AngleController : ControllerBase
    {
        string timeSeparator = ":";
        private readonly IClockBusiness _ClockBusiness;
        private readonly ILogger _logger;

        /// <summary>
        /// Constructor
        /// </summary>
        /// <param name="ClockBusiness"></param>
        /// <param name="logger"></param>
        public AngleController(IClockBusiness ClockBusiness, ILogger<AngleController> logger)
        {
            _ClockBusiness = ClockBusiness ?? throw new ArgumentNullException(nameof(ClockBusiness));
            _logger = logger ?? throw new ArgumentNullException(nameof(logger));
        }

        /// <summary>
        /// Convert Time to Angle
        /// </summary>
        /// <param name="time"></param>
        /// <returns>Object of angle and message</returns>
        [HttpPost]
        public async Task<IActionResult> Post([FromBody] string time)
        {
            if (String.IsNullOrWhiteSpace(time) || !time.Contains(timeSeparator))
            {
                var message = "Input should be in format 00:00";
                _logger.LogDebug(message);
                return BadRequest(message);
            }
            try
            {
                var splittedValues = time.Split(timeSeparator);
                var timeModel = new ClockModel
                {
                    Hour = Convert.ToInt32(splittedValues[0]),
                    Min = Convert.ToInt32(splittedValues[1])
                };
                var angle = await _ClockBusiness.GetAngle(timeModel);              
                return Ok(new
                {
                    Message = $"Angle between {timeModel.Hour} h and {timeModel.Min} m is {angle} degree.",
                    Angle = angle
                });

            }
            catch (Exception ex)
            {
                _logger.LogDebug(ex.Message);
                return BadRequest(ex.Message);
            }



        }


    }
}
