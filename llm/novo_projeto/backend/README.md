# criar projeto novo de API

dotnet new web -n <nome_do_projeto>

# adicionar pacotes
dotnet add package Microsoft.EntityFrameworkCore
dotnet add package Microsoft.EntityFrameworkCore.Sqlite
dotnet add package Microsoft.EntityFrameworkCore.Tools

# instalar o entity framework
dotnet tool install --global dotnet-ef

# criar o banco de dados
dotnet ef migrations add InitialCreate
dotnet ef database update

# rodar a api
dotnet run