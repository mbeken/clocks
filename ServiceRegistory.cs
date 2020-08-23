using Microsoft.Extensions.DependencyInjection;
using Microsoft.OpenApi.Models;
using SLB_Clock.Business;
using SLB_Clock.Events;
using System;
using System.IO;
using System.Reflection;

namespace SLB_Clock
{
    public static class ServiceRegistory
    {
        /// <summary>
        /// AddSwager
        /// </summary>
        /// <param name="services"></param>
        public static void AddSwager(this IServiceCollection services)
        {
            services.AddSwaggerGen(c =>
            {
                c.SwaggerDoc("v1", new OpenApiInfo
                {
                    Version = "v1",
                    Title = "SLB-Clock",
                    Description = "Find Angle between clock arms",

                });
                // Set the comments path for the Swagger JSON and UI.
                var xmlFile = $"{Assembly.GetExecutingAssembly().GetName().Name}.xml";
                var xmlPath = Path.Combine(AppContext.BaseDirectory, xmlFile);
                c.IncludeXmlComments(xmlPath);
            });
        }
        /// <summary>
        /// AddDependency
        /// </summary>
        /// <param name="services"></param>
        public static void AddDependency(this IServiceCollection services)
        {
            services.AddSingleton<IClockBusiness, ClockBusiness>();
            services.AddSingleton<IHandler, Events.EventHandler>();
        }
    }
}
