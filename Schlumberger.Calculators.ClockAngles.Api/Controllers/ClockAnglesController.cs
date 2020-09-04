using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Schlumberger.Calculators.ClockAngles.Bal.Interface;
using Swashbuckle.Swagger.Annotations;

namespace Schlumberger.Calculators.ClockAngles.Api.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class ClockAnglesController : Controller
    {
        /// <summary>
        /// Bal layer object to get access of Bal
        /// </summary>
        private readonly IClockAngleCalculatorBal _clockAngleCalculatorBal = null;

        /// <summary>
        /// Constructor to used injected Bal Object
        /// </summary>
        /// <param name="clockAngleCalculatorBal"></param>
        public ClockAnglesController(IClockAngleCalculatorBal clockAngleCalculatorBal)
        {
            _clockAngleCalculatorBal = clockAngleCalculatorBal;
        }

        [SwaggerResponse(StatusCodes.Status200OK)]
        [SwaggerResponse(StatusCodes.Status400BadRequest)]
        [SwaggerResponse(StatusCodes.Status500InternalServerError)]
        [HttpGet("{inputTime}", Name = "GetClockAngle")]

        public async Task<ActionResult<int>> Get(string inputTime, CancellationToken cancellationToken)
        {
            try
            {
                var calculateAngleModel = await _clockAngleCalculatorBal.ValidateInputTime(inputTime);
                if (calculateAngleModel.isValid)
                {
                    calculateAngleModel.angle = _clockAngleCalculatorBal.GetAngles(calculateAngleModel.hour, calculateAngleModel.minute);
                }
                else
                {
                    Response.StatusCode = StatusCodes.Status400BadRequest;
                    return Json(new { status = "Invalid Input", message = "Please Provide valid input in HH:MM format. HH between 1 to 12,  MM between 1 to 60" });
                }
                Response.StatusCode = StatusCodes.Status200OK;
                return calculateAngleModel.angle;
            }
            catch (Exception)
            {
                Response.StatusCode = StatusCodes.Status500InternalServerError;
                return Json(new { message = "Error" });
            }
        }

    }
}
