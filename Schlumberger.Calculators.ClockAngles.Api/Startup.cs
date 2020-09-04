using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using Schlumberger.Calculators.ClockAngles.Bal.Implement;
using Schlumberger.Calculators.ClockAngles.Bal.Interface;
using Schlumberger.Calculators.ClockAngles.Dal.DataAccess;
using Schlumberger.Calculators.ClockAngles.Dal.Interface;

namespace Schlumberger.Calculators.ClockAngles.Api
{
    public class Startup
    {
        public Startup(IConfiguration configuration)
        {
            Configuration = configuration;
        }

        public IConfiguration Configuration { get; }

        // This method gets called by the runtime. Use this method to add services to the container.
        public void ConfigureServices(IServiceCollection services)
        {
            services.AddControllers();
            services.AddTransient<IClockAngleCalculatorBal, ClockAngleCalculatorBal>();
            services.AddTransient<IClockAngleCalculatorDal, ClockAngleCalculatorDal>();
            services.AddSwaggerGen(options =>
            {
                options.SwaggerDoc("v1", new Microsoft.OpenApi.Models.OpenApiInfo
                {
                    Title = "Clock Angle Calculator Service",
                    Version = "v1",
                    Description = "Service to get angle of hour and minute hands of clock",
                });
            });
        }

        // This method gets called by the runtime. Use this method to configure the HTTP request pipeline.
        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
            }

            app.UseRouting();

            app.UseAuthorization();

            app.UseEndpoints(endpoints =>
            {
                endpoints.MapControllers();
            });

            app.UseSwagger();
            app.UseSwaggerUI(options => options.SwaggerEndpoint("v1/swagger.json", "Clock Angle Calculator Service"));
        }
    }
}
