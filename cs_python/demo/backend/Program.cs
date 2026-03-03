using Microsoft.AspNetCore.Mvc;
using System.Net.Http.Json;

var builder = WebApplication.CreateBuilder(args);

// habilita CORS para o front
builder.Services.AddCors(options => options.AddPolicy("AllowAll", p => p.AllowAnyOrigin().AllowAnyMethod().AllowAnyHeader()));
builder.Services.AddHttpClient();

var app = builder.Build();
app.UseCors("AllowAll");

// 1. status
app.MapGet("/", () => new { status = "Backend C# Online" });

// 2. listagem
app.MapGet("/info", () => new { version = "1.0", provider = "DotNet Middleware" });

// 3. POST para o agente
app.MapPost("/ask", async (HttpClient client, [FromBody] UserRequest req) => {
    var agentUrl = "http://localhost:8001/process";
    var response = await client.PostAsJsonAsync(agentUrl, new { text = req.Message });
    var result = await response.Content.ReadFromJsonAsync<dynamic>();
    return Results.Ok(result);
    // 200 -> OK -> sucesso
});

app.Run("http://localhost:5000");

public record UserRequest(string Message);