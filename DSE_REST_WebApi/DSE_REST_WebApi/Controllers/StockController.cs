﻿using WSE_REST_WebApi.Models;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.Data.SqlClient.DataClassification;

namespace WSE_REST_WebApi.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class StockController : ControllerBase
    {
        private readonly StockContext _dbContext;
        public StockController(StockContext dbContext)
        {
            _dbContext = dbContext;
        }

        //GET: api/Stocks
        [HttpGet]
        public async Task<ActionResult<IEnumerable<Stock>>> GetStocks()
        {
            if (_dbContext.Stocks == null) { return NotFound(); }

            return await _dbContext.Stocks.ToListAsync();
        }

        //GET: api/Stock/5
        [HttpGet("{id}")]
        public async Task<ActionResult<Stock>> GetStockId(int id)
        {
            if (_dbContext.Stocks == null) { return NotFound(); }

            var stock = await _dbContext.Stocks.FindAsync(id);
            if (stock == null) { return NotFound(); }
            return stock;
        }

        //GET: /api/Stock/s/APPL
        [HttpGet("s/{input}")]
        public async Task<ActionResult<Stock>> GetStockNameSymbol(string input)
        {
            if (_dbContext.Stocks == null) { return NotFound(); }

            var stock = await _dbContext.Stocks.FirstOrDefaultAsync(s => s.Name == input||s.Symbol==input);
            if (stock == null) { return NotFound(); }
            return stock;
        }

        //GET: /api/Stock/q/APPL
        [HttpGet("q/{query}")]
        public async Task<ActionResult<IEnumerable<Stock>>> GetStockByQuery(string query)
        {
            if (_dbContext.Stocks == null) { return NotFound(); }

            var stocks = await _dbContext.Stocks
                .Where(s => s.Name.Contains(query) || s.Symbol.Contains(query))
                .ToListAsync();

            if (!stocks.Any()) { return NotFound(); }

            return stocks;
        }

        // GET: /api/Stock/AboveValue/{value}
        [HttpGet("AboveValue/{value}")]
        public async Task<ActionResult<IEnumerable<Stock>>> GetStocksAboveValue(double value)
        {
            if (_dbContext.Stocks == null) { return NotFound(); }

            var stocks = await _dbContext.Stocks
                .Where(s => s.Value > value)
                .ToListAsync();

            if (!stocks.Any()) { return NotFound(); }

            return stocks;
        }

        // GET: /api/Stock/BelowValue/{value}
        [HttpGet("BelowValue/{value}")]
        public async Task<ActionResult<IEnumerable<Stock>>> GetStocksBelowValue(double value)
        {
            if (_dbContext.Stocks == null) { return NotFound(); }

            var stocks = await _dbContext.Stocks
                .Where(s => s.Value < value)
                .ToListAsync();

            if (!stocks.Any()) { return NotFound(); }

            return stocks;
        }
        //POST: api/Stocks
        [HttpPost]
        public async Task<ActionResult<Stock>> PostStock(Stock stock)
        {
            _dbContext.Stocks.Add(stock);
            await _dbContext.SaveChangesAsync();
            return CreatedAtAction(nameof(PostStock), new { id = stock.Id }, stock);
        }

        //PUT:
        [HttpPut("{id}")]
        public async Task<IActionResult> PutStock(int id,Stock stock)
        {
            if (id!=stock.Id)   
            {
                return BadRequest();
            }
            _dbContext.Entry(stock).State = EntityState.Modified;

            try
            {
                await _dbContext.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!StockExists(id))
                {
                    return NotFound();
                }
                else { throw; }
            }
            return NoContent();
        }
        private bool StockExists(int id)
        {
            return(_dbContext.Stocks?.Any(e => e.Id == id)).GetValueOrDefault();
        }

        //DELETE:
        [HttpDelete("{id}")]
        public async Task<IActionResult>DeleteStock(int id)
        {
            if (_dbContext.Stocks == null) { return NotFound(); }

            var stock = await _dbContext.Stocks.FindAsync(id);
            if (stock == null) { return NotFound(); }

            _dbContext.Stocks.Remove(stock);
            await _dbContext.SaveChangesAsync();

            return NoContent();

        }

        //shtut
        [HttpGet("search")]
        public async Task<ActionResult<string>> Shtut(int x,int y)
        {
            return Ok($"shtut about {x} and {y}\n");
        }
    }
}