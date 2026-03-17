# .NET CLI Cheat Sheet

- [.NET CLI Cheat Sheet](#net-cli-cheat-sheet)
  - [Project Creation](#project-creation)
  - [Build \& Run](#build--run)
  - [Testing](#testing)
  - [NuGet Packages](#nuget-packages)
  - [Solutions](#solutions)
  - [Publishing \& Packing](#publishing--packing)
  - [Project File (.csproj)](#project-file-csproj)
  - [Useful Globals](#useful-globals)


## Project Creation

```bash
dotnet new console -n MyApp        # console app
dotnet new classlib -n MyLib       # class library
dotnet new webapi -n MyApi         # ASP.NET Web API
dotnet new blazorwasm -n MyBlazor  # Blazor WebAssembly
dotnet new sln -n MySolution       # solution file

dotnet new list                    # list all available templates
```

## Build & Run

```bash
dotnet build                       # build (Debug by default)
dotnet build -c Release            # release build
dotnet run                         # build + run
dotnet run --project ./MyApp       # specify project
dotnet run -- arg1 arg2            # pass args to the app
dotnet watch run                   # hot-reload on file changes
```

## Testing

```bash
dotnet test                        # run all tests
dotnet test --filter "MyTestName"  # run specific test by name
dotnet test --filter "Category=Unit"
dotnet test -v normal              # verbose output
dotnet test --collect "Code Coverage"
```

## NuGet Packages

```bash
dotnet add package Newtonsoft.Json
dotnet add package Serilog --version 3.1.1
dotnet remove package Newtonsoft.Json
dotnet list package                # list installed packages
dotnet list package --outdated     # check for updates
dotnet restore                     # restore all packages
```

## Solutions

```bash
dotnet sln add ./MyApp/MyApp.csproj
dotnet sln remove ./MyApp/MyApp.csproj
dotnet sln list                    # list projects in solution
```

## Publishing & Packing

```bash
dotnet publish -c Release -o ./out
dotnet publish -r win-x64 --self-contained   # self-contained binary
dotnet publish -r linux-x64 -p:PublishSingleFile=true

dotnet pack                        # create NuGet package
dotnet pack -c Release -o ./nupkgs
```

## Project File (.csproj)

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>Exe</OutputType>          <!-- Exe | Library -->
    <TargetFramework>net9.0</TargetFramework>
    <Nullable>enable</Nullable>
    <ImplicitUsings>enable</ImplicitUsings>
    <LangVersion>latest</LangVersion>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="Newtonsoft.Json" Version="13.0.3" />
    <ProjectReference Include="..\MyLib\MyLib.csproj" />
  </ItemGroup>
</Project>
```

## Useful Globals

```bash
dotnet --version                   # SDK version
dotnet --list-sdks                 # all installed SDKs
dotnet --list-runtimes             # all installed runtimes
dotnet tool install -g dotnet-ef   # install a global tool
dotnet tool list -g                # list global tools
dotnet format                      # format code (built-in)
```
