using Microsoft.AspNetCore.Mvc;
using Backend.Data;
using Backend.Models;
using Microsoft.EntityFrameworkCore;
using Microsoft.VisualBasic;

namespace Backend.Controllers;

[ApiController]
[Route("api/people")]
public class PeopleController : ControllerBase
{
    private readonly AppDbContext _context;

    public PeopleController(AppDbContext context)
    {
        _context = context;
    }
    [HttpGet]
    public IEnumerable<Person> Get()
    {
        return _context.People.ToList();
    }

    [HttpPost]
    public IActionResult Post(Person person)
    {
        _context.People.Add(person);
        _context.SaveChanges();
        return Ok(person);
    }
// ROTA PATCH PARA ATUALIZAR UMA PESSOA (PERSON)
    [HttpPatch("{id}")]
    public IActionResult Patch(int id, Person updated)
    {
        var person = _context.People.Find(id); // LINQ
        if (person == null)
        {
            return NotFound();
        }
        person.Name = updated.Name;
        _context.SaveChanges();
        return Ok($"Nome da pessoa foi atualizado c sucesso: {person.Name}");
    }

    [HttpDelete("{id}")]
    public IActionResult Delete(int id)
    {
        var person = _context.People.Find(id); // LINQ
        if (person == null)
        {
            return NotFound();
        }
        _context.People.Remove(person);
        _context.SaveChanges();
        return Ok($"O usuário {person.Name} foi removido do BD!");
    }
}
