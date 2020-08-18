using System;
using System.Collections.Generic;
using System.Linq;
using System.Linq.Expressions;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;

// For more information on enabling Web API for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace ClockAngle.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class ClockController : ControllerBase
    {
        /*********************************************************************************************************************************************
        Q.How will you deploy this solution(in code or as a todo list if time is limited). i.e.how and where will this run?

        Ans: This is API project developed in .NET Core. This can be deplyoed as webapp on cloud services.
        In Azure we can create web app and then deploy this as service . The URL of this API can be consumed by the client applciations.
        In Onpremise scenarion it can be hosted on IIS.


        Q.How will you manage any infrastructure needed?
        
        Ans:In Azure , we can create one resource group based on project need, enterprise policies. Under this resource group we
        can create the required resources. e.g For hosting such API we would need Azure web app service. We need to manage this service.
        As this is PAAS service no infrastructure is involved as such. In real project scenarios we end up creating multiple services on cloud
        and those needs to be adminstrerd from cost perspecive.



       I have implemented SWAGGER so this can be tested by executing . It provide UI from where we can test.
       Same applciation can be publised from visual studio to any azure subscription web app service.

        *******************************************************************************************************************************************************/

        /// <summary>
        /// This is api method which will be consumed by client application.
        /// </summary>
        /// <param name="timevalue">Timestamp value for which angel needs to be determined.</param>
        /// <returns></returns>
        [HttpGet]
        public IActionResult Get(string timevalue)
        {
            try
            {
               return Ok("The calcualted angle is " +  GetAngle(timevalue).ToString() + " degrees.");
            }
            catch (Exception ex)
            {
                return BadRequest(ex.Message.ToString());
            }
           
        }

        /// <summary>
        /// Thie method takes the time string value as input and returns the calculted degree value.
        /// </summary>
        /// <param name="timevalue">A string containing timestamp.e.g. 03:30</param>
        /// <returns></returns>
        private int GetAngle(string timevalue)
        {
            //1. Get the values of Hour & Minute from intput string
            //2, Determine the relative position of hour and minute hands.
            //3. Determine the angle.
            //To DO: {24 Hrs format can be implmented in validation}.

            string[] timesplit = timevalue.Split(":");
            int angleDegree = 0;

            try
            {
                int hourValue = Convert.ToInt16(timesplit[0]);
                int minuteValue = Convert.ToInt16(timesplit[1]);
                if (hourValue <= 12 && minuteValue <= 60)
                {
                    int hourPosition = hourValue * 5;
                    int hourDelta = minuteValue / 12;
                    hourPosition = hourPosition + hourDelta;

                    if (minuteValue >= hourPosition)
                        angleDegree = (minuteValue - hourPosition) * 6;
                    else
                        angleDegree = (hourPosition - minuteValue) * 6;

                    return angleDegree;
                }
                else
                    throw new Exception("Invalid Hour or Minute value");
            }
            catch (Exception ex)
            {
                throw ex;
            }
        }
    }
}
