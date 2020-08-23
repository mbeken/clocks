using IoTHubTrigger = Microsoft.Azure.WebJobs.EventHubTriggerAttribute;

using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Host;
using Microsoft.Azure.EventHubs;
using System.Text;
using System.Net.Http;
using Microsoft.Extensions.Logging;

namespace ClockAngel
{
    public static class Function1
    {
        private static HttpClient client = new HttpClient();

        [FunctionName("GetClockAngel")]
        [return: EventHub("outputEventHubMessage", Connection = "EventHubConnectionAppSetting")]
        public static float Run([IoTHubTrigger("messages/events", Connection = "")]EventData message, ILogger log)
        {
            log.LogInformation($"C# IoT Hub trigger function processed a message: {Encoding.UTF8.GetString(message.Body.Array)}");
            return CalculateAngel.CalculateAngelfromDateTime(Encoding.UTF8.GetString(message.Body.Array), log);
        }
    }
}