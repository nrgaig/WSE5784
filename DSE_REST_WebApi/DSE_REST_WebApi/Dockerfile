#See https://aka.ms/customizecontainer to learn how to customize your debug container and how Visual Studio uses this Dockerfile to build your images for faster debugging.

FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
WORKDIR /app
EXPOSE 80

FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
ARG BUILD_CONFIGURATION=Release
WORKDIR /src
COPY ["DSE_REST_WebApi/DSE_REST_WebApi.csproj", "DSE_REST_WebApi/"]
RUN dotnet restore "./DSE_REST_WebApi/DSE_REST_WebApi.csproj"
COPY . .
WORKDIR "/src/DSE_REST_WebApi"
RUN dotnet build "./DSE_REST_WebApi.csproj" -c $BUILD_CONFIGURATION -o /app/build

FROM build AS publish
ARG BUILD_CONFIGURATION=Release
RUN dotnet publish "./DSE_REST_WebApi.csproj" -c $BUILD_CONFIGURATION -o /app/publish /p:UseAppHost=false

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "DSE_REST_WebApi.dll"]