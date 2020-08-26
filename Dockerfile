FROM microsoft/dotnet:2.1-aspnetcore-runtime AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM microsoft/dotnet:2.1-sdk AS build
WORKDIR /src
COPY ["clocks/SLB-Clock.csproj", "clocks/"]
RUN dotnet restore "clocks/SLB-Clock.csproj"
COPY . .
WORKDIR "/src/clocks"
RUN dotnet build "SLB-Clock.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "SLB-Clock.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "SLB-Clock.dll"]